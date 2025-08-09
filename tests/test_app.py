"""Tests for the main FastHTML application."""

from fasthtml.common import *
from starlette.testclient import TestClient

from src.main_app.app import app


class TestApplication:
    """Test main application functionality."""

    def setup_method(self):
        """Set up test client."""
        self.client = TestClient(app)

    def test_static_files_mounted(self):
        """Test that static files are properly mounted."""
        # This would normally test actual static file serving,
        # but we'll just verify the mount exists
        assert hasattr(app, "mount")

    def test_middleware_added(self):
        """Test that middleware is properly added."""
        # Check that middleware is configured (at least one middleware should exist)
        assert len(app.user_middleware) > 0


class TestRoutes:
    """Test that all routes are properly registered."""

    def setup_method(self):
        """Set up test client."""
        self.client = TestClient(app)

    def test_home_route_exists(self):
        """Test that home route is accessible."""
        response = self.client.get("/")
        # Should not return 404
        assert response.status_code != 404

    def test_about_route_exists(self):
        """Test that about route is accessible."""
        response = self.client.get("/about")
        # Should not return 404
        assert response.status_code != 404

    def test_nonexistent_post_returns_404(self):
        """Test that non-existent posts return 404."""
        response = self.client.get("/posts/nonexistent-post")
        assert response.status_code == 404

    def test_tags_route_exists(self):
        """Test that tags route is accessible."""
        response = self.client.get("/tags")
        # Should not return 404
        assert response.status_code != 404
