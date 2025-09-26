"""
Tests for FastAPI utility functions
"""

from unittest.mock import Mock, patch

import pytest
from fastapi import Depends, FastAPI, HTTPException
from fastapi.testclient import TestClient

from auth_gate import UserContext
from auth_gate.fastapi_utils import (
    get_optional_user,
    is_bypass_mode,
    is_using_keycloak,
    is_using_kong,
    require_admin,
    require_roles,
    require_scopes,
    verify_hmac_signature,
)


@pytest.fixture
def test_app():
    """Create test FastAPI application"""
    return FastAPI()


class TestAuthenticationDependencies:
    """Test authentication dependencies"""

    def test_require_roles_success(self, test_app, sample_user_context, kong_headers):
        """Test require_roles with valid roles"""
        require_editor = require_roles("customer", "editor")

        @test_app.get("/test")
        async def test_endpoint(user: UserContext = Depends(require_editor)):
            return {"user_id": user.user_id}

        client = TestClient(test_app)

        with patch(
            "auth_gate.fastapi_utils.get_current_user", return_value=sample_user_context
        ):
            response = client.get("/test", headers=kong_headers)
            assert response.status_code == 200
            assert response.json()["user_id"] == "test-user-123"

    def test_require_roles_failure(self, test_app, sample_user_context, kong_headers):
        """Test require_roles with invalid roles"""
        require_admin_only = require_roles("admin")

        @test_app.get("/test")
        async def test_endpoint(user: UserContext = Depends(require_admin_only)):
            return {"user_id": user.user_id}

        client = TestClient(test_app)

        with patch(
            "auth_gate.fastapi_utils.get_current_user", return_value=sample_user_context
        ):
            response = client.get("/test", headers=kong_headers)
            assert response.status_code == 403
            assert "Requires one of roles" in response.json()["detail"]

    def test_require_admin_with_admin_user(self, test_app, admin_user_context, kong_headers):
        """Test require_admin with admin user"""
        kong_headers["X-User-Roles"] = "admin"
        kong_headers["X-User-ID"] = "admin-user-789"
        kong_headers["X-Username"] = "adminuser"
        kong_headers["X-User-Email"] = "admin@example.com"

        @test_app.get("/test")
        async def test_endpoint(user: UserContext = Depends(require_admin)):
            return {"user_id": user.user_id}

        client = TestClient(test_app)

        with patch(
            "auth_gate.fastapi_utils.get_current_user", return_value=admin_user_context
        ):
            response = client.get("/test", headers=kong_headers)
            assert response.status_code == 200
            assert response.json()["user_id"] == "admin-user-789"

    def test_require_scopes_success(self, test_app, sample_user_context, kong_headers):
        """Test require_scopes with valid scopes"""
        require_read_write = require_scopes("read", "write")

        @test_app.get("/test")
        async def test_endpoint(user: UserContext = Depends(require_read_write)):
            return {"user_id": user.user_id}

        client = TestClient(test_app)

        with patch(
            "auth_gate.fastapi_utils.get_current_user", return_value=sample_user_context
        ):
            response = client.get("/test", headers=kong_headers)
            assert response.status_code == 200

    def test_require_scopes_failure(self, test_app, sample_user_context, kong_headers):
        """Test require_scopes with missing scopes"""
        require_admin_scope = require_scopes("admin")

        @test_app.get("/test")
        async def test_endpoint(user: UserContext = Depends(require_admin_scope)):
            return {"user_id": user.user_id}

        client = TestClient(test_app)

        with patch(
            "auth_gate.fastapi_utils.get_current_user", return_value=sample_user_context
        ):
            response = client.get("/test", headers=kong_headers)
            assert response.status_code == 403
            assert "Requires scopes" in response.json()["detail"]

    @pytest.mark.asyncio
    async def test_get_optional_user_with_auth(self, sample_user_context):
        """Test get_optional_user with authentication"""
        mock_request = Mock()

        with patch(
            "auth_gate.fastapi_utils.get_current_user", return_value=sample_user_context
        ):
            user = await get_optional_user(mock_request)
            assert user is not None
            assert user.user_id == "test-user-123"

    @pytest.mark.asyncio
    async def test_get_optional_user_without_auth(self):
        """Test get_optional_user without authentication"""
        mock_request = Mock()

        with patch(
            "auth_gate.fastapi_utils.get_current_user",
            side_effect=HTTPException(status_code=401, detail="Unauthorized"),
        ):
            user = await get_optional_user(mock_request)
            assert user is None


class TestHMACVerification:
    """Test HMAC verification dependency"""

    @pytest.mark.asyncio
    async def test_verify_hmac_signature_disabled(self, sample_user_context, mock_settings):
        """Test HMAC verification when disabled"""
        mock_settings.VERIFY_HMAC = False

        with patch("auth_gate.fastapi_utils.get_settings", return_value=mock_settings):
            mock_request = Mock()
            user = await verify_hmac_signature(
                mock_request, x_authz_signature=None, x_authz_ts=None, user=sample_user_context
            )
            assert user == sample_user_context

    @pytest.mark.asyncio
    async def test_verify_hmac_signature_missing_headers(self, sample_user_context, mock_settings):
        """Test HMAC verification with missing headers"""
        mock_settings.VERIFY_HMAC = True

        with patch("auth_gate.fastapi_utils.get_settings", return_value=mock_settings):
            mock_request = Mock()

            with pytest.raises(HTTPException) as exc_info:
                await verify_hmac_signature(
                    mock_request, x_authz_signature=None, x_authz_ts=None, user=sample_user_context
                )

            assert exc_info.value.status_code == 401
            assert "Missing HMAC headers" in exc_info.value.detail


class TestUtilityFunctions:
    """Test utility functions"""

    def test_is_using_kong(self, mock_settings):
        """Test is_using_kong utility"""
        mock_settings.AUTH_MODE = "kong_headers"

        with patch("auth_gate.fastapi_utils.get_settings", return_value=mock_settings):
            assert is_using_kong() is True

        mock_settings.AUTH_MODE = "direct_keycloak"
        with patch("auth_gate.fastapi_utils.get_settings", return_value=mock_settings):
            assert is_using_kong() is False

    def test_is_using_keycloak(self, mock_settings):
        """Test is_using_keycloak utility"""
        mock_settings.AUTH_MODE = "direct_keycloak"

        with patch("auth_gate.fastapi_utils.get_settings", return_value=mock_settings):
            assert is_using_keycloak() is True

        mock_settings.AUTH_MODE = "kong_headers"
        with patch("auth_gate.fastapi_utils.get_settings", return_value=mock_settings):
            assert is_using_keycloak() is False

    def test_is_bypass_mode(self, mock_settings):
        """Test is_bypass_mode utility"""
        mock_settings.AUTH_MODE = "bypass"

        with patch("auth_gate.fastapi_utils.get_settings", return_value=mock_settings):
            assert is_bypass_mode() is True

        mock_settings.AUTH_MODE = "kong_headers"
        with patch("auth_gate.fastapi_utils.get_settings", return_value=mock_settings):
            assert is_bypass_mode() is False
