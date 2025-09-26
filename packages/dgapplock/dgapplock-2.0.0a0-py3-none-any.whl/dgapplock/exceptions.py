class AlreadyLockedError(Exception):
    """Исключение когда приложение уже заблокировано"""
    pass

class InsufficientPrivilegesError(Exception):
    """Ошибка недостаточных прав доступа"""
    pass

class LockAcquisitionError(Exception):
    """Ошибка получения блокировки"""
    pass