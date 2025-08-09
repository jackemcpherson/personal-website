"""Homepage route displaying blog index."""

from fasthtml.common import *

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

        content = Main(
            Header(
                H1("Personal Blog", cls="post-title"),
                P(
                    "Welcome to my personal blog where I write about technology, development, and other interesting topics.",
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
                            *[
                                A(tag, href=f"/tags/{tag}", cls="tag")
                                for tag in post["tags"]
                            ],
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
            cls="content",
        )

        return Html(
            Head(
                Meta(charset="UTF-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                Title("Personal Blog"),
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
                                                post["title"],
                                                href=f"/posts/{post['slug']}",
                                                title=post["title"],
                                            )
                                        )
                                        for post in request.state.recent_posts
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
