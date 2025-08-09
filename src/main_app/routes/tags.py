"""Tag filtering routes."""

from fasthtml.common import *

from ..utils.content import load_posts_by_tag, get_all_tags


def register_tag_routes(app):
    """Register tag routes with the FastHTML app.

    Args:
        app: FastHTML application instance
    """

    @app.get("/tags/{tag}")
    def tag_posts(request, tag: str):
        """Display all posts with specific tag.

        Args:
            request: HTTP request object with navigation context
            tag: The tag name to filter posts by

        Returns:
            Rendered HTML page with filtered posts
        """
        posts = load_posts_by_tag(tag)
        all_tags = get_all_tags()

        content = Main(
            Header(
                H1(f"Posts tagged with '{tag}'", cls="post-title"),
                P(
                    f"Found {len(posts)} post{'s' if len(posts) != 1 else ''} with this tag.",
                    cls="tag-meta",
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
                        ),
                        P(
                            post["excerpt"] or "No excerpt available.",
                            cls="blog-post-excerpt",
                        )
                        if post["excerpt"]
                        else None,
                        Div(
                            *[
                                A(post_tag, href=f"/tags/{post_tag}", cls="tag")
                                for post_tag in post["tags"]
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
                else [P(f"No posts found with the tag '{tag}'.")],
                cls="tag-posts-list",
            ),
            Section(
                H2("All Tags"),
                P("Browse posts by other tags:"),
                Div(
                    *[
                        A(available_tag, href=f"/tags/{available_tag}", cls="tag")
                        for available_tag in all_tags
                        if available_tag != tag
                    ]
                    if all_tags
                    else [P("No tags available.")],
                    cls="all-tags",
                ),
                cls="tags-section",
            )
            if all_tags
            else None,
            Footer(
                Nav(A("← Back to Home", href="/", cls="back-link")), cls="tag-footer"
            ),
            cls="content",
        )

        return Html(
            Head(
                Meta(charset="UTF-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                Title(f"Posts tagged '{tag}' - Personal Blog"),
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

    @app.get("/tags")
    def all_tags_page(request):
        """Display all available tags.

        Args:
            request: HTTP request object with navigation context

        Returns:
            Rendered HTML page with all tags
        """
        all_tags = get_all_tags()

        content = Main(
            Header(
                H1("All Tags", cls="post-title"),
                P(f"Browse all {len(all_tags)} available tags.", cls="tag-meta"),
                cls="post-header",
            ),
            Section(
                Div(
                    *[A(tag, href=f"/tags/{tag}", cls="tag") for tag in all_tags]
                    if all_tags
                    else [P("No tags available yet.")],
                    cls="all-tags-grid",
                ),
                cls="all-tags-section",
            ),
            Footer(
                Nav(A("← Back to Home", href="/", cls="back-link")), cls="tags-footer"
            ),
            cls="content",
        )

        return Html(
            Head(
                Meta(charset="UTF-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                Title("All Tags - Personal Blog"),
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
