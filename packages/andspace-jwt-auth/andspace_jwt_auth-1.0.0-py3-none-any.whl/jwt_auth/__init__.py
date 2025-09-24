"""
JWT Auth Library - Framework-agnostic JWT token validation.

A lightweight, framework-agnostic library for JWT token validation with support
for multiple providers and easy integration with web frameworks.
"""

from .core.user import User
from .core.errors import (
    AuthError,
    TokenExpiredError,
    InvalidSignatureError,
    InvalidTokenError,
    MissingTokenError,
    InvalidAudienceError,
    InvalidIssuerError,
    TokenNotYetValidError,
    AuthProviderError
)
from .core.base import AuthProvider
from .providers.jwt_provider import JWTProvider
from .providers.casdoor import CasdoorProvider
from .core.config import JWTConfig, CasdoorConfig

__version__ = "1.0.0"
__author__ = "And"
__email__ = "and.webdev@gmail.com"
__description__ = "Framework-agnostic JWT token validation library"

__all__ = [
    # Core classes
    "User",
    "AuthProvider",
    
    # Exceptions
    "AuthError",
    "TokenExpiredError", 
    "InvalidSignatureError",
    "InvalidTokenError",
    "MissingTokenError",
    "InvalidAudienceError",
    "InvalidIssuerError",
    "TokenNotYetValidError",
    "AuthProviderError",
    
    # Providers
    "JWTProvider",
    "CasdoorProvider",
    
    # Configuration
    "JWTConfig",
    "CasdoorConfig",
]
