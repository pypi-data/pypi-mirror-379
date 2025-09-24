"""
Example usage of JWT Auth Library.
"""
import asyncio
import os
from jwt_auth import (
    CasdoorProvider, 
    CasdoorConfig, 
    JWTProvider,
    JWTConfig,
    AuthError,
    User
)


async def example_casdoor_validation():
    """Example: Casdoor token validation."""
    print("=== Casdoor Token Validation Example ===")
    
    # Configure Casdoor (in real usage, load from env or config file)
    config = CasdoorConfig(
        endpoint="https://auth.appz.cloud",
        client_id="your-client-id",
        client_secret="your-client-secret",
        certificate="""-----BEGIN CERTIFICATE-----
MIIBkTCB+wIJANkqU3mLk3+XMA0GCSqGSIb3DQEBCwUAMBYxFDASBgNVBAMMC2Nh
c2Rvb3IuY29tMB4XDTI0MTAyODA3NDUwOVoXDTM0MTAyNjA3NDUwOVowFjEUMBIG
... (your certificate content)
-----END CERTIFICATE-----""",
        org_name="flame-go",
        app_name="whisper_dev"
    )
    
    # Create provider
    auth_provider = CasdoorProvider(config)
    
    # Check provider health
    is_healthy = await auth_provider.health_check()
    print(f"Provider health: {'✅ Healthy' if is_healthy else '❌ Unhealthy'}")
    
    # Example token validation
    test_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."  # Your test token
    
    try:
        user = await auth_provider.validate_token(test_token)
        print(f"✅ Authentication successful!")
        print(f"   User ID: {user.id}")
        print(f"   Email: {user.email}")
        print(f"   Name: {user.name}")
        print(f"   Display Name: {user.display_name}")
        print(f"   Roles: {user.roles}")
        print(f"   Provider: {user.metadata.get('provider')}")
        
    except AuthError as e:
        print(f"❌ Authentication failed: {e.code}")
        print(f"   Message: {e.message}")
        print(f"   Details: {e.details}")


async def example_generic_jwt():
    """Example: Generic JWT validation."""
    print("\n=== Generic JWT Validation Example ===")
    
    # Configure generic JWT
    config = JWTConfig(
        certificate="""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...
-----END PUBLIC KEY-----""",
        algorithms=["RS256"],
        verify_exp=True,
        verify_aud=True,
        audience="your-audience",
        issuer="your-issuer"
    )
    
    # Create provider
    auth_provider = JWTProvider(config)
    
    print(f"Provider: {auth_provider.get_provider_name()}")
    print(f"Version: {auth_provider.get_provider_version()}")
    print(f"Configured: {'✅ Yes' if auth_provider.is_configured() else '❌ No'}")


async def example_error_handling():
    """Example: Comprehensive error handling."""
    print("\n=== Error Handling Example ===")
    
    from jwt_auth import (
        TokenExpiredError,
        InvalidSignatureError,
        InvalidTokenError,
        MissingTokenError
    )
    
    config = CasdoorConfig.from_env() if all([
        os.getenv("CASDOOR_ENDPOINT"),
        os.getenv("CASDOOR_CLIENT_ID"),
        os.getenv("CASDOOR_CLIENT_SECRET"),
        os.getenv("CASDOOR_CERTIFICATE")
    ]) else None
    
    if not config:
        print("❌ Casdoor not configured (set environment variables)")
        return
    
    auth_provider = CasdoorProvider(config)
    
    # Test different error scenarios
    test_cases = [
        ("", "Empty token"),
        ("invalid", "Invalid token format"),
        ("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.invalid", "Invalid token"),
    ]
    
    for token, description in test_cases:
        try:
            user = await auth_provider.validate_token(token)
            print(f"✅ {description}: Success (unexpected)")
        except TokenExpiredError:
            print(f"⏰ {description}: Token expired")
        except InvalidSignatureError:
            print(f"🔐 {description}: Invalid signature")
        except InvalidTokenError:
            print(f"🔍 {description}: Invalid token format")
        except MissingTokenError:
            print(f"❓ {description}: Missing token")
        except AuthError as e:
            print(f"❌ {description}: {e.code}")


def example_fastapi_integration():
    """Example: FastAPI integration (demonstration only)."""
    print("\n=== FastAPI Integration Example ===")
    
    try:
        from fastapi import FastAPI, Depends, HTTPException
        from jwt_auth.adapters.fastapi import create_auth_dependency
        
        print("FastAPI integration code example:")
        print("""
from fastapi import FastAPI, Depends
from jwt_auth import CasdoorProvider, CasdoorConfig, User
from jwt_auth.adapters.fastapi import create_auth_dependency

app = FastAPI()

# Setup authentication
config = CasdoorConfig.from_env()
auth_provider = CasdoorProvider(config)
get_current_user = create_auth_dependency(auth_provider)

@app.get("/profile")
async def get_profile(user: User = Depends(get_current_user)):
    return {
        "user_id": user.id,
        "email": user.email,
        "name": user.name,
        "roles": user.roles
    }

@app.get("/admin")
async def admin_endpoint(user: User = Depends(get_current_user)):
    if not user.has_role("admin"):
        raise HTTPException(403, "Admin role required")
    return {"message": "Admin access granted"}
        """)
        
    except ImportError:
        print("❌ FastAPI not installed. Install with: pip install fastapi")


async def example_user_object():
    """Example: User object features."""
    print("\n=== User Object Features Example ===")
    
    # Create a sample user (normally this would come from token validation)
    user = User(
        id="user123",
        email="user@example.com", 
        name="John Doe",
        display_name="Johnny",
        avatar="https://example.com/avatar.jpg",
        roles=["user", "admin"],
        permissions=["read", "write", "delete"],
        metadata={
            "provider": "casdoor",
            "org": "my-org",
            "custom_field": "custom_value"
        }
    )
    
    print(f"User: {user.get_display_name()}")
    print(f"Has 'admin' role: {'✅' if user.has_role('admin') else '❌'}")
    print(f"Has 'super_admin' role: {'✅' if user.has_role('super_admin') else '❌'}")
    print(f"Has 'write' permission: {'✅' if user.has_permission('write') else '❌'}")
    print(f"Has any admin roles: {'✅' if user.has_any_role(['admin', 'super_admin']) else '❌'}")
    print(f"Has all required roles: {'✅' if user.has_all_roles(['user', 'admin']) else '❌'}")
    
    # Convert to dict for serialization
    user_dict = user.to_dict()
    print(f"Serializable: {len(str(user_dict))} chars")
    
    # Recreate from dict
    user_copy = User.from_dict(user_dict)
    print(f"Roundtrip successful: {'✅' if user_copy.email == user.email else '❌'}")


async def main():
    """Run all examples."""
    print("JWT Auth Library Examples")
    print("=" * 50)
    
    await example_generic_jwt()
    await example_error_handling()
    example_fastapi_integration()
    await example_user_object()
    # await example_casdoor_validation()  # Uncomment if you have valid config


if __name__ == "__main__":
    asyncio.run(main())
