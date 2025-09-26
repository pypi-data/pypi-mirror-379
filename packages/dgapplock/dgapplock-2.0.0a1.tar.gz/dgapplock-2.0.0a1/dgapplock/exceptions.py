class AlreadyLockedError(Exception):
    """Исключение когда приложение уже заблокировано"""
    pass


class InsufficientPrivilegesError(Exception):
    """Ошибка недостаточных прав доступа"""
    pass


class LockAcquisitionError(Exception):
    """Ошибка получения блокировки"""
    pass


class BackendNotAvailableError(Exception):
    """Ошибка когда бэкенд не доступен"""
    pass