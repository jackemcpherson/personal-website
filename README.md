# Personal Blog & Portfolio

A modern, minimalist personal blog built with [FastHTML](https://www.fastht.ml/), featuring a clean design inspired by mid-century corporate aesthetics.

## Features

- **Clean, Professional Design**: Minimalist layout with responsive design
- **Markdown-Based Content**: Write blog posts in Markdown with YAML frontmatter
- **Dynamic Navigation**: Sidebar with recent posts on every page  
- **Tag System**: Organize and filter posts by tags
- **Syntax Highlighting**: Code blocks with Pygments syntax highlighting
- **Fast Performance**: Built on FastHTML for speed and efficiency
- **Docker Ready**: Containerized for easy deployment

## Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Development Setup

1. **Clone and setup**:
   ```bash
   cd personal-website
   uv sync
   ```

2. **Run development server**:
   ```bash
   uv run uvicorn src.main_app.app:app --reload
   ```

3. **Visit your site**:
   Open http://localhost:8000

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_content.py
```

### Code Quality

```bash
# Format code
uv run ruff format .

# Check code quality
uv run ruff check .
```

## Project Structure

```
personal-website/
├── src/main_app/           # Main application
│   ├── app.py             # FastHTML app and middleware
│   ├── routes/            # Route handlers
│   │   ├── home.py        # Homepage (blog index)
│   │   ├── posts.py       # Individual post pages
│   │   ├── about.py       # About page
│   │   └── tags.py        # Tag filtering
│   ├── utils/             # Utility functions
│   │   └── content.py     # Content management
│   ├── templates/         # HTML templates
│   ├── static/            # CSS, images, fonts
│   └── posts/             # Markdown blog posts
├── tests/                 # Test suite
├── Dockerfile             # Container configuration
└── pyproject.toml         # Dependencies and config
```

## Writing Blog Posts

Create new posts in `src/main_app/posts/` as Markdown files with YAML frontmatter:

```markdown
---
title: Your Post Title
date: 2025-08-08
tags: [python, web-development, tutorial]
excerpt: A brief description of your post
---

# Your Post Title

Your blog content goes here...

```python
# Code blocks are automatically highlighted
print("Hello, World!")
```
```

## Docker Deployment

### Build and Run

```bash
# Build image
docker build -t personal-blog .

# Run container
docker run -p 8000:8000 personal-blog
```

### Docker Compose (Optional)

```yaml
version: '3.8'
services:
  blog:
    build: .
    ports:
      - "8000:8000"
    restart: unless-stopped
```

## Architecture

### Core Technologies

- **[FastHTML](https://www.fastht.ml/)**: Modern Python web framework
- **[uv](https://docs.astral.sh/uv/)**: Fast Python package manager  
- **[Pico.css](https://picocss.com/)**: Minimal CSS framework
- **[Pygments](https://pygments.org/)**: Syntax highlighting
- **[Markdown](https://python-markdown.github.io/)**: Content processing

### Key Components

- **Content Management**: Markdown files with YAML frontmatter
- **Navigation Middleware**: Injects recent posts into all pages
- **Modular Routes**: Organized by functionality (home, posts, tags, about)
- **Responsive Design**: Mobile-friendly layout
- **Docker Ready**: Production deployment configuration

## Customization

### Styling

Edit `src/main_app/static/css/custom.css` to customize:
- Color scheme (currently orange accent: `#FF5733`)
- Typography (Montserrat + Lora fonts)
- Layout and spacing

### Content

- **About Page**: Edit `src/main_app/routes/about.py`
- **Homepage**: Modify `src/main_app/routes/home.py`
- **Navigation**: Customize `src/main_app/templates/base.html`

## Development Commands

```bash
# Start development server
uv run uvicorn src.main_app.app:app --reload --port 8001

# Run tests
uv run pytest tests/ -v

# Format code  
uv run ruff format .

# Check code quality
uv run ruff check .

# Add new dependencies
uv add package-name

# Add development dependencies  
uv add --dev package-name
```

## Design Philosophy

This blog follows several key principles:

- **Minimalism**: Clean, uncluttered design focused on readability
- **Performance**: Fast loading with efficient caching
- **Maintainability**: Well-structured, documented code
- **Accessibility**: Responsive design that works on all devices
- **Professional**: Suitable for both personal and professional use

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

While this is a personal blog template, contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Submit a pull request

## Support

For questions or issues, please [open an issue](https://github.com/your-username/personal-website/issues) on GitHub.