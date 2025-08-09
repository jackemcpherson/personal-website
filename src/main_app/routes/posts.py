"""Individual blog post routes."""

from fasthtml.common import *

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

        content = Main(
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
            Footer(
                Nav(A("← Back to Home", href="/", cls="back-link")), cls="post-footer"
            ),
            cls="content",
        )

        return Html(
            Head(
                Meta(charset="UTF-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                Title(f"{post['title']} - Personal Blog"),
                Link(
                    rel="stylesheet",
                    href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css",
                ),
                Link(rel="preconnect", href="https://fonts.googleapis.com"),
                Link(
                    rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True
                ),
                Link(
                    rel="stylesheet",
                    href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Lora:wght@400;500;600&display=swap",
                ),
                Link(rel="stylesheet", href="/static/css/custom.css"),
                Style(request.state.pygments_css),
            ),
            Body(
                Div(
                    Div(
                        Nav(
                            Header(H2(A("Personal Blog", href="/"))),
                            Ul(
                                Li(A("Home", href="/")),
                                Li(A("About", href="/about")),
                                cls="nav-links",
                            ),
                            Section(
                                H3("Recent Posts"),
                                Ul(
                                    *[
                                        Li(
                                            A(
                                                recent_post["title"][:40] + "..."
                                                if len(recent_post["title"]) > 40
                                                else recent_post["title"],
                                                href=f"/posts/{recent_post['slug']}",
                                                title=recent_post["title"],
                                            ),
                                            Small(
                                                recent_post["date"].strftime(
                                                    "%b %d, %Y"
                                                )
                                            ),
                                        )
                                        for recent_post in request.state.recent_posts
                                    ]
                                )
                                if request.state.recent_posts
                                else P("No recent posts."),
                                cls="recent-posts",
                            )
                            if request.state.recent_posts
                            else None,
                            cls="sidebar",
                        ),
                        content,
                        cls="grid",
                    ),
                    cls="container-fluid",
                )
            ),
        )
