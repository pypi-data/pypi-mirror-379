"""
Tests for authentication middleware
"""

from unittest.mock import patch

import pytest
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient

from auth_gate import AuthMiddleware


@pytest.fixture
def app():
    """Create test FastAPI app"""
    app = FastAPI()

    @app.get("/public")
    async def public_endpoint():
        return {"message": "public"}

    @app.get("/protected")
    async def protected_endpoint(request: Request):
        user = request.state.user
        return {"user_id": user.user_id if user else None}

    @app.get("/optional")
    async def optional_endpoint(request: Request):
        user = getattr(request.state, "user", None)
        return {"authenticated": user is not None}

    return app


class TestAuthMiddleware:
    """Test AuthMiddleware"""

    def test_middleware_excludes_paths(self, app, mock_settings):
        """Test middleware excludes configured paths"""
        app.add_middleware(
            AuthMiddleware,
            excluded_paths={"/public", "/health"},
            excluded_prefixes={"/static"},
        )

        client = TestClient(app)

        # Public endpoint should work without auth
        response = client.get("/public")
        assert response.status_code == 200
        assert response.json() == {"message": "public"}

    def test_middleware_requires_auth_for_protected(self, app, mock_settings):
        """Test middleware requires auth for protected endpoints"""
        with patch("auth_gate.middleware.get_settings", return_value=mock_settings):
            app.add_middleware(
                AuthMiddleware,
                excluded_paths={"/public"},
            )

            client = TestClient(app)

            # Protected endpoint should fail without auth
            response = client.get("/protected")
            assert response.status_code == 401
            assert "Authentication required" in response.json()["message"]

    def test_middleware_with_kong_headers(self, app, mock_settings, kong_headers):
        """Test middleware with Kong headers"""
        with patch("auth_gate.middleware.get_settings", return_value=mock_settings):
            with patch("auth_gate.user_auth.get_settings", return_value=mock_settings):
                app.add_middleware(
                    AuthMiddleware,
                    excluded_paths={"/public"},
                )

                client = TestClient(app)

                # Protected endpoint should work with Kong headers
                response = client.get("/protected", headers=kong_headers)
                assert response.status_code == 200
                assert response.json()["user_id"] == "test-user-123"

    def test_middleware_optional_auth(self, app, mock_settings, kong_headers):
        """Test middleware with optional authentication paths"""
        with patch("auth_gate.middleware.get_settings", return_value=mock_settings):
            app.add_middleware(
                AuthMiddleware,
                excluded_paths={"/public"},
                optional_auth_paths={"/optional"},
            )

            client = TestClient(app)

            # Optional endpoint should work without auth
            response = client.get("/optional")
            assert response.status_code == 200
            assert response.json()["authenticated"] is False

            # Optional endpoint should detect auth when present
            with patch("auth_gate.user_auth.get_settings", return_value=mock_settings):
                response = client.get("/optional", headers=kong_headers)
                assert response.status_code == 200
                assert response.json()["authenticated"] is True

    def test_middleware_adds_security_headers(self, app, mock_settings):
        """Test middleware adds security headers"""
        app.add_middleware(
            AuthMiddleware,
            excluded_paths={"/public"},
        )

        client = TestClient(app)

        response = client.get("/public")
        assert response.status_code == 200

        # Check security headers
        assert "X-Request-ID" in response.headers
        assert response.headers["X-Content-Type-Options"] == "nosniff"
        assert response.headers["X-Frame-Options"] == "DENY"
        assert response.headers["X-XSS-Protection"] == "1; mode=block"
        assert "Strict-Transport-Security" in response.headers
        assert "X-Process-Time" in response.headers

    def test_middleware_bypass_mode(self, app, mock_settings):
        """Test middleware in bypass mode"""
        mock_settings.AUTH_MODE = "bypass"

        with patch("auth_gate.middleware.get_settings", return_value=mock_settings):
            with patch("auth_gate.user_auth.get_settings", return_value=mock_settings):
                app.add_middleware(
                    AuthMiddleware,
                    excluded_paths={"/public"},
                )

                client = TestClient(app)

                # Should work without any auth headers in bypass mode
                response = client.get("/protected")
                assert response.status_code == 200
                assert response.json()["user_id"] == "test_user"
