class BaseError:
    """
    Base class for custom errors in the application.

    This class provides a base implementation for custom error types by defining a generic error message
    and a method to raise the error with that message.
    """

    MESSAGE = "Unknown error"

    @classmethod
    def raise_error(cls):
        """
        Raises the custom error with the defined message.

        This method raises a `ValueError` with the error message specified in the `MESSAGE` class attribute.

        :raises ValueError: Raises a ValueError with the message defined in the `MESSAGE` attribute.
        """
        raise ValueError(cls.MESSAGE)


class PositiveNumberError(BaseError):
    """
    Error raised when an input is not a valid positive integer.

    This class extends `BaseError` to provide a specific error message for cases where an input is expected
    to be a positive integer but is not. It inherits the `raise_error` method from `BaseError` to raise
    a `ValueError` with a custom message.
    """

    MESSAGE = "Input must be a positive integer."
