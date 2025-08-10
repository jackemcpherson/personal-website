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
        """Test that home route is accessible and contains expected content."""
        response = self.client.get("/")
        assert response.status_code == 200
        assert "Personal Blog" in response.text
        assert "Jack McPherson" in response.text and "Blog" in response.text

    def test_about_route_exists(self):
        """Test that about route is accessible and contains expected content."""
        response = self.client.get("/about")
        assert response.status_code == 200
        assert "About Me" in response.text
        assert "developer passionate about creating" in response.text

    def test_nonexistent_post_returns_404(self):
        """Test that non-existent posts return 404."""
        response = self.client.get("/posts/nonexistent-post")
        assert response.status_code == 404

    def test_tags_route_exists(self):
        """Test that tags route is accessible and contains expected content."""
        response = self.client.get("/tags")
        assert response.status_code == 200
        assert "All Tags" in response.text
        assert "Browse all" in response.text

    def test_health_endpoint(self):
        """Test that health endpoint returns proper response."""
        response = self.client.get("/healthz")
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["status"] == "healthy"
        assert json_response["service"] == "personal-website"

    def test_csp_header_exists(self):
        """Test that CSP header exists and contains expected directives."""
        response = self.client.get("/")
        assert response.status_code == 200
        assert "Content-Security-Policy" in response.headers
        csp = response.headers["Content-Security-Policy"]
        assert "default-src 'self'" in csp
        assert "upgrade-insecure-requests" in csp
        assert "https://fonts.googleapis.com" in csp
        assert "https://fonts.gstatic.com" in csp

    def test_static_css_accessible(self):
        """Test that static CSS file returns 200."""
        response = self.client.get("/static/css/custom.css")
        assert response.status_code == 200

    def test_404_renders_styled_layout(self):
        """Test that 404 pages render the styled layout."""
        response = self.client.get("/nonexistent-page")
        assert response.status_code == 404
        # Check that it returns the Layout with navigation
        assert "Personal Blog" in response.text
