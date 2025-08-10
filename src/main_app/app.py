"""Main FastHTML application entry point."""

from pathlib import Path

from fasthtml.common import *
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse

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

        csp = (
            "default-src 'self'; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            "img-src 'self' data:; "
            "connect-src 'self'; "
            "script-src 'self'; "
            "object-src 'none'; "
            "base-uri 'self'; "
            "form-action 'self'; "
            "upgrade-insecure-requests"
        )
        response.headers["Content-Security-Policy"] = csp

        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"

        return response


class CacheControlMiddleware(BaseHTTPMiddleware):
    """Middleware to add appropriate Cache-Control headers."""

    async def dispatch(self, request: Request, call_next) -> Response:
        """Add Cache-Control headers based on request path.

        Args:
            request: The incoming HTTP request
            call_next: The next middleware or route handler

        Returns:
            HTTP response with Cache-Control headers added
        """
        response = await call_next(request)

        if request.url.path.startswith("/static/"):
            response.headers["Cache-Control"] = "public, max-age=31536000"
        elif request.url.path == "/health":
            response.headers["Cache-Control"] = "no-store"
        else:
            response.headers["Cache-Control"] = "public, max-age=300"

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

app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(CacheControlMiddleware)
app.add_middleware(NavigationMiddleware)

static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")

from .routes.about import register_about_routes
from .routes.home import register_home_routes
from .routes.posts import register_post_routes
from .routes.tags import register_tag_routes

register_home_routes(app)
register_about_routes(app)
register_post_routes(app)
register_tag_routes(app)


@app.get("/health")
def health_check():
    """Health check endpoint for Docker and monitoring.

    Returns:
        Dictionary containing service health status and name
    """
    return {"status": "healthy", "service": "personal-website"}


@app.exception_handler(404)
def not_found(request, exc):
    """Custom 404 page with styled layout.

    Args:
        request: HTTP request object with navigation context
        exc: The 404 exception that was raised

    Returns:
        HTML response containing styled 404 page
    """
    from .components import Layout

    page_content = (
        H1("Page Not Found", cls="post-title"),
        P("Sorry, the page you're looking for doesn't exist."),
        A("← Back to Home", href="/", cls="back-link"),
    )

    layout_content = Layout(request, *page_content, title="Not Found")
    return HTMLResponse(str(layout_content), status_code=404)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=30)
