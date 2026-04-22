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

// Stat counter: count up to data-count when tile scrolls into view.
const statValues = document.querySelectorAll(".stat-value[data-count]");
if (statValues.length) {
    const animateCount = (el) => {
        const target = Number(el.dataset.count || 0);
        const suffix = el.dataset.suffix || "";
        const duration = 1200;
        const start = performance.now();

        const step = (now) => {
            const progress = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            const value = Math.round(target * eased);
            el.textContent = `${value}${suffix}`;
            if (progress < 1) {
                requestAnimationFrame(step);
            } else {
                el.textContent = `${target}${suffix}`;
            }
        };

        requestAnimationFrame(step);
    };

    if (prefersReducedMotion.matches) {
        statValues.forEach((el) => {
            el.textContent = `${el.dataset.count || 0}${el.dataset.suffix || ""}`;
        });
    } else {
        const statObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) {
                    return;
                }
                animateCount(entry.target);
                statObserver.unobserve(entry.target);
            });
        }, { threshold: 0.45 });

        statValues.forEach((el) => statObserver.observe(el));
    }
}

// Logo video fallback: if the video can't play, swap to the static PNG.
const logoVideos = document.querySelectorAll(".logo-video");
logoVideos.forEach((video) => {
    const handleFailure = () => {
        document.documentElement.classList.add("no-video");
    };
    video.addEventListener("error", handleFailure);
    const playPromise = video.play();
    if (playPromise && typeof playPromise.catch === "function") {
        playPromise.catch(handleFailure);
    }
});

// Before/after comparison slider: drag, touch, or arrow keys to reveal.
const beforeAfter = document.querySelector(".before-after");
if (beforeAfter) {
    const setPos = (pct) => {
        const clamped = Math.max(0, Math.min(100, pct));
        beforeAfter.style.setProperty("--ba-pos", `${clamped}%`);
        beforeAfter.setAttribute("aria-valuenow", String(Math.round(clamped)));
    };

    const pctFromEvent = (event) => {
        const rect = beforeAfter.getBoundingClientRect();
        const clientX = event.touches ? event.touches[0].clientX : event.clientX;
        return ((clientX - rect.left) / rect.width) * 100;
    };

    let active = false;
    const start = (event) => {
        active = true;
        beforeAfter.setPointerCapture?.(event.pointerId);
        setPos(pctFromEvent(event));
    };
    const move = (event) => {
        if (!active) return;
        event.preventDefault();
        setPos(pctFromEvent(event));
    };
    const end = () => { active = false; };

    beforeAfter.addEventListener("pointerdown", start);
    beforeAfter.addEventListener("pointermove", move);
    beforeAfter.addEventListener("pointerup", end);
    beforeAfter.addEventListener("pointercancel", end);
    beforeAfter.addEventListener("pointerleave", end);

    beforeAfter.addEventListener("keydown", (event) => {
        const current = Number(beforeAfter.getAttribute("aria-valuenow") || 50);
        if (event.key === "ArrowLeft") {
            setPos(current - 5);
            event.preventDefault();
        } else if (event.key === "ArrowRight") {
            setPos(current + 5);
            event.preventDefault();
        } else if (event.key === "Home") {
            setPos(0);
            event.preventDefault();
        } else if (event.key === "End") {
            setPos(100);
            event.preventDefault();
        }
    });
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
