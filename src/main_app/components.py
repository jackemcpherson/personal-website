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
            Meta(name="language", content="en"),
            Title(f"{title} - Personal Blog"),
            Link(rel="preconnect", href="https://fonts.googleapis.com"),
            Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
            Link(
                rel="stylesheet",
                href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:wght@400;500;600&display=swap",
            ),
            Link(rel="stylesheet", href="/static/css/custom.css"),
            Link(rel="alternate", type="application/rss+xml", title="RSS Feed", href="/feed.xml"),
            Style(request.state.pygments_css),
            Script(src="/static/js/dark-mode.js"),
        ),
        Body(
            # Skip to content link for accessibility
            A("Skip to content", href="#main-content", cls="skip-link"),
            Div(
                # Sidebar Navigation
                Nav(
                    Header(H2(A("Personal Blog", href="/")), cls="sidebar-header"),
                    Ul(
                        Li(A("Home", href="/")),
                        Li(A("About", href="/about")),
                        cls="nav-links",
                    ),
                    # This is the corrected 'Recent Posts' section from Issue #2
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
                                    Small(post["date"].strftime("%b %d, %Y"), cls="post-date"),
                                )
                                for post in request.state.recent_posts
                            ]
                        )
                        if request.state.recent_posts
                        else P("No posts yet.", style="font-style: italic; color: #999;"),
                        cls="recent-posts",
                    ),
                    cls="sidebar",
                ),
                # Page-specific content is injected here
                Main(*content, cls="content", id="main-content"),
                cls="grid-container",
            ),
            # Subtle dark mode toggle button - fixed bottom left
            Button(
                NotStr(
                    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" '
                    + 'stroke="currentColor" stroke-width="2" stroke-linecap="round">'
                    + '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>'
                ),
                id="theme-toggle",
                cls="theme-toggle",
                type="button",
                title="Toggle dark mode",
                **{"aria-pressed": "false"},
            ),
        ),
    )
