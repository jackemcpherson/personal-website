# Personal Website Implementation Plan

**Author:** Jack McPherson  
**Version:** 1.0  
**Last Updated:** August 2025  

## 1. Environment Setup & Project Structure

### 1.1 Initialize Project with uv
```bash
uv init personal-website
cd personal-website
```

### 1.2 Create Project Structure
```
/personal-website
├── .gitignore
├── pyproject.toml
├── README.md
├── Dockerfile
└── /src
    └── /main_app
        ├── __init__.py
        ├── app.py
        ├── /routes
        │   ├── __init__.py
        │   ├── home.py
        │   ├── about.py
        │   ├── posts.py
        │   └── tags.py
        ├── /templates
        │   ├── base.html
        │   ├── home.html
        │   ├── about.html
        │   ├── post.html
        │   └── tag_list.html
        ├── /static
        │   ├── /css
        │   │   └── custom.css
        │   ├── /fonts
        │   └── /images
        └── /posts
            └── sample-post.md
```

### 1.3 Configure Dependencies
Add to `pyproject.toml`:
```toml
[project]
dependencies = [
    "fasthtml",
    "python-frontmatter",
    "markdown",
    "pygments",
    "uvicorn[standard]",
]

[project.optional-dependencies]
dev = [
    "ruff",
    "pytest",
    "pytest-asyncio",
]
```

## 2. Core Application Development

### 2.1 Main Application Entry Point (`app.py`)
```python
"""Main FastHTML application entry point."""

from fasthtml.common import *
from routes import home, about, posts, tags
from utils.content import load_recent_posts

app = FastHTML()

# Global context function for navigation data
@app.middleware("http")
async def add_navigation_context(request, call_next):
    """Add recent posts to request context for navigation menu."""
    request.state.recent_posts = load_recent_posts(limit=3)
    response = await call_next(request)
    return response

# Include route modules
app.mount("/", home.router)
app.mount("/about", about.router)
app.mount("/posts", posts.router)
app.mount("/tags", tags.router)
app.mount("/static", StaticFiles(directory="static"), name="static")
```

### 2.2 Base HTML Template (`templates/base.html`)
Create responsive layout with:
- Pico.css CDN link
- Google Fonts (Montserrat, Lora)
- Custom CSS overrides
- Left-hand navigation menu
- Color scheme: Background `#F5F5F5`, Text `#111111`, Accent `#FF5733`

### 2.3 Left-Hand Navigation Menu
Include in base template:
- "Home" link
- "About" link
- 3 most recent blog post titles (dynamic)

**Implementation Note:** Recent posts will be available via `request.state.recent_posts` in all templates through the middleware. Create a navigation component or template partial that can access this data consistently across all pages.

## 3. Content Management System

### 3.1 Markdown Parser Module
Create utility functions to:
- Parse YAML front matter (title, date, tags)
- Convert Markdown to HTML
- Apply syntax highlighting with Pygments
- Extract post metadata

### 3.2 Post Loading System
Implement functions to:
- Scan `/posts` directory for `.md` files
- Parse and cache post metadata
- Sort posts by date (reverse chronological)
- Filter posts by tags

**Key Functions:**
```python
def load_recent_posts(limit: int = 3) -> list[dict]:
    """Load the most recent blog posts for navigation.
    
    Args:
        limit: Maximum number of recent posts to return
        
    Returns:
        List of post dictionaries with metadata
    """
    # Implementation with caching for performance
```

## 4. Route Implementation

### 4.1 Home Route (`routes/home.py`)
```python
"""Homepage route displaying blog index."""

@rt("/")
def home():
    """Display all blog posts in reverse chronological order."""
    posts = load_all_posts()  # Returns sorted list
    return render_template("home.html", posts=posts)
```

Features:
- Load all posts with metadata
- Display title, date, summary, tags
- Link titles to individual post pages
- Make tags clickable (link to tag pages)

### 4.2 About Route (`routes/about.py`)
```python
"""About page route."""

@rt("/about")
def about(request):
    """Display about page with bio and links."""
    return render_template("about.html", recent_posts=request.state.recent_posts)
```

### 4.3 Posts Route (`routes/posts.py`)
```python
"""Individual blog post routes."""

@rt("/posts/{post_name}")
def post_detail(post_name: str):
    """Display individual blog post."""
    post = load_post(post_name)
    if not post:
        return NotFound()
    return render_template("post.html", post=post)
```

Features:
- Load specific post by filename
- Render Markdown content
- Display metadata (title, date, tags)
- Include navigation back to home

### 4.4 Tags Route (`routes/tags.py`)
```python
"""Tag filtering routes."""

@rt("/tags/{tag_name}")
def tag_posts(tag_name: str):
    """Display all posts with specific tag."""
    posts = load_posts_by_tag(tag_name)
    return render_template("tag_list.html", tag=tag_name, posts=posts)
```

## 5. Styling & Design

