"""
Exception classes for JWT authentication errors.
"""
from typing import Optional, Dict, Any


class AuthError(Exception):
    """Base authentication error."""
    
    def __init__(self, code: str, message: str, details: Optional[Dict[str, Any]] = None):
        self.code = code
        self.message = message
        self.details = details or {}
        super().__init__(f"{code}: {message}")

    def to_dict(self) -> Dict[str, Any]:
        """Convert error to dictionary for serialization."""
        return {
            "code": self.code,
            "message": self.message,
            "details": self.details
        }


class TokenExpiredError(AuthError):
    """JWT token has expired."""
    
    def __init__(self, details: Optional[Dict[str, Any]] = None):
        super().__init__("AUTH_TOKEN_EXPIRED", "JWT token expired", details)


class InvalidSignatureError(AuthError):
    """JWT token has invalid signature."""
    
    def __init__(self, details: Optional[Dict[str, Any]] = None):
        super().__init__("AUTH_INVALID_SIGNATURE", "Invalid JWT signature", details)


class InvalidTokenError(AuthError):
    """JWT token format is invalid."""
    
    def __init__(self, details: Optional[Dict[str, Any]] = None):
        super().__init__("AUTH_INVALID_TOKEN", "Invalid JWT token format", details)


class MissingTokenError(AuthError):
    """Authentication token is missing."""
    
    def __init__(self, details: Optional[Dict[str, Any]] = None):
        super().__init__("AUTH_MISSING_TOKEN", "Missing authentication token", details)


class InvalidAudienceError(AuthError):
    """JWT token audience is invalid."""
    
    def __init__(self, details: Optional[Dict[str, Any]] = None):
        super().__init__("AUTH_INVALID_AUDIENCE", "Invalid JWT audience", details)


class InvalidIssuerError(AuthError):
    """JWT token issuer is invalid."""
    
    def __init__(self, details: Optional[Dict[str, Any]] = None):
        super().__init__("AUTH_INVALID_ISSUER", "Invalid JWT issuer", details)


class TokenNotYetValidError(AuthError):
    """JWT token is not yet valid (nbf claim)."""
    
    def __init__(self, details: Optional[Dict[str, Any]] = None):
        super().__init__("AUTH_TOKEN_NOT_YET_VALID", "JWT token not yet valid", details)


class AuthProviderError(AuthError):
    """Generic authentication provider error."""
    
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__("AUTH_PROVIDER_ERROR", message, details)


# Mapping from exception messages to specific error classes
ERROR_MAPPING = {
    "expired": TokenExpiredError,
    "signature": InvalidSignatureError,
    "audience": InvalidAudienceError,
    "issuer": InvalidIssuerError,
    "not yet valid": TokenNotYetValidError,
    "nbf": TokenNotYetValidError,
}


def map_jwt_error(error_message: str) -> AuthError:
    """
    Map JWT library error messages to specific AuthError subclasses.
    
    Args:
        error_message: Error message from JWT library
        
    Returns:
        Appropriate AuthError subclass
    """
    error_lower = error_message.lower()
    
    for keyword, error_class in ERROR_MAPPING.items():
        if keyword in error_lower:
            return error_class(details={"original_error": error_message})
    
    # Default to generic invalid token error
    return InvalidTokenError(details={"original_error": error_message})
