"""
Tests for user authentication
"""

import base64
import hashlib
import hmac
import time
from unittest.mock import AsyncMock, Mock, patch

import httpx
import pytest
from fastapi import HTTPException, Request

from auth_gate import AuthMode
from auth_gate.user_auth import HMACVerifier, UserValidator


class TestUserValidator:
    @pytest.mark.asyncio
    async def test_validate_kong_headers_success(self, kong_headers):
        """Test successful Kong header validation"""
        validator = UserValidator(mode=AuthMode.KONG_HEADERS)

        user = await validator.validate_kong_headers(
            x_token_verified=kong_headers["X-Token-Verified"],
            x_user_id=kong_headers["X-User-ID"],
            x_username=kong_headers["X-Username"],
            x_user_email=kong_headers["X-User-Email"],
            x_user_roles=kong_headers["X-User-Roles"],
            x_user_scopes=kong_headers["X-User-Scopes"],
            x_session_id=kong_headers["X-Session-ID"],
            x_client_id=kong_headers["X-Client-ID"],
            x_auth_source=kong_headers["X-Auth-Source"],
        )

        assert user.user_id == "test-user-123"
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.roles == ["customer", "verified"]
        assert user.scopes == ["read", "write"]

    @pytest.mark.asyncio
    async def test_validate_kong_headers_not_verified(self):
        """Test Kong header validation with unverified token"""
        validator = UserValidator(mode=AuthMode.KONG_HEADERS)

        with pytest.raises(HTTPException) as exc_info:
            await validator.validate_kong_headers(
                x_token_verified="false",
                x_user_id="test-user",
            )

        assert exc_info.value.status_code == 401
        assert "not verified" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_validate_kong_headers_missing_user_id(self):
        """Test Kong header validation with missing user ID"""
        validator = UserValidator(mode=AuthMode.KONG_HEADERS)

        with pytest.raises(HTTPException) as exc_info:
            await validator.validate_kong_headers(
                x_token_verified="true",
                x_user_id=None,
            )

        assert exc_info.value.status_code == 401
        assert "Invalid authentication headers" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_validate_keycloak_token_success(
        self, mock_settings, kc_validator, keycloak_token_response
    ):
        """Test successful Keycloak token validation"""
        with patch.object(httpx.AsyncClient, "post", new=AsyncMock()) as mock_post:
            mock_post.return_value = httpx.Response(status_code=200, json=keycloak_token_response)

            # Call the method
            user = await kc_validator.validate_keycloak_token("test-token")

            assert user.user_id == "test-user-123"
            assert user.username == "testuser"
            assert user.email == "test@example.com"
            assert user.roles == ["customer", "verified"]
            mock_post.assert_called_once()

    @pytest.mark.asyncio
    async def test_validate_keycloak_token_inactive(self, mock_settings, kc_validator):
        """Test Keycloak validation with inactive token"""
        mock_response = {"active": False}

        with patch.object(httpx.AsyncClient, "post", new=AsyncMock()) as mock_post:
            mock_post.return_value = httpx.Response(status_code=200, json=mock_response)

            with pytest.raises(HTTPException) as exc_info:
                await kc_validator.validate_keycloak_token("test-token")

            assert exc_info.value.status_code == 401
            assert "Token is not active" in exc_info.value.detail
            mock_post.assert_called_once()

    @pytest.mark.asyncio
    async def test_validate_keycloak_token_connection_error(self, mock_settings, kc_validator):
        """Test Keycloak validation with connection error"""
        with patch.object(httpx.AsyncClient, "post", new=AsyncMock()) as mock_post:
            mock_post.side_effect = httpx.RequestError("Connection failed")

            with pytest.raises(HTTPException) as exc_info:
                await kc_validator.validate_keycloak_token("test-token")

            assert exc_info.value.status_code == 503
            assert "unavailable" in exc_info.value.detail
            mock_post.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_current_user_bypass_mode(self):
        """Test get_current_user in bypass mode"""
        validator = UserValidator(mode=AuthMode.BYPASS)

        request = Mock(spec=Request)
        user = await validator.get_current_user(request)

        assert user.user_id == "test_user"
        assert user.username == "testuser"
        assert user.roles == ["admin"]
        assert user.auth_source == "bypass"

    @pytest.mark.asyncio
    async def test_get_current_user_kong_mode(self, kong_headers):
        """Test get_current_user in Kong mode"""
        validator = UserValidator(mode=AuthMode.KONG_HEADERS)

        request = Mock(spec=Request)
        user = await validator.get_current_user(
            request,
            x_token_verified=kong_headers["X-Token-Verified"],
            x_user_id=kong_headers["X-User-ID"],
            x_username=kong_headers["X-Username"],
            x_user_email=kong_headers["X-User-Email"],
            x_user_roles=kong_headers["X-User-Roles"],
            x_user_scopes=kong_headers["X-User-Scopes"],
        )

        assert user.user_id == "test-user-123"
        assert user.auth_source == "kong"

    @pytest.mark.asyncio
    async def test_get_current_user_keycloak_mode_no_token(self, mock_settings):
        """Test get_current_user in Keycloak mode without token"""
        validator = UserValidator(mode=AuthMode.DIRECT_KEYCLOAK)

        request = Mock(spec=Request)

        with pytest.raises(HTTPException) as exc_info:
            await validator.get_current_user(request, authorization=None)

        assert exc_info.value.status_code == 401
        assert "Missing or invalid authorization header" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_extract_roles_from_claims(self):
        """Test role extraction from various claim formats"""
        validator = UserValidator()

        # Test realm roles
        claims = {
            "realm_access": {"roles": ["user", "admin"]},
            "resource_access": {
                "app1": {"roles": ["editor"]},
                "app2": {"roles": ["viewer", "contributor"]},
            },
        }

        roles = validator._extract_roles_from_claims(claims)

        assert "user" in roles
        assert "admin" in roles
        assert "app1:editor" in roles
        assert "app2:viewer" in roles
        assert "app2:contributor" in roles


class TestHMACVerifier:
    """Test HMAC verification"""

    def test_verify_signature_success(self):
        """Test successful HMAC signature verification"""
        secret_key = "test-secret-key"
        verifier = HMACVerifier(secret_key)

        timestamp = str(int(time.time()))
        user_id = "user-123"
        session_id = "session-456"
        method = "POST"
        path = "/api/test"

        # Generate correct signature
        payload = "|".join([user_id, session_id, timestamp, method, path])
        signature = base64.b64encode(
            hmac.new(secret_key.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).digest()
        ).decode("utf-8")

        result = verifier.verify_signature(signature, timestamp, user_id, session_id, method, path)

        assert result is True

    def test_verify_signature_invalid(self):
        """Test HMAC verification with invalid signature"""
        verifier = HMACVerifier("test-secret-key")

        timestamp = str(int(time.time()))

        result = verifier.verify_signature(
            "invalid-signature", timestamp, "user-123", "session-456", "POST", "/api/test"
        )

        assert result is False

    def test_verify_signature_expired_timestamp(self):
        """Test HMAC verification with expired timestamp"""
        verifier = HMACVerifier("test-secret-key", max_skew_seconds=60)

        # Timestamp from 2 minutes ago
        old_timestamp = str(int(time.time()) - 120)

        result = verifier.verify_signature(
            "any-signature", old_timestamp, "user-123", "session-456", "POST", "/api/test"
        )

        assert result is False
