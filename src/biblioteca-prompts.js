import './biblioteca-prompts.css'

document.addEventListener('DOMContentLoaded', () => {
  // 1. Tab Switching Logic
  const tabContainers = document.querySelectorAll('.tab-container');
  
  tabContainers.forEach(container => {
    const tabButtons = container.querySelectorAll('.tab-btn');
    const tabPanes = container.querySelectorAll('.tab-pane');
    
    tabButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-target');
        
        tabButtons.forEach(b => b.classList.remove('active'));
        tabPanes.forEach(p => p.classList.remove('active'));
        
        btn.classList.add('active');
        const targetPane = container.querySelector(`#${targetId}`);
        if (targetPane) {
          targetPane.classList.add('active');
        }
      });
    });
  });

  // 2. Clipboard Copy Functionality with Cobalt Neon Sparks
  const copyButtons = document.querySelectorAll('.copy-btn');
  
  copyButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const container = btn.closest('.prompt-container') || btn.closest('.card-brutal') || btn.closest('.library-card') || btn.parentElement;
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
          
          // Spawn neon blue particle sparks at click coordinates
          spawnBlueSparks(e.clientX, e.clientY);
          
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

  function spawnBlueSparks(x, y) {
    const particleCount = 15;
    const shapes = ['circle', 'square', 'cross', 'triangle'];
    
    for (let i = 0; i < particleCount; i++) {
      const spark = document.createElement('div');
      const shape = shapes[Math.floor(Math.random() * shapes.length)];
      spark.className = `spark-particle spark-${shape}`;
      
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

  // 4. Live Customizer Playground
  const configInputs = document.querySelectorAll('.builder-input');
  const livePromptOut = document.getElementById('live-builder-prompt');
  const liveJsonOut = document.getElementById('live-builder-json');
  
  const categoryTemplates = {
    clean_product: {
      text: "Clean ecommerce product photography of [GARMENT], [SILHOUETTE], [POSE] on a [BACKGROUND], visible fabric texture, natural folds, [LIGHTING], centered composition, premium online store aesthetic, high resolution, no model, no fake logos, no wrinkles, no shadows too harsh, no distorted garment.",
      json: {
        "image_type": "ecommerce product photography",
        "subject": "product lay flat",
        "garment": "[GARMENT]",
        "silhouette": "[SILHOUETTE]",
        "pose": "[POSE]",
        "location": "[BACKGROUND]",
        "lighting": "[LIGHTING]",
        "composition": "centered, product focus",
        "aesthetic": "premium ecommerce online store",
        "negative_prompt": "deformed hands, fake logos, distorted clothing, wrinkles, harsh shadows"
      }
    },
    quiet_luxury: {
      text: "Luxury product campaign image of [GARMENT], [SILHOUETTE] placed on a [BACKGROUND], quiet luxury aesthetic, [LIGHTING], refined shadows, elegant fabric texture, minimal composition, [COLOR] palette, high-end fashion catalog style, no text, no logo, no messy background, no harsh contrast.",
      json: {
        "image_type": "luxury editorial campaign",
        "subject": "product layout",
        "garment": "[GARMENT]",
        "silhouette": "[SILHOUETTE]",
        "location": "[BACKGROUND]",
        "lighting": "[LIGHTING]",
        "composition": "minimal, quiet luxury",
        "color_palette": "[COLOR]",
        "aesthetic": "quiet luxury, high-end catalog",
        "negative_prompt": "deformed hands, fake logos, text on image, messy background, high contrast"
      }
    },
    editorial_female: {
      text: "High-fashion editorial campaign of a [MODEL] wearing [GARMENT], [SILHOUETTE], [POSE], minimal [BACKGROUND], [LIGHTING], full body shot, modern luxury fashion aesthetic, sophisticated attitude, vertical 4:5, no deformed hands, no fake logos, no distorted clothing, no plastic skin.",
      json: {
        "image_type": "high-fashion editorial",
        "subject": "[MODEL]",
        "garment": "[GARMENT]",
        "silhouette": "[SILHOUETTE]",
        "pose": "[POSE]",
        "location": "[BACKGROUND]",
        "lighting": "[LIGHTING]",
        "camera": "full body shot, 85mm lens",
        "mood": "sophisticated, modern luxury",
        "format": "vertical 4:5",
        "negative_prompt": "deformed hands, fake logos, distorted garments, plastic skin, bad anatomy"
      }
    },
    streetwear: {
      text: "Urban streetwear fashion campaign featuring a [MODEL] wearing [GARMENT], [SILHOUETTE], [POSE], clean [BACKGROUND], afternoon [LIGHTING], strong shadows, cinematic street style, low angle full body shot, edgy commercial look for Instagram drop, vertical 4:5, no graffiti text, no fake logos, no deformed hands, no messy outfit.",
      json: {
        "image_type": "urban streetwear campaign",
        "subject": "[MODEL]",
        "garment": "[GARMENT]",
        "silhouette": "[SILHOUETTE]",
        "pose": "[POSE]",
        "location": "[BACKGROUND]",
        "lighting": "[LIGHTING], afternoon hard light",
        "camera": "low angle, full body",
        "mood": "edgy, rebellious, drop launch",
        "format": "vertical 4:5",
        "negative_prompt": "deformed hands, fake logos, graffiti text, low resolution, messy outfit"
      }
    }
  };

  if (configInputs.length > 0) {
    function updatePlayground() {
      const templateKey = document.getElementById('layer-category').value;
      const garment = document.getElementById('layer-garment').value || "beige linen wide-leg pants";
      const silhouette = document.getElementById('layer-silhouette').value || "fluid elegant silhouette";
      const model = document.getElementById('layer-model').value || "female model";
      const background = document.getElementById('layer-background').value || "clean white cyclorama studio background";
      const lighting = document.getElementById('layer-lighting').value || "soft diffused luxury studio light";
      const pose = document.getElementById('layer-pose').value || "relaxed standing pose";
      const color = document.getElementById('layer-color').value || "neutral beige and ivory";
      
      const template = categoryTemplates[templateKey] || categoryTemplates.editorial_female;
      
      let textPrompt = template.text;
      textPrompt = textPrompt.replace('[GARMENT]', garment);
      textPrompt = textPrompt.replace('[SILHOUETTE]', silhouette);
      textPrompt = textPrompt.replace('[MODEL]', model);
      textPrompt = textPrompt.replace('[BACKGROUND]', background);
      textPrompt = textPrompt.replace('[LIGHTING]', lighting);
      textPrompt = textPrompt.replace('[POSE]', pose);
      textPrompt = textPrompt.replace('[COLOR]', color);
      
      let jsonVal = JSON.stringify(template.json, null, 2);
      jsonVal = jsonVal.replace('[GARMENT]', garment);
      jsonVal = jsonVal.replace('[SILHOUETTE]', silhouette);
      jsonVal = jsonVal.replace('[MODEL]', model);
      jsonVal = jsonVal.replace('[BACKGROUND]', background);
      jsonVal = jsonVal.replace('[LIGHTING]', lighting);
      jsonVal = jsonVal.replace('[POSE]', pose);
      jsonVal = jsonVal.replace('[COLOR]', color);
      
      if (livePromptOut) livePromptOut.textContent = textPrompt;
      if (liveJsonOut) liveJsonOut.textContent = jsonVal;
    }
    
    configInputs.forEach(input => {
      input.addEventListener('input', updatePlayground);
    });
    
    // Run once on load
    updatePlayground();
  }

  // 5. Scroll Animation Reveal
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

  // 6. Accordion Toggle Logic
  const accordionTriggers = document.querySelectorAll('.accordion-trigger');
  accordionTriggers.forEach(trigger => {
    trigger.addEventListener('click', () => {
      const item = trigger.closest('.accordion-item');
      const content = item.querySelector('.accordion-content');
      const isOpen = item.classList.contains('active');
      
      // Close all other accordions for neat presentation
      document.querySelectorAll('.accordion-item.active').forEach(activeItem => {
        if (activeItem !== item) {
          activeItem.classList.remove('active');
          activeItem.querySelector('.accordion-content').style.maxHeight = null;
        }
      });
      
      if (isOpen) {
        item.classList.remove('active');
        content.style.maxHeight = null;
      } else {
        item.classList.add('active');
        content.style.maxHeight = (content.scrollHeight + 100) + 'px'; // +100 to account for child margins/paddings
      }
    });
  });
});


