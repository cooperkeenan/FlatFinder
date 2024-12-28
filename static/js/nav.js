document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navLinksSliding = document.querySelector('.nav-links-sliding');
    const backdrop = document.querySelector('.backdrop');

    hamburger.addEventListener('click', () => {
        navLinksSliding.classList.toggle('active'); // Toggle sliding menu
        backdrop.classList.toggle('active'); // Toggle backdrop
    });

    backdrop.addEventListener('click', () => {
        navLinksSliding.classList.remove('active'); // Hide menu
        backdrop.classList.remove('active'); // Hide backdrop
    });
});
