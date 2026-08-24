document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Drawer Toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileCloseBtn = document.getElementById('mobileCloseBtn');
    const mobileDrawer = document.getElementById('mobileDrawer');
    const drawerOverlay = document.getElementById('drawerOverlay');

    function openDrawer() {
        if (mobileDrawer && drawerOverlay) {
            mobileDrawer.classList.add('open');
            drawerOverlay.classList.add('open');
            document.body.style.overflow = 'hidden';
        }
    }

    function closeDrawer() {
        if (mobileDrawer && drawerOverlay) {
            mobileDrawer.classList.remove('open');
            drawerOverlay.classList.remove('open');
            document.body.style.overflow = '';
        }
    }

    if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', openDrawer);
    if (mobileCloseBtn) mobileCloseBtn.addEventListener('click', closeDrawer);
    if (drawerOverlay) drawerOverlay.addEventListener('click', closeDrawer);

    // 2. Sticky Navbar Scroll Effect
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (navbar) {
            if (window.scrollY > 20) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        }

        // Back to top button visibility
        const backToTop = document.getElementById('backToTop');
        if (backToTop) {
            if (window.scrollY > 400) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        }
    });

    // 3. Back to Top Smooth Scroll
    const backToTop = document.getElementById('backToTop');
    if (backToTop) {
        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // 4. Project Filter Tabs
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-glass-card[data-category]');

    if (filterButtons.length > 0 && projectCards.length > 0) {
        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                filterButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filterValue = btn.getAttribute('data-filter');

                projectCards.forEach(card => {
                    const categories = card.getAttribute('data-category').split(' ');
                    if (filterValue === 'all' || categories.includes(filterValue)) {
                        card.style.display = 'flex';
                        card.style.animation = 'fadeInUp 0.4s ease forwards';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    // 5. FAQ Accordion
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(btn => {
        btn.addEventListener('click', () => {
            const item = btn.parentElement;
            const isOpen = item.classList.contains('active');

            // Close other FAQs
            document.querySelectorAll('.faq-item').forEach(other => {
                if (other !== item) {
                    other.classList.remove('active');
                    const otherBtn = other.querySelector('.faq-question');
                    if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
                }
            });

            // Toggle current FAQ
            if (isOpen) {
                item.classList.remove('active');
                btn.setAttribute('aria-expanded', 'false');
            } else {
                item.classList.add('active');
                btn.setAttribute('aria-expanded', 'true');
            }
        });
    });

    // 6. Auto-dismiss alerts after 6 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            alert.style.transition = 'all 0.4s ease';
            setTimeout(() => alert.remove(), 400);
        }, 6000);
    });

    // 7. Form submission feedback
    const contactForm = document.getElementById('contactForm');
    const submitBtn = document.getElementById('submitBtn');
    if (contactForm && submitBtn) {
        contactForm.addEventListener('submit', () => {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span>Sending Message...</span> <i class="fa-solid fa-spinner fa-spin"></i>';
        });
    }

    // Toast notification function
    function showToast(message, iconClass = 'fa-solid fa-circle-check') {
        let toast = document.querySelector('.zd-toast');
        if (!toast) {
            toast = document.createElement('div');
            toast.className = 'zd-toast';
            document.body.appendChild(toast);
        }
        toast.innerHTML = `<i class="${iconClass}"></i> <span>${message}</span>`;
        toast.classList.add('zd-toast-show');

        if (window.toastTimeout) clearTimeout(window.toastTimeout);
        window.toastTimeout = setTimeout(() => {
            toast.classList.remove('zd-toast-show');
        }, 4000);
    }

    // 8. Enhanced Email Link Handler (copies email + shows toast notification)
    const emailLinks = document.querySelectorAll('a[href^="mailto:"]');
    emailLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const rawHref = link.getAttribute('href') || '';
            const email = rawHref.replace('mailto:', '').split('?')[0].strip ? rawHref.replace('mailto:', '').split('?')[0].strip() : rawHref.replace('mailto:', '').split('?')[0].trim();
            
            if (email) {
                // Copy email address to clipboard
                if (navigator.clipboard && navigator.clipboard.writeText) {
                    navigator.clipboard.writeText(email).then(() => {
                        showToast(`Email copied: ${email}`, 'fa-solid fa-envelope-circle-check');
                    }).catch(() => {
                        showToast(`Contact email: ${email}`, 'fa-solid fa-envelope');
                    });
                } else {
                    showToast(`Contact email: ${email}`, 'fa-solid fa-envelope');
                }
            }
        });
    });

    // 9. Light & Dark Theme Switcher
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const mobileThemeToggleBtn = document.getElementById('mobileThemeToggleBtn');

    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('zd_theme', theme);

        const modeTexts = document.querySelectorAll('.theme-mode-text');
        modeTexts.forEach(txt => {
            txt.textContent = theme === 'light' ? 'Light Mode' : 'Dark Mode';
        });
    }

    function toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        applyTheme(newTheme);
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', toggleTheme);
    }

    if (mobileThemeToggleBtn) {
        mobileThemeToggleBtn.addEventListener('click', toggleTheme);
    }

    // Set initial text state for mobile theme button
    const initialTheme = localStorage.getItem('zd_theme') || 'dark';
    applyTheme(initialTheme);

    // 10. Skills Matrix Category Filter Tabs
    const skillTabBtns = document.querySelectorAll('.skill-tab-btn');
    const skillCards = document.querySelectorAll('.skill-detail-card[data-category]');

    if (skillTabBtns.length > 0 && skillCards.length > 0) {
        skillTabBtns.forEach(tab => {
            tab.addEventListener('click', () => {
                skillTabBtns.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');

                const targetCategory = tab.getAttribute('data-skill-category');

                skillCards.forEach(card => {
                    const cardCategory = card.getAttribute('data-category');
                    if (targetCategory === 'all' || cardCategory === targetCategory) {
                        card.style.display = 'flex';
                        card.style.animation = 'fadeInUp 0.35s ease forwards';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    // 11. Developer Terminal Copy Code Snippet
    const copyProfileBtn = document.getElementById('copyProfileBtn');
    const devProfileCode = document.getElementById('devProfileCode');

    if (copyProfileBtn && devProfileCode) {
        copyProfileBtn.addEventListener('click', async () => {
            try {
                const rawText = devProfileCode.innerText;
                if (navigator.clipboard) {
                    await navigator.clipboard.writeText(rawText);
                    const copyTextSpan = copyProfileBtn.querySelector('.copy-text');
                    const copyIcon = copyProfileBtn.querySelector('i');
                    
                    if (copyTextSpan) copyTextSpan.textContent = 'Copied!';
                    if (copyIcon) copyIcon.className = 'fa-solid fa-check text-cyan';
                    copyProfileBtn.style.borderColor = 'var(--cyan)';

                    setTimeout(() => {
                        if (copyTextSpan) copyTextSpan.textContent = 'Copy';
                        if (copyIcon) copyIcon.className = 'fa-regular fa-clone';
                        copyProfileBtn.style.borderColor = '';
                    }, 2200);
                }
            } catch (err) {
                console.error('Failed to copy code:', err);
            }
        });
    }
});