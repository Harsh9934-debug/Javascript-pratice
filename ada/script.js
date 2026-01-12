document.addEventListener('DOMContentLoaded', () => {
    // MOBILE MENU
    const mobileToggle = document.getElementById('mobileToggle');
    const navLinks = document.getElementById('navLinks');
    const links = navLinks.querySelectorAll('a');

    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = mobileToggle.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Close menu when clicking a link
    links.forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            const icon = mobileToggle.querySelector('i');
            if (icon) {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    });

    // AUTO SLIDER
    const slides = [
        { title: "Pure Sharbati Wheat", subtitle: "Handpicked for Softest Rotis" },
        { title: "Premium Toor Dal", subtitle: "Unpolished & Protein Rich" },
        { title: "Organic Spices", subtitle: "Aroma That Tells a Story" }
    ];

    const sliderContainer = document.getElementById('heroSlider');
    if (sliderContainer) {
        let currentSlide = 0;

        // Init slides
        slides.forEach((slide, index) => {
            const el = document.createElement('div');
            el.className = `pa-slide ${index === 0 ? 'active' : ''}`;
            el.innerHTML = `
                <h2 style="color:var(--primary); margin-bottom:10px;">${slide.title}</h2>
                <p style="color:#666;">${slide.subtitle}</p>
            `;
            sliderContainer.appendChild(el);
        });

        // Rotate
        setInterval(() => {
            const elSlides = sliderContainer.querySelectorAll('.pa-slide');
            elSlides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % elSlides.length;
            elSlides[currentSlide].classList.add('active');
        }, 3000);
    }

    // SCROLL REVEAL (Simple Intersection Observer)
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.pa-section').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'all 0.8s ease-out';
        observer.observe(section);
    });
});
