"""
Casdoor-specific JWT token validation provider.
"""
from typing import Dict, Any, Optional
from ..core.user import User
from ..core.config import CasdoorConfig
from ..core.errors import (
    AuthError,
    AuthProviderError,
    InvalidTokenError
)
from .jwt_provider import JWTProvider


class CasdoorProvider(JWTProvider):
    """
    Casdoor-specific JWT token validation provider.
    
    This provider extends the generic JWT provider with Casdoor-specific
    functionality and uses the Casdoor SDK when available.
    """
    
    def __init__(self, config: CasdoorConfig):
        """
        Initialize Casdoor provider with configuration.
        
        Args:
            config: Casdoor configuration object
        """
        self.casdoor_config = config
        self.casdoor_sdk = None
        super().__init__(config)
        self._initialize_casdoor_sdk()
    
    def _initialize_casdoor_sdk(self) -> None:
        """Initialize Casdoor SDK if available."""
        if not self.casdoor_config.is_configured():
            return
        
        try:
            from casdoor import CasdoorSDK
            
            self.casdoor_sdk = CasdoorSDK(
                endpoint=self.casdoor_config.endpoint,
                client_id=self.casdoor_config.client_id,
                client_secret=self.casdoor_config.client_secret,
                certificate=self.casdoor_config.certificate,
                org_name=self.casdoor_config.org_name,
                application_name=self.casdoor_config.app_name
            )
        except ImportError:
            # Casdoor SDK not available, fall back to generic JWT validation
            self.casdoor_sdk = None
        except Exception as e:
            raise AuthProviderError(f"Failed to initialize Casdoor SDK: {str(e)}")
    
    async def validate_token(self, token: str) -> User:
        """
        Validate Casdoor JWT token and return user information.
        
        Uses Casdoor SDK if available, otherwise falls back to generic JWT validation.
        
        Args:
            token: JWT token string
            
        Returns:
            User object with validated user information
            
        Raises:
            AuthError: If token validation fails
        """
        if not token:
            raise InvalidTokenError(details={"reason": "Empty token"})
        
        try:
            if self.casdoor_sdk:
                # Use Casdoor SDK for validation
                claims = self.casdoor_sdk.parse_jwt_token(token)
                if not claims:
                    raise InvalidTokenError(details={"reason": "Casdoor SDK returned no claims"})
                
                return self._extract_casdoor_user(claims)
            else:
                # Fall back to generic JWT validation
                return await super().validate_token(token)
                
        except AuthError:
            # Re-raise our own errors
            raise
        except Exception as e:
            raise AuthProviderError(f"Casdoor token validation failed: {str(e)}")
    
    def _extract_casdoor_user(self, claims: Dict[str, Any]) -> User:
        """
        Extract user information from Casdoor JWT claims.
        
        Args:
            claims: Casdoor JWT claims
            
        Returns:
            User object
            
        Raises:
            InvalidTokenError: If required user fields are missing
        """
        # Casdoor-specific claim extraction
        user_id = claims.get("id") or claims.get("sub")
        email = claims.get("email")
        name = claims.get("name")
        display_name = claims.get("displayName")
        avatar = claims.get("avatar")
        
        if not user_id:
            raise InvalidTokenError(details={"reason": "Missing user ID in Casdoor token"})
        
        if not email:
            raise InvalidTokenError(details={"reason": "Missing email in Casdoor token"})
        
        if not name:
            name = email  # Fallback to email
        
        # Extract Casdoor-specific metadata
        metadata = {
            "casdoor": {
                "owner": claims.get("owner"),
                "org": claims.get("org"),
                "application": claims.get("application"),
                "iss": claims.get("iss"),
                "aud": claims.get("aud"),
                "exp": claims.get("exp"),
                "iat": claims.get("iat")
            },
            "jwt_payload": claims,
            "provider": self.get_provider_name()
        }
        
        # Casdoor doesn't typically have roles/permissions in JWT
        # These would usually come from separate API calls
        roles = []
        permissions = []
        
        return User(
            id=str(user_id),
            email=str(email),
            name=str(name),
            display_name=display_name,
            avatar=avatar,
            roles=roles,
            permissions=permissions,
            metadata=metadata
        )
    
    def get_provider_name(self) -> str:
        """Get the name of this authentication provider."""
        return "casdoor"
    
    def get_provider_version(self) -> Optional[str]:
        """Get the version of the Casdoor SDK if available."""
        if self.casdoor_sdk:
            try:
                import casdoor
                return casdoor.__version__
            except AttributeError:
                return "unknown"
        return "sdk_not_available"
    
    def is_configured(self) -> bool:
        """Check if this provider is properly configured."""
        return self.casdoor_config.is_configured()
    
    async def health_check(self) -> bool:
        """
        Perform a health check on the Casdoor provider.
        
        This checks configuration and optionally tests connectivity
        to the Casdoor endpoint.
        """
        if not self.is_configured():
            return False
        
        # Basic configuration check
        base_health = await super().health_check()
        if not base_health:
            return False
        
        # If we have SDK, we could test connectivity
        # For now, just return the base health check
        return True
    
    def get_casdoor_endpoint(self) -> str:
        """Get the Casdoor endpoint URL."""
        return self.casdoor_config.endpoint
    
    def get_casdoor_org(self) -> str:
        """Get the Casdoor organization name."""
        return self.casdoor_config.org_name
    
    def get_casdoor_app(self) -> str:
        """Get the Casdoor application name."""
        return self.casdoor_config.app_name
