import logging
import os
import threading
import time
import json
import uuid
from contextlib import contextmanager
from typing import Optional, Union, Dict, Any
import psycopg2
from psycopg2.extras import RealDictCursor
import dglog
from .exceptions import AlreadyLockedError, InsufficientPrivilegesError


class AppLockerPg:
    """
    Класс для управления блокировками с использованием PostgreSQL.
    Блокирует запуск других инстансов с тем же application_name.
    Автоматически освобождает висящие блокировки при аварийных завершениях.
    """

    def __init__(self, conf_dict: Dict[str, Any], application: str,
                 ttl: int = 60, logger_: Optional[logging.Logger] = None,
                 show_logs: bool = True, stale_timeout: int = 300):
        """
        Инициализация блокировщика.

        :param conf_dict: Словарь с конфигурацией подключения к PostgreSQL
        :param application: Имя приложения/сервиса
        :param ttl: Время жизни блокировки в секундах
        :param logger_: Логгер
        :param show_logs: Показывать логи
        :param stale_timeout: Время через которое блокировка считается висящей (секунды)
        """
        self.application = application
        self.instance_id = f"{application}-{uuid.uuid4().hex[:8]}"
        self.ttl = ttl
        self.stale_timeout = stale_timeout
        self._stop_heartbeat = threading.Event()
        self._heartbeat_thread = None
        self._is_locked = False
        self._connection = None
        self._notification_shown = False  # Флаг для отслеживания показанного уведомления
        self._table_initialized = False

        self.logger = logger_ if logger_ else dglog.Logger()
        if isinstance(self.logger, dglog.Logger) and self.logger.logger is None:
            self.logger.auto_configure()

        self._show_logs = show_logs

        # Параметры для подключения
        self.connection_params = {
            'host': conf_dict.get('db_host', 'localhost'),
            'port': conf_dict.get('db_port', 5432),
            'dbname': conf_dict.get('db_name', 'postgres'),
            'user': conf_dict.get('db_user', 'postgres'),
            'password': conf_dict.get('db_pass', '')
        }

        # Проверяем и инициализируем таблицу
        self._check_and_init_table()

    def _get_connection(self):
        """Получить соединение с базой данных"""
        if self._connection is None or self._connection.closed:
            self._connection = psycopg2.connect(**self.connection_params)
            self._connection.autocommit = False
        return self._connection

    def _close_connection(self):
        """Закрыть соединение с базой данных"""
        if self._connection and not self._connection.closed:
            self._connection.close()
        self._connection = None

    def _check_and_init_table(self):
        """Проверить наличие таблицы и прав доступа, при необходимости инициализировать"""
        conn = None
        try:
            conn = psycopg2.connect(**self.connection_params)
            conn.autocommit = True

            with conn.cursor() as cur:
                # Проверяем существование таблицы
                cur.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_name = 'app_locks'
                    )
                """)
                table_exists = cur.fetchone()[0]

                if table_exists:
                    # Проверяем права доступа к таблице
                    if not self._check_table_permissions(conn):
                        raise InsufficientPrivilegesError(
                            f"User '{self.connection_params['user']}' has insufficient privileges "
                            f"for table 'app_locks'. Need SELECT, INSERT, UPDATE, DELETE permissions."
                        )
                    self._table_initialized = True
                    if self._show_logs:
                        self.logger.info("Table 'app_locks' exists and permissions are sufficient")
                else:
                    # Пытаемся создать таблицу
                    self._init_table(conn)
                    self._table_initialized = True

        except psycopg2.Error as e:
            if "permission denied" in str(e).lower() or "insufficient privilege" in str(e).lower():
                raise InsufficientPrivilegesError(
                    f"Database user '{self.connection_params['user']}' has insufficient privileges. "
                    f"Error: {e}"
                ) from e
            raise
        except Exception as e:
            self.logger.error(f"Error checking table: {e}")
            raise
        finally:
            if conn and not conn.closed:
                conn.close()

    def _check_table_permissions(self, conn) -> bool:
        """Проверить права доступа к таблице app_locks"""
        try:
            with conn.cursor() as cur:
                # Проверяем основные права: SELECT, INSERT, UPDATE, DELETE
                cur.execute("""
                    SELECT has_table_privilege(%s, 'app_locks', 'SELECT'),
                           has_table_privilege(%s, 'app_locks', 'INSERT'),
                           has_table_privilege(%s, 'app_locks', 'UPDATE'),
                           has_table_privilege(%s, 'app_locks', 'DELETE')
                """, (self.connection_params['user'],) * 4)

                select, insert, update, delete = cur.fetchone()

                if not all([select, insert, update, delete]):
                    missing_perms = []
                    if not select: missing_perms.append('SELECT')
                    if not insert: missing_perms.append('INSERT')
                    if not update: missing_perms.append('UPDATE')
                    if not delete: missing_perms.append('DELETE')

                    self.logger.warning(
                        f"Missing permissions for table 'app_locks': {', '.join(missing_perms)}"
                    )
                    return False

                return True

        except Exception as e:
            self.logger.error(f"Error checking table permissions: {e}")
            return False

    def _init_table(self, conn=None):
        """Инициализировать таблицу для блокировок"""
        close_conn = False
        if conn is None:
            conn = psycopg2.connect(**self.connection_params)
            conn.autocommit = True
            close_conn = True

        try:
            with conn.cursor() as cur:
                # Проверяем права на создание таблиц
                cur.execute("SELECT has_schema_privilege(%s, 'public', 'CREATE')",
                            (self.connection_params['user'],))
                can_create = cur.fetchone()[0]

                if not can_create:
                    raise InsufficientPrivilegesError(
                        f"User '{self.connection_params['user']}' cannot create tables in public schema. "
                        "Please ask database administrator to create 'app_locks' table or grant CREATE privilege."
                    )

                # Создаем таблицу если не существует
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS app_locks (
                        application VARCHAR(255) PRIMARY KEY,
                        instance_id VARCHAR(255) NOT NULL,
                        acquired_at DOUBLE PRECISION NOT NULL,
                        expires_at DOUBLE PRECISION NOT NULL,
                        last_heartbeat DOUBLE PRECISION NOT NULL,
                        host_info TEXT NOT NULL,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)

                # Индексы для быстрой очистки
                cur.execute("""
                    CREATE INDEX IF NOT EXISTS idx_app_locks_expires_at 
                    ON app_locks (expires_at)
                """)
                cur.execute("""
                    CREATE INDEX IF NOT EXISTS idx_app_locks_last_heartbeat 
                    ON app_locks (last_heartbeat)
                """)

                if self._show_logs:
                    self.logger.info("Table 'app_locks' created successfully")

        except psycopg2.Error as e:
            if "permission denied" in str(e).lower():
                raise InsufficientPrivilegesError(
                    f"User '{self.connection_params['user']}' has insufficient privileges "
                    f"to create table 'app_locks'. Error: {e}"
                ) from e
            raise
        except Exception as e:
            self.logger.error(f"Error initializing table: {e}")
            raise
        finally:
            if close_conn and conn and not conn.closed:
                conn.close()

    def acquire(self, max_retries: int = 3, retry_delay: float = 1.0) -> bool:
        """
        Получить блокировку для приложения с автоматическим освобождением висящих блокировок.

        :param max_retries: Максимальное количество попыток
        :param retry_delay: Задержка между попытками (секунды)
        """
        for attempt in range(max_retries):
            try:
                if self._try_acquire():
                    return True

                # Если не удалось, проверяем и освобождаем висящие блокировки
                if self._check_and_release_stale_lock():
                    time.sleep(retry_delay)
                    continue

                # Показываем уведомление только один раз
                if not self._notification_shown and self._show_logs:
                    self._show_blocked_notification()
                    self._notification_shown = True

                return False

            except Exception as e:
                self.logger.error(f"Acquire attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    return False
                time.sleep(retry_delay)

        return False

    def _show_blocked_notification(self):
        """Показать уведомление о том, что блокировка невозможна"""
        info = self.get_lock_info()
        if info:
            # current_time = time.time()
            # running_time = current_time - info['acquired_at']
            # last_activity = current_time - info['last_heartbeat']

            self.logger.info(f"🚫 Application '{self.application}' is already running!")
            self.logger.info(f"   Host: {info['host_info']}")
            self.logger.info(f"   Instance: {info['instance_id']}")
            # self.logger.info(f"   Running for: {running_time:.1f} seconds")
            # self.logger.info(f"   Last activity: {last_activity:.1f} seconds ago")
            self.logger.info("   Waiting for lock to be released...\n")

    def _try_acquire(self) -> bool:
        """Попытка получить блокировку"""
        conn = None
        try:
            conn = psycopg2.connect(**self.connection_params)
            conn.autocommit = False

            # Сначала очищаем устаревшие блокировки
            self._cleanup_stale_locks(conn)

            current_time = time.time()
            expires_at = current_time + self.ttl

            with conn.cursor() as cur:
                # Атомарная попытка получить блокировку
                cur.execute("""
                    INSERT INTO app_locks (application, instance_id, acquired_at, 
                                         expires_at, last_heartbeat, host_info)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (application) 
                    DO UPDATE SET
                        instance_id = EXCLUDED.instance_id,
                        acquired_at = EXCLUDED.acquired_at,
                        expires_at = EXCLUDED.expires_at,
                        last_heartbeat = EXCLUDED.last_heartbeat,
                        host_info = EXCLUDED.host_info,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE app_locks.expires_at <= EXCLUDED.acquired_at
                    OR app_locks.last_heartbeat < %s
                    RETURNING instance_id
                """, (self.application, self.instance_id, current_time, expires_at,
                      current_time, self._get_host_info(), current_time - self.stale_timeout))

                result = cur.fetchone()

                if result and result[0] == self.instance_id:
                    # Мы получили блокировку
                    conn.commit()
                    self._is_locked = True
                    self._start_heartbeat()

                    if self._show_logs:
                        # self.logger.info(f"Application '{self.application}' locked by instance {self.instance_id}")
                        self.logger.info(f"Application '{self.application}' locked!")
                        self.logger.info(f"   Host: {self._get_host_info()}")
                        self.logger.info(f"   Instance: {self.instance_id}")

                    return True
                else:
                    # Блокировка уже занята
                    conn.rollback()
                    return False

        except Exception as e:
            if conn:
                conn.rollback()
            self.logger.error(f"Error acquiring lock: {e}")
            return False
        finally:
            if conn and not conn.closed:
                conn.close()

    def _check_and_release_stale_lock(self) -> bool:
        """Проверить и освободить висящую блокировку"""
        conn = None
        try:
            conn = psycopg2.connect(**self.connection_params)
            conn.autocommit = False

            current_time = time.time()
            stale_threshold = current_time - self.stale_timeout

            with conn.cursor() as cur:
                # Проверяем, есть ли висящая блокировка
                cur.execute("""
                    SELECT instance_id, last_heartbeat, acquired_at
                    FROM app_locks 
                    WHERE application = %s 
                    AND last_heartbeat < %s
                """, (self.application, stale_threshold))

                result = cur.fetchone()

                if result:
                    instance_id, last_heartbeat, acquired_at = result

                    # Освобождаем висящую блокировку
                    cur.execute("""
                        DELETE FROM app_locks 
                        WHERE application = %s 
                        AND last_heartbeat < %s
                    """, (self.application, stale_threshold))

                    conn.commit()

                    if self._show_logs:
                        self.logger.warning(
                            f"Released stale lock for application '{self.application}'. "
                            f"Instance: {instance_id}, "
                            f"last heartbeat: {current_time - last_heartbeat:.1f}s ago, "
                            f"held for: {current_time - acquired_at:.1f}s"
                        )

                    return True

                conn.rollback()
                return False

        except Exception as e:
            if conn:
                conn.rollback()
            self.logger.error(f"Error checking stale lock: {e}")
            return False
        finally:
            if conn and not conn.closed:
                conn.close()

    def release(self) -> None:
        """Освободить блокировку приложения"""
        if not self._is_locked:
            return

        try:
            # Останавливаем heartbeat
            self._stop_heartbeat.set()
            if self._heartbeat_thread:
                self._heartbeat_thread.join(timeout=1)

            conn = psycopg2.connect(**self.connection_params)
            conn.autocommit = False

            try:
                with conn.cursor() as cur:
                    # Удаляем только нашу блокировку
                    cur.execute("""
                        DELETE FROM app_locks 
                        WHERE application = %s AND instance_id = %s
                    """, (self.application, self.instance_id))

                    if cur.rowcount > 0:
                        conn.commit()
                        if self._show_logs:
                            self.logger.info(f"Application '{self.application}' unlocked by instance {self.instance_id}")
                    else:
                        conn.rollback()
                        if self._show_logs:
                            self.logger.warning(f"Lock for application '{self.application}' not found")

            finally:
                conn.close()

        except Exception as e:
            self.logger.error(f"Error releasing lock: {e}")
        finally:
            self._is_locked = False
            # Сбрасываем флаг уведомления при освобождении блокировки
            self._notification_shown = False

    def _start_heartbeat(self):
        """Запустить фоновый поток для продления блокировки"""

        def heartbeat():
            while not self._stop_heartbeat.is_set():
                time.sleep(self.ttl / 3)
                try:
                    if self._is_locked:
                        self._refresh_lock()
                except Exception as e:
                    self.logger.error(f"Heartbeat error: {e}")
                    # При ошибке heartbeat считаем блокировку потерянной
                    self._is_locked = False
                    break

        self._stop_heartbeat.clear()
        self._heartbeat_thread = threading.Thread(target=heartbeat, daemon=True)
        self._heartbeat_thread.start()

    def _refresh_lock(self):
        """Обновить время жизни блокировки"""
        conn = None
        try:
            conn = psycopg2.connect(**self.connection_params)
            conn.autocommit = False

            current_time = time.time()
            expires_at = current_time + self.ttl

            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE app_locks 
                    SET expires_at = %s, last_heartbeat = %s, updated_at = CURRENT_TIMESTAMP
                    WHERE application = %s AND instance_id = %s
                    RETURNING application
                """, (expires_at, current_time, self.application, self.instance_id))

                if cur.rowcount > 0:
                    conn.commit()
                else:
                    conn.rollback()
                    self._is_locked = False
                    if self._show_logs:
                        self.logger.warning(f"Lock refresh failed - possibly released by another process")

        except Exception as e:
            if conn:
                conn.rollback()
            self.logger.error(f"Error refreshing lock: {e}")
            self._is_locked = False
        finally:
            if conn and not conn.closed:
                conn.close()

    def _cleanup_stale_locks(self, conn=None):
        """Очистить все устаревшие блокировки"""
        close_conn = False
        if conn is None:
            conn = psycopg2.connect(**self.connection_params)
            conn.autocommit = False
            close_conn = True

        try:
            with conn.cursor() as cur:
                current_time = time.time()
                stale_threshold = current_time - self.stale_timeout

                cur.execute("""
                    DELETE FROM app_locks 
                    WHERE expires_at <= %s 
                    OR last_heartbeat < %s
                    RETURNING application, instance_id, acquired_at
                """, (current_time, stale_threshold))

                stale_locks = cur.fetchall()
                conn.commit()

                if stale_locks and self._show_logs:
                    for app, instance_id, acquired_at in stale_locks:
                        held_time = current_time - acquired_at
                        self.logger.warning(
                            f"Cleaned up stale lock for application '{app}', "
                            f"instance: {instance_id}, held for: {held_time:.1f}s"
                        )

        except Exception as e:
            conn.rollback()
            self.logger.error(f"Error cleaning up stale locks: {e}")
        finally:
            if close_conn and conn and not conn.closed:
                conn.close()

    def get_lock_info(self) -> Optional[dict]:
        """Получить информацию о текущей блокировке приложения."""
        conn = None
        try:
            conn = psycopg2.connect(**self.connection_params)

            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT application, instance_id, acquired_at, expires_at, 
                           last_heartbeat, host_info, updated_at, created_at
                    FROM app_locks 
                    WHERE application = %s
                """, (self.application,))

                result = cur.fetchone()
                return dict(result) if result else None

        except Exception as e:
            self.logger.error(f"Error getting lock info: {e}")
            return None
        finally:
            if conn and not conn.closed:
                conn.close()

    def get_lock_duration(self) -> Optional[float]:
        """Получить продолжительность текущей блокировки приложения в секундах."""
        info = self.get_lock_info()
        if not info or 'acquired_at' not in info:
            return None
        return time.time() - info['acquired_at']

    def get_time_until_expiry(self) -> Optional[float]:
        """Получить оставшееся время до истечения блокировки в секундах."""
        info = self.get_lock_info()
        if not info or 'expires_at' not in info:
            return None
        return info['expires_at'] - time.time()

    def is_my_lock(self) -> bool:
        """Проверить, принадлежит ли текущая блокировка приложения этому экземпляру."""
        try:
            info = self.get_lock_info()
            return bool(info and info.get('instance_id') == self.instance_id)
        except Exception as e:
            self.logger.error(f"Error checking lock ownership: {e}")
            return False

    def is_application_locked(self) -> bool:
        """Проверить, заблокировано ли приложение (с учетом актуальности блокировки)."""
        info = self.get_lock_info()
        if not info:
            return False

    def force_release(self) -> bool:
        """Принудительно освободить блокировку приложения."""
        conn = None
        try:
            conn = psycopg2.connect(**self.connection_params)
            conn.autocommit = False

            with conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM app_locks 
                    WHERE application = %s
                    RETURNING instance_id, acquired_at
                """, (self.application,))

                if cur.rowcount > 0:
                    result = cur.fetchone()
                    conn.commit()

                    if self._show_logs:
                        self.logger.warning(f"Force released lock for application '{self.application}'. "
                                            f"Instance: {result[0]}, held for {time.time() - result[1]:.1f}s")

                    return True
                else:
                    conn.rollback()
                    return False

        except Exception as e:
            if conn:
                conn.rollback()
            self.logger.error(f"Error force releasing lock: {e}")
            return False
        finally:
            if conn and not conn.closed:
                conn.close()

    @staticmethod
    def _get_host_info() -> str:
        """Получить информацию о хосте (для диагностики)"""
        import socket
        return f"{socket.gethostname()}-{os.getpid()}"

    def check_connection(self) -> bool:
        """Проверить подключение к базе данных и права доступа"""
        try:
            self._check_and_init_table()
            return True
        except InsufficientPrivilegesError as e:
            self.logger.error(f"Insufficient privileges: {e}")
            return False
        except Exception as e:
            self.logger.error(f"Connection check failed: {e}")
            return False

    def get_table_status(self) -> Dict[str, Any]:
        """Получить статус таблицы и прав доступа"""
        try:
            conn = psycopg2.connect(**self.connection_params)
            conn.autocommit = True

            with conn.cursor() as cur:
                # Проверяем существование таблицы
                cur.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_name = 'app_locks'
                    )
                """)
                table_exists = cur.fetchone()[0]

                status = {
                    'table_exists': table_exists,
                    'table_initialized': self._table_initialized,
                    'user': self.connection_params['user'],
                    'database': self.connection_params['dbname']
                }

                if table_exists:
                    # Проверяем права доступа
                    status['permissions'] = self._check_table_permissions(conn)

                return status

        except Exception as e:
            return {
                'table_exists': False,
                'table_initialized': False,
                'error': str(e)
            }
        finally:
            if conn and not conn.closed:
                conn.close()

    @contextmanager
    def acquired(self, max_retries: int = 3, retry_delay: float = 1.0):
        """Контекстный менеджер с автоматическим освобождением висящих блокировок."""
        acquired = self.acquire(max_retries, retry_delay)
        if not acquired:
            info = self.get_lock_info()
            if info:
                current_time = time.time()
                raise AlreadyLockedError(
                    f"Application '{self.application}' is already running. "
                    f"Host: {info['host_info']}, "
                    f"Instance: {info['instance_id']}, "
                    f"running for: {current_time - info['acquired_at']:.1f}s, "
                    f"last activity: {current_time - info['last_heartbeat']:.1f}s ago"
                )
            else:
                raise AlreadyLockedError(f"Failed to acquire lock for application '{self.application}'")

        try:
            yield
        finally:
            self.release()

    def __enter__(self):
        return self.acquired().__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Гарантированное освобождение блокировки при выходе из контекста"""
        self.release()

    def is_locked(self) -> bool:
        """Проверить, активна ли блокировка приложения в данный момент для этого инстанса"""
        return self._is_locked

    def cleanup(self):
        """Очистить все ресурсы"""
        if self._is_locked:
            self.release()

    def __del__(self):
        """Деструктор - гарантированное освобождение ресурсов"""
        self.cleanup()