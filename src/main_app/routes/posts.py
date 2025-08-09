"""Individual blog post routes."""

from fasthtml.common import *

from ..components import Layout
from ..utils.content import load_post


def register_post_routes(app):
    """Register post routes with the FastHTML app.

    Args:
        app: FastHTML application instance
    """

    @app.get("/posts/{slug}")
    def post_detail(request, slug: str):
        """Display individual blog post.

        Args:
            request: HTTP request object with navigation context
            slug: The post slug (filename without .md extension)

        Returns:
            Rendered HTML page with blog post content or 404
        """
        post = load_post(slug)

        if not post:
            from starlette.responses import HTMLResponse

            return HTMLResponse(
                """<!DOCTYPE html>
                <html>
                <head><title>Post Not Found</title></head>
                <body><h1>Post Not Found</h1><p>The requested blog post could not be found.</p></body>
                </html>""",
                status_code=404,
            )

        page_content = (
            Header(
                H1(post["title"], cls="post-title"),
                P(
                    f"Published on {post['date'].strftime('%B %d, %Y')}",
                    cls="post-meta",
                ),
                Div(
                    *[A(tag, href=f"/tags/{tag}", cls="tag") for tag in post["tags"]],
                    cls="post-tags",
                )
                if post["tags"]
                else None,
                cls="post-header",
            ),
            Article(
                NotStr(post["content"]),  # Raw HTML content from markdown
                cls="post-content",
            ),
            Footer(Nav(A("← Back to Home", href="/", cls="back-link")), cls="post-footer"),
        )

        return Layout(request, *page_content, title=post["title"])
