"""Reusable UI components for the FastHTML blog application."""

from fasthtml.common import *


def Layout(request, *content, title: str):
    """A reusable layout component for all pages.

    Args:
        request: The FastHTML request object containing state
        *content: Variable number of content elements to render in main
        title: The page title (will be prefixed with site name)

    Returns:
        Complete HTML document with consistent layout
    """
    return Html(
        Head(
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Title(f"{title} - Personal Blog"),
            Link(rel="preconnect", href="https://fonts.googleapis.com"),
            Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
            Link(
                href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:wght@400;500;600&display=swap",
                rel="stylesheet",
            ),
            Link(rel="stylesheet", href="/static/css/custom.css"),
            Style(request.state.pygments_css),
            Script("""
                // Dark mode toggle functionality
                (function() {
                    // Get saved theme or detect system preference
                    const savedTheme = localStorage.getItem('theme');
                    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                    const initialTheme = savedTheme || (systemPrefersDark ? 'dark' : 'light');
                    
                    // Apply theme immediately to prevent flash
                    document.documentElement.setAttribute('data-theme', initialTheme);
                    
                    // Wait for DOM to load
                    document.addEventListener('DOMContentLoaded', function() {
                        const toggle = document.getElementById('theme-toggle');
                        const body = document.body;
                        
                        // Update toggle button text
                        function updateToggleText(theme) {
                            if (toggle) {
                                const newMode = theme === 'dark' ? 'light' : 'dark';
                                const sunIcon = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" ' +
                                    'stroke="currentColor" stroke-width="2" stroke-linecap="round">' +
                                    '<circle cx="12" cy="12" r="4"/>' +
                                    '<path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41' +
                                    'M2 12h2M20 12h2M6.34 17.66L4.93 19.07M19.07 4.93L17.66 6.34"/></svg>';
                                const moonIcon = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" ' +
                                    'stroke="currentColor" stroke-width="2" stroke-linecap="round">' +
                                    '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
                                const iconSvg = theme === 'dark' ? sunIcon : moonIcon;
                                toggle.innerHTML = iconSvg;
                                toggle.setAttribute('aria-label', `Switch to ${newMode} mode`);
                                toggle.setAttribute('title', `Switch to ${newMode} mode`);
                            }
                        }
                        
                        // Set initial state
                        updateToggleText(initialTheme);
                        
                        // Toggle theme
                        if (toggle) {
                            toggle.addEventListener('click', function() {
                                const currentTheme = document.documentElement.getAttribute('data-theme');
                                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                                
                                document.documentElement.setAttribute('data-theme', newTheme);
                                localStorage.setItem('theme', newTheme);
                                updateToggleText(newTheme);
                            });
                        }
                        
                        // Listen for system theme changes
                        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
                            if (!localStorage.getItem('theme')) {
                                const newTheme = e.matches ? 'dark' : 'light';
                                document.documentElement.setAttribute('data-theme', newTheme);
                                updateToggleText(newTheme);
                            }
                        });
                    });
                })();
            """),
        ),
        Body(
            Div(
                # Sidebar Navigation
                Nav(
                    Header(H2(A("Personal Blog", href="/")), cls="sidebar-header"),
                    Ul(
                        Li(A("Home", href="/")),
                        Li(A("About", href="/about")),
                        cls="nav-links",
                    ),
                    # This is the corrected 'Recent Posts' section from Issue #2
                    Section(
                        H3("Recent Posts"),
                        Ul(
                            *[
                                Li(
                                    A(
                                        post["title"],
                                        href=f"/posts/{post['slug']}",
                                        title=post["title"],
                                    ),
                                    Small(post["date"].strftime("%b %d, %Y"), cls="post-date"),
                                )
                                for post in request.state.recent_posts
                            ]
                        )
                        if request.state.recent_posts
                        else P("No posts yet.", style="font-style: italic; color: #999;"),
                        cls="recent-posts",
                    ),
                    cls="sidebar",
                ),
                # Page-specific content is injected here
                Main(*content, cls="content"),
                cls="grid-container",
            ),
            # Subtle dark mode toggle button - fixed bottom left
            Button(
                NotStr(
                    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" '
                    + 'stroke="currentColor" stroke-width="2" stroke-linecap="round">'
                    + '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>'
                ),
                id="theme-toggle",
                cls="theme-toggle",
                type="button",
                title="Toggle dark mode",
            ),
        ),
    )
