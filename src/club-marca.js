import './club-marca.css'

document.addEventListener('DOMContentLoaded', () => {
  // 1. Copy to Clipboard Functionality with Particle Sparks
  const copyButtons = document.querySelectorAll('.copy-btn');
  
  copyButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const parent = btn.closest('.prompt-container') || btn.closest('.card-brutal') || btn.closest('.compare-box') || btn.parentElement;
      const textEl = parent.querySelector('.prompt-text') || parent.querySelector('code') || parent.querySelector('.copy-target') || parent.querySelector('pre') || parent.querySelector('p');
      
      if (textEl) {
        let textToCopy = textEl.innerText || textEl.textContent;
        textToCopy = textToCopy.trim();
        
        navigator.clipboard.writeText(textToCopy).then(() => {
          const originalContent = btn.innerHTML;
          btn.innerHTML = `
            <svg style="width: 14px; height: 14px; fill: currentColor;" viewBox="0 0 24 24">
              <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
            </svg>
            Copiado
          `;
          btn.classList.add('copied');
          
          // Spawn particle sparks (colored red and blue!)
          spawnSparks(e.clientX, e.clientY);
          
          setTimeout(() => {
            btn.innerHTML = originalContent;
            btn.classList.remove('copied');
          }, 2000);
        }).catch(err => {
          console.error('Error al copiar el texto: ', err);
        });
      }
    });
  });

  // Function to spawn particle sparks on click (Themed with Red/Blue/Black/White colors)
  function spawnSparks(x, y) {
    const particleCount = 16;
    const colors = ['#FF3B30', '#0040FF', '#000000', '#FFFFFF'];
    
    for (let i = 0; i < particleCount; i++) {
      const spark = document.createElement('div');
      const color = colors[Math.floor(Math.random() * colors.length)];
      
      spark.style.position = 'absolute';
      spark.style.pointerEvents = 'none';
      spark.style.zIndex = '10000';
      
      // Randomize shape (circle or square)
      const isCircle = Math.random() > 0.5;
      spark.style.borderRadius = isCircle ? '50%' : '0px';
      spark.style.border = '1.5px solid #000000';
      spark.style.backgroundColor = color;
      
      // Random directions, sizes, and rotations
      const angle = (i / particleCount) * 2 * Math.PI + (Math.random() * 0.4 - 0.2);
      const velocity = 30 + Math.random() * 60;
      const tx = Math.cos(angle) * velocity;
      const ty = Math.sin(angle) * velocity;
      const size = 5 + Math.random() * 8;
      const rot = Math.random() * 360;
      
      spark.style.width = `${size}px`;
      spark.style.height = `${size}px`;
      spark.style.left = `${x + window.scrollX - size/2}px`;
      spark.style.top = `${y + window.scrollY - size/2}px`;
      
      // Animation style
      spark.style.transform = `translate(0, 0) rotate(0deg)`;
      spark.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.6s ease';
      
      document.body.appendChild(spark);
      
      // Force repaint to trigger transition
      requestAnimationFrame(() => {
        spark.style.transform = `translate(${tx}px, ${ty}px) rotate(${rot}deg) scale(0)`;
        spark.style.opacity = '0';
      });
      
      // Clean up
      setTimeout(() => {
        spark.remove();
      }, 600);
    }
  }

  // 2. Active Sidebar Links on Scroll (Scrollspy)
  const sections = document.querySelectorAll('section, header');
  const navLinks = document.querySelectorAll('.nav-link');
  
  function updateActiveLink() {
    let scrollPosition = window.scrollY || document.documentElement.scrollTop;
    let currentSectionId = '';
    
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      
      if (scrollPosition >= (sectionTop - 250)) {
        currentSectionId = section.getAttribute('id');
      }
    });
    
    navLinks.forEach(link => {
      link.classList.remove('active');
      const href = link.getAttribute('href');
      if (href === `#${currentSectionId}` || (href === '#' && currentSectionId === 'hero')) {
        link.classList.add('active');
      }
    });
  }
  
  window.addEventListener('scroll', updateActiveLink);
  updateActiveLink(); // Run once on load

  // 3. Dynamic Reveal on Scroll
  const selectorsToAnimate = [
    '.section-title',
    '.card-brutal',
    '.card-brutal-dark',
    '.rules-container-brutal',
    '.feature-card',
    '.club-bottom-infobar',
    '.telegram-cta-container',
    '.text-editorial'
  ];
  
  document.querySelectorAll(selectorsToAnimate.join(', ')).forEach(el => {
    if (!el.closest('header') && !el.closest('.top-announcement-bar')) {
      el.classList.add('reveal-element');
    }
  });

  const revealElements = document.querySelectorAll('.reveal-element');
  
  if ('IntersectionObserver' in window && revealElements.length > 0) {
    const observerOptions = {
      root: null,
      threshold: 0.05,
      rootMargin: '0px 0px -45px 0px'
    };
    
    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);
    
    revealElements.forEach(el => {
      observer.observe(el);
    });
  } else {
    revealElements.forEach(el => {
      el.classList.add('visible');
    });
  }
});
