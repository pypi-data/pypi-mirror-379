import importlib.metadata
import sys
from typing import Type, Dict, Any, Optional

from .redis_backend import AppLockerRedis
from .pg_backend import AppLockerPg

# Импортируем исключения из pg_backend если они там определены
try:
    from .exceptions import AlreadyLockedError, InsufficientPrivilegesError
except ImportError:
    # Создаем заглушки если исключения не импортируются
    class AlreadyLockedError(Exception):
        """Исключение когда приложение уже заблокировано"""
        pass


    class InsufficientPrivilegesError(Exception):
        """Ошибка недостаточных прав доступа"""
        pass


__all__ = [
    'AppLocker',
    'AppLockerRedis',
    'AppLockerPg',
    'AlreadyLockedError',
    'InsufficientPrivilegesError'
]


def _detect_backend() -> str:
    """Определить доступный бэкенд на основе установленных зависимостей"""
    try:
        # Проверяем установленные extras
        dist = importlib.metadata.distribution('dgapplock')
        requirements = dist.requires or []

        if any('redis' in str(req) for req in requirements):
            return 'redis'
        elif any('pg' in str(req) for req in requirements):
            return 'pg'
    except importlib.metadata.PackageNotFoundError:
        pass

    # Проверяем доступные библиотеки
    try:
        import redis
        return 'redis'
    except ImportError:
        pass

    try:
        import psycopg2
        return 'pg'
    except ImportError:
        pass

    # Если ничего не найдено, пробуем импортировать dgredis как индикатор
    try:
        from dgredis import RedisClient
        return 'redis'
    except ImportError:
        raise RuntimeError(
            "No suitable backend found. Install dgapplock[redis] or dgapplock[pg]"
        )


def _get_app_locker_class() -> Type:
    """Получить класс AppLocker в зависимости от доступного бэкенда"""
    backend = _detect_backend()

    if backend == 'redis':
        return AppLockerRedis
    elif backend == 'pg':
        return AppLockerPg
    else:
        raise RuntimeError(f"Unsupported backend: {backend}")


# Динамически определяем основной класс
try:
    AppLocker = _get_app_locker_class()
except RuntimeError as e:
    # Fallback для случаев когда бэкенд еще не определен
    AppLocker = None


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
    if backend:
        if backend == 'redis':
            cls = AppLockerRedis
        elif backend == 'pg':
            cls = AppLockerPg
        else:
            raise ValueError(f"Unknown backend: {backend}")
    else:
        cls = _get_app_locker_class()

    return cls(conf_dict, application, ttl, **kwargs)


def use_backend(backend: str):
    """Явно указать используемый бэкенд"""
    global AppLocker
    if backend == 'redis':
        AppLocker = AppLockerRedis
    elif backend == 'pg':
        AppLocker = AppLockerPg
    else:
        raise ValueError(f"Unknown backend: {backend}")