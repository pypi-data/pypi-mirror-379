"""
SIGRID Systems Exceptions

Structured exception hierarchy for HTTP error handling.

Available Exceptions:
    SigridError - Base exception for all SIGRID errors
    ClientError - Client-side HTTP errors (4xx)
    ServerError - Server-side HTTP errors (5xx)
    AuthenticationError - Auth failures (401, 403)
    ValidationError - Input validation errors (400, 422)
    RateLimitError - Rate limit exceeded (429)
    NetworkError - Connection/network failures

Usage:
    try:
        await client.analyze(docs, query)
    except exceptions.AuthenticationError:
        print("Check API key")
    except exceptions.ValidationError as e:
        print(f"Input error: {e}")
    except exceptions.RateLimitError as e:
        print(f"Rate limited. Retry after: {e.retry_after}s")
"""

from typing import Optional, Dict, Any


class SigridError(Exception):
    """Base exception for all SIGRID-related errors."""
    
    def __init__(
        self, 
        message: str, 
        *,
        details: Optional[Dict[str, Any]] = None,
        cause: Optional[Exception] = None
    ):
        super().__init__(message)
        self.message = message
        self.details = details or {}
        self.cause = cause


class ClientError(SigridError):
    """Base class for client-side (4xx) HTTP errors."""
    
    def __init__(
        self, 
        message: str, 
        status_code: int,
        *,
        response_body: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
        cause: Optional[Exception] = None
    ):
        super().__init__(message, details=details, cause=cause)
        self.status_code = status_code
        self.response_body = response_body


class ServerError(SigridError):
    """Base class for server-side (5xx) HTTP errors."""
    
    def __init__(
        self, 
        message: str, 
        status_code: int,
        *,
        response_body: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
        cause: Optional[Exception] = None
    ):
        super().__init__(message, details=details, cause=cause)
        self.status_code = status_code
        self.response_body = response_body


class AuthenticationError(ClientError):
    """Raised for authentication failures (401, 403)."""
    pass


class ValidationError(ClientError):
    """Raised for validation failures (400)."""
    pass


class RateLimitError(ClientError):
    """Raised for rate limit exceeded (429)."""
    
    def __init__(
        self, 
        message: str,
        *,
        retry_after: Optional[int] = None,
        response_body: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
        cause: Optional[Exception] = None
    ):
        super().__init__(message, 429, response_body=response_body, details=details, cause=cause)
        self.retry_after = retry_after


class NetworkError(SigridError):
    """Raised for network-related failures."""
    pass


class StreamingError(SigridError):
    """Raised for streaming response handling failures."""
    pass


# Status code mapping functions
def _exception_class_for_http_status(status_code: int):
    """Map HTTP status codes to exception classes."""
    if status_code in [401, 403]:
        return AuthenticationError
    elif status_code == 400:
        return ValidationError
    elif status_code == 429:
        return RateLimitError
    elif 400 <= status_code < 500:
        return ClientError
    elif 500 <= status_code < 600:
        return ServerError
    else:
        return SigridError


def from_http_status(
    status_code: int, 
    message: str, 
    *,
    response_body: Optional[str] = None,
    details: Optional[Dict[str, Any]] = None,
    cause: Optional[Exception] = None
):
    """Create appropriate exception from HTTP status code."""
    exception_class = _exception_class_for_http_status(status_code)
    
    if issubclass(exception_class, (ClientError, ServerError)):
        return exception_class(
            message, 
            status_code, 
            response_body=response_body, 
            details=details, 
            cause=cause
        )
    else:
        return exception_class(message, details=details, cause=cause)