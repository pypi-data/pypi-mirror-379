"""
FastAPI adapter for JWT authentication.
"""
from typing import Callable, Optional
from functools import wraps
from ..core.base import AuthProvider
from ..core.user import User
from ..core.errors import AuthError


def create_auth_dependency(auth_provider: AuthProvider) -> Callable:
    """
    Create a FastAPI dependency for JWT authentication.
    
    Args:
        auth_provider: Authentication provider instance
        
    Returns:
        FastAPI dependency function that returns authenticated user
        
    Example:
        ```python
        from fastapi import FastAPI, Depends
        from jwt_auth import CasdoorProvider, CasdoorConfig
        from jwt_auth.adapters.fastapi import create_auth_dependency
        
        app = FastAPI()
        config = CasdoorConfig.from_env()
        auth_provider = CasdoorProvider(config)
        get_current_user = create_auth_dependency(auth_provider)
        
        @app.get("/profile")
        async def get_profile(user: User = Depends(get_current_user)):
            return {"user_id": user.id, "email": user.email}
        ```
    """
    try:
        from fastapi import Depends, HTTPException
        from fastapi.security import HTTPBearer
    except ImportError:
        raise ImportError("FastAPI is required to use the FastAPI adapter. Install it with: pip install fastapi")
    
    security = HTTPBearer(auto_error=False)
    
    async def get_current_user(credentials = Depends(security)) -> User:
        """FastAPI dependency that validates JWT token and returns user."""
        if not credentials:
            raise HTTPException(
                status_code=401,
                detail={
                    "error": {
                        "code": "AUTH_MISSING_AUTHORIZATION",
                        "message": "Missing Authorization header"
                    }
                }
            )
        
        try:
            user = await auth_provider.validate_token(credentials.credentials)
            return user
            
        except AuthError as e:
            raise HTTPException(
                status_code=401,
                detail={"error": e.to_dict()}
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail={
                    "error": {
                        "code": "AUTH_INTERNAL_ERROR", 
                        "message": "Internal authentication error"
                    }
                }
            )
    
    return get_current_user


def create_role_dependency(auth_provider: AuthProvider, required_role: str) -> Callable:
    """
    Create a FastAPI dependency that requires a specific role.
    
    Args:
        auth_provider: Authentication provider instance
        required_role: Role that the user must have
        
    Returns:
        FastAPI dependency function that returns authenticated user with required role
        
    Example:
        ```python
        get_admin_user = create_role_dependency(auth_provider, "admin")
        
        @app.delete("/admin/users/{user_id}")
        async def delete_user(user_id: str, admin: User = Depends(get_admin_user)):
            # Only users with 'admin' role can access this endpoint
            pass
        ```
    """
    get_current_user = create_auth_dependency(auth_provider)
    
    try:
        from fastapi import Depends, HTTPException
    except ImportError:
        raise ImportError("FastAPI is required to use the FastAPI adapter. Install it with: pip install fastapi")
    
    async def get_user_with_role(user: User = Depends(get_current_user)) -> User:
        """FastAPI dependency that checks for required role."""
        if not user.has_role(required_role):
            raise HTTPException(
                status_code=403,
                detail={
                    "error": {
                        "code": "AUTH_INSUFFICIENT_PERMISSIONS",
                        "message": f"Required role '{required_role}' not found"
                    }
                }
            )
        return user
    
    return get_user_with_role


def create_permission_dependency(auth_provider: AuthProvider, required_permission: str) -> Callable:
    """
    Create a FastAPI dependency that requires a specific permission.
    
    Args:
        auth_provider: Authentication provider instance
        required_permission: Permission that the user must have
        
    Returns:
        FastAPI dependency function that returns authenticated user with required permission
    """
    get_current_user = create_auth_dependency(auth_provider)
    
    try:
        from fastapi import Depends, HTTPException
    except ImportError:
        raise ImportError("FastAPI is required to use the FastAPI adapter. Install it with: pip install fastapi")
    
    async def get_user_with_permission(user: User = Depends(get_current_user)) -> User:
        """FastAPI dependency that checks for required permission."""
        if not user.has_permission(required_permission):
            raise HTTPException(
                status_code=403,
                detail={
                    "error": {
                        "code": "AUTH_INSUFFICIENT_PERMISSIONS",
                        "message": f"Required permission '{required_permission}' not found"
                    }
                }
            )
        return user
    
    return get_user_with_permission


def auth_required(auth_provider: AuthProvider):
    """
    Decorator for FastAPI route functions that require authentication.
    
    Args:
        auth_provider: Authentication provider instance
        
    Returns:
        Decorator function
        
    Example:
        ```python
        @app.get("/profile")
        @auth_required(auth_provider)
        async def get_profile(user: User):
            return {"user_id": user.id, "email": user.email}
        ```
    
    Note: This is an alternative to using Depends() directly.
    """
    get_current_user = create_auth_dependency(auth_provider)
    
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # This approach requires manual token extraction
            # It's better to use the Depends() approach in most cases
            raise NotImplementedError(
                "Decorator-based auth is not implemented. "
                "Use create_auth_dependency() with Depends() instead."
            )
        return wrapper
    return decorator
