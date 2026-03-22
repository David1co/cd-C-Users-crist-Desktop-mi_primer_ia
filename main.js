document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.5)';
            navbar.style.padding = '5px 0';
        } else {
            navbar.style.boxShadow = 'none';
            navbar.style.padding = '0';
        }
    });

    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileBtn && navLinks) {
        mobileBtn.addEventListener('click', () => {
            navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
        });
    }

    initComparisonSlider();

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const headerOffset = 70;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                window.scrollTo({ top: offsetPosition, behavior: "smooth" });
            }
        });
    });
});

function initComparisonSlider() {
    const slider = document.querySelector('.comparison-slider');
    if (!slider) return;
    const beforeImage = slider.querySelector('.before');
    const handle = slider.querySelector('.slider-handle');
    let isDragging = false;

    const getPos = (e) => {
        const rect = slider.getBoundingClientRect();
        let x = e.type.includes('touch') ? e.changedTouches[0].pageX - rect.left - window.scrollX : e.pageX - rect.left - window.scrollX;
        if (x < 0) x = 0;
        if (x > rect.width) x = rect.width;
        return x;
    };

    const updateSlider = (x) => {
        beforeImage.style.width = x + "px";
        handle.style.left = x + "px";
    };

    handle.addEventListener('mousedown', () => isDragging = true);
    window.addEventListener('mouseup', () => isDragging = false);
    window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        updateSlider(getPos(e));
    });

    handle.addEventListener('touchstart', (e) => { isDragging = true; e.preventDefault(); }, { passive: false });
    window.addEventListener('touchend', () => isDragging = false);
    window.addEventListener('touchmove', (e) => { if (!isDragging) return; updateSlider(getPos(e)); }, { passive: false });
}
