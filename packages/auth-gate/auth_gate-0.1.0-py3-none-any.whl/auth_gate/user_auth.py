"""
User authentication and validation logic
"""

import base64
import hashlib
import hmac
import logging
import time
from typing import Dict, List, Optional

import httpx
from fastapi import HTTPException, Request, status

from .config import AuthMode, get_settings
from .schemas import UserContext

logger = logging.getLogger(__name__)


class UserValidator:
    """
    Validates user authentication tokens and headers.
    Supports multiple authentication modes for different environments.
    """

    def __init__(self, mode: Optional[AuthMode] = None):
        """
        Initialize user validator.

        Args:
            mode: Authentication mode to use. If None, uses config default.
        """
        settings = get_settings()
        self.mode = mode or settings.auth_mode_enum
        self.keycloak_url = settings.KEYCLOAK_REALM_URL
        self.client_id = settings.KEYCLOAK_CLIENT_ID
        self.client_secret = settings.KEYCLOAK_CLIENT_SECRET
        self._http_client: Optional[httpx.AsyncClient] = None

    @property
    def http_client(self) -> httpx.AsyncClient:
        """Lazy-loaded HTTP client with connection pooling"""
        if self._http_client is None:
            settings = get_settings()
            self._http_client = httpx.AsyncClient(
                timeout=httpx.Timeout(settings.HTTP_TIMEOUT),
                limits=httpx.Limits(
                    max_keepalive_connections=settings.HTTP_MAX_KEEPALIVE_CONNECTIONS
                ),
            )
        return self._http_client

    async def validate_kong_headers(
        self,
        x_token_verified: Optional[str] = None,
        x_user_id: Optional[str] = None,
        x_username: Optional[str] = None,
        x_user_email: Optional[str] = None,
        x_user_roles: Optional[str] = None,
        x_user_scopes: Optional[str] = None,
        x_session_id: Optional[str] = None,
        x_client_id: Optional[str] = None,
        x_auth_source: Optional[str] = None,
    ) -> UserContext:
        """
        Validate headers from Kong token introspector.

        Args:
            Various Kong headers containing user claims

        Returns:
            UserContext with validated user information

        Raises:
            HTTPException: If validation fails
        """
        # Verify Kong has validated the token
        if x_token_verified != "true":
            logger.warning(f"Token not verified by Kong: {x_token_verified}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token not verified by API Gateway",
            )

        # User ID is required
        if not x_user_id:
            logger.error("Missing X-User-ID header from Kong")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication headers",
            )

        # Parse roles and scopes
        roles = []
        if x_user_roles:
            roles = [r.strip() for r in x_user_roles.split(",") if r.strip()]

        scopes = []
        if x_user_scopes:
            scopes = [s.strip() for s in x_user_scopes.split(" ") if s.strip()]

        return UserContext(
            user_id=x_user_id,
            username=x_username,
            email=x_user_email,
            roles=roles,
            scopes=scopes,
            session_id=x_session_id,
            client_id=x_client_id,
            auth_source=x_auth_source or "kong",
        )

    async def validate_keycloak_token(self, token: str) -> UserContext:
        """
        Direct token validation with Keycloak.

        Args:
            token: Bearer token to validate

        Returns:
            UserContext with validated user information

        Raises:
            HTTPException: If validation fails
        """
        introspection_url = f"{self.keycloak_url}/protocol/openid-connect/token/introspect"

        try:
            response = await self.http_client.post(
                introspection_url,
                data={
                    "token": token,
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )

            if response.status_code != 200:
                logger.error(f"Keycloak introspection failed: {response.status_code}")
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token validation failed",
                )

            data = response.json()

            if not data.get("active"):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token is not active",
                )

            # Extract roles from various claim locations
            roles = self._extract_roles_from_claims(data)

            return UserContext(
                user_id=data.get("sub"),
                username=data.get("username") or data.get("preferred_username"),
                email=data.get("email"),
                roles=roles,
                scopes=data.get("scope", "").split(" "),
                session_id=data.get("sid"),
                client_id=data.get("client_id"),
                auth_source="keycloak",
            )

        except httpx.RequestError as e:
            logger.error(f"Failed to connect to Keycloak: {e}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Authentication service unavailable",
            )

    def _extract_roles_from_claims(self, claims: Dict) -> List[str]:
        """Extract roles from various claim locations"""
        roles = []

        # Realm roles
        if "realm_access" in claims and "roles" in claims["realm_access"]:
            roles.extend(claims["realm_access"]["roles"])

        # Resource/client roles
        if "resource_access" in claims:
            for client, access in claims["resource_access"].items():
                if "roles" in access:
                    # Prefix client roles to distinguish them
                    roles.extend([f"{client}:{role}" for role in access["roles"]])

        return roles

    async def get_current_user(
        self,
        request: Request,
        authorization: Optional[str] = None,
        x_token_verified: Optional[str] = None,
        x_user_id: Optional[str] = None,
        x_username: Optional[str] = None,
        x_user_email: Optional[str] = None,
        x_user_roles: Optional[str] = None,
        x_user_scopes: Optional[str] = None,
        x_session_id: Optional[str] = None,
        x_client_id: Optional[str] = None,
        x_auth_source: Optional[str] = None,
    ) -> UserContext:
        """
        Main authentication method supporting multiple modes.

        Args:
            request: FastAPI request object
            authorization: Authorization header
            Various Kong headers

        Returns:
            UserContext with authenticated user information

        Raises:
            HTTPException: If authentication fails
        """
        if self.mode == AuthMode.BYPASS:
            # Testing mode - return mock user
            logger.warning("SECURITY BYPASS MODE - FOR TESTING ONLY")
            return UserContext(
                user_id="test_user",
                username="testuser",
                roles=["admin"],
                auth_source="bypass",
                email="test@example.com",
                session_id="test_session",
                client_id="test_client",
            )

        elif self.mode == AuthMode.KONG_HEADERS:
            # Production mode - validate Kong headers
            return await self.validate_kong_headers(
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

        elif self.mode == AuthMode.DIRECT_KEYCLOAK:
            # Development mode - validate directly with Keycloak
            if not authorization or not authorization.startswith("Bearer "):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Missing or invalid authorization header",
                )

            token = authorization.replace("Bearer ", "")
            return await self.validate_keycloak_token(token)

        else:
            raise ValueError(f"Invalid auth mode: {self.mode}")

    async def close(self):
        """Clean up resources"""
        if self._http_client:
            await self._http_client.aclose()
            self._http_client = None


