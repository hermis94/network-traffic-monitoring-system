document.addEventListener('DOMContentLoaded', () => {
  const links = document.querySelectorAll('nav a');
  links.forEach((link) => {
    const isCurrent = link.getAttribute('href') === window.location.pathname.split('/').pop();
    if (isCurrent) link.classList.add('active');
  });
});
