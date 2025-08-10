"""Main FastHTML application entry point."""

from fasthtml.common import *
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from .utils.content import get_pygments_css, load_recent_posts


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


app = FastHTML(
    hdrs=(
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
        Link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:wght@400;500;600&display=swap",
        ),
        Link(rel="stylesheet", href="/static/css/custom.css"),
    )
)

app.add_middleware(NavigationMiddleware)

# Mount static files
app.mount("/static", StaticFiles(directory="src/main_app/static"), name="static")


# Import and register routes
from .routes.about import register_about_routes
from .routes.home import register_home_routes
from .routes.posts import register_post_routes
from .routes.tags import register_tag_routes

register_home_routes(app)
register_about_routes(app)
register_post_routes(app)
register_tag_routes(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=30, timeout_notify=30)
