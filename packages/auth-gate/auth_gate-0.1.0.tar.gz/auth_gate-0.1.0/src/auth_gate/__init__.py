"""
Tradelink Authentication Client

Enterprise authentication client for microservices with Kong/Keycloak integration.
"""

from .config import AuthMode, AuthSettings
from .fastapi_utils import (
    get_current_user,
    get_optional_user,
    require_admin,
    require_customer,
    require_moderator,
    require_roles,
    require_scopes,
    require_supplier,
    require_supplier_or_admin,
    verify_hmac_signature,
)
from .middleware import AuthMiddleware
from .s2s_auth import CircuitBreaker, CircuitBreakerOpenError, ServiceAuthClient
from .schemas import UserContext
from .user_auth import UserValidator

__version__ = "1.0.0"

__all__ = [
    # Configuration
    "AuthSettings",
    "AuthMode",
    # Schemas
    "UserContext",
    # User Authentication
    "UserValidator",
    # Service-to-Service
    "ServiceAuthClient",
    "CircuitBreaker",
    "CircuitBreakerOpenError",
    # Middleware
    "AuthMiddleware",
    # FastAPI Dependencies
    "get_current_user",
    "get_optional_user",
    "require_roles",
    "require_scopes",
    "require_admin",
    "require_supplier",
    "require_customer",
    "require_moderator",
    "require_supplier_or_admin",
    "verify_hmac_signature",
]
