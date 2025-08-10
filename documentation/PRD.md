# Personal Website Product Requirements Document

**Project Name:** Personal Website & Blog  
**Author:** Jack McPherson  
**Version:** 1.0  
**Status:** Production Ready  
**Last Updated:** August 2025  

## 1. Overview & Vision

### 1.1 Project Purpose
To create a production-ready personal website for publishing technical blog posts. A secondary purpose is to serve as a professional landing page with "About" information and links to professional profiles.

### 1.2 Target Audience
Potential employers and fellow developers.

### 1.3 Success Metrics
The website is enjoyable to use and update, leading to an increase in the author's writing and publishing frequency. The codebase serves as a high-quality example of the author's work.

## 2. Design & User Experience (UX)

### 2.1 Aesthetic
Minimalist, professional, and responsive. Inspired by 1960s IBM corporate design and Penguin Classics book design.

### 2.2 Core Pages
- Homepage (Blog Index)
- About Page
- Individual Blog Post pages
- Tag-filtered list pages

### 2.3 Navigation
A persistent left-hand sidebar serves as the primary site navigation.

### 2.4 Production Styling
- **Framework:** Pico.css with comprehensive custom overrides
- **Color Palette:** IBM Heritage Blue (`#006699`) with neutral grays
- **Typography:** IBM Plex Sans, Serif, and Mono fonts
- **Layout:** 8px baseline grid system with responsive breakpoints

## 3. Functional Requirements

### 3.1 Homepage (Blog Index)
- Displays all blog entries in reverse chronological order
- Each entry shows: Title, Publication Date, excerpt, and clickable Tags
- Post titles link to individual post pages
### 3.2 Blog Content & Posts
- Blog posts created from Markdown files with YAML frontmatter
- Metadata structure:
  ```yaml
  ---
  title: My First Post
  date: 2025-08-15
  tags: [python, fasthtml, webdev]
  excerpt: Brief description
  ---
  ```
- Full Markdown rendering with syntax-highlighted code blocks (Pygments)
- Unique URLs: `/posts/<post-name>`
### 3.3 About Page
Contains biographical information and links to professional profiles.
### 3.4 Tag Functionality
- Tag links navigate to filtered list pages
- Pages display all posts sharing the specific tag
- **Tag Normalization:** All tags automatically converted to lowercase for consistency
### 3.5 Sidebar Navigation
- Visible on all pages
- Contains "Home" and "About" links
- Displays 3 most recent blog post titles with direct links

## 4. Technical & Non-Functional Requirements

### 4.1 Core Technologies
- **Framework:** FastHTML (Python web framework)
- **Package Manager:** uv
- **Server:** Uvicorn ASGI server

### 4.2 Code Quality Standards
- Repository must be exceptionally clean and well-structured
- All Python code formatted with `ruff`
- 'Requests' style docstrings for all functions
- No inline code comments permitted

### 4.3 Architecture
- Modular design for maintainability
- Docker containerization for deployment
- Comprehensive testing with pytest

### 4.4 Project Structure
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
            ├── /routes         # Handlers for /, /about, /posts/*, /tags/*
            ├── /templates      # HTML layout and page templates
            ├── /static         # Custom CSS, fonts, images
            └── /posts          # Markdown blog files
    ```