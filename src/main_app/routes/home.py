"""Homepage route displaying blog index."""

from fasthtml.common import *

from ..components import Layout
from ..utils.content import load_all_posts


def register_home_routes(app):
    """Register home page routes with the FastHTML app.

    Args:
        app: FastHTML application instance
    """

    @app.get("/")
    def home(request):
        """Display all blog posts in reverse chronological order.

        Args:
            request: HTTP request object with navigation context

        Returns:
            Rendered HTML page with blog post list
        """
        posts = load_all_posts()

        page_content = (
            Header(
                H1("Personal Blog", cls="post-title"),
                P(
                    "Welcome to my personal blog where I write about technology, development, "
                    "and other interesting topics.",
                    cls="blog-intro",
                ),
                cls="post-header",
            ),
            Section(
                *[
                    Article(
                        Header(
                            H2(A(post["title"], href=f"/posts/{post['slug']}")),
                            P(
                                f"Published on {post['date'].strftime('%B %d, %Y')}",
                                cls="blog-post-meta",
                            ),
                            cls="blog-post-header",
                        ),
                        P(
                            post["excerpt"] or "No excerpt available.",
                            cls="blog-post-excerpt",
                        )
                        if post["excerpt"]
                        else None,
                        Div(
                            *[A(tag, href=f"/tags/{tag}", cls="tag") for tag in post["tags"]],
                            cls="post-tags",
                        )
                        if post["tags"]
                        else None,
                        cls="blog-post",
                    )
                    for post in posts
                ]
                if posts
                else [P("No blog posts available yet.")],
                cls="blog-index",
            ),
        )

        return Layout(request, *page_content, title="Home")
