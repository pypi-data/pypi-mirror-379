import logging
import os
import threading
import time
import uuid
from contextlib import contextmanager
from typing import Optional, Union, Dict, Any

import dglog
from dgredis import RedisClient
from dgredis.conf import RedisConfig


class AppLockerRedis:
    """
    Класс для управления блокировками с использованием Redis.
    Поддерживает уникальную идентификацию экземпляров и контроль времени блокировки.
    """

    def __init__(self, conf_dict: dict, application: str, ttl: int = 60,
                 logger_: logging.Logger | dglog.Logger | None = None, show_logs: bool = True):
        """
        Инициализация блокировщика.

        :param conf_dict: Словарь с конфигурацией Redis
        :param application: Имя приложения/сервиса
        :param ttl: Время жизни блокировки в секундах
        :param logger_: Логгер
        :param show_logs: Показывать логи
        """
        self.conf = RedisConfig(**conf_dict)
        self.client = RedisClient(self.conf)
        self.application = application
        self.instance_id = f"{application}-{uuid.uuid4().hex[:8]}"  # Уникальный ID экземпляра
        self.lock = None
        self.lock_key = None
        self.ttl = ttl
        self._stop_heartbeat = threading.Event()
        self._heartbeat_thread = None
        self._is_locked = False  # Флаг состояния блокировки
        self._notification_shown = False  # Флаг для отслеживания показанного уведомления

        self.logger = logger_ if logger_ else dglog.Logger()
        if isinstance(self.logger, dglog.Logger) and self.logger.logger is None:
            self.logger.auto_configure()

        self._show_logs = show_logs

    def acquire(self, key: Optional[Union[int, str]] = None, max_retries: int = 3, retry_delay: float = 1.0) -> bool:
        """
        Получить блокировку с записью времени и ID экземпляра в Redis.

        :param key: Ключ блокировки (опционально)
        :param max_retries: Максимальное количество попыток
        :param retry_delay: Задержка между попытками (секунды)
        :return: True если блокировка получена, False если нет
        """
        for attempt in range(max_retries):
            try:
                if self._try_acquire(key):
                    return True

                # Если не удалось, проверяем и освобождаем висящие блокировки
                if self._check_and_release_stale_lock(key):
                    time.sleep(retry_delay)
                    continue

                # Показываем уведомление только один раз
                if not self._notification_shown and self._show_logs:
                    self._show_blocked_notification(key)
                    self._notification_shown = True

                return False

            except Exception as e:
                self.logger.error(f"Acquire attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    return False
                time.sleep(retry_delay)

        return False

    def _show_blocked_notification(self, key: Optional[Union[int, str]] = None):
        """Показать уведомление о том, что блокировка невозможна"""
        info = self.get_lock_info(key)
        if info:
            self.logger.info(f"🚫 Application '{self.application}' is already running!")
            self.logger.info(f"   Host: {info.get('host', 'Unknown')}")
            self.logger.info(f"   Instance: {info.get('owner', 'Unknown')}")
            self.logger.info("   Waiting for lock to be released...\n")

    def _try_acquire(self, key: Optional[Union[int, str]] = None) -> bool:
        """
        Попытка получить блокировку.

        :param key: Ключ блокировки
        :return: True если блокировка получена
        """
        try:
            self.lock_key = key or f'LOCK:{self.application}'
            lock_info_key = f"{self.lock_key}:INFO"

            # Пытаемся получить блокировку
            self.lock = self.client.client.lock(self.lock_key, timeout=self.ttl)
            if not self.lock.acquire(blocking=False):
                if self._show_logs:
                    self.logger.info(f"Lock acquire failed for {self.lock_key} / {self.instance_id}")
                return False

            # Записываем информацию о блокировке
            lock_info = {
                'acquired_at': time.time(),
                'owner': self.instance_id,
                'application': self.application,
                'host': self._get_host_info()
            }
            locked = self.client.client.set(lock_info_key, lock_info, ex=self.ttl)
            if locked:
                self._is_locked = True
                self._start_heartbeat()
                if self._show_logs:
                    self.logger.info(f"Lock {self.lock_key} / {self.instance_id} acquired")
            return locked

        except Exception as e:
            self.logger.error(f"Error acquiring lock: {e}")
            return False

    def release(self) -> None:
        """Освободить блокировку и очистить информацию о ней"""
        if not self._is_locked or not self.lock or not self.lock_key:
            return

        try:
            # Останавливаем heartbeat
            self._stop_heartbeat.set()
            if self._heartbeat_thread:
                self._heartbeat_thread.join(timeout=1)

            # Проверяем, наша ли это блокировка
            if self.is_my_lock(self.lock_key):
                lock_info_key = f"{self.lock_key}:INFO"

                # Сначала удаляем информацию о блокировке
                self.client.client.delete(lock_info_key)

                # Затем освобождаем саму блокировку
                try:
                    self.lock.release()
                except Exception as lock_release_error:
                    # Если не удалось освободить через lock.release(),
                    # пытаемся удалить ключ напрямую
                    if self._show_logs:
                        self.logger.warning(f"Lock release failed, trying direct delete: {lock_release_error}")
                    try:
                        self.client.client.delete(self.lock_key)
                    except Exception as delete_error:
                        self.logger.error(f"Failed to delete lock key: {delete_error}")

                if self._show_logs:
                    self.logger.info(f"Lock {self.lock_key} / {self.instance_id} released")
            else:
                if self._show_logs:
                    self.logger.warning(f"Trying to release lock that doesn't belong to this instance: {self.lock_key}")

        except Exception as e:
            self.logger.error(f"Error releasing lock: {e}")
        finally:
            self._is_locked = False
            self.lock = None
            self.lock_key = None
            # Сбрасываем флаг уведомления при освобождении блокировки
            self._notification_shown = False

    def _start_heartbeat(self):
        """Запустить фоновый поток для продления блокировки"""

        def heartbeat():
            while not self._stop_heartbeat.is_set():
                time.sleep(self.ttl / 3)
                try:
                    if self._is_locked and self.is_my_lock(self.lock_key):
                        lock_info_key = f"{self.lock_key}:INFO"
                        # Обновляем TTL для информации о блокировке
                        self.client.client.expire(lock_info_key, self.ttl)
                        # Обновляем TTL для самого ключа блокировки
                        self.client.client.expire(self.lock_key, self.ttl)
                except Exception as e:
                    self.logger.error(f"Heartbeat error: {e}")
                    break

        self._stop_heartbeat.clear()
        self._heartbeat_thread = threading.Thread(target=heartbeat, daemon=True)
        self._heartbeat_thread.start()

    def get_lock_info(self, key: Optional[Union[int, str]] = None) -> Optional[dict]:
        """
        Получить информацию о текущей блокировке из Redis.

        :param key: Ключ блокировки (опционально)
        :return: Словарь с информацией или None если блокировки нет
        """
        try:
            key = key or f'LOCK:{self.application}'
            lock_info_key = f"{key}:INFO"

            data = self.client.client.get(lock_info_key)
            if not data:
                return None

            return data

        except Exception as e:
            self.logger.error(f"Error getting lock info: {e}")
            return None

    def get_lock_duration(self, key: Optional[Union[int, str]] = None) -> Optional[float]:
        """
        Получить продолжительность текущей блокировки в секундах.

        :param key: Ключ блокировки (опционально)
        :return: Продолжительность в секундах или None
        """
        info = self.get_lock_info(key)
        if not info or 'acquired_at' not in info:
            return None
        return time.time() - info['acquired_at']

    def is_my_lock(self, key: Optional[Union[int, str]] = None) -> bool:
        """
        Проверить, принадлежит ли текущая блокировка этому экземпляру.

        :param key: Ключ блокировки (опционально)
        :return: True если блокировка принадлежит этому экземпляру
        """
        try:
            info = self.get_lock_info(key)
            return bool(info and info.get('owner') == self.instance_id)
        except Exception as e:
            self.logger.error(f"Error checking lock ownership: {e}")
            return False

    def _check_and_release_stale_lock(self, key: Optional[Union[int, str]] = None,
                                      stale_timeout: float = 300.0) -> bool:
        """
        Проверить и освободить висящую блокировку.

        :param key: Ключ блокировки (опционально)
        :param stale_timeout: Время в секундах, после которого блокировка считается устаревшей
        :return: True если блокировка была освобождена
        """
        try:
            key = key or f'LOCK:{self.application}'
            info = self.get_lock_info(key)

            if not info:
                return False

            # Проверяем, не устарела ли блокировка
            if time.time() - info['acquired_at'] > stale_timeout:
                # Удаляем информацию о блокировке
                self.client.client.delete(f"{key}:INFO")
                # Удаляем сам ключ блокировки
                self.client.client.delete(key)
                if self._show_logs:
                    self.logger.info(f"Released stale lock: {key}")
                return True

            return False
        except Exception as e:
            self.logger.error(f"Error checking stale lock: {e}")
            return False

    def force_release(self, key: Optional[Union[int, str]] = None) -> bool:
        """
        Принудительно освободить блокировку.

        :param key: Ключ блокировки (опционально)
        :return: True если блокировка была освобождена
        """
        try:
            key = key or f'LOCK:{self.application}'
            lock_info_key = f"{key}:INFO"

            # Удаляем информацию о блокировке
            self.client.client.delete(lock_info_key)
            # Удаляем сам ключ блокировки
            self.client.client.delete(key)

            if self._show_logs:
                self.logger.warning(f"Force released lock: {key}")
            return True

        except Exception as e:
            self.logger.error(f"Error force releasing lock: {e}")
            return False

    @contextmanager
    def acquired(self, key: Optional[Union[int, str]] = None, max_retries: int = 3, retry_delay: float = 1.0):
        """
        Контекстный менеджер для работы с блокировкой.

        Пример использования:
        with lock.acquired():
            # Код, выполняемый под блокировкой
            ...
        """
        acquired = self.acquire(key, max_retries, retry_delay)
        if not acquired:
            info = self.get_lock_info(key)
            if info:
                raise RuntimeError(
                    f"Failed to acquire lock for {key or self.application}. "
                    f"Already locked by {info.get('owner')} on {info.get('host')}"
                )
            else:
                raise RuntimeError(f"Failed to acquire lock for {key or self.application}")

        try:
            yield
        finally:
            self.release()

    def _get_host_info(self) -> str:
        """Получить информацию о хосте (для диагностики)"""
        import socket
        return f"{socket.gethostname()}-{os.getpid()}"

    def __enter__(self):
        """Поддержка использования объекта как контекстного менеджера"""
        if not self.acquire():
            raise RuntimeError("Failed to acquire queue lock")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Гарантированное освобождение блокировки при выходе из контекста"""
        self.release()

    def is_locked(self) -> bool:
        """Проверить, активна ли блокировка в данный момент"""
        return self._is_locked

    def cleanup(self):
        """Очистить все ресурсы"""
        if self._is_locked:
            self.release()

    def __del__(self):
        """Деструктор - гарантированное освобождение ресурсов"""
        self.cleanup()