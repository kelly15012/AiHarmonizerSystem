// Theme toggle script
document.addEventListener("DOMContentLoaded", function() {
  const themeToggleButton = document.getElementById('toggle-theme');
  themeToggleButton.addEventListener('click', function() {
    document.body.classList.toggle('dark');
  });
});
