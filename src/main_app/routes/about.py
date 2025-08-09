"""About page route."""

from fasthtml.common import *


def register_about_routes(app):
    """Register about page routes with the FastHTML app.

    Args:
        app: FastHTML application instance
    """

    @app.get("/about")
    def about(request):
        """Display about page with bio and links.

        Args:
            request: HTTP request object with navigation context

        Returns:
            Rendered HTML page with about content
        """
        content = Main(
            Header(H1("About Me", cls="post-title"), cls="post-header"),
            Article(
                Section(
                    P(
                        "Welcome to my personal blog! I'm a developer passionate about creating "
                        "clean, efficient, and maintainable software. This space serves as both "
                        "a technical journal and a platform to share insights from my journey "
                        "in software development."
                    ),
                    P(
                        "I specialize in Python development, web technologies, and building "
                        "scalable applications. When I'm not coding, you can find me exploring "
                        "new technologies, contributing to open source projects, or writing "
                        "about the latest developments in tech."
                    ),
                    P(
                        "This blog covers a range of topics including software architecture, "
                        "development best practices, technology reviews, and occasional deep "
                        "dives into interesting technical challenges I encounter."
                    ),
                ),
                Section(
                    H2("Connect With Me"),
                    P("Feel free to reach out or follow my work:"),
                    Ul(
                        Li(A("GitHub", href="https://github.com", target="_blank")),
                        Li(A("LinkedIn", href="https://linkedin.com", target="_blank")),
                        Li(A("Twitter", href="https://twitter.com", target="_blank")),
                        Li(A("Email", href="mailto:contact@example.com")),
                    ),
                    cls="social-links",
                ),
                Section(
                    H2("About This Site"),
                    P(
                        "This website is built with FastHTML, a modern Python web framework. "
                        "The source code is clean, well-documented, and serves as an example "
                        "of professional web development practices. The design is inspired by "
                        "mid-century corporate aesthetics, emphasizing clarity and readability."
                    ),
                    P(
                        "All blog posts are written in Markdown with syntax highlighting for "
                        "code examples. The site is fully responsive and optimized for both "
                        "desktop and mobile reading experiences."
                    ),
                ),
                cls="about-content",
            ),
            cls="content",
        )

        return Html(
            Head(
                Meta(charset="UTF-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                Title("About - Personal Blog"),
                Link(
                    rel="stylesheet",
                    href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css",
                ),
                Link(rel="preconnect", href="https://fonts.googleapis.com"),
                Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
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
                                                post["title"][:40] + "..."
                                                if len(post["title"]) > 40
                                                else post["title"],
                                                href=f"/posts/{post['slug']}",
                                                title=post["title"],
                                            ),
                                            Small(post["date"].strftime("%b %d, %Y")),
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
