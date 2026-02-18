// Scroll Animation Observer
const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px"
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target); // Only animate once
        }
    });
}, observerOptions);

document.addEventListener('DOMContentLoaded', () => {
    // Select elements to animate
    const hiddenElements = document.querySelectorAll(
        '.service-card, .section-header, .hero-content, .package-card, .addons-card, .scope-notes, .booking-card, .final-cta'
    );

    hiddenElements.forEach((el) => {
        el.classList.add('hidden-content'); // Add initial hidden class
        observer.observe(el);
    });
});
console.log("Peace Love Social - Loaded");
