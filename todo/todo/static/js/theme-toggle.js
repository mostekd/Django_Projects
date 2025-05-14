// theme-toggle.js
function setTheme(theme) {
    if (theme === 'dark') {
        document.body.classList.add('darkmode');
        localStorage.setItem('theme', 'dark');
        document.getElementById('theme-toggle-icon').textContent = 'dark_mode';
    } else {
        document.body.classList.remove('darkmode');
        localStorage.setItem('theme', 'light');
        document.getElementById('theme-toggle-icon').textContent = 'light_mode';
    }
}

function toggleTheme() {
    const current = localStorage.getItem('theme') || 'dark';
    setTheme(current === 'dark' ? 'light' : 'dark');
}

window.addEventListener('DOMContentLoaded', function() {
    // Set default theme to dark
    const saved = localStorage.getItem('theme') || 'dark';
    setTheme(saved);
    // Add event listener to toggle button
    const btn = document.getElementById('theme-toggle-btn');
    if (btn) {
        btn.addEventListener('click', toggleTheme);
    }
});
