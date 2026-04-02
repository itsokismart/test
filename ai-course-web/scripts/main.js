// Main JavaScript functionality

// Smooth scroll to section
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

// Open module modal
function openModule(moduleId) {
    const modal = document.getElementById('module-modal');
    const content = document.getElementById('module-content');
    const moduleData = courseData.modules[moduleId];
    
    if (moduleData) {
        content.innerHTML = `
            <h2>${moduleData.title}</h2>
            ${moduleData.content}
        `;
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

// Open practice modal
function openPractice(practiceId) {
    const modal = document.getElementById('practice-modal');
    const content = document.getElementById('practice-content');
    const practiceData = courseData.practices[practiceId];
    
    if (practiceData) {
        content.innerHTML = `
            <h2>${practiceData.title}</h2>
            ${practiceData.content}
        `;
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

// Close modal
function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Close modal on outside click
window.addEventListener('click', (e) => {
    if (e.target.classList.contains('modal')) {
        e.target.classList.remove('active');
        document.body.style.overflow = 'auto';
    }
});

// Close modal on Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        document.querySelectorAll('.modal.active').forEach(modal => {
            modal.classList.remove('active');
            document.body.style.overflow = 'auto';
        });
    }
});

// Resources tabs functionality
document.addEventListener('DOMContentLoaded', () => {
    // Render resources
    renderResources();
    
    // Render glossary
    renderGlossary();
    
    // Tab switching
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active from all tabs
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            
            // Add active to clicked tab
            btn.classList.add('active');
            const tabId = btn.getAttribute('data-tab');
            document.getElementById(tabId).classList.add('active');
        });
    });
    
    // Glossary search
    const searchInput = document.getElementById('glossary-search');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const searchTerm = e.target.value.toLowerCase();
            filterGlossary(searchTerm);
        });
    }
    
    // Active nav link on scroll
    window.addEventListener('scroll', () => {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-link');
        
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            if (window.scrollY >= sectionTop) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
});

// Render resources
function renderResources() {
    const categories = ['books', 'courses', 'youtube', 'tools'];
    
    categories.forEach(category => {
        const container = document.getElementById(`${category}-list`);
        if (container && courseData.resources[category]) {
            container.innerHTML = courseData.resources[category].map(item => `
                <div class="resource-item">
                    <h4>${item.title}</h4>
                    <p><strong>${item.author}</strong></p>
                    <p>${item.desc}</p>
                </div>
            `).join('');
        }
    });
}

// Render glossary
function renderGlossary() {
    const container = document.getElementById('glossary-container');
    if (container && courseData.glossary) {
        container.innerHTML = courseData.glossary.map(item => `
            <div class="glossary-item" data-term="${item.term.toLowerCase()}">
                <h4>${item.term}</h4>
                <p>${item.def}</p>
            </div>
        `).join('');
    }
}

// Filter glossary
function filterGlossary(searchTerm) {
    const items = document.querySelectorAll('.glossary-item');
    items.forEach(item => {
        const term = item.getAttribute('data-term');
        if (term.includes(searchTerm)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}

// Animate elements on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.module-card, .practice-card, .stat-card, .resource-item, .glossary-item');
    
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// Stats counter animation
function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);
    
    function updateCounter() {
        start += increment;
        if (start < target) {
            element.textContent = Math.floor(start);
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target;
        }
    }
    
    updateCounter();
}

// Trigger stats animation when visible
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const statCards = entry.target.querySelectorAll('.stat-card h3');
            statCards.forEach(card => {
                const text = card.textContent;
                const hasPlus = text.includes('+');
                const number = parseInt(text.replace(/\D/g, ''));
                if (!isNaN(number)) {
                    card.textContent = hasPlus ? `${number}+` : number;
                }
            });
            statsObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

document.addEventListener('DOMContentLoaded', () => {
    const statsSection = document.querySelector('.stats');
    if (statsSection) {
        statsObserver.observe(statsSection);
    }
});

console.log('AI Course website loaded successfully! 🚀');