### 5.1 Custom CSS (`static/css/custom.css`)
Override Pico.css defaults:
- Set color palette (background, text, accent)
- Style left navigation menu
- Configure typography (Montserrat/Lora)
- Ensure responsive design
- Style code blocks and syntax highlighting

### 5.2 Typography Implementation
- Import Google Fonts in base template
- Apply Montserrat to headings
- Apply Lora to body text

## 6. Content Creation

### 6.1 Sample Blog Post
Create `posts/sample-post.md`:
```markdown
---
title: Welcome to My Blog
date: 2025-08-08
tags: [introduction, meta]
---

# Welcome to My Blog

This is a sample blog post demonstrating the Markdown rendering capabilities...
```

### 6.2 About Page Content
Write biographical content and social links in `templates/about.html`

## 7. Code Quality & Documentation

### 7.1 Python Documentation
Add docstrings to all functions using requests style:
```python
def load_post(post_name: str) -> dict | None:
    """Load and parse a blog post from markdown file.
    
    Args:
        post_name: The filename (without .md extension) of the post to load
        
    Returns:
        Dictionary containing post data and metadata, or None if not found
    """
```

### 7.2 Code Formatting
Configure `ruff` in `pyproject.toml` and format all Python files

## 8. Containerization

### 8.1 Dockerfile
```dockerfile
# Use a specific version for reproducibility
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install uv for dependency management
RUN pip install uv

# Copy dependency file first to leverage Docker cache
COPY pyproject.toml .

# Install dependencies using uv
RUN uv pip install --system --no-cache .

# Copy application source code
COPY ./src ./src

# Expose port
EXPOSE 8000

# Run application with uvicorn
CMD ["uvicorn", "src.main_app.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 9. Project Documentation

### 9.1 README.md
Include:
- Project overview
- Setup instructions
- Development workflow
- Deployment guide

### 9.2 .gitignore
Exclude:
- `__pycache__/`
- `.venv/`
- `.env`
- IDE files

## 10. Security Model

### 10.1 Markdown Trust Model

**ASSUMPTION: All blog posts are trusted content authored by the site owner.**

The application processes Markdown files directly without sanitization based on the following security model:

1. **Source Control**: All blog posts are stored in the `/posts` directory and committed to the repository
2. **Author Trust**: The site owner is the sole author of all content 
3. **No User Input**: The application does not accept user-generated Markdown content
4. **Content Security Policy**: CSP headers restrict inline scripts and external resources
5. **File System Access**: Only pre-existing `.md` files in the designated posts directory are processed

**Security Implications:**
- Raw HTML in Markdown files will be rendered as-is
- JavaScript in Markdown content could execute (mitigated by CSP)
- No protection against malicious Markdown if the source is compromised

**Rationale:** This trust model is appropriate for a personal blog where:
- The author controls all content creation and deployment
- Content undergoes review through the git workflow
- Performance benefits of avoiding sanitization overhead
- Flexibility to include custom HTML when needed

If this application were to accept untrusted user content in the future, Markdown sanitization with a library like `bleach` or `markdown-safe` would be required.

## 11. Testing & Validation

### 10.1 Automated Testing Framework
Set up `pytest` for unit and integration tests:
```python
# tests/test_content.py
def test_load_recent_posts():
    """Test loading recent posts for navigation."""
    posts = load_recent_posts(limit=2)
    assert len(posts) <= 2
    # Additional assertions

# tests/test_routes.py
def test_home_page_loads():
    """Test homepage returns 200 status."""
    # FastHTML test client integration
```

### 10.2 Manual Testing Checklist
- [ ] Homepage displays posts correctly
- [ ] Individual post pages render properly
- [ ] Tags filter posts correctly
- [ ] About page displays
- [ ] Navigation works on all pages (with recent posts)
- [ ] Responsive design on mobile
- [ ] Syntax highlighting works

### 10.3 Code Quality Checks
- [ ] All Python code formatted with `ruff`
- [ ] All functions have docstrings
- [ ] No inline comments present
- [ ] Clean project structure
- [ ] All tests pass with `pytest`

## Implementation Order

1. Set up project structure and dependencies (including pytest)
2. Implement post parsing and loading utilities (with recent posts function)
3. Create base HTML template with dynamic navigation
4. Set up middleware for global navigation context
5. Build home page route and template
6. Create individual post route and template
7. Add about page functionality
8. Implement tag filtering system
9. Apply styling and design
10. Add sample content
11. Write basic unit tests for content utilities
12. Create optimized Docker configuration
13. Final testing and documentation

## Critical Implementation Notes

### Dynamic Navigation Data Solution
The key challenge of providing recent posts data to the base template is solved through FastHTML middleware that adds `recent_posts` to the request state, making it available in all route handlers and templates.

### Performance Considerations
- Implement caching for post metadata to avoid filesystem reads on every request
- Consider using application startup events to pre-load and cache post data
- Recent posts data should be cached with a reasonable TTL

### Testing Strategy
While V1 focuses on core functionality, the pytest framework is configured from the start to enable easy addition of tests for utility functions, especially the content management system components.