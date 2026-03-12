const header = document.querySelector(".site-header");
const navToggle = document.querySelector(".nav-toggle");
const navShell = document.querySelector(".nav-shell");
const revealElements = document.querySelectorAll("[data-reveal]");
const parallaxRoot = document.querySelector("[data-parallax-root]");
const parallaxItems = document.querySelectorAll("[data-parallax]");
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

const setScrolledState = () => {
    if (!header) {
        return;
    }

    header.classList.toggle("is-scrolled", window.scrollY > 24);
};

const closeMenu = () => {
    if (!header || !navToggle) {
        return;
    }

    header.classList.remove("menu-open");
    navToggle.setAttribute("aria-expanded", "false");
};

if (navToggle && header && navShell) {
    navToggle.addEventListener("click", () => {
        const isOpen = header.classList.toggle("menu-open");
        navToggle.setAttribute("aria-expanded", String(isOpen));
    });

    navShell.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", closeMenu);
    });

    window.addEventListener("resize", () => {
        if (window.innerWidth > 820) {
            closeMenu();
        }
    });
}

setScrolledState();
window.addEventListener("scroll", setScrolledState, { passive: true });

if (!prefersReducedMotion.matches && revealElements.length) {
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) {
                return;
            }

            entry.target.classList.add("is-visible");
            revealObserver.unobserve(entry.target);
        });
    }, {
        threshold: 0.15,
        rootMargin: "0px 0px -10% 0px"
    });

    revealElements.forEach((element) => revealObserver.observe(element));
} else {
    revealElements.forEach((element) => element.classList.add("is-visible"));
}

if (!prefersReducedMotion.matches && parallaxRoot && parallaxItems.length) {
    const handleParallax = (event) => {
        const rect = parallaxRoot.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width - 0.5;
        const y = (event.clientY - rect.top) / rect.height - 0.5;

        parallaxItems.forEach((item) => {
            const depth = Number(item.dataset.parallax || 0.1);
            item.style.transform = `translate3d(${x * depth * 48}px, ${y * depth * 42}px, 0)`;
        });
    };

    const resetParallax = () => {
        parallaxItems.forEach((item) => {
            item.style.transform = "translate3d(0, 0, 0)";
        });
    };

    parallaxRoot.addEventListener("pointermove", handleParallax);
    parallaxRoot.addEventListener("pointerleave", resetParallax);
}
