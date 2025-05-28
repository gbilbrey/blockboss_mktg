// Minimal JavaScript for BlockBoss Landing Page
// Most functionality handled by HTMX and Alpine.js

// Only keep essential utilities that are hard to do with HTMX/Alpine
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links (could also be done with CSS scroll-behavior)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

// Utility function for Alpine.js to use
window.isValidEmail = function(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
};

// HTMX event listeners
document.addEventListener('htmx:afterSwap', function(event) {
    // Initialize Calendly widget after HTMX swaps content
    if (event.target.id === 'advisory-modal' && window.Calendly) {
        setTimeout(() => {
            const calendlyWidget = document.querySelector('.calendly-inline-widget');
            if (calendlyWidget && calendlyWidget.dataset.url) {
                window.Calendly.initInlineWidget({
                    url: calendlyWidget.dataset.url,
                    parentElement: calendlyWidget
                });
            }
        }, 100);
    }
});

// Close modal when clicking outside
document.addEventListener('click', function(event) {
    const modal = document.getElementById('advisory-modal');
    if (event.target === modal) {
        modal.innerHTML = '';
    }
}); 