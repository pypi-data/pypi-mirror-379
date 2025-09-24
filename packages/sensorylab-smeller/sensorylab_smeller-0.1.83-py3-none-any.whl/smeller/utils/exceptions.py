# smeller/utils/exceptions.py
class SmellerException(Exception):
    """Базовый класс исключений для приложения Smeller."""
    pass
class ValidationError(SmellerException):
    """Исключение, возникающее при ошибках валидации данных."""
    def __init__(self, message, field=None):
        super().__init__(message)
        self.field = field  # Поле, в котором произошла ошибка

    def __str__(self):
        if self.field:
            return f"Ошибка валидации поля '{self.field}': {self.args[0]}"
        else:
            return f"Ошибка валидации: {self.args[0]}"

class DeviceError(SmellerException):
    """Base class for device-related errors."""
    pass

class CommunicationError(DeviceError):
    """Raised when there is a problem communicating with the device."""
    pass

class ConnectionError(CommunicationError):
    """Raised when the connection to the device fails."""
    pass

class CommandError(DeviceError):
    """Raised when a command fails to execute."""
    pass

class InvalidResponseError(DeviceError):
    """Raised when the device returns an invalid response."""
    pass


class DatabaseError(SmellerException):
    """Исключение, возникающее при ошибках работы с базой данных."""
    pass

class ConfigurationError(SmellerException):
    """Исключение, возникающее при ошибках конфигурации."""
    pass

class BlockNotFoundError(SmellerException):
    """Блок не найден."""
    pass