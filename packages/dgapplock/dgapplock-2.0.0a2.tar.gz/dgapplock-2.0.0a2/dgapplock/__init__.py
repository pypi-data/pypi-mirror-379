import importlib.metadata
import sys
from typing import Type, Dict, Any, Optional

# Импортируем исключения
from .exceptions import AlreadyLockedError, InsufficientPrivilegesError

__all__ = [
    'AppLocker',
    'AppLockerRedis',
    'AppLockerPg',
    'AlreadyLockedError',
    'InsufficientPrivilegesError'
]

# Глобальные переменные для ленивой загрузки классов
_AppLockerRedis = None
_AppLockerPg = None
_AppLocker = None


def _import_redis_backend():
    """Лениво импортировать Redis бэкенд"""
    global _AppLockerRedis
    if _AppLockerRedis is None:
        try:
            from .redis_backend import AppLockerRedis
            _AppLockerRedis = AppLockerRedis
        except ImportError as e:
            # Проверяем, это ошибка из-за отсутствия зависимостей
            if "dgredis" in str(e) or "redis" in str(e):
                _AppLockerRedis = None
            else:
                raise
    return _AppLockerRedis


def _import_pg_backend():
    """Лениво импортировать PostgreSQL бэкенд"""
    global _AppLockerPg
    if _AppLockerPg is None:
        try:
            from .pg_backend import AppLockerPg
            _AppLockerPg = AppLockerPg
        except ImportError as e:
            # Проверяем, это ошибка из-за отсутствия зависимостей
            if "psycopg2" in str(e):
                _AppLockerPg = None
            else:
                raise
    return _AppLockerPg


def _detect_backend() -> str:
    """Определить доступный бэкенд на основе установленных зависимостей"""
    try:
        # Проверяем установленные extras (имя пакета должно быть правильным)
        dist_name = 'dgapplocker'  # Исправьте на правильное имя пакета
        try:
            dist = importlib.metadata.distribution(dist_name)
            requirements = dist.requires or []

            if any('redis' in str(req) for req in requirements):
                return 'redis'
            elif any('pg' in str(req) for req in requirements):
                return 'pg'
        except importlib.metadata.PackageNotFoundError:
            pass

        # Проверяем доступные библиотеки через ленивую загрузку
        if _import_redis_backend() is not None:
            # Дополнительная проверка, что зависимости Redis доступны
            try:
                from dgredis import RedisClient
                return 'redis'
            except ImportError:
                pass

        if _import_pg_backend() is not None:
            # Дополнительная проверка, что зависимости PG доступны
            try:
                import psycopg2
                return 'pg'
            except ImportError:
                pass

        # Если дошли сюда, проверяем что вообще можно импортировать
        if _import_redis_backend() is not None:
            return 'redis'
        elif _import_pg_backend() is not None:
            return 'pg'
        else:
            raise RuntimeError(
                "No suitable backend found. Install dgapplocker[redis] or dgapplocker[pg]"
            )

    except Exception as e:
        raise RuntimeError(f"Error detecting backend: {e}")


def _get_app_locker_class() -> Type:
    """Получить класс AppLocker в зависимости от доступного бэкенда"""
    backend = _detect_backend()

    if backend == 'redis':
        cls = _import_redis_backend()
        if cls is None:
            raise RuntimeError("Redis backend is not available. Install dgapplocker[redis]")
        return cls
    elif backend == 'pg':
        cls = _import_pg_backend()
        if cls is None:
            raise RuntimeError("PostgreSQL backend is not available. Install dgapplocker[pg]")
        return cls
    else:
        raise RuntimeError(f"Unsupported backend: {backend}")


def get_app_locker_class() -> Type:
    """Получить класс AppLocker (кэшированная версия)"""
    global _AppLocker
    if _AppLocker is None:
        _AppLocker = _get_app_locker_class()
    return _AppLocker


