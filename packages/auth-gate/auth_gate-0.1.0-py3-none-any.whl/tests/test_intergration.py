"""
Integration tests for the auth client package
"""

from unittest.mock import AsyncMock, patch

import httpx
import pytest
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from auth_gate import (
    AuthMiddleware,
    UserContext,
    get_current_user,
    get_optional_user,
    require_admin,
    require_supplier_or_admin,
)


@pytest.fixture
def integrated_app():
    """Create fully integrated FastAPI app"""
    app = FastAPI()

    # Add authentication middleware
    app.add_middleware(
        AuthMiddleware,
        excluded_paths={"/health", "/metrics"},
        excluded_prefixes={"/docs"},
        optional_auth_paths={"/api/products"},
    )

    @app.get("/health")
    async def health():
        return {"status": "healthy"}

    @app.get("/api/profile")
    async def get_profile(user: UserContext = Depends(get_current_user)):
        return {
            "user_id": user.user_id,
            "username": user.username,
            "roles": user.roles,
        }

    @app.get("/api/admin/users")
    async def list_users(admin: UserContext = Depends(require_admin)):
        return {"users": ["user1", "user2"]}

    @app.get("/api/supplier/products")
    async def supplier_products(user: UserContext = Depends(require_supplier_or_admin)):
        return {"products": ["product1", "product2"]}

    @app.get("/api/products")
    async def public_products(user: UserContext = Depends(get_optional_user)):
        if user:
            return {"products": ["product1", "product2"], "personalized": True}
        return {"products": ["product1"], "personalized": False}

    return app


class TestEndToEndIntegration:
    """End-to-end integration tests"""

    def test_health_endpoint_no_auth(self, integrated_app, mock_settings):
        """Test health endpoint requires no authentication"""
        with patch("auth_gate.middleware.get_settings", return_value=mock_settings):
            client = TestClient(integrated_app)
            response = client.get("/health")
            assert response.status_code == 200
            assert response.json()["status"] == "healthy"

    def test_protected_endpoint_with_kong_headers(
        self, integrated_app, mock_settings, kong_headers
    ):
        """Test protected endpoint with Kong headers"""
        with patch("auth_gate.middleware.get_settings", return_value=mock_settings):
            with patch("auth_gate.user_auth.get_settings", return_value=mock_settings):
                with patch(
                    "auth_gate.fastapi_utils.get_user_validator"
                ) as mock_validator:
                    mock_validator.return_value.get_current_user = AsyncMock(
                        return_value=UserContext(
                            user_id="test-user-123",
                            username="testuser",
                            roles=["customer"],
                        )
                    )

                    client = TestClient(integrated_app)
                    response = client.get("/api/profile", headers=kong_headers)
                    assert response.status_code == 200
                    assert response.json()["user_id"] == "test-user-123"

    def test_admin_endpoint_with_insufficient_roles(
        self, integrated_app, mock_settings, kong_headers
    ):
        """Test admin endpoint with insufficient roles"""
        with patch("auth_gate.middleware.get_settings", return_value=mock_settings):
            with patch("auth_gate.user_auth.get_settings", return_value=mock_settings):
                with patch(
                    "auth_gate.fastapi_utils.get_user_validator"
                ) as mock_validator:
                    mock_validator.return_value.get_current_user = AsyncMock(
                        return_value=UserContext(
                            user_id="test-user-123",
                            username="testuser",
                            roles=["customer"],
                        )
                    )

                    client = TestClient(integrated_app)
                    response = client.get("/api/admin/users", headers=kong_headers)
                    assert response.status_code == 403
                    assert "Requires one of roles" in response.json()["detail"]

    def test_optional_auth_endpoint(self, integrated_app, mock_settings, kong_headers):
        """Test optional authentication endpoint"""
        with patch("auth_gate.middleware.get_settings", return_value=mock_settings):
            client = TestClient(integrated_app)

            # Without authentication
            response = client.get("/api/products")
            assert response.status_code == 200
            assert response.json()["personalized"] is False

            # With authentication
            with patch("auth_gate.user_auth.get_settings", return_value=mock_settings):
                with patch(
                    "auth_gate.fastapi_utils.get_user_validator"
                ) as mock_validator:
                    mock_validator.return_value.get_current_user = AsyncMock(
                        return_value=UserContext(
                            user_id="test-user-123",
                            username="testuser",
                            roles=["customer"],
                        )
                    )

                    response = client.get("/api/products", headers=kong_headers)
                    assert response.status_code == 200
                    assert response.json()["personalized"] is True

    @pytest.mark.asyncio
    async def test_service_to_service_auth(
        self, mock_settings, service_auth_client, service_token_response
    ):
        """Test service-to-service authentication flow"""
        with patch("auth_gate.s2s_auth.get_settings", return_value=mock_settings):
            with patch.object(httpx.AsyncClient, "post", new=AsyncMock()) as mock_post:
                mock_post.return_value = httpx.Response(
                    status_code=200,
                    json=service_token_response,
                )
                # Get service token
                token = await service_auth_client.get_service_token()
                assert token.startswith("Bearer ")

                # Token should be cached
                token2 = await service_auth_client.get_service_token()
                assert token == token2
                mock_post.assert_called_once()  # Only one HTTP call made

    def test_bypass_mode_integration(self, integrated_app, mock_settings):
        """Test bypass mode for testing"""
        # Override for this test only (doesn't affect other tests using the fixture)
        mock_settings.AUTH_MODE = "bypass"

        with patch("auth_gate.middleware.get_settings", return_value=mock_settings):
            with patch(
                "auth_gate.fastapi_utils.get_settings", return_value=mock_settings
            ):
                with patch(
                    "auth_gate.fastapi_utils.get_user_validator"
                ) as mock_validator:
                    # Mock the validator's get_current_user to return bypass user
                    mock_validator.return_value.get_current_user = AsyncMock(
                        return_value=UserContext(
                            user_id="test_user",
                            username="testuser",
                            roles=["admin"],
                            auth_source="bypass",
                            email="test@example.com",
                            session_id="test_session",
                            client_id="test_client",
                        )
                    )

                    client = TestClient(integrated_app)

                    # Should work without any headers
                    response = client.get("/api/profile")
                    assert response.status_code == 200
                    assert response.json()["user_id"] == "test_user"

                    # Admin endpoint should work (due to "admin" role)
                    response = client.get("/api/admin/users")
                    assert response.status_code == 200
