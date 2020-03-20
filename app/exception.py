
class BlockchainException(Exception):
    """
    Base class for all BlockchainException errors.
    """
    pass

class ValueError(BlockchainException):
    """
    Raised when does not contain the required data.
    """
    pass

class TypeError(BlockchainException):
    """
    Raised when does not contain the required type.
    """
    pass

class EmptyError(BlockchainException):
    """
    Raised when there is nothing to transfer.
    """
    pass

class CannotValidation(BlockchainException):
    """
    Raised when something does not pass a validation check.
    """
    pass