# Динамическое свойство для AppLocker
class _AppLockerProxy:
    """Прокси для ленивой загрузки основного класса"""

    def __call__(self, *args, **kwargs):
        cls = get_app_locker_class()
        return cls(*args, **kwargs)

    def __instancecheck__(self, instance):
        cls = get_app_locker_class()
        return isinstance(instance, cls)

    def __subclasscheck__(self, subclass):
        cls = get_app_locker_class()
        return issubclass(subclass, cls)

    @property
    def __name__(self):
        cls = get_app_locker_class()
        return cls.__name__

    def __getattr__(self, name):
        cls = get_app_locker_class()
        return getattr(cls, name)


# Основной класс как прокси
AppLocker = _AppLockerProxy()


# Явные классы также как прокси
class _RedisBackendProxy:
    """Прокси для Redis бэкенда"""

    def __call__(self, *args, **kwargs):
        cls = _import_redis_backend()
        if cls is None:
            raise RuntimeError("Redis backend is not available. Install dgapplocker[redis]")
        return cls(*args, **kwargs)

    def __getattr__(self, name):
        cls = _import_redis_backend()
        if cls is None:
            raise RuntimeError("Redis backend is not available. Install dgapplocker[redis]")
        return getattr(cls, name)


class _PgBackendProxy:
    """Прокси для PostgreSQL бэкенда"""

    def __call__(self, *args, **kwargs):
        cls = _import_pg_backend()
        if cls is None:
            raise RuntimeError("PostgreSQL backend is not available. Install dgapplocker[pg]")
        return cls(*args, **kwargs)

    def __getattr__(self, name):
        cls = _import_pg_backend()
        if cls is None:
            raise RuntimeError("PostgreSQL backend is not available. Install dgapplocker[pg]")
        return getattr(cls, name)


AppLockerRedis = _RedisBackendProxy()
AppLockerPg = _PgBackendProxy()


def get_app_locker(conf_dict: Dict[str, Any], application: str,
                   ttl: int = 60, backend: Optional[str] = None,
                   **kwargs):
    """
    Фабричная функция для создания экземпляра AppLocker.

    :param conf_dict: Конфигурация бэкенда
    :param application: Имя приложения
    :param ttl: Время жизни блокировки
    :param backend: Явное указание бэкенда ('redis' или 'pg')
    :param kwargs: Дополнительные параметры
    :return: Экземпляр AppLocker
    """
    if backend == 'redis':
        cls = _import_redis_backend()
        if cls is None:
            raise RuntimeError("Redis backend is not available. Install dgapplocker[redis]")
    elif backend == 'pg':
        cls = _import_pg_backend()
        if cls is None:
            raise RuntimeError("PostgreSQL backend is not available. Install dgapplocker[pg]")
    elif backend is None:
        cls = get_app_locker_class()
    else:
        raise ValueError(f"Unknown backend: {backend}")

    return cls(conf_dict, application, ttl, **kwargs)


def use_backend(backend: str):
    """Явно указать используемый бэкенд"""
    global _AppLocker
    if backend == 'redis':
        cls = _import_redis_backend()
        if cls is None:
            raise RuntimeError("Redis backend is not available. Install dgapplocker[redis]")
        _AppLocker = cls
    elif backend == 'pg':
        cls = _import_pg_backend()
        if cls is None:
            raise RuntimeError("PostgreSQL backend is not available. Install dgapplocker[pg]")
        _AppLocker = cls
    else:
        raise ValueError(f"Unknown backend: {backend}")


def is_backend_available(backend: str) -> bool:
    """Проверить доступность бэкенда"""
    if backend == 'redis':
        return _import_redis_backend() is not None
    elif backend == 'pg':
        return _import_pg_backend() is not None
    else:
        return False


def get_available_backends() -> list[str]:
    """Получить список доступных бэкендов"""
    backends = []
    if is_backend_available('redis'):
        backends.append('redis')
    if is_backend_available('pg'):
        backends.append('pg')
    return backends
