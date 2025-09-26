"""
Tests for authentication schemas
"""

from auth_gate import UserContext


class TestUserContext:
    """Test UserContext model"""

    def test_user_context_creation(self):
        """Test creating user context"""
        user = UserContext(
            user_id="user-123",
            username="testuser",
            email="test@example.com",
            roles=["customer"],
            scopes=["read"],
            session_id="session-123",
            client_id="web-app",
            auth_source="kong",
        )

        assert user.user_id == "user-123"
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.roles == ["customer"]
        assert user.scopes == ["read"]

    def test_minimal_user_context(self):
        """Test creating user context with minimal data"""
        user = UserContext(user_id="user-123")

        assert user.user_id == "user-123"
        assert user.username is None
        assert user.email is None
        assert user.roles == []
        assert user.scopes == []
        assert user.auth_source == "unknown"

    def test_is_admin_property(self):
        """Test is_admin property"""
        user = UserContext(user_id="user-123", roles=["customer"])
        assert user.is_admin is False

        admin = UserContext(user_id="admin-123", roles=["admin"])
        assert admin.is_admin is True

    def test_is_supplier_property(self):
        """Test is_supplier property"""
        user = UserContext(user_id="user-123", roles=["customer"])
        assert user.is_supplier is False

        supplier = UserContext(user_id="supplier-123", roles=["supplier"])
        assert supplier.is_supplier is True

        admin = UserContext(user_id="admin-123", roles=["admin"])
        assert admin.is_supplier is True  # Admin has supplier access

    def test_is_customer_property(self):
        """Test is_customer property"""
        user = UserContext(user_id="user-123", roles=["customer"])
        assert user.is_customer is True

        supplier = UserContext(user_id="supplier-123", roles=["supplier"])
        assert supplier.is_customer is False

    def test_is_moderator_property(self):
        """Test is_moderator property"""
        user = UserContext(user_id="user-123", roles=["customer"])
        assert user.is_moderator is False

        moderator = UserContext(user_id="mod-123", roles=["moderator"])
        assert moderator.is_moderator is True

        admin = UserContext(user_id="admin-123", roles=["admin"])
        assert admin.is_moderator is True  # Admin has moderator access

    def test_has_role(self):
        """Test has_role method"""
        user = UserContext(user_id="user-123", roles=["customer", "verified"])

        assert user.has_role("customer") is True
        assert user.has_role("verified") is True
        assert user.has_role("admin") is False
        assert user.has_role("supplier") is False

    def test_has_any_role(self):
        """Test has_any_role method"""
        user = UserContext(user_id="user-123", roles=["customer", "verified"])

        assert user.has_any_role(["customer", "admin"]) is True
        assert user.has_any_role(["verified"]) is True
        assert user.has_any_role(["admin", "supplier"]) is False
        assert user.has_any_role([]) is False

    def test_has_all_roles(self):
        """Test has_all_roles method"""
        user = UserContext(user_id="user-123", roles=["customer", "verified"])

        assert user.has_all_roles(["customer", "verified"]) is True
        assert user.has_all_roles(["customer"]) is True
        assert user.has_all_roles(["customer", "admin"]) is False
        assert user.has_all_roles([]) is True

    def test_has_scope(self):
        """Test has_scope method"""
        user = UserContext(user_id="user-123", scopes=["read", "write"])

        assert user.has_scope("read") is True
        assert user.has_scope("write") is True
        assert user.has_scope("admin") is False

    def test_has_any_scope(self):
        """Test has_any_scope method"""
        user = UserContext(user_id="user-123", scopes=["read", "write"])

        assert user.has_any_scope(["read", "admin"]) is True
        assert user.has_any_scope(["write"]) is True
        assert user.has_any_scope(["admin", "delete"]) is False
        assert user.has_any_scope([]) is False

    def test_admin_role_privileges(self):
        """Test admin role has special privileges"""
        admin = UserContext(user_id="admin-123", roles=["admin"])

        # Admin should pass all role checks
        assert admin.has_role("customer") is True
        assert admin.has_role("supplier") is True
        assert admin.has_role("moderator") is True
        assert admin.has_any_role(["customer", "supplier"]) is True
