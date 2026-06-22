import './rostro-marca.css'

document.addEventListener('DOMContentLoaded', () => {
  // 1. Copy to Clipboard with Brutalist Particle Sparks
  const copyButtons = document.querySelectorAll('.copy-btn');
  
  copyButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const container = btn.closest('.prompt-container');
      const textEl = container ? container.querySelector('.prompt-text') : null;
      
      if (textEl) {
        let textToCopy = textEl.innerText || textEl.textContent;
        textToCopy = textToCopy.trim();
        
        navigator.clipboard.writeText(textToCopy).then(() => {
          const originalContent = btn.innerHTML;
          btn.innerHTML = `
            <svg style="width: 14px; height: 14px; fill: currentColor;" viewBox="0 0 24 24">
              <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
            </svg>
            ¡Copiado!
          `;
          btn.classList.add('copied');
          
          // Spawn brutalist red/black sparks
          spawnSparks(e.clientX, e.clientY);
          
          setTimeout(() => {
            btn.innerHTML = originalContent;
            btn.classList.remove('copied');
          }, 2000);
        }).catch(err => {
          console.error('Error al copiar: ', err);
        });
      }
    });
  });

  function spawnSparks(x, y) {
    const particleCount = 14;
    const colors = ['#D71913', '#050505', '#F5B51A', '#ffffff'];
    const shapes = ['circle', 'square', 'cross', 'triangle'];
    
    for (let i = 0; i < particleCount; i++) {
      const spark = document.createElement('div');
      const shape = shapes[Math.floor(Math.random() * shapes.length)];
      const color = colors[Math.floor(Math.random() * colors.length)];
      
      spark.className = `spark-particle spark-${shape}`;
      spark.style.backgroundColor = shape !== 'cross' ? color : 'transparent';
      if (shape === 'cross') {
        spark.style.color = color;
      }
      
      const angle = (i / particleCount) * 2 * Math.PI + (Math.random() * 0.4 - 0.2);
      const velocity = 50 + Math.random() * 70;
      const tx = Math.cos(angle) * velocity;
      const ty = Math.sin(angle) * velocity;
      const size = 8 + Math.random() * 8;
      const rot = Math.random() * 360;
      
      spark.style.width = `${size}px`;
      spark.style.height = `${size}px`;
      spark.style.left = `${x + window.scrollX - size/2}px`;
      spark.style.top = `${y + window.scrollY - size/2}px`;
      spark.style.setProperty('--tx', `${tx}px`);
      spark.style.setProperty('--ty', `${ty}px`);
      spark.style.setProperty('--rot', `${rot}deg`);
      
      document.body.appendChild(spark);
      
      setTimeout(() => {
        spark.remove();
      }, 800);
    }
  }

  // 2. Scrollspy - Highlight active sidebar link
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
  updateActiveLink();

  // 3. Image Lightbox for Collage/Polaroid view
  const zoomableImages = document.querySelectorAll('.zoomable-img, .collage-figure img');
  
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
  
  zoomableImages.forEach(img => {
    img.style.cursor = 'zoom-in';
    img.addEventListener('click', () => {
      lightboxImg.src = img.src;
      lightboxCaption.textContent = img.alt || 'Visualización de Consistencia';
      lightbox.classList.add('active');
    });
  });
  
  lightbox.addEventListener('click', (e) => {
    if (e.target !== lightboxImg && e.target !== lightboxCaption) {
      lightbox.classList.remove('active');
    }
  });

  // 4. Reveal Animations on Scroll
  const animSelectors = [
    '.section-title',
    '.card-brutal',
    '.card-brutal-dark',
    '.step-container',
    '.prompt-container',
    '.doodle-annotation',
    '.rules-container-brutal',
    '.grid-editorial'
  ];
  
  document.querySelectorAll(animSelectors.join(', ')).forEach(el => {
    if (!el.closest('header')) {
      el.classList.add('reveal-element');
    }
  });
  
  const revealElements = document.querySelectorAll('.reveal-element');
  
  if ('IntersectionObserver' in window && revealElements.length > 0) {
    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.05,
      rootMargin: '0px 0px -30px 0px'
    });
    
    revealElements.forEach(el => observer.observe(el));
  } else {
    revealElements.forEach(el => el.classList.add('visible'));
  }

  // 5. Before/After Image Slider Drag Logic
  const beforeAfterSliders = document.querySelectorAll('.before-after-slider');
  beforeAfterSliders.forEach(slider => {
    const handle = slider.querySelector('.slider-handle');
    if (handle) {
      handle.addEventListener('input', (e) => {
        slider.style.setProperty('--slider-pos', `${e.target.value}%`);
      });
    }
  });

  // 6. Interactive Prompt Builder Logic
  const builderPanel = document.querySelector('.prompt-builder-panel');
  if (builderPanel) {
    const optionButtons = builderPanel.querySelectorAll('.opt-btn');
    const outputText = builderPanel.querySelector('#builder-output-text');
    const copyBuilderBtn = builderPanel.querySelector('#copy-builder-btn');

    function updateGeneratedPrompt() {
      const activeOptions = {};
      const coords = ['prenda', 'actitud', 'escenario', 'rol', 'formato'];
      
      coords.forEach(coord => {
        const activeBtn = builderPanel.querySelector(`.builder-options[data-coord="${coord}"] .opt-btn.active`);
        if (activeBtn) {
          activeOptions[coord] = activeBtn.getAttribute('data-val');
        } else {
          activeOptions[coord] = '';
        }
      });

      const generatedText = `Crea una imagen de esta persona como ${activeOptions.rol} usando ${activeOptions.prenda} con ${activeOptions.actitud}. Entorno: ${activeOptions.escenario}. Mantén su identidad facial exactamente igual usando las referencias del Kit de Identidad proporcionadas. ${activeOptions.formato}`;
      
      if (outputText) {
        outputText.textContent = generatedText;
      }
    }

    optionButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const group = btn.closest('.builder-options');
        if (group) {
          group.querySelectorAll('.opt-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          updateGeneratedPrompt();
        }
      });
    });

    if (copyBuilderBtn) {
      copyBuilderBtn.addEventListener('click', (e) => {
        if (outputText) {
          const textToCopy = (outputText.innerText || outputText.textContent).trim();
          navigator.clipboard.writeText(textToCopy).then(() => {
            const originalContent = copyBuilderBtn.innerHTML;
            copyBuilderBtn.innerHTML = `
              <svg style="width: 14px; height: 14px; fill: currentColor;" viewBox="0 0 24 24">
                <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
              </svg>
              ¡Copiado!
            `;
            copyBuilderBtn.classList.add('copied');
            spawnSparks(e.clientX, e.clientY);
            setTimeout(() => {
              copyBuilderBtn.innerHTML = originalContent;
              copyBuilderBtn.classList.remove('copied');
            }, 2000);
          }).catch(err => {
            console.error('Error al copiar: ', err);
          });
        }
      });
    }

    // Run once on load to fill initial prompt
    updateGeneratedPrompt();
  }
});
