"""
Incept SDK Exceptions
"""


class InceptAPIError(Exception):
    """Base exception for Incept API errors"""
    pass


class AuthenticationError(InceptAPIError):
    """Raised when API key authentication fails"""
    pass


class ValidationError(InceptAPIError):
    """Raised when request validation fails"""
    pass


class RateLimitError(InceptAPIError):
    """Raised when rate limit is exceeded"""
    pass


class ServerError(InceptAPIError):
    """Raised when server returns 5xx error"""
    pass


class NetworkError(InceptAPIError):
    """Raised when network connection fails"""
    pass