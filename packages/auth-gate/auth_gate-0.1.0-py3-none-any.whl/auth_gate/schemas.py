"""
Data models for authentication
"""

from typing import List, Optional

from pydantic import BaseModel, Field


class UserContext(BaseModel):
    """
    Authenticated user context containing all user claims and metadata.
    This is the primary model passed through the application after authentication.
    """

    user_id: str = Field(..., description="Unique user identifier")
    username: Optional[str] = Field(None, description="Username")
    email: Optional[str] = Field(None, description="User email address")
    roles: List[str] = Field(default_factory=list, description="User roles")
    scopes: List[str] = Field(default_factory=list, description="OAuth scopes")
    session_id: Optional[str] = Field(None, description="Session identifier")
    client_id: Optional[str] = Field(None, description="OAuth client ID")
    auth_source: str = Field("unknown", description="Authentication source (kong/keycloak/bypass)")

    @property
    def is_admin(self) -> bool:
        """Check if user has admin role"""
        return "admin" in self.roles

    @property
    def is_supplier(self) -> bool:
        """Check if user has supplier role"""
        return "supplier" in self.roles or self.is_admin

    @property
    def is_customer(self) -> bool:
        """Check if user has customer role"""
        return "customer" in self.roles

    @property
    def is_moderator(self) -> bool:
        """Check if user has moderator role"""
        return "moderator" in self.roles or self.is_admin

    def has_role(self, role: str) -> bool:
        """Check if user has specific role"""
        return role in self.roles or self.is_admin

    def has_any_role(self, roles: List[str]) -> bool:
        """Check if user has any of the specified roles"""
        return bool(set(roles) & set(self.roles)) or self.is_admin

    def has_all_roles(self, roles: List[str]) -> bool:
        """Check if user has all of the specified roles"""
        return all(self.has_role(role) for role in roles)

    def has_scope(self, scope: str) -> bool:
        """Check if user has specific scope"""
        return scope in self.scopes

    def has_any_scope(self, scopes: List[str]) -> bool:
        """Check if user has any of the specified scopes"""
        return bool(set(scopes) & set(self.scopes))

    class Config:
        frozen = False  # Allow mutation for middleware enrichment
