"""Reusable UI components for the FastHTML blog application."""

from fasthtml.common import *


def Layout(request, *content, title: str):
    """A reusable layout component for all pages.

    Args:
        request: The FastHTML request object containing state
        *content: Variable number of content elements to render in main
        title: The page title (will be prefixed with site name)

    Returns:
        Complete HTML document with consistent layout
    """
    return Html(
        Head(
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Title(f"{title} - Personal Blog"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"),
            Link(rel="preconnect", href="https://fonts.googleapis.com"),
            Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
            Link(
                href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;1,400&family=Montserrat:wght@400;500;600;700&display=swap",
                rel="stylesheet",
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
                                        ),
                                        Small(post["date"].strftime("%b %d, %Y")),
                                    )
                                    for post in request.state.recent_posts
                                ]
                            ),
                            cls="recent-posts",
                        )
                        if request.state.recent_posts
                        else None,
                        cls="sidebar",
                    ),
                    Main(*content, cls="content"),
                    cls="grid",
                ),
                cls="container-fluid",
            )
        ),
    )
