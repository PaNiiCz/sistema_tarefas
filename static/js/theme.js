// Alternar tema claro/escuro
const themeToggle = document.getElementById('themeToggle');
const themeIcon = themeToggle.querySelector('i');
const themeText = themeToggle.querySelector('span');

// Verificar tema salvo
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
    document.body.classList.add('dark-mode');
    themeIcon.className = 'bi bi-sun-fill';
    themeText.textContent = 'Modo Claro';
}

themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    
    if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
        themeIcon.className = 'bi bi-sun-fill';
        themeText.textContent = 'Modo Claro';
    } else {
        localStorage.setItem('theme', 'light');
        themeIcon.className = 'bi bi-moon-stars';
        themeText.textContent = 'Modo Escuro';
    }
});