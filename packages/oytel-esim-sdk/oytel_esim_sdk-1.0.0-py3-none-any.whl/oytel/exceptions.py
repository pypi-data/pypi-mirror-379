"""
Oytel SDK Exceptions
"""


class OytelError(Exception):
    """Base exception for all Oytel SDK errors."""
    pass


class OytelAPIError(OytelError):
    """Exception raised for API errors."""
    
    def __init__(self, message: str, status_code: int, error_code: str = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
    
    def __str__(self):
        if self.error_code:
            return f"{self.message} (Status: {self.status_code}, Code: {self.error_code})"
        return f"{self.message} (Status: {self.status_code})"


class OytelAuthError(OytelError):
    """Exception raised for authentication errors."""
    pass
