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
                                toggle.textContent = theme === 'dark' ? '☀️' : '🌙';
                                const newMode = theme === 'dark' ? 'light' : 'dark';
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
            Button("🌙", id="theme-toggle", cls="theme-toggle", type="button", title="Toggle dark mode"),
        ),
    )
