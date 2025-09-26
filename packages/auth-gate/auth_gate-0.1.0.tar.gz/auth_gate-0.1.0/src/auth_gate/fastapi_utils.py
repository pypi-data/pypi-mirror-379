"""
FastAPI dependency injection utilities for authentication
"""

import logging
from typing import Optional

from fastapi import Depends, Header, HTTPException, Request, status

from .config import get_settings
from .schemas import UserContext
from .user_auth import HMACVerifier, get_user_validator

logger = logging.getLogger(__name__)


# Core authentication dependencies
async def get_current_user(
    request: Request,
    authorization: Optional[str] = Header(None),
    x_token_verified: Optional[str] = Header(None, alias="X-Token-Verified"),
    x_user_id: Optional[str] = Header(None, alias="X-User-ID"),
    x_username: Optional[str] = Header(None, alias="X-Username"),
    x_user_email: Optional[str] = Header(None, alias="X-User-Email"),
    x_user_roles: Optional[str] = Header(None, alias="X-User-Roles"),
    x_user_scopes: Optional[str] = Header(None, alias="X-User-Scopes"),
    x_session_id: Optional[str] = Header(None, alias="X-Session-ID"),
    x_client_id: Optional[str] = Header(None, alias="X-Client-ID"),
    x_auth_source: Optional[str] = Header(None, alias="X-Auth-Source"),
) -> UserContext:
    """
    Main dependency for getting authenticated user.

    This is the primary dependency to use in your FastAPI endpoints.

    Example:
        @app.get("/api/profile")
        async def get_profile(user: UserContext = Depends(get_current_user)):
            return {"user_id": user.user_id}

    Args:
        Various authentication headers

    Returns:
        UserContext with authenticated user information

    Raises:
        HTTPException: If authentication fails
    """
    validator = get_user_validator()
    return await validator.get_current_user(
        request,
        authorization,
        x_token_verified,
        x_user_id,
        x_username,
        x_user_email,
        x_user_roles,
        x_user_scopes,
        x_session_id,
        x_client_id,
        x_auth_source,
    )


async def get_optional_user(
    request: Request,
    authorization: Optional[str] = Header(None),
    x_token_verified: Optional[str] = Header(None, alias="X-Token-Verified"),
    x_user_id: Optional[str] = Header(None, alias="X-User-ID"),
    x_username: Optional[str] = Header(None, alias="X-Username"),
    x_user_email: Optional[str] = Header(None, alias="X-User-Email"),
    x_user_roles: Optional[str] = Header(None, alias="X-User-Roles"),
    x_user_scopes: Optional[str] = Header(None, alias="X-User-Scopes"),
    x_session_id: Optional[str] = Header(None, alias="X-Session-ID"),
    x_client_id: Optional[str] = Header(None, alias="X-Client-ID"),
    x_auth_source: Optional[str] = Header(None, alias="X-Auth-Source"),
) -> Optional[UserContext]:
    """
    Optional authentication - returns None if not authenticated.

    Use this for endpoints where authentication is optional.

    Example:
        @app.get("/api/products")
        async def list_products(user: Optional[UserContext] = Depends(get_optional_user)):
            if user:
                # Show personalized products
                pass
            else:
                # Show public products
                pass

    Args:
        Various authentication headers

    Returns:
        UserContext if authenticated, None otherwise
    """
    try:
        return await get_current_user(
            request,
            authorization,
            x_token_verified,
            x_user_id,
            x_username,
            x_user_email,
            x_user_roles,
            x_user_scopes,
            x_session_id,
            x_client_id,
            x_auth_source,
        )
    except HTTPException:
        return None


# Role-based access control factories
def require_roles(*required_roles: str):
    """
    Factory for role-checking dependencies.

    Creates a dependency that ensures the user has at least one of the specified roles.

    Example:
        require_editor = require_roles("editor", "admin")

        @app.post("/api/articles")
        async def create_article(user: UserContext = Depends(require_editor)):
            return {"created_by": user.user_id}

    Args:
        *required_roles: Variable number of role names

    Returns:
        Dependency function that validates roles
    """

    async def role_checker(user: UserContext = Depends(get_current_user)) -> UserContext:
        if not user.has_any_role(list(required_roles)):
            logger.warning(f"User {user.user_id} lacks required roles: {required_roles}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Requires one of roles: {', '.join(required_roles)}",
            )
        return user

    return role_checker


def require_scopes(*required_scopes: str):
    """
    Factory for scope-checking dependencies.

    Creates a dependency that ensures the user has all specified scopes.

    Example:
        require_write = require_scopes("write", "publish")

        @app.post("/api/publish")
        async def publish(user: UserContext = Depends(require_write)):
            return {"published_by": user.user_id}

    Args:
        *required_scopes: Variable number of scope names

    Returns:
        Dependency function that validates scopes
    """

    async def scope_checker(user: UserContext = Depends(get_current_user)) -> UserContext:
        missing_scopes = [s for s in required_scopes if not user.has_scope(s)]
        if missing_scopes:
            logger.warning(f"User {user.user_id} lacks required scopes: {missing_scopes}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Requires scopes: {', '.join(missing_scopes)}",
            )
        return user

    return scope_checker


# Pre-configured role dependencies for common use cases
require_admin = require_roles("admin")
"""Dependency that requires admin role"""

require_supplier = require_roles("supplier")
"""Dependency that requires supplier role"""

require_customer = require_roles("customer")
"""Dependency that requires customer role"""

require_moderator = require_roles("moderator")
"""Dependency that requires moderator role"""

require_supplier_or_admin = require_roles("supplier", "admin")
"""Dependency that requires either supplier or admin role"""


# HMAC verification for service-to-service communication
async def verify_hmac_signature(
    request: Request,
    x_authz_signature: Optional[str] = Header(None, alias="X-Authz-Signature"),
    x_authz_ts: Optional[str] = Header(None, alias="X-Authz-Ts"),
    user: UserContext = Depends(get_current_user),
) -> UserContext:
    """
    Dependency to verify HMAC signatures from Kong.

    Use this when Kong is configured with HMAC plugin for additional security.

    Example:
        @app.post("/api/sensitive")
        async def sensitive_operation(user: UserContext = Depends(verify_hmac_signature)):
            return {"verified_user": user.user_id}

    Args:
        request: FastAPI request
        x_authz_signature: HMAC signature header
        x_authz_ts: Timestamp header
        user: Authenticated user context

    Returns:
        UserContext if HMAC is valid

    Raises:
        HTTPException: If HMAC verification fails
    """
    settings = get_settings()

    if not settings.VERIFY_HMAC:
        return user

    if not x_authz_signature or not x_authz_ts:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing HMAC headers",
        )

    verifier = HMACVerifier(settings.INTERNAL_HMAC_KEY)

    if not verifier.verify_signature(
        x_authz_signature,
        x_authz_ts,
        user.user_id,
        user.session_id or "",
        request.method,
        request.url.path,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid HMAC signature",
        )

    return user


# Utility functions for checking authentication mode
def is_using_kong() -> bool:
    """Check if using Kong authentication"""
    settings = get_settings()
    return settings.is_production


def is_using_keycloak() -> bool:
    """Check if using direct Keycloak authentication"""
    settings = get_settings()
    return settings.is_development


def is_bypass_mode() -> bool:
    """Check if in bypass/testing mode"""
    settings = get_settings()
    return settings.is_testing
