"""
Standard User object for authentication results.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


@dataclass
class User:
    """
    Standard user object returned by authentication providers.
    
    This provides a consistent interface regardless of the underlying
    authentication system (Casdoor, Auth0, custom JWT, etc.).
    """
    
    # Core user identity
    id: str
    email: str
    name: str
    
    # Optional display information
    display_name: Optional[str] = None
    avatar: Optional[str] = None
    
    # Authorization data
    roles: List[str] = field(default_factory=list)
    permissions: List[str] = field(default_factory=list)
    
    # Provider-specific and custom metadata
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def has_role(self, role: str) -> bool:
        """Check if user has a specific role."""
        return role in self.roles
    
    def has_permission(self, permission: str) -> bool:
        """Check if user has a specific permission."""
        return permission in self.permissions
    
    def has_any_role(self, roles: List[str]) -> bool:
        """Check if user has any of the specified roles."""
        return any(role in self.roles for role in roles)
    
    def has_all_roles(self, roles: List[str]) -> bool:
        """Check if user has all of the specified roles."""
        return all(role in self.roles for role in roles)
    
    def get_display_name(self) -> str:
        """Get the best available display name."""
        return self.display_name or self.name or self.email
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert user to dictionary for serialization."""
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "display_name": self.display_name,
            "avatar": self.avatar,
            "roles": self.roles,
            "permissions": self.permissions,
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "User":
        """Create User from dictionary."""
        return cls(
            id=data["id"],
            email=data["email"],
            name=data["name"],
            display_name=data.get("display_name"),
            avatar=data.get("avatar"),
            roles=data.get("roles", []),
            permissions=data.get("permissions", []),
            metadata=data.get("metadata", {})
        )
