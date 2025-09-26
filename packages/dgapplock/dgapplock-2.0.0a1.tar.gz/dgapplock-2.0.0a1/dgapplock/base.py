import logging
import os
import threading
import time
import uuid
from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import Optional, Union, Dict, Any

import dglog
from .exceptions import AlreadyLockedError, InsufficientPrivilegesError


class BaseAppLocker(ABC):
    """Абстрактный базовый класс для блокировщика приложений"""

    def __init__(self, conf_dict: Dict[str, Any], application: str,
                 ttl: int = 60, logger_: Optional[logging.Logger] = None,
                 show_logs: bool = True):
        self.application = application
        self.instance_id = f"{application}-{uuid.uuid4().hex[:8]}"
        self.ttl = ttl
        self._stop_heartbeat = threading.Event()
        self._heartbeat_thread = None
        self._is_locked = False
        self._notification_shown = False

        self.logger = logger_ if logger_ else dglog.Logger()
        if isinstance(self.logger, dglog.Logger) and self.logger.logger is None:
            self.logger.auto_configure()

        self._show_logs = show_logs

    @abstractmethod
    def acquire(self, key: Optional[Union[int, str]] = None) -> bool:
        """Получить блокировку"""
        pass

    @abstractmethod
    def release(self) -> None:
        """Освободить блокировку"""
        pass

    @abstractmethod
    def get_lock_info(self, key: Optional[Union[int, str]] = None) -> Optional[dict]:
        """Получить информацию о блокировке"""
        pass

    @abstractmethod
    def is_my_lock(self, key: Optional[Union[int, str]] = None) -> bool:
        """Проверить принадлежность блокировки"""
        pass

    def get_lock_duration(self, key: Optional[Union[int, str]] = None) -> Optional[float]:
        """Получить продолжительность блокировки"""
        info = self.get_lock_info(key)
        if not info or 'acquired_at' not in info:
            return None
        return time.time() - info['acquired_at']

    def _get_host_info(self) -> str:
        """Получить информацию о хосте"""
        import socket
        return f"{socket.gethostname()}-{os.getpid()}"

    @contextmanager
    def acquired(self, key: Optional[Union[int, str]] = None):
        """Контекстный менеджер для блокировки"""
        acquired = self.acquire(key)
        if not acquired:
            raise AlreadyLockedError("Failed to acquire lock")
        try:
            yield
        finally:
            self.release()

    def __enter__(self):
        if not self.acquire():
            raise AlreadyLockedError("Failed to acquire lock")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()

    def is_locked(self) -> bool:
        """Проверить активность блокировки"""
        return self._is_locked

    def cleanup(self):
        """Очистить ресурсы"""
        if self._is_locked:
            self.release()

    def __del__(self):
        self.cleanup()