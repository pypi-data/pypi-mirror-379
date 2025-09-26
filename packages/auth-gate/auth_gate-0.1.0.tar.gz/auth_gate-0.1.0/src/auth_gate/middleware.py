"""
FastAPI middleware for authentication
"""

import logging
import time
from typing import Optional, Set

from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from .config import get_settings
from .user_auth import get_user_validator

logger = logging.getLogger(__name__)


class AuthMiddleware(BaseHTTPMiddleware):
    """
    Middleware for handling authentication in Kong/Keycloak environment.

    Features:
    - Automatic authentication based on configured mode
    - Configurable path exclusions
    - Optional authentication paths
    - Request enrichment with user context
    - Security headers injection
    """

    def __init__(
        self,
        app: ASGIApp,
        excluded_paths: Optional[Set[str]] = None,
        excluded_prefixes: Optional[Set[str]] = None,
        optional_auth_paths: Optional[Set[str]] = None,
    ):
        """
        Initialize authentication middleware.

        Args:
            app: ASGI application
            excluded_paths: Exact paths that don't require authentication
            excluded_prefixes: Path prefixes that don't require authentication
            optional_auth_paths: Paths where authentication is optional
        """
        super().__init__(app)

        # Paths that don't require authentication
        self.excluded_paths = excluded_paths or {
            "/health",
            "/metrics",
            "/openapi.json",
            "/favicon.ico",
        }

        # Path prefixes that don't require authentication
        self.excluded_prefixes = excluded_prefixes or {
            "/api/docs",
            "/api/redoc",
            "/static",
            "/_health",
        }

        # Paths where authentication is optional
        self.optional_auth_paths = optional_auth_paths or set()

        self.validator = get_user_validator()
        self.settings = get_settings()

    def is_excluded(self, path: str) -> bool:
        """Check if path is excluded from authentication"""
        # Exact match
        if path in self.excluded_paths:
            return True

        # Prefix match
        for prefix in self.excluded_prefixes:
            if path.startswith(prefix):
                return True

        return False

    def is_optional_auth(self, path: str) -> bool:
        """Check if path has optional authentication"""
        return path in self.optional_auth_paths

    async def dispatch(self, request: Request, call_next):
        """Process request with authentication"""
        start_time = time.time()

        # Add request ID for tracing
        request_id = request.headers.get("X-Request-ID", str(time.time()))

        # Skip authentication for excluded paths
        if self.is_excluded(request.url.path):
            response = await call_next(request)
            self._add_security_headers(response, request_id, start_time)
            return response

        try:
            # Extract authentication headers
            auth_headers = self._extract_auth_headers(request)

            # Check if we have any authentication
            has_auth = self._has_authentication(auth_headers)

            if not has_auth:
                # No authentication present
                if self.is_optional_auth(request.url.path):
                    request.state.user = None
                else:
                    logger.warning(f"Missing authentication for {request.url.path}")
                    return JSONResponse(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        content={
                            "error": "unauthorized",
                            "message": "Authentication required",
                            "request_id": request_id,
                        },
                    )
            else:
                # Validate authentication
                user_context = await self.validator.get_current_user(request, **auth_headers)
                request.state.user = user_context

                # Log authentication details
                logger.info(
                    f"Authenticated request: user={user_context.user_id}, "
                    f"roles={user_context.roles}, path={request.url.path}, "
                    f"method={request.method}, source={user_context.auth_source}"
                )

            # Process request
            response = await call_next(request)

            # Add security headers
            self._add_security_headers(response, request_id, start_time)

            return response

        except HTTPException as e:
            # Handle authentication exceptions
            logger.warning(f"Auth failed: {e.detail}, path={request.url.path}")
            return JSONResponse(
                status_code=e.status_code,
                content={
                    "error": "authentication_failed",
                    "message": e.detail,
                    "request_id": request_id,
                },
            )
        except Exception as e:
            # Handle unexpected errors
            logger.error(f"Middleware error: {e}", exc_info=True)
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "error": "internal_error",
                    "message": "An internal error occurred",
                    "request_id": request_id,
                },
            )

    def _extract_auth_headers(self, request: Request) -> dict:
        """Extract all authentication-related headers"""
        return {
            "authorization": request.headers.get("Authorization"),
            "x_token_verified": request.headers.get("X-Token-Verified"),
            "x_user_id": request.headers.get("X-User-ID"),
            "x_username": request.headers.get("X-Username"),
            "x_user_email": request.headers.get("X-User-Email"),
            "x_user_roles": request.headers.get("X-User-Roles"),
            "x_user_scopes": request.headers.get("X-User-Scopes"),
            "x_session_id": request.headers.get("X-Session-ID"),
            "x_client_id": request.headers.get("X-Client-ID"),
            "x_auth_source": request.headers.get("X-Auth-Source"),
        }

    def _has_authentication(self, auth_headers: dict) -> bool:
        """Check if request has any authentication"""
        if self.settings.is_production:
            # Kong mode - check for verified token header
            return auth_headers.get("x_token_verified") == "true"
        elif self.settings.is_development:
            # Direct Keycloak mode - check for Bearer token
            auth: str = auth_headers.get("authorization", "")
            return auth.startswith("Bearer ")
        elif self.settings.is_testing:
            # Bypass mode - always authenticated
            return True
        return False

    def _add_security_headers(self, response, request_id: str, start_time: float):
        """Add security and performance headers to response"""
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"

        # Add performance metrics
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
