import './lanzamientos-editoriales.css'

document.addEventListener('DOMContentLoaded', () => {
  // 1. Tab Switching Logic for Mundos & Extra Campaigns
  const tabContainers = document.querySelectorAll('.tab-container');
  
  tabContainers.forEach(container => {
    const tabButtons = container.querySelectorAll('.tab-btn');
    const tabPanes = container.querySelectorAll('.tab-pane');
    
    tabButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-target');
        
        // Deactivate all buttons in this container
        tabButtons.forEach(b => b.classList.remove('active'));
        // Hide all panes in this container
        tabPanes.forEach(p => p.classList.remove('active'));
        
        // Activate clicked button and target pane
        btn.classList.add('active');
        const targetPane = container.querySelector(`#${targetId}`);
        if (targetPane) {
          targetPane.classList.add('active');
        }
      });
    });
  });

  // 2. Clipboard Copy Functionality with Fuchsia Sparks
  const copyButtons = document.querySelectorAll('.copy-btn');
  
  copyButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const container = btn.closest('.prompt-container') || btn.closest('.card-brutal') || btn.closest('.card-brutal-neon') || btn.parentElement;
      const targetTextEl = container.querySelector('.prompt-text') || container.querySelector('code') || container.querySelector('pre') || container.querySelector('.copy-target');
      
      if (targetTextEl) {
        const textToCopy = (targetTextEl.innerText || targetTextEl.textContent).trim();
        
        navigator.clipboard.writeText(textToCopy).then(() => {
          const originalContent = btn.innerHTML;
          btn.innerHTML = `
            <svg style="width: 14px; height: 14px; fill: currentColor;" viewBox="0 0 24 24">
              <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
            </svg>
            Copiado!
          `;
          btn.classList.add('copied');
          
          // Spawn neon fuchsia particle sparks
          spawnFuchsiaSparks(e.clientX, e.clientY);
          
          setTimeout(() => {
            btn.innerHTML = originalContent;
            btn.classList.remove('copied');
          }, 2000);
        }).catch(err => {
          console.error('Failed to copy text: ', err);
        });
      }
    });
  });

  // Particle Spark Spawning Function
  function spawnFuchsiaSparks(x, y) {
    const particleCount = 15;
    const shapes = ['circle', 'square', 'cross', 'triangle'];
    
    for (let i = 0; i < particleCount; i++) {
      const spark = document.createElement('div');
      const shape = shapes[Math.floor(Math.random() * shapes.length)];
      spark.className = `spark-particle spark-${shape}`;
      
      // Random directions, sizes, and rotations
      const angle = (i / particleCount) * 2 * Math.PI + (Math.random() * 0.4 - 0.2);
      const velocity = 50 + Math.random() * 80;
      const tx = Math.cos(angle) * velocity;
      const ty = Math.sin(angle) * velocity;
      const size = 6 + Math.random() * 8;
      const rot = Math.random() * 360;
      
      spark.style.width = `${size}px`;
      spark.style.height = `${size}px`;
      spark.style.left = `${x + window.scrollX - size/2}px`;
      spark.style.top = `${y + window.scrollY - size/2}px`;
      
      spark.style.setProperty('--tx', `${tx}px`);
      spark.style.setProperty('--ty', `${ty}px`);
      spark.style.setProperty('--rot', `${rot}deg`);
      
      document.body.appendChild(spark);
      
      // Clean up after animation finishes
      setTimeout(() => {
        spark.remove();
      }, 750);
    }
  }

  // 3. Scrollspy active link highlight
  const sections = document.querySelectorAll('section, header');
  const navLinks = document.querySelectorAll('.nav-link');
  
  function updateActiveLink() {
    let scrollPosition = window.scrollY || document.documentElement.scrollTop;
    let currentSectionId = '';
    
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      
      // If scroll is near section top, mark as active
      if (scrollPosition >= (sectionTop - 220)) {
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

  // 4. Live Prompt Compiler / Customizer
  const compilerInputs = document.querySelectorAll('.builder-input');
  const livePromptCode = document.getElementById('live-builder-prompt');
  const liveJsonCode = document.getElementById('live-builder-json');
  
  if (compilerInputs.length > 0) {
    function updateLivePrompt() {
      const gender = document.getElementById('layer-gender').value;
      const age = document.getElementById('layer-age').value;
      const ethnicity = document.getElementById('layer-ethnicity').value;
      const face = document.getElementById('layer-face').value;
      const hair = document.getElementById('layer-hair').value;
      const realism = document.getElementById('layer-realism').value;
      const energy = document.getElementById('layer-energy').value;
      const wardrobe = document.getElementById('layer-wardrobe').value;
      const environment = document.getElementById('layer-environment').value;
      const lighting = document.getElementById('layer-lighting').value;
      const camera = document.getElementById('layer-camera').value;
      
      const compiledPrompt = `Same ${gender} editorial fashion model from references, visual age ${age}, ${ethnicity} ethnicity, face features with ${face}, hair styled in ${hair}, showing ${energy} expression. Wearing ${wardrobe}, realistic fabric texture, natural wrinkles. Environment set in ${environment}. Shot under ${lighting}. Cinematic details: ${camera}, sharp focus, visible skin details, ${realism}, high-end fashion campaign styling, no generated text, no watermark, no illustration, no CGI.`;
      
      const compiledJson = `{
  "model_identity": {
    "gender": "${gender}",
    "age": "${age}",
    "ethnicity": "${ethnicity}",
    "facial_details": "${face}",
    "hair_style": "${hair}"
  },
  "aesthetic": {
    "energy": "${energy}",
    "realism_constraints": "${realism}"
  },
  "styling": {
    "wardrobe": "${wardrobe}"
  },
  "production": {
    "environment": "${environment}",
    "lighting": "${lighting}",
    "camera_settings": "${camera}"
  }
}`;
      
      if (livePromptCode) livePromptCode.textContent = compiledPrompt;
      if (liveJsonCode) liveJsonCode.textContent = compiledJson;
    }
    
    compilerInputs.forEach(input => {
      input.addEventListener('input', updateLivePrompt);
    });
    
    // Run compiler once
    updateLivePrompt();
  }

  // 5. Interactive Dossier Switcher (Angie Nicol vs Model 2)
  const dossierNameInput = document.getElementById('dos-input-name');
  if (dossierNameInput) {
    const inputs = {
      name: document.getElementById('dos-input-name'),
      age: document.getElementById('dos-input-age'),
      origin: document.getElementById('dos-input-origin'),
      role: document.getElementById('dos-input-role'),
      essence: document.getElementById('dos-input-essence'),
      thesis: document.getElementById('dos-input-thesis'),
      contradiction: document.getElementById('dos-input-contradiction'),
      quote: document.getElementById('dos-input-quote')
    };

    const outputs = {
      name: document.getElementById('dos-out-name'),
      role: document.getElementById('dos-out-role'),
      cardAge: document.getElementById('dos-card-age'),
      cardOrigin: document.getElementById('dos-card-origin'),
      cardRole: document.getElementById('dos-card-role'),
      essence: document.getElementById('dos-out-essence'),
      thesis: document.getElementById('dos-out-thesis'),
      contradiction: document.getElementById('dos-out-contradiction'),
      quote: document.getElementById('dos-out-quote'),
      jsonBlock: document.getElementById('dossier-output-text')
    };

    function updateDossierCard() {
      const name = inputs.name.value;
      const age = inputs.age.value;
      const origin = inputs.origin.value;
      const role = inputs.role.value;
      const essence = inputs.essence.value;
      const thesis = inputs.thesis.value;
      const contradiction = inputs.contradiction.value;
      const quote = inputs.quote.value;

      if (outputs.name) outputs.name.textContent = name;
      if (outputs.role) outputs.role.textContent = role;
      if (outputs.cardAge) outputs.cardAge.textContent = age;
      if (outputs.cardOrigin) outputs.cardOrigin.textContent = origin;
      if (outputs.cardRole) outputs.cardRole.textContent = role;
      if (outputs.essence) outputs.essence.textContent = essence;
      if (outputs.thesis) outputs.thesis.textContent = thesis;
      if (outputs.contradiction) outputs.contradiction.textContent = contradiction;
      if (outputs.quote) outputs.quote.textContent = `"${quote}"`;

      const jsonStr = `Model Profile [${name}]:
- Role: ${role}
- Age: ${age}
- Origin: ${origin}
- Essence: ${essence}
- Thesis: ${thesis}
- Contradiction: ${contradiction}
- Key Quote: "${quote}"`;

      if (outputs.jsonBlock) outputs.jsonBlock.textContent = jsonStr;
    }

    Object.values(inputs).forEach(input => {
      if (input) input.addEventListener('input', updateDossierCard);
    });

    // Run dossier once on load
    updateDossierCard();
  }

  // 6. Lightbox Zoom Modal Logic
  const lightbox = document.querySelector('.brutal-lightbox');
  
  if (lightbox) {
    const lightboxImg = lightbox.querySelector('.lightbox-img');
    const lightboxCaption = lightbox.querySelector('.lightbox-caption');
    const lightboxClose = lightbox.querySelector('.lightbox-close');
    const zoomableImages = document.querySelectorAll('.showcase-item img, .dossier-portrait-wrapper img');

    zoomableImages.forEach(img => {
      img.addEventListener('click', () => {
        lightboxImg.src = img.src;
        // Determine caption
        const itemParent = img.closest('.showcase-item') || img.closest('.dossier-portrait-card') || img.closest('.hero-section') || img.parentElement;
        const captionText = itemParent.querySelector('.showcase-caption') || itemParent.querySelector('.dossier-role') || itemParent.querySelector('.filename') || { textContent: 'Detalle de Lanzamiento' };
        
        lightboxCaption.textContent = captionText.textContent || 'Detalle de Lanzamiento';
        lightbox.classList.add('active');
      });
    });

    // Close on click outside or close button
    lightbox.addEventListener('click', (e) => {
      if (e.target !== lightboxImg && e.target !== lightboxCaption) {
        lightbox.classList.remove('active');
      }
    });
  }

  // 7. Scroll Animation Reveal Observer
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
      rootMargin: '0px 0px -40px 0px'
    });
    
    revealElements.forEach(el => {
      observer.observe(el);
    });
  } else {
    revealElements.forEach(el => {
      el.classList.add('visible');
    });
  }
});
