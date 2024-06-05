document.addEventListener('DOMContentLoaded', function () {
    const themeSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
    const body = document.body;

    // Function to switch theme
    function switchTheme(e) {
        if (e.target.checked) {
            body.classList.add('light-theme');
            localStorage.setItem('theme', 'light');
        } else {
            body.classList.remove('light-theme');
            localStorage.setItem('theme', 'dark');
        }
    }

    // Event listener for checkbox state change
    themeSwitch.addEventListener('change', switchTheme, false);

    // Check the saved theme on page load
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme) {
        body.classList.add(currentTheme + '-theme');
        if (currentTheme === 'light') {
            themeSwitch.checked = true;
        }
    }
});
