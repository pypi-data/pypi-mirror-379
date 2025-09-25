"""
Configuration classes for authentication providers.
"""
import os
import json
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from pathlib import Path


@dataclass
class UserMapping:
    """Configuration for mapping JWT claims to User object fields."""
    
    id_field: str = "sub"
    email_field: str = "email"
    name_field: str = "name"
    display_name_field: Optional[str] = "displayName"
    avatar_field: Optional[str] = "avatar"
    roles_field: Optional[str] = "roles"
    permissions_field: Optional[str] = "permissions"


@dataclass
class JWTConfig:
    """Configuration for JWT token validation."""
    
    # Required settings
    certificate: str
    
    # Optional JWT validation settings
    algorithms: List[str] = field(default_factory=lambda: ["RS256"])
    verify_exp: bool = True
    verify_aud: bool = True
    verify_iss: bool = True
    verify_nbf: bool = True
    
    # Expected values (if verification enabled)
    audience: Optional[str] = None
    issuer: Optional[str] = None
    
    # Claim mapping configuration
    user_mapping: UserMapping = field(default_factory=UserMapping)
    
    # Token extraction settings
    leeway: int = 0  # Seconds of leeway for time-based claims
    
    @classmethod
    def from_env(cls, prefix: str = "JWT") -> "JWTConfig":
        """
        Create configuration from environment variables.
        
        Args:
            prefix: Environment variable prefix (default: JWT)
            
        Returns:
            JWTConfig instance
        """
        certificate = os.getenv(f"{prefix}_CERTIFICATE")
        if not certificate:
            raise ValueError(f"Environment variable {prefix}_CERTIFICATE is required")
        
        return cls(
            certificate=certificate,
            algorithms=os.getenv(f"{prefix}_ALGORITHMS", "RS256").split(","),
            verify_exp=os.getenv(f"{prefix}_VERIFY_EXP", "true").lower() == "true",
            verify_aud=os.getenv(f"{prefix}_VERIFY_AUD", "true").lower() == "true",
            verify_iss=os.getenv(f"{prefix}_VERIFY_ISS", "true").lower() == "true",
            verify_nbf=os.getenv(f"{prefix}_VERIFY_NBF", "true").lower() == "true",
            audience=os.getenv(f"{prefix}_AUDIENCE"),
            issuer=os.getenv(f"{prefix}_ISSUER"),
            leeway=int(os.getenv(f"{prefix}_LEEWAY", "0"))
        )
    
    @classmethod
    def from_file(cls, file_path: Path) -> "JWTConfig":
        """
        Create configuration from JSON file.
        
        Args:
            file_path: Path to JSON configuration file
            
        Returns:
            JWTConfig instance
        """
        with open(file_path) as f:
            data = json.load(f)
        
        return cls(
            certificate=data["certificate"],
            algorithms=data.get("algorithms", ["RS256"]),
            verify_exp=data.get("verify_exp", True),
            verify_aud=data.get("verify_aud", True),
            verify_iss=data.get("verify_iss", True),
            verify_nbf=data.get("verify_nbf", True),
            audience=data.get("audience"),
            issuer=data.get("issuer"),
            leeway=data.get("leeway", 0)
        )


@dataclass
class CasdoorConfig(JWTConfig):
    """Configuration for Casdoor authentication provider."""
    
    # Casdoor-specific settings
    endpoint: str = ""
    client_id: str = ""
    client_secret: str = ""
    org_name: str = "built-in"
    app_name: str = ""
    
    # Override default user mapping for Casdoor
    user_mapping: UserMapping = field(default_factory=lambda: UserMapping(
        id_field="id",
        email_field="email",
        name_field="name",
        display_name_field="displayName",
        avatar_field="avatar"
    ))
    
    @classmethod
    def from_env(cls, prefix: str = "CASDOOR") -> "CasdoorConfig":
        """
        Create Casdoor configuration from environment variables.
        
        Args:
            prefix: Environment variable prefix (default: CASDOOR)
            
        Returns:
            CasdoorConfig instance
        """
        # Required Casdoor settings
        endpoint = os.getenv(f"{prefix}_ENDPOINT")
        client_id = os.getenv(f"{prefix}_CLIENT_ID")
        client_secret = os.getenv(f"{prefix}_CLIENT_SECRET")
        certificate = os.getenv(f"{prefix}_CERTIFICATE")
        
        if not all([endpoint, client_id, client_secret, certificate]):
            missing = []
            if not endpoint: missing.append(f"{prefix}_ENDPOINT")
            if not client_id: missing.append(f"{prefix}_CLIENT_ID")
            if not client_secret: missing.append(f"{prefix}_CLIENT_SECRET")
            if not certificate: missing.append(f"{prefix}_CERTIFICATE")
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        
        return cls(
            certificate=certificate,
            endpoint=endpoint,
            client_id=client_id,
            client_secret=client_secret,
            org_name=os.getenv(f"{prefix}_ORG_NAME", "built-in"),
            app_name=os.getenv(f"{prefix}_APP_NAME", ""),
            algorithms=os.getenv(f"{prefix}_ALGORITHMS", "RS256").split(","),
            verify_exp=os.getenv(f"{prefix}_VERIFY_EXP", "true").lower() == "true",
            verify_aud=os.getenv(f"{prefix}_VERIFY_AUD", "true").lower() == "true",
            verify_iss=os.getenv(f"{prefix}_VERIFY_ISS", "true").lower() == "true",
            verify_nbf=os.getenv(f"{prefix}_VERIFY_NBF", "true").lower() == "true",
            audience=os.getenv(f"{prefix}_AUDIENCE"),
            issuer=os.getenv(f"{prefix}_ISSUER"),
            leeway=int(os.getenv(f"{prefix}_LEEWAY", "0"))
        )
    
    def is_configured(self) -> bool:
        """Check if all required Casdoor settings are provided."""
        return all([
            self.endpoint,
            self.client_id,
            self.client_secret,
            self.certificate
        ])
