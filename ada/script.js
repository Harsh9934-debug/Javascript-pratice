document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
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

    // AUTO SLIDER (Headers from User)
    const slides = [
        "assets/images/wheat_harvest_farm.png",
        "assets/images/pulses_variety_premium.png",
        "assets/images/masala_spices_premium.png",
        "assets/images/about_our_story.png",
        "assets/images/grain_processing_factory.png",
        "assets/images/hero_slider_family_meal.png"
    ];

    const sliderContainer = document.getElementById('heroBgSlider');
    if (sliderContainer) {
        let currentSlide = 0;

        // Init slides
        slides.forEach((imgUrl, index) => {
            const el = document.createElement('div');
            el.className = `pa-hero-bg-slide ${index === 0 ? 'active' : ''}`;
            el.style.backgroundImage = `url('${imgUrl}')`;
            sliderContainer.appendChild(el);
        });

        // Rotate
        setInterval(() => {
            const elSlides = sliderContainer.querySelectorAll('.pa-hero-bg-slide');
            elSlides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % elSlides.length;
            elSlides[currentSlide].classList.add('active');
        }, 5000);
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
