"""About page route."""

from fasthtml.common import *

from ..components import Layout


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
        page_content = (
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
                    Div(
                        A(
                            NotStr(
                                (
                                    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" '
                                    'stroke="currentColor" stroke-width="2">'
                                    '<path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61'
                                    "c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1"
                                    "S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1"
                                    "A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7"
                                    'A3.37 3.37 0 0 0 9 18.13V22"></path></svg>'
                                )
                            ),
                            "GitHub",
                            href="https://github.com",
                            target="_blank",
                            cls="social-link",
                        ),
                        A(
                            NotStr(
                                (
                                    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" '
                                    'stroke="currentColor" stroke-width="2">'
                                    '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7'
                                    'a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect>'
                                    '<circle cx="4" cy="4" r="2"></circle></svg>'
                                )
                            ),
                            "LinkedIn",
                            href="https://linkedin.com",
                            target="_blank",
                            cls="social-link",
                        ),
                        A(
                            NotStr(
                                (
                                    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" '
                                    'stroke="currentColor" stroke-width="2">'
                                    '<path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1'
                                    "A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5"
                                    'a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>'
                                )
                            ),
                            "Twitter",
                            href="https://twitter.com",
                            target="_blank",
                            cls="social-link",
                        ),
                        A(
                            NotStr(
                                (
                                    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" '
                                    'stroke="currentColor" stroke-width="2">'
                                    '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2'
                                    'V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6">'
                                    "</polyline></svg>"
                                )
                            ),
                            "Email",
                            href="mailto:contact@example.com",
                            cls="social-link",
                        ),
                        cls="social-links",
                    ),
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
        )

        return Layout(request, *page_content, title="About")
