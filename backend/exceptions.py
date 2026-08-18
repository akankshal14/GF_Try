class BackendException(Exception):
    """
    Base exception for the backend.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class DatabaseException(BackendException):
    """
    Raised when a database operation fails.
    """

    pass


class ValidationException(BackendException):
    """
    Raised when input validation fails.
    """

    pass


class NotFoundException(BackendException):
    """
    Raised when a requested record does not exist.
    """

    pass


class DuplicateException(BackendException):
    """
    Raised when a duplicate record is detected.
    """

    pass


class BusinessRuleException(BackendException):
    """
    Raised when a business rule is violated.
    """

    pass