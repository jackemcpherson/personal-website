"""Content management utilities for blog posts."""

from datetime import date, datetime
from functools import lru_cache
from pathlib import Path
from typing import Any

import frontmatter
import markdown
from pygments.formatters import HtmlFormatter


def _get_posts_directory() -> Path:
    """Get the path to the posts directory.

    Returns:
        Path object pointing to the posts directory
    """
    return Path(__file__).parent.parent / "posts"


def _parse_post_file(file_path: Path) -> dict[str, Any] | None:
    """Parse a single markdown post file.

    Args:
        file_path: Path to the markdown file to parse

    Returns:
        Dictionary containing post data and metadata, or None if parsing fails
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            post = frontmatter.load(f)

        md = markdown.Markdown(
            extensions=["codehilite", "fenced_code", "tables"],
            extension_configs={
                "codehilite": {
                    "css_class": "highlight",
                    "use_pygments": True,
                }
            },
        )

        html_content = md.convert(post.content)

        post_data = {
            "slug": file_path.stem,
            "title": post.metadata.get("title", "Untitled"),
            "date": post.metadata.get("date"),
            "tags": post.metadata.get("tags", []),
            "excerpt": post.metadata.get("excerpt", ""),
            "content": html_content,
            "raw_content": post.content,
        }

        if isinstance(post_data["date"], str):
            try:
                post_data["date"] = datetime.fromisoformat(post_data["date"])
            except ValueError:
                post_data["date"] = datetime.now()
        elif isinstance(post_data["date"], date):
            # Convert date to datetime
            post_data["date"] = datetime.combine(post_data["date"], datetime.min.time())
        elif post_data["date"] is None:
            post_data["date"] = datetime.now()
        elif not isinstance(post_data["date"], datetime):
            post_data["date"] = datetime.now()

        return post_data

    except Exception:
        return None


@lru_cache(maxsize=None)
def load_all_posts() -> list[dict[str, Any]]:
    """Load all blog posts from the posts directory.

    Returns:
        List of post dictionaries sorted by date in reverse chronological order
    """
    posts_dir = _get_posts_directory()
    posts = []

    if not posts_dir.exists():
        return posts

    for file_path in posts_dir.glob("*.md"):
        post_data = _parse_post_file(file_path)
        if post_data:
            posts.append(post_data)

    posts.sort(key=lambda x: x["date"], reverse=True)
    return posts


def load_recent_posts(limit: int = 3) -> list[dict[str, Any]]:
    """Load the most recent blog posts for navigation.

    Args:
        limit: Maximum number of recent posts to return

    Returns:
        List of post dictionaries with metadata
    """
    all_posts = load_all_posts()
    return all_posts[:limit]


@lru_cache(maxsize=128)
def load_post(slug: str) -> dict[str, Any] | None:
    """Load a specific blog post by its slug.

    Args:
        slug: The filename (without .md extension) of the post to load

    Returns:
        Dictionary containing post data and metadata, or None if not found
    """
    posts_dir = _get_posts_directory()
    file_path = posts_dir / f"{slug}.md"

    if not file_path.exists():
        return None

    return _parse_post_file(file_path)


def load_posts_by_tag(tag: str) -> list[dict[str, Any]]:
    """Load all posts that contain a specific tag.

    Args:
        tag: The tag to filter posts by

    Returns:
        List of post dictionaries that contain the specified tag
    """
    all_posts = load_all_posts()
    return [post for post in all_posts if tag in post["tags"]]


def get_all_tags() -> list[str]:
    """Get a list of all unique tags across all posts.

    Returns:
        Sorted list of unique tag names
    """
    all_posts = load_all_posts()
    tags = set()

    for post in all_posts:
        tags.update(post["tags"])

    return sorted(list(tags))


def get_pygments_css() -> str:
    """Generate CSS for Pygments syntax highlighting.

    Returns:
        CSS string for syntax highlighting
    """
    formatter = HtmlFormatter(style="default", cssclass="highlight")
    return formatter.get_style_defs()


def clear_content_cache():
    """Clear cached content for testing purposes.
    
    This function clears the LRU cache for content loading functions
    to ensure tests can run with fresh data.
    """
    load_all_posts.cache_clear()
    load_post.cache_clear()
