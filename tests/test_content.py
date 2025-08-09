"""Tests for content management utilities."""

import tempfile
from datetime import datetime
from pathlib import Path

import pytest

from src.main_app.utils.content import (
    _parse_post_file,
    get_all_tags,
    load_all_posts,
    load_post,
    load_posts_by_tag,
    load_recent_posts,
)


@pytest.fixture
def temp_posts_dir(monkeypatch):
    """Create a temporary posts directory for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        posts_dir = Path(temp_dir) / "posts"
        posts_dir.mkdir()

        # Mock the posts directory path
        monkeypatch.setattr("src.main_app.utils.content._get_posts_directory", lambda: posts_dir)

        yield posts_dir


@pytest.fixture
def sample_posts(temp_posts_dir):
    """Create sample blog posts for testing."""
    posts = [
        {
            "filename": "first-post.md",
            "content": """---
title: First Post
date: 2025-08-08
tags: [python, testing]
excerpt: This is the first post
---

# First Post

This is the content of the first post.

```python
print("Hello, World!")
```
""",
        },
        {
            "filename": "second-post.md",
            "content": """---
title: Second Post
date: 2025-08-07
tags: [python, web-development]
excerpt: This is the second post
---

# Second Post

This is the content of the second post.
""",
        },
        {
            "filename": "third-post.md",
            "content": """---
title: Third Post
date: 2025-08-06
tags: [testing]
excerpt: This is the third post
---

# Third Post

This is the content of the third post.
""",
        },
    ]

    for post in posts:
        post_path = temp_posts_dir / post["filename"]
        post_path.write_text(post["content"], encoding="utf-8")

    return posts


class TestContentParsing:
    """Test content parsing functionality."""

    def test_parse_post_file_valid(self, temp_posts_dir):
        """Test parsing a valid post file."""
        post_content = """---
title: Test Post
date: 2025-08-08
tags: [test, example]
excerpt: A test post
---

# Test Post

This is a test post with **bold** text.
"""
        post_path = temp_posts_dir / "test-post.md"
        post_path.write_text(post_content, encoding="utf-8")

        result = _parse_post_file(post_path)

        assert result is not None
        assert result["slug"] == "test-post"
        assert result["title"] == "Test Post"
        assert isinstance(result["date"], datetime)
        assert result["tags"] == ["test", "example"]
        assert result["excerpt"] == "A test post"
        assert "<h1>Test Post</h1>" in result["content"]
        assert "<strong>bold</strong>" in result["content"]

    def test_parse_post_file_invalid(self, temp_posts_dir):
        """Test parsing an invalid post file."""
        post_path = temp_posts_dir / "invalid.md"
        post_path.write_text("Invalid content without frontmatter", encoding="utf-8")

        result = _parse_post_file(post_path)

        assert result is not None  # Should still parse, just with defaults
        assert result["slug"] == "invalid"
        assert result["title"] == "Untitled"

    def test_parse_post_file_nonexistent(self, temp_posts_dir):
        """Test parsing a non-existent file."""
        result = _parse_post_file(temp_posts_dir / "nonexistent.md")
        assert result is None


class TestPostLoading:
    """Test post loading functionality."""

    def test_load_all_posts(self, sample_posts):
        """Test loading all posts in reverse chronological order."""
        posts = load_all_posts()

        assert len(posts) == 3
        assert posts[0]["title"] == "First Post"  # Most recent
        assert posts[1]["title"] == "Second Post"
        assert posts[2]["title"] == "Third Post"  # Oldest

        # Verify they're in reverse chronological order
        for i in range(len(posts) - 1):
            assert posts[i]["date"] >= posts[i + 1]["date"]

    def test_load_recent_posts_default_limit(self, sample_posts):
        """Test loading recent posts with default limit."""
        posts = load_recent_posts()

        assert len(posts) == 3  # All posts since we have fewer than default limit
        assert posts[0]["title"] == "First Post"

    def test_load_recent_posts_custom_limit(self, sample_posts):
        """Test loading recent posts with custom limit."""
        posts = load_recent_posts(limit=2)

        assert len(posts) == 2
        assert posts[0]["title"] == "First Post"
        assert posts[1]["title"] == "Second Post"

    def test_load_post_existing(self, sample_posts):
        """Test loading a specific existing post."""
        post = load_post("first-post")

        assert post is not None
        assert post["title"] == "First Post"
        assert post["slug"] == "first-post"
        assert "Hello, World!" in post["content"]

    def test_load_post_nonexistent(self, sample_posts):
        """Test loading a non-existent post."""
        post = load_post("nonexistent-post")
        assert post is None

    def test_load_posts_by_tag(self, sample_posts):
        """Test loading posts filtered by tag."""
        python_posts = load_posts_by_tag("python")
        assert len(python_posts) == 2
        assert python_posts[0]["title"] == "First Post"
        assert python_posts[1]["title"] == "Second Post"

        testing_posts = load_posts_by_tag("testing")
        assert len(testing_posts) == 2
        assert testing_posts[0]["title"] == "First Post"
        assert testing_posts[1]["title"] == "Third Post"

        nonexistent_posts = load_posts_by_tag("nonexistent")
        assert len(nonexistent_posts) == 0

    def test_get_all_tags(self, sample_posts):
        """Test getting all unique tags."""
        tags = get_all_tags()

        expected_tags = ["python", "testing", "web-development"]
        assert sorted(tags) == sorted(expected_tags)


class TestEmptyPostsDirectory:
    """Test behavior with empty posts directory."""

    def test_load_all_posts_empty_directory(self, temp_posts_dir):
        """Test loading posts from empty directory."""
        posts = load_all_posts()
        assert posts == []

    def test_load_recent_posts_empty_directory(self, temp_posts_dir):
        """Test loading recent posts from empty directory."""
        posts = load_recent_posts()
        assert posts == []

    def test_get_all_tags_empty_directory(self, temp_posts_dir):
        """Test getting tags from empty directory."""
        tags = get_all_tags()
        assert tags == []
