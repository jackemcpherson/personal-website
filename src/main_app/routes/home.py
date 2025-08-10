"""Homepage route displaying blog index."""

from datetime import datetime

from fasthtml.common import *
from starlette.responses import Response

from ..components import Layout
from ..utils.content import load_all_posts


def register_home_routes(app):
    """Register home page routes with the FastHTML app.

    Args:
        app: FastHTML application instance
    """

    @app.get("/")
    def home(request, page: int = 1):
        """Display blog posts with pagination.

        Args:
            request: HTTP request object with navigation context
            page: Page number for pagination (default: 1)

        Returns:
            Rendered HTML page with paginated blog post list
        """
        posts_per_page = 10
        all_posts = load_all_posts()
        total_posts = len(all_posts)

        start = (page - 1) * posts_per_page
        end = start + posts_per_page
        posts = all_posts[start:end]

        total_pages = (total_posts + posts_per_page - 1) // posts_per_page
        has_prev = page > 1
        has_next = page < total_pages

        page_content = (
            H1("Jack McPherson's Blog", cls="sr-only"),
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
            Nav(
                Div(
                    A("← Previous", href=f"/?page={page - 1}", cls="pagination-link prev")
                    if has_prev
                    else Span("← Previous", cls="pagination-link prev disabled"),
                    Span(f"Page {page} of {total_pages}", cls="pagination-info"),
                    A("Next →", href=f"/?page={page + 1}", cls="pagination-link next")
                    if has_next
                    else Span("Next →", cls="pagination-link next disabled"),
                    cls="pagination",
                ),
                cls="pagination-nav",
            )
            if total_pages > 1
            else None,
        )

        return Layout(request, *page_content, title="Home")

    @app.get("/feed.xml")
    def rss_feed():
        """Generate RSS feed for the blog.

        Returns:
            XML RSS feed response containing the latest 10 blog posts
        """
        posts = load_all_posts()[:10]

        rss_items = []
        for post in posts:
            pub_date = post["date"].strftime("%a, %d %b %Y %H:%M:%S +0000")
            description = post["excerpt"] or post["content"][:200] + "..."
            rss_items.append(f"""
            <item>
                <title><![CDATA[{post["title"]}]]></title>
                <link>https://yoursite.com/posts/{post["slug"]}</link>
                <description><![CDATA[{description}]]></description>
                <pubDate>{pub_date}</pubDate>
                <guid>https://yoursite.com/posts/{post["slug"]}</guid>
            </item>""")

        rss_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
    <channel>
        <title>Jack McPherson's Blog</title>
        <link>https://yoursite.com</link>
        <description>Technical blog posts about software development</description>
        <language>en-US</language>
        <lastBuildDate>{datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")}</lastBuildDate>
        <atom:link href="https://yoursite.com/feed.xml" rel="self" type="application/rss+xml"/>
        {"".join(rss_items)}
    </channel>
</rss>"""

        return Response(rss_content, media_type="application/rss+xml")

    @app.get("/sitemap.xml")
    def sitemap():
        """Generate XML sitemap for the website.

        Returns:
            XML sitemap response containing all pages and blog posts
        """
        posts = load_all_posts()

        urls = [
            """
            <url>
                <loc>https://yoursite.com/</loc>
                <changefreq>weekly</changefreq>
                <priority>1.0</priority>
            </url>""",
            """
            <url>
                <loc>https://yoursite.com/about</loc>
                <changefreq>monthly</changefreq>
                <priority>0.8</priority>
            </url>""",
            """
            <url>
                <loc>https://yoursite.com/tags</loc>
                <changefreq>weekly</changefreq>
                <priority>0.7</priority>
            </url>""",
        ]

        for post in posts:
            last_mod = post["date"].strftime("%Y-%m-%d")
            urls.append(f"""
            <url>
                <loc>https://yoursite.com/posts/{post["slug"]}</loc>
                <lastmod>{last_mod}</lastmod>
                <changefreq>monthly</changefreq>
                <priority>0.9</priority>
            </url>""")

        sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    {"".join(urls)}
</urlset>"""

        return Response(sitemap_content, media_type="application/xml")

    @app.get("/robots.txt")
    def robots_txt():
        """Generate robots.txt file for search engine crawlers.

        Returns:
            Plain text response containing robots.txt directives
        """
        robots_content = """User-agent: *
Allow: /

Sitemap: https://yoursite.com/sitemap.xml
"""
        return Response(robots_content, media_type="text/plain")
