class NegativeNumberError(Exception):
    """
    Custom exception raised when a negative number is encountered.

    Attributes:
        number -- the negative number that caused the error
        message -- explanation of the error
    """
    def __init__(self, number, message="A negative number is not allowed"):
        self.number = number
        self.message = f"{message}: {number}"
        # Call the base class constructor with the message
        super().__init__(self.message)