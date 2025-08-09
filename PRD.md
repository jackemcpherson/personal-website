### **Product Requirements Document (PRD) - v1.0 (Initial Build)**

*   **Project Name:** Personal Blog & Portfolio
*   **Author:** [Your Name]
*   **Version:** 1.0
*   **Status:** Finalized for Initial Build

#### **1. Overview & Vision**

*   **1.1. Project Purpose:** To create a personal website for publishing technical blog posts. A secondary purpose is to serve as a professional landing page with "About" information and links to professional profiles.
*   **1.2. Target Audience:** Potential employers and fellow developers.
*   **1.3. Success Metrics:** The website is enjoyable to use and update, leading to an increase in the author's writing and publishing frequency. The codebase serves as a high-quality example of the author's work.

#### **2. Design & User Experience (UX)**

*   **2.1. Aesthetic:** Minimalist, professional, and responsive. Inspired by 1950s/60s corporate graphic design (e.g., Saul Bass, Penguin paperbacks, Blue Note/Atlantic record labels).
*   **2.2. Core Pages:** Homepage (Blog Index), "About" Page, individual Blog Post pages, and a Tag-filtered list page.
*   **2.3. Navigation:** A persistent left-hand side menu will serve as the primary site navigation.
*   **2.4. Initial Styling:**
    *   **Framework:** Pico.css.
    *   **Color Palette (Initial):** Background: `#F5F5F5` (off-white), Text: `#111111` (near-black), Accent: `#FF5733` (bold orange).
    *   **Typography (Initial):** Headings: *Montserrat*, Body: *Lora*. These will be imported via Google Fonts.

#### **3. Functional Requirements**

*   **3.1. Homepage (Blog Index):**
    *   Displays a list of all blog entries in reverse chronological order.
    *   Each entry in the list will display the post's Title, Publication Date, a short summary, and a list of clickable "Tags".
    *   Clicking a post's title navigates the user to the full post page.
*   **3.2. Blog Content & Posts:**
    *   Blog posts are created from Markdown files.
    *   Each Markdown file will use YAML front matter to define metadata (title, date, tags). Example:
        ```yaml
        ---
        title: My First Post
        date: 2025-08-15
        tags: [python, fasthtml, webdev]
        ---
        ```
    *   The application will render full Markdown, including syntax-highlighted code blocks.
    *   Each post will have a unique page at a URL like `/posts/<post-name>`.
*   **3.3. "About" Page:**
    *   Contains a short biographical paragraph and links to social/professional profiles.
*   **3.4. Tag Functionality:**
    *   Clicking a tag link (either on the homepage or a post page) will take the user to a new page.
    *   This page will list all blog posts that share that specific tag.
*   **3.5. Left-Hand Menu:**
    *   Visible on all pages.
    *   Contains links to "Home" and "About".
    *   Displays a list of the 3 most recent blog post titles, which link directly to their pages.

#### **4. Technical & Non-Functional Requirements**

*   **4.1. Application Framework:** FastHTML.
*   **4.2. Project Management:** `uv`.
*   **4.3. Code Quality:**
    *   The repository must be exceptionally clean and well-structured. Every file must have a clear purpose.
    *   All Python code must be formatted using `ruff`.
    *   All Python functions, methods, and modules must include 'requests' style docstrings.
    *   No inline code comments are permitted.
*   **4.4. Architecture:**
    *   The project will have a modular design to facilitate future enhancements.
    *   The application will be containerized using a `Dockerfile` for deployment portability.
*   **4.5. Project Structure:**
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