# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal website built with FastHTML (Python web framework). The project is currently in the planning phase with comprehensive documentation in `PRD.md` and `IMPLEMENTATION.md`.

## Development Commands

### Project Setup
- `uv init` - Initialize the project structure
- `uv add <package>` - Add dependencies
- `uv add --dev <package>` - Add development dependencies

### Development Server
- `uvicorn src.main_app.app:app --reload` - Start development server with hot reload
- `uvicorn src.main_app.app:app --reload --port 8001` - Start on custom port

### Code Quality
- `ruff format .` - Format all Python code (required before commits)
- `ruff check .` - Lint and check code quality

### Testing
- `pytest` - Run all tests
- `pytest tests/test_<module>.py` - Run specific test file
- `pytest -v` - Run tests with verbose output
- `pytest --asyncio-mode=auto` - Run async tests

## Architecture

### Core Technologies
- **Framework**: FastHTML (Python web framework)
- **Package Manager**: uv
- **Content**: Markdown files with YAML front matter
- **Styling**: Pico.css with custom overrides
- **Server**: Uvicorn ASGI server

### Project Structure
```
/src
└── /main_app
    ├── app.py              # Main FastHTML application
    ├── /routes             # Route handlers (home, about, posts, tags)
    ├── /templates          # HTML templates
    ├── /static             # CSS, fonts, images
    ├── /posts              # Markdown blog files
    └── /utils              # Content parsing utilities
```

### Key Dependencies
- `fasthtml` - Web framework
- `python-frontmatter` - YAML front matter parsing
- `markdown` - Markdown to HTML conversion
- `pygments` - Code syntax highlighting
- `uvicorn[standard]` - ASGI server

### Content Management
- Blog posts are Markdown files in `/src/main_app/posts/`
- Each post has YAML front matter with: title, date, tags, excerpt
- Content parsing utilities handle Markdown conversion and metadata extraction
- Navigation shows recent posts globally via middleware

### Design System
- **Colors**: Background `#F5F5F5`, Text `#111111`, Accent `#FF5733`
- **Fonts**: Montserrat (headings), Lora (body) via Google Fonts
- **Layout**: Left-hand navigation, responsive design
- **Framework**: Pico.css with custom CSS overrides

## Code Quality Standards

### Python Formatting
- All code MUST be formatted with `ruff format` before commits
- Use 'requests' style docstrings for all functions
- No inline code comments permitted
- Maintain modular, clean architecture

### File Structure
- Route handlers in separate modules by functionality
- Templates follow consistent naming conventions
- Static assets organized by type (CSS, images, fonts)
- Utilities separated from application logic

## Development Notes

### Current Status
The project exists in planning phase with detailed documentation in:
- `PRD.md` - Product requirements and specifications
- `IMPLEMENTATION.md` - Technical implementation plan

### Implementation Order
1. Initialize project with `uv` and dependencies
2. Create content parsing utilities
3. Build base HTML templates with Pico.css
4. Implement route handlers (home, posts, about, tags)
5. Add sample content and styling
6. Set up testing framework
7. Create Docker configuration

### Testing Strategy
- Unit tests for content parsing utilities
- Integration tests for route handlers
- Use `pytest-asyncio` for async testing
- Maintain comprehensive test coverage
- let's make sure we use a timeout when we start the fasthtml app

## Git Workflow & Commit Standards

### Commit Requirements
- ALWAYS format code with `ruff format .` before commits
- Create logical, detailed commits as development progresses
- Never batch multiple unrelated changes into one commit
- Each commit should represent a single logical unit of work

### Commit Message Format
- Use descriptive commit messages that explain WHAT and WHY
- Start with a concise summary (50 chars max)
- Include detailed description if changes are complex
- Reference any issues or requirements being addressed

### When to Commit
- After implementing a complete feature or fix
- After major refactoring or architectural changes
- After fixing layout/styling issues
- Before starting work on a new feature
- When reaching stable milestones

### Examples of Good Commits
- "Fix sidebar layout issues with CSS Grid and Pico.css conflicts"
- "Implement vertical layout for recent posts navigation"
- "Add FastHTML blog application with routes and content parsing"
- "Update responsive design for mobile navigation"