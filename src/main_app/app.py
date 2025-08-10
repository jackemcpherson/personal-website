"""Main FastHTML application entry point."""

from fasthtml.common import *
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from .utils.content import get_pygments_css, load_recent_posts


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Middleware to add security headers to all responses."""

    async def dispatch(self, request: Request, call_next) -> Response:
        """Add security headers to response.

        Args:
            request: The incoming HTTP request
            call_next: The next middleware or route handler

        Returns:
            HTTP response with security headers added
        """
        response = await call_next(request)

        # Content Security Policy - strict policy for security
        csp = (
            "default-src 'self'; "
            "style-src 'self' 'unsafe-inline' fonts.googleapis.com; "
            "font-src 'self' fonts.gstatic.com; "
            "img-src 'self' data:; "
            "connect-src 'self'; "
            "script-src 'self'; "
            "object-src 'none'; "
            "base-uri 'self'; "
            "form-action 'self'"
        )
        response.headers["Content-Security-Policy"] = csp

        # Additional security headers
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"

        return response


class NavigationMiddleware(BaseHTTPMiddleware):
    """Middleware to add navigation context to all requests."""

    async def dispatch(self, request: Request, call_next) -> Response:
        """Add recent posts to request state for navigation menu.

        Args:
            request: The incoming HTTP request
            call_next: The next middleware or route handler

        Returns:
            HTTP response with navigation context added
        """
        request.state.recent_posts = load_recent_posts(limit=3)
        request.state.pygments_css = get_pygments_css()
        response = await call_next(request)
        return response


app = FastHTML()

app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(NavigationMiddleware)

# Mount static files with absolute path
import os

static_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "main_app", "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


# Import and register routes
from .routes.about import register_about_routes
from .routes.home import register_home_routes
from .routes.posts import register_post_routes
from .routes.tags import register_tag_routes

register_home_routes(app)
register_about_routes(app)
register_post_routes(app)
register_tag_routes(app)


# Health check endpoint
@app.get("/healthz")
def health_check():
    """Health check endpoint for Docker and monitoring."""
    return {"status": "healthy", "service": "personal-website"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=30)
