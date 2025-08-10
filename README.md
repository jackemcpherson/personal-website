# Personal Website & Blog

[![CI Status](https://github.com/jackmcpherson/personal-website/actions/workflows/ci.yml/badge.svg)](https://github.com/jackmcpherson/personal-website/actions)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![FastHTML](https://img.shields.io/badge/FastHTML-modern-green.svg)](https://fastht.ml/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

A production-ready personal blog and portfolio built with **FastHTML**, featuring a minimalist design inspired by 1960s IBM corporate aesthetics. Designed for developers who value clean code, fast performance, and professional presentation.

## ✨ Features

- **🎨 Professional Design**: Minimalist IBM Heritage-inspired theme with responsive layout
- **📝 Markdown Content**: Write posts in Markdown with YAML frontmatter support
- **🚀 High Performance**: Built on FastHTML with optimized caching and compression
- **🏷️ Smart Tagging**: Organize and filter content by tags with automatic normalization
- **🔍 SEO Optimized**: Automatic sitemap, RSS feed, and robots.txt generation
- **🎯 Syntax Highlighting**: Beautiful code blocks powered by Pygments
- **🐳 Docker Ready**: Production-ready containerization with cloud deployment support
- **🔒 Security First**: Content Security Policy, security headers, and best practices
- **📱 Mobile Friendly**: Responsive design that works on all devices
- **⚡ Fast Loading**: Optimized assets with intelligent caching strategies

## 🚀 Quick Start

### Prerequisites

- **Python 3.12+** (required)
- **[uv](https://docs.astral.sh/uv/)** (recommended package manager)
- **Docker** (optional, for containerized deployment)

### Local Development

```bash
# Clone the repository
git clone https://github.com/your-username/personal-website.git
cd personal-website

# Install dependencies
uv sync

# Start development server with hot reload
uv run uvicorn src.main_app.app:app --reload

# Visit your site
open http://localhost:8000
```

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

Edit `src/main_app/static/css/custom.css` to customize the IBM Heritage design system:
- **Color Scheme**: IBM Heritage Blue (`#006699`) with neutral grays
- **Typography**: IBM Plex Sans, Serif, and Mono fonts
- **Layout**: 8px baseline grid system with semantic spacing tokens
- **Responsive Breakpoints**: Mobile ≤480px, Tablet 481-960px, Desktop 961-1440px

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