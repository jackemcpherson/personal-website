"""Tag filtering routes."""

from fasthtml.common import *

from ..components import Layout
from ..utils.content import get_all_tags, load_posts_by_tag


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

        page_content = (
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
                            *[A(post_tag, href=f"/tags/{post_tag}", cls="tag") for post_tag in post["tags"]],
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
            Footer(Nav(A("← Back to Home", href="/", cls="back-link")), cls="tag-footer"),
        )

        return Layout(request, *page_content, title=f"Posts tagged '{tag}'")

    @app.get("/tags")
    def all_tags_page(request):
        """Display all available tags.

        Args:
            request: HTTP request object with navigation context

        Returns:
            Rendered HTML page with all tags
        """
        all_tags = get_all_tags()

        page_content = (
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
            Footer(Nav(A("← Back to Home", href="/", cls="back-link")), cls="tags-footer"),
        )

        return Layout(request, *page_content, title="All Tags")
