"""
Generic JWT token validation provider.
"""
import jwt
from typing import Dict, Any, Optional
from ..core.base import AuthProvider
from ..core.user import User
from ..core.config import JWTConfig
from ..core.errors import (
    AuthError,
    InvalidTokenError,
    AuthProviderError,
    map_jwt_error
)


class JWTProvider(AuthProvider):
    """
    Generic JWT token validation provider.
    
    This provider can validate JWT tokens using standard JWT libraries
    and is suitable for most JWT-based authentication systems.
    """
    
    def __init__(self, config: JWTConfig):
        """
        Initialize JWT provider with configuration.
        
        Args:
            config: JWT configuration object
        """
        self.config = config
        self._validate_config()
    
    def _validate_config(self) -> None:
        """Validate the provided configuration."""
        if not self.config.certificate:
            raise AuthProviderError("JWT certificate is required")
        
        if not self.config.algorithms:
            raise AuthProviderError("At least one JWT algorithm must be specified")
    
    async def validate_token(self, token: str) -> User:
        """
        Validate JWT token and return user information.
        
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
            # Decode and validate JWT token
            payload = jwt.decode(
                token,
                self.config.certificate,
                algorithms=self.config.algorithms,
                options={
                    "verify_exp": self.config.verify_exp,
                    "verify_aud": self.config.verify_aud,
                    "verify_iss": self.config.verify_iss,
                    "verify_nbf": self.config.verify_nbf
                },
                audience=self.config.audience,
                issuer=self.config.issuer,
                leeway=self.config.leeway
            )
            
            # Extract user information from token payload
            user = self._extract_user_from_payload(payload)
            return user
            
        except jwt.InvalidTokenError as e:
            # Map JWT library errors to our specific error types
            raise map_jwt_error(str(e))
        except Exception as e:
            raise AuthProviderError(f"Unexpected error during token validation: {str(e)}")
    
    def _extract_user_from_payload(self, payload: Dict[str, Any]) -> User:
        """
        Extract user information from JWT payload.
        
        Args:
            payload: Decoded JWT payload
            
        Returns:
            User object
            
        Raises:
            InvalidTokenError: If required user fields are missing
        """
        mapping = self.config.user_mapping
        
        # Extract required fields
        user_id = payload.get(mapping.id_field)
        email = payload.get(mapping.email_field)
        name = payload.get(mapping.name_field)
        
        if not user_id:
            raise InvalidTokenError(details={"reason": f"Missing required field: {mapping.id_field}"})
        
        if not email:
            raise InvalidTokenError(details={"reason": f"Missing required field: {mapping.email_field}"})
        
        if not name:
            name = email  # Fallback to email if name is missing
        
        # Extract optional fields
        display_name = None
        if mapping.display_name_field:
            display_name = payload.get(mapping.display_name_field)
        
        avatar = None
        if mapping.avatar_field:
            avatar = payload.get(mapping.avatar_field)
        
        roles = []
        if mapping.roles_field and mapping.roles_field in payload:
            roles_data = payload[mapping.roles_field]
            if isinstance(roles_data, list):
                roles = [str(role) for role in roles_data]
            elif isinstance(roles_data, str):
                roles = [roles_data]
        
        permissions = []
        if mapping.permissions_field and mapping.permissions_field in payload:
            perms_data = payload[mapping.permissions_field]
            if isinstance(perms_data, list):
                permissions = [str(perm) for perm in perms_data]
            elif isinstance(perms_data, str):
                permissions = [perms_data]
        
        # Store all payload data in metadata
        metadata = {
            "jwt_payload": payload,
            "provider": self.get_provider_name()
        }
        
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
        return "jwt"
    
    def get_provider_version(self) -> Optional[str]:
        """Get the version of the JWT library being used."""
        return jwt.__version__
    
    def is_configured(self) -> bool:
        """Check if this provider is properly configured."""
        try:
            self._validate_config()
            return True
        except AuthProviderError:
            return False
    
    async def health_check(self) -> bool:
        """
        Perform a health check on the JWT provider.
        
        This validates the certificate format and algorithms.
        """
        if not self.is_configured():
            return False
        
        try:
            # Try to load the certificate to verify it's valid
            # This is a basic check - in a real scenario you might want
            # to verify certificate expiration, etc.
            from cryptography import x509
            from cryptography.hazmat.backends import default_backend
            
            if self.config.certificate.startswith("-----BEGIN"):
                # PEM format certificate
                x509.load_pem_x509_certificate(
                    self.config.certificate.encode(), 
                    default_backend()
                )
            else:
                # Assume it's a raw key/secret
                pass
            
            return True
        except Exception:
            return False
