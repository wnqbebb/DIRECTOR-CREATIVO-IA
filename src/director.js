import './director.css'

document.addEventListener('DOMContentLoaded', () => {
  // 1. Copy to Clipboard Functionality with Particle Sparks
  const copyButtons = document.querySelectorAll('.copy-btn');
  
  copyButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const parent = btn.closest('.prompt-container') || btn.closest('.card-brutal') || btn.closest('.compare-box') || btn.parentElement;
      const textEl = parent.querySelector('.prompt-text') || parent.querySelector('code') || parent.querySelector('.copy-target') || parent.querySelector('pre');
      
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
          
          // Spawn particle sparks
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

  // Function to spawn particle sparks on click
  function spawnSparks(x, y) {
    const particleCount = 12;
    const shapes = ['circle', 'square', 'cross', 'triangle'];
    for (let i = 0; i < particleCount; i++) {
      const spark = document.createElement('div');
      const shape = shapes[Math.floor(Math.random() * shapes.length)];
      spark.className = `spark-particle spark-${shape}`;
      
      // Random directions, sizes, and rotations
      const angle = (i / particleCount) * 2 * Math.PI + (Math.random() * 0.4 - 0.2);
      const velocity = 40 + Math.random() * 80;
      const tx = Math.cos(angle) * velocity;
      const ty = Math.sin(angle) * velocity;
      const size = 6 + Math.random() * 10;
      const rot = Math.random() * 360;
      
      spark.style.width = `${size}px`;
      spark.style.height = `${size}px`;
      spark.style.left = `${x + window.scrollX - size/2}px`;
      spark.style.top = `${y + window.scrollY - size/2}px`;
      spark.style.setProperty('--tx', `${tx}px`);
      spark.style.setProperty('--ty', `${ty}px`);
      spark.style.setProperty('--rot', `${rot}deg`);
      
      document.body.appendChild(spark);
      
      // Clean up
      setTimeout(() => {
        spark.remove();
      }, 750);
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
      
      if (scrollPosition >= (sectionTop - 280)) {
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

  // 3. Interactive Tabs for Case Studies
  const tabButtons = document.querySelectorAll('.tab-btn');
  
  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const tabsContainer = btn.closest('.tabs-container');
      const targetPanelId = btn.getAttribute('data-tab');
      
      tabsContainer.querySelectorAll('.tab-btn').forEach(b => {
        b.classList.remove('active');
      });
      
      tabsContainer.querySelectorAll('.tab-panel').forEach(p => {
        p.classList.remove('active');
      });
      
      btn.classList.add('active');
      const targetPanel = tabsContainer.querySelector(`#${targetPanelId}`);
      if (targetPanel) {
        targetPanel.classList.add('active');
      }
    });
  });

  // 4. Live Prompt Builder (Interactive Customizer)
  const builderInputs = document.querySelectorAll('.builder-input');
  const livePromptCode = document.getElementById('live-prompt-code');
  
  if (builderInputs.length > 0 && livePromptCode) {
    function updateLivePrompt() {
      const product = document.getElementById('bp-product').value || '[chaqueta sastre / vestido largo / hoodie]';
      const color = document.getElementById('bp-color').value || '[negro / blanco roto / gris]';
      const material = document.getElementById('bp-material').value || '[cuero sintético / tejido knit / denim]';
      const silueta = document.getElementById('bp-silueta').value || '[oversized / cropped / ajustada]';
      const publico = document.getElementById('bp-publico').value || '[mujeres de 22 a 35 años / estilo urbano]';
      const estilo = document.getElementById('bp-estilo').value || '[lujo minimalista / streetwear premium]';
      const emocion = document.getElementById('bp-emocion').value || '[seguridad / comodidad / elegancia]';
      
      const promptText = `Fotografía editorial de moda vertical 4:5 para campaña de Instagram, modelo usando ${product} de color ${color}, material ${material} en silueta ${silueta}, diseñado para un público de ${publico}, con styling estilo ${estilo}, pose de modelo natural y relajada, expresión que transmita ${emocion}, iluminación suave de estudio con sombras sólidas brutalistas, fondo de papel texturizado gris claro, encuadre plano medio, composición premium, alta definición de texturas, sin texto, sin logos inventados, sin manos deformes, sin ropa distorsionada, sin fondo caótico.`;
      
      livePromptCode.textContent = promptText;
    }
    
    builderInputs.forEach(input => {
      input.addEventListener('input', updateLivePrompt);
    });
    
    // Initial run
    updateLivePrompt();
  }

  // 5. Polaroid Image Lightbox Modal
  const polaroidImgs = document.querySelectorAll('.polaroid-img-wrapper img');
  
  // Create Modal element programmatically
  const lightbox = document.createElement('div');
  lightbox.className = 'brutal-lightbox';
  lightbox.innerHTML = `
    <div class="lightbox-content">
      <span class="lightbox-close">&times;</span>
      <img src="" alt="Zoom" class="lightbox-img">
      <div class="lightbox-caption"></div>
    </div>
  `;
  document.body.appendChild(lightbox);
  
  const lightboxImg = lightbox.querySelector('.lightbox-img');
  const lightboxCaption = lightbox.querySelector('.lightbox-caption');
  const lightboxClose = lightbox.querySelector('.lightbox-close');
  
  polaroidImgs.forEach(img => {
    img.style.cursor = 'zoom-in';
    img.addEventListener('click', () => {
      const parent = img.closest('.polaroid-item');
      const captionText = parent ? parent.querySelector('.polaroid-caption').textContent : '';
      
      lightboxImg.src = img.src;
      lightboxCaption.textContent = captionText;
      lightbox.classList.add('active');
    });
  });
  
  lightbox.addEventListener('click', (e) => {
    if (e.target !== lightboxImg && e.target !== lightboxCaption) {
      lightbox.classList.remove('active');
    }
  });

  // 6. Dynamic Reveal and Intersection Observer for Scroll Animations
  const selectorsToAnimate = [
    '.section-title',
    '.card-brutal',
    '.card-brutal-dark',
    '.compare-grid',
    '.table-brutal-wrapper',
    '.step-item',
    '.polaroid-item',
    '.bubble-brutal-dark',
    '.prompt-container',
    '.bento-grid'
  ];
  
  document.querySelectorAll(selectorsToAnimate.join(', ')).forEach(el => {
    // Skip if it's within header/hero to keep the initial fold fast and responsive
    if (!el.closest('header') && !el.closest('.top-announcement-bar')) {
      el.classList.add('reveal-element');
    }
  });

  const revealElements = document.querySelectorAll('.reveal-element');
  
  if ('IntersectionObserver' in window && revealElements.length > 0) {
    const observerOptions = {
      root: null,
      threshold: 0.05, // Lower threshold so it starts animating as soon as it enters viewport
      rootMargin: '0px 0px -40px 0px'
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
