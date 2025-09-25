"""
Abstract base class for authentication providers.
"""
from abc import ABC, abstractmethod
from typing import Optional
from .user import User


class AuthProvider(ABC):
    """
    Abstract base class for authentication providers.
    
    All authentication providers must implement this interface
    to ensure consistent behavior across different auth systems.
    """
    
    @abstractmethod
    async def validate_token(self, token: str) -> User:
        """
        Validate an authentication token and return user information.
        
        Args:
            token: The authentication token to validate
            
        Returns:
            User object with validated user information
            
        Raises:
            AuthError: If token validation fails for any reason
        """
        pass
    
    @abstractmethod
    def get_provider_name(self) -> str:
        """
        Get the name of this authentication provider.
        
        Returns:
            Provider name (e.g., "jwt", "casdoor", "oauth2")
        """
        pass
    
    def get_provider_version(self) -> Optional[str]:
        """
        Get the version of this authentication provider.
        
        Returns:
            Provider version string, or None if not applicable
        """
        return None
    
    def is_configured(self) -> bool:
        """
        Check if this provider is properly configured.
        
        Returns:
            True if provider is ready to validate tokens, False otherwise
        """
        return True
    
    async def health_check(self) -> bool:
        """
        Perform a health check on the authentication provider.
        
        This can be used to verify connectivity to external services,
        certificate validity, etc.
        
        Returns:
            True if provider is healthy, False otherwise
        """
        return self.is_configured()