class HMACVerifier:
    """
    Verifies HMAC signatures for service-to-service communication.
    Used when Kong is configured with HMAC plugin.
    """

    def __init__(self, secret_key: str, max_skew_seconds: int = 60):
        """
        Initialize HMAC verifier.

        Args:
            secret_key: HMAC secret key
            max_skew_seconds: Maximum allowed timestamp skew
        """
        self.secret_key = secret_key.encode("utf-8")
        self.max_skew_seconds = max_skew_seconds

    def verify_signature(
        self,
        signature: str,
        timestamp: str,
        user_id: str,
        session_id: str,
        method: str,
        path: str,
    ) -> bool:
        """
        Verify HMAC signature matches expected value.

        Args:
            signature: HMAC signature from header
            timestamp: Request timestamp
            user_id: User ID from context
            session_id: Session ID from context
            method: HTTP method
            path: Request path

        Returns:
            True if signature is valid
        """
        try:
            # Check timestamp freshness
            req_timestamp = int(timestamp)
            current_time = int(time.time())

            if abs(current_time - req_timestamp) > self.max_skew_seconds:
                logger.warning(f"HMAC timestamp too old: {req_timestamp}")
                return False

            # Reconstruct payload (must match Kong's format)
            payload = "|".join(
                [
                    user_id or "",
                    session_id or "",
                    timestamp,
                    method,
                    path,
                ]
            )

            # Calculate expected signature
            expected_sig = base64.b64encode(
                hmac.new(
                    self.secret_key,
                    payload.encode("utf-8"),
                    hashlib.sha256,
                ).digest()
            ).decode("utf-8")

            # Constant-time comparison
            return hmac.compare_digest(signature, expected_sig)

        except (ValueError, TypeError) as e:
            logger.error(f"HMAC verification error: {e}")
            return False


# Global validator instance management
_user_validator: Optional[UserValidator] = None


def get_user_validator() -> UserValidator:
    """Get or create user validator instance"""
    global _user_validator
    if _user_validator is None:
        _user_validator = UserValidator()
    return _user_validator


async def cleanup_user_validator():
    """Clean up user validator resources"""
    global _user_validator
    if _user_validator:
        await _user_validator.close()
        _user_validator = None
