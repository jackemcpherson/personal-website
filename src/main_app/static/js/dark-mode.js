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