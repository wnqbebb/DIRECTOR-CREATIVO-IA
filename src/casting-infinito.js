import './casting-infinito.css'

document.addEventListener('DOMContentLoaded', () => {
  
  // 1. Terms Bank Database
  const termsDatabase = [
    // General
    { text: "model casting session", category: "general" },
    { text: "consistent character template", category: "general" },
    { text: "brand ambassador identity", category: "general" },
    { text: "raw fashion portrait photography", category: "general" },
    { text: "high fidelity clothing model", category: "general" },
    { text: "editorial fashion model casting", category: "general" },
    { text: "digital avatar reference card", category: "general" },
    { text: "model portfolio photoshoot", category: "general" },
    { text: "consistent facial structure anchor", category: "general" },
    { text: "editorial studio model composition", category: "general" },

    // Realismo
    { text: "visible skin pores", category: "realismo" },
    { text: "natural skin texture imperfections", category: "realismo" },
    { text: "micro asymmetry facial structure", category: "realismo" },
    { text: "subtle skin redness raw", category: "realismo" },
    { text: "fine lines around eyes smile", category: "realismo" },
    { text: "individual hair flyaways frizz sutil", category: "realismo" },
    { text: "no beauty smoothing filter", category: "realismo" },
    { text: "natural cotton clothing wrinkles", category: "realismo" },
    { text: "soft focus background depth", category: "realismo" },
    { text: "photographic grain analog look", category: "realismo" },

    // Femenino
    { text: "petite female fashion model 23 years old", category: "femenino" },
    { text: "abundant shiny jet black natural curls", category: "femenino" },
    { text: "warm small-teeth smile candid", category: "femenino" },
    { text: "slender neck delicate jawline", category: "femenino" },
    { text: "fair light skin tone mestiza", category: "femenino" },
    { text: "elegant woman structured cream blazer", category: "femenino" },
    { text: "curvy female fitted ribbed knit dress", category: "femenino" },
    { text: "young woman messy ponytail street style", category: "femenino" },
    { text: "casual girlfriend bedroom window daylight", category: "femenino" },
    { text: "romantic flowy dress summer sunset", category: "femenino" },

    // Masculino
    { text: "male fashion model Southern European mix", category: "masculino" },
    { text: "short slightly unstyled dark hair", category: "masculino" },
    { text: "irregular beard growth stubble", category: "masculino" },
    { text: "heavyweight cotton hoodie slouched posture", category: "masculino" },
    { text: "premium menswear navy knit polo", category: "masculino" },
    { text: "clean jawline confident neutral gaze", category: "masculino" },
    { text: "young urban street style concrete alley", category: "masculino" },
    { text: "athletic male runner sportswear tracking", category: "masculino" },
    { text: "light olive skin natural redness under-eyes", category: "masculino" },
    { text: "smart casual menswear minimal studio", category: "masculino" },

    // Accesorios
    { text: "close-up delicate hands minimal rings", category: "accesorios" },
    { text: "wrist watch leather bracelet grip", category: "accesorios" },
    { text: "extreme close-up ear silver earring", category: "accesorios" },
    { text: "structured leather handbag holding", category: "accesorios" },
    { text: "candid walk modern cafe bag strap", category: "accesorios" },
    { text: "close-up portrait black optical glasses", category: "accesorios" },
    { text: "softbox reflections lenses clear gaze", category: "accesorios" },
    { text: "hand knuckles skin details texture", category: "accesorios" },
    { text: "manicure natural clean nails jewelry", category: "accesorios" },
    { text: "neck collarbone gold necklace close-up", category: "accesorios" }
  ];

  // Render search terms in Term Bank
  const resultsGrid = document.querySelector('.terms-results');
  const searchInput = document.querySelector('.search-input');
  const filterButtons = document.querySelectorAll('.filter-pill');

  if (resultsGrid) {
    let activeFilter = 'all';
    let searchQuery = '';

    function renderTerms() {
      resultsGrid.innerHTML = '';
      const filtered = termsDatabase.filter(term => {
        const matchesCategory = activeFilter === 'all' || term.category === activeFilter;
        const matchesSearch = term.text.toLowerCase().includes(searchQuery.toLowerCase());
        return matchesCategory && matchesSearch;
      });

      if (filtered.length === 0) {
        resultsGrid.innerHTML = `
          <div style="grid-column: 1/-1; text-align: center; padding: 2.5rem; color: var(--color-purple-light); font-family: var(--font-mono); font-size: 0.9rem;">
            No se encontraron términos. Intenta otra búsqueda.
          </div>
        `;
        return;
      }

      filtered.forEach(term => {
        const card = document.createElement('div');
        card.className = 'term-item-card';
        card.innerHTML = `
          <div>
            <div class="term-category-badge">[ ${term.category} ]</div>
            <div class="term-text">${term.text}</div>
          </div>
          <button class="copy-btn mini-copy" type="button" style="margin-top: 0.8rem; width: fit-content; align-self: flex-end; padding: 0.35rem 0.8rem; font-size: 0.65rem;">
            <svg style="width: 12px; height: 12px; fill: currentColor; margin-right: 0.2rem;" viewBox="0 0 24 24">
              <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
            </svg>
            Copiar
          </button>
        `;

        const btn = card.querySelector('.mini-copy');
        btn.addEventListener('click', (e) => {
          navigator.clipboard.writeText(term.text).then(() => {
            const originalContent = btn.innerHTML;
            btn.innerHTML = `Listo`;
            btn.classList.add('copied');
            spawnSparks(e.clientX, e.clientY);
            setTimeout(() => {
              btn.innerHTML = originalContent;
              btn.classList.remove('copied');
            }, 1500);
          });
        });

        resultsGrid.appendChild(card);
      });
    }

    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value;
        renderTerms();
      });
    }

    filterButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeFilter = btn.getAttribute('data-filter');
        renderTerms();
      });
    });

    renderTerms();
  }

  // 2. Clipboard Copy Functionality with Particle Sparks
  const copyButtons = document.querySelectorAll('.copy-btn:not(.mini-copy)');
  
  copyButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const parent = btn.closest('.prompt-container') || btn.closest('.card-brutal') || btn.closest('.sheet-card') || btn.closest('.angle-viewer') || btn.parentElement;
      const textEl = parent.querySelector('.prompt-text') || parent.querySelector('code') || parent.querySelector('pre') || parent.querySelector('.term-text') || parent.querySelector('.copy-target');
      
      if (textEl) {
        let textToCopy = textEl.innerText || textEl.textContent;
        textToCopy = textToCopy.trim();
        
        navigator.clipboard.writeText(textToCopy).then(() => {
          const originalContent = btn.innerHTML;
          btn.innerHTML = `
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.3rem;" viewBox="0 0 24 24">
              <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
            </svg>
            Copiado
          `;
          btn.classList.add('copied');
          
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

  // Spawn particle sparks function
  function spawnSparks(x, y) {
    const particleCount = 14;
    const shapes = ['circle', 'square', 'cross', 'triangle'];
    for (let i = 0; i < particleCount; i++) {
      const spark = document.createElement('div');
      const shape = shapes[Math.floor(Math.random() * shapes.length)];
      spark.className = `spark-particle spark-${shape}`;
      
      const angle = (i / particleCount) * 2 * Math.PI + (Math.random() * 0.4 - 0.2);
      const velocity = 50 + Math.random() * 85;
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

  // 3. Active Sidebar Links on Scroll (Scrollspy)
  const sections = document.querySelectorAll('section, header');
  const navLinks = document.querySelectorAll('.nav-link');
  
  function updateActiveLink() {
    let scrollPosition = window.scrollY || document.documentElement.scrollTop;
    let currentSectionId = '';
    
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
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
  updateActiveLink(); // Run on load

  // 4. Interactive 6-Layer Model JSON & Prompt Builder
  const layerInputs = document.querySelectorAll('.builder-input');
  const liveBuilderPrompt = document.getElementById('live-builder-prompt');
  const liveBuilderJson = document.getElementById('live-builder-json');

  if (layerInputs.length > 0 && liveBuilderPrompt && liveBuilderJson) {
    function compileBuilderData() {
      // Gather selections
      const gender = document.getElementById('layer-gender').value;
      const age = document.getElementById('layer-age').value;
      const ethnicity = document.getElementById('layer-ethnicity').value;
      const face = document.getElementById('layer-face').value;
      const hair = document.getElementById('layer-hair').value;
      
      const skinRealism = document.getElementById('layer-realism').value;
      const energy = document.getElementById('layer-energy').value;
      const wardrobe = document.getElementById('layer-wardrobe').value;
      const environment = document.getElementById('layer-environment').value;
      const lighting = document.getElementById('layer-lighting').value;
      const camera = document.getElementById('layer-camera').value;

      // Compile Prompt String
      const generatedPrompt = `Universal identity anchor portrait: Stunningly realistic ${age}-year-old ${gender} model of ${ethnicity} ethnicity. Face details: ${face}. Hair: ${hair}. Realism parameters: ${skinRealism}, no beauty smoothing, retain natural skin texture and pores. Outfit: ${wardrobe}. Energy attitude: ${energy}. Environment backdrop: ${environment}. Production details: ${lighting}, shot on ${camera}, extremely sharp focus, editorial realism, aspect ratio 3:4.`;
      
      liveBuilderPrompt.textContent = generatedPrompt;

      // Compile JSON Object
      const jsonObj = {
        "task": "generate_consistent_casting",
        "subject": {
          "type": "human",
          "gender": gender,
          "age_range": age,
          "ethnicity": ethnicity,
          "face_details": face.split(', '),
          "hair": hair,
          "expression_energy": energy
        },
        "realism_constraints": {
          "no_beauty_smoothing": true,
          "retain_imperfections": true,
          "pores_visible": true,
          "special_detail": skinRealism
        },
        "wardrobe": {
          "description": wardrobe,
          "fit": "realistic fabric folds"
        },
        "environment": {
          "scene": environment
        },
        "camera_production": {
          "lighting": lighting,
          "camera_spec": camera,
          "resolution": "8k raw texturing"
        }
      };

      liveBuilderJson.textContent = JSON.stringify(jsonObj, null, 2);
    }

    layerInputs.forEach(input => {
      input.addEventListener('change', compileBuilderData);
      input.addEventListener('input', compileBuilderData);
    });

    compileBuilderData(); // Initial run
  }

  // 5. Andrea Identity Angles Showcase panel
  const angleButtons = document.querySelectorAll('.angle-btn');
  const viewerImg = document.getElementById('viewer-img');
  const viewerPrompt = document.getElementById('viewer-prompt');
  const viewerTitle = document.getElementById('viewer-title');
  const viewerDesc = document.getElementById('viewer-desc');

  // Database of the 11 Andrea/Angie angles prompts and data
  const anglesDatabase = {
    "frontal": {
      title: "1. Retrato Ancla Universal",
      img: "/media/bonus_4/image5.png",
      desc: "Establece la identidad base: rasgos físicos, sonrisa cálida, dientes pequeños, abundante cabello rizado negro brillante, y el fondo lavanda sólido.",
      prompt: "Universal identity anchor portrait, petite and feminine high-fashion. Scene: Stunningly attractive 23-year-old female model of fair, light-skinned Mestiza complexion. She has a petite and very slender, delicate physique with a tender facial structure. She is looking directly at the camera with a beautiful, warm smile showing small, perfectly formed teeth. Her hair is incredibly abundant, shiny jet black, styled in tight, bouncy natural curls (rulitos) and waves that catch the light. Wearing a simple dark charcoal black crewneck t-shirt. Environment: Professional photo studio set with a solid, seamless deep lavender (plum-tone) backdrop. Lighting: Soft, high-end editorial butterfly lighting; a large softbox providing gentle shadows to define her petite structure. Camera: Full-frame photography, 85mm lens, f/1.8, ISO 100, extremely sharp focus on the smile and eyes. Style: Raw photographic realism, 8k, no_beauty_smoothing: true, retain_imperfections: true."
    },
    "close-up": {
      title: "2. Primer Plano Extremo",
      img: "/media/bonus_4/image4.png",
      desc: "Fija el rostro de cerca para auditar imperfecciones, poros de la piel, y evitar que la IA suavice o altere los rasgos característicos.",
      prompt: "Extreme close-up of the 23-year-old petite fair-skinned woman from reference. Focus on her warm smile and small, perfectly aligned teeth. Raw skin texture with visible pores and natural delicate lines. Intense shine on the jet black hair curls framing her face. Deep lavender solid backdrop. 85mm lens, no_beauty_smoothing: true."
    },
    "3-4-profile": {
      title: "3. Perfil Tres Cuartos Derecha",
      img: "/media/bonus_4/image15.png",
      desc: "Evalúa volumen facial, contorno de mejillas, mandíbula y cuello. Clave para comprobar estabilidad tridimensional del rostro.",
      prompt: "3/4 right profile of the reference subject. High-definition focus on the abundant, shiny jet black natural curls (rulitos). Her fair skin shows natural texture and tiny freckles. Solid deep plum-lavender studio background. Large softbox lighting defining her slender facial structure. Raw photographic quality."
    },
    "90-profile": {
      title: "4. Perfil Lateral 90 Grados",
      img: "/media/bonus_4/image6.png",
      desc: "Define la línea pura de la nariz, mandíbula, oreja y nuca. Es el ángulo donde la IA suele desviarse más.",
      prompt: "90-degree left profile. The deep lavender background highlights her very slender neck and petite, delicate jawline. Sharp focus on the individual curls and the ear anatomy matching the reference. Retain all skin imperfections and natural texture. Editorial 8k."
    },
    "high-angle": {
      title: "5. Picado (Ángulo Alto)",
      img: "/media/bonus_4/image11.png",
      desc: "Toma desde arriba. Agrega vulnerabilidad tierna, ideal para catálogos románticos. Enfatiza los rizos y su volumen.",
      prompt: "High-angle shot looking down at the petite model. She is looking up towards the lens with a romantic, innocent expression. Visible forehead pores and natural skin texture. Her black curls spread beautifully around her head. Lavender studio backdrop. 50mm lens feel."
    },
    "low-angle": {
      title: "6. Contrapicado (Ángulo Bajo)",
      img: "/media/bonus_4/image10.png",
      desc: "Toma desde abajo. Brinda autoridad, estatus y presencia segura sin perder la delicadeza física.",
      prompt: "Low-angle shot looking up at the reference subject. Confident yet tender presence. Sharp focus on the delicate structure of her collarbones and thin neck. Deep lavender background with soft purple reflections on her fair skin. Crude realism, 8k."
    },
    "back-view": {
      title: "7. Vista Posterior (Espalda)",
      img: "/media/bonus_4/image3.png",
      desc: "Esencial para mostrar el diseño de prendas por la espalda. Conserva el volumen y rizo del pelo, y nuca.",
      prompt: "Back view of the subject's head and shoulders, turning 45 degrees towards the camera. Sharp focus on the glossy texture of her tight black curls. Fair skin visible on the nape of the neck. Deep lavender studio backdrop. No smoothing, 100% skin realism."
    },
    "hands": {
      title: "8. Plano Medio con Manos",
      img: "/media/bonus_4/image14.png",
      desc: "Fuerza a la IA a renderizar manos coherentes, dedos simétricos y uñas naturales junto al rostro. Ideal para accesorios.",
      prompt: "Medium shot of the petite model with her small hands lightly touching her cheeks. Extreme detail on the knuckles and the delicate skin of her hands matching her face. Deep lavender background. 8k raw quality with subtle photographic grain."
    },
    "laughing": {
      title: "9. Expresión: Sonrisa Abierta",
      img: "/media/bonus_4/image12.png",
      desc: "Prueba la expresividad emocional del avatar. Evita el rostro congelado 'robótico' y conserva arrugas de risa reales.",
      prompt: "Spontaneous shot of the fair-skinned model laughing naturally, showing her small teeth. Authentic human expression with natural lines around the eyes. Lavender background. Raw, imperfect perfection, no filters."
    },
    "waist-up": {
      title: "10. Plano Medio (Cintura Arriba)",
      img: "/media/bonus_4/image7.png",
      desc: "Muestra silueta, hombros y caída de la tela de la prenda. Conector entre el rostro e-commerce y el modelaje de moda.",
      prompt: "Waist-up shot of the petite and slender model standing with grace. Wearing the dark charcoal t-shirt. Realistic fabric folds and skin details on her thin arms. Solid deep lavender studio backdrop. Cinematic lighting, 8k resolution."
    },
    "contact-sheet": {
      title: "11. Contact Sheet (Hoja de Auditoría)",
      img: "/media/bonus_4/image16.png",
      desc: "Permite auditar la consistencia facial en una sola cuadrícula de 3x3 para validar si el personaje se mantiene idéntico.",
      prompt: "A 3x3 contact sheet grid of the same petite, fair-skinned model with black rulos from reference. Nine different angles including frontal, profile, and extreme close-ups. Identical identity and small teeth in every panel. Solid deep lavender studio background for all images. Crude, raw textures throughout."
    }
  };

  if (angleButtons.length > 0 && viewerImg && viewerPrompt && viewerTitle && viewerDesc) {
    angleButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        angleButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        const target = btn.getAttribute('data-target');
        const data = anglesDatabase[target];
        
        if (data) {
          viewerImg.src = data.img;
          viewerTitle.textContent = data.title;
          viewerDesc.textContent = data.desc;
          viewerPrompt.textContent = data.prompt;
        }
      });
    });
  }

  // 6. Interactive Character Dossier Custom Builder
  const presetSelector = document.getElementById('dossier-preset');
  const inputsDossier = document.querySelectorAll('.preset-input');
  
  const presetsCharacter = {
    angie: {
      name: "Angie Nicol",
      age: "27 años",
      origin: "Bogotá, Colombia",
      role: "Atracción de Audiencia",
      essence: "Mujer subestimada por su belleza serena que convirtió esa lectura en inteligencia competitiva.",
      thesis: "Si te ven como un adorno, usa su error como ventaja táctica.",
      contradiction: "Calidez luminosa externa con ambición selectiva y competitiva interna.",
      quote: "No vine a decorar marcas. Vine a volverlas memorables.",
      portrait: "/media/bonus_4/image5.png"
    }
  };

  if (presetSelector) {
    presetSelector.addEventListener('change', () => {
      const selected = presetSelector.value;
      const data = presetsCharacter[selected];
      
      if (data) {
        // Update inputs
        document.getElementById('dos-input-name').value = data.name;
        document.getElementById('dos-input-age').value = data.age;
        document.getElementById('dos-input-origin').value = data.origin;
        document.getElementById('dos-input-role').value = data.role;
        document.getElementById('dos-input-essence').value = data.essence;
        document.getElementById('dos-input-thesis').value = data.thesis;
        document.getElementById('dos-input-contradiction').value = data.contradiction;
        document.getElementById('dos-input-quote').value = data.quote;
        
        // Update outputs
        updateDossierOutputs();
      }
    });

    function updateDossierOutputs() {
      const name = document.getElementById('dos-input-name').value;
      const age = document.getElementById('dos-input-age').value;
      const origin = document.getElementById('dos-input-origin').value;
      const role = document.getElementById('dos-input-role').value;
      
      const essence = document.getElementById('dos-input-essence').value;
      const thesis = document.getElementById('dos-input-thesis').value;
      const contradiction = document.getElementById('dos-input-contradiction').value;
      const quote = document.getElementById('dos-input-quote').value;

      // Update visible dossier elements
      document.getElementById('dos-out-name').textContent = name;
      document.getElementById('dos-out-role').textContent = role;
      document.getElementById('dos-card-age').textContent = age;
      document.getElementById('dos-card-origin').textContent = origin;
      document.getElementById('dos-card-role').textContent = role;
      
      document.getElementById('dos-out-essence').textContent = essence;
      document.getElementById('dos-out-thesis').textContent = thesis;
      document.getElementById('dos-out-contradiction').textContent = contradiction;
      document.getElementById('dos-out-quote').textContent = `"${quote}"`;

      // Match portrait image dynamically based on name
      const portraitImg = document.getElementById('dos-portrait');
      if (name.toLowerCase().includes('mateo')) {
        portraitImg.src = presetsCharacter.mateo.portrait;
      } else if (name.toLowerCase().includes('elena')) {
        portraitImg.src = presetsCharacter.elena.portrait;
      } else {
        portraitImg.src = presetsCharacter.angie.portrait;
      }

      // Compile generated text block
      const generatedDossierText = `FICHA DE EMBAJADOR IA DE MARCA\n\nNombre: ${name}\nEdad Aparente: ${age}\nOrigen: ${origin}\nRol Comercial: ${role}\n\nEsencia Narrativa: ${essence}\nTesis del Personaje: ${thesis}\nContradicción Interna: ${contradiction}\nFrase Típica: "${quote}"`;
      document.getElementById('dossier-output-text').textContent = generatedDossierText;
    }

    inputsDossier.forEach(inp => {
      inp.addEventListener('input', updateDossierOutputs);
    });

    updateDossierOutputs(); // Initialize
  }

  // 7. Interactive Deliverables checklist and progress tracker
  const checklistItems = document.querySelectorAll('.checklist-task-item');
  const progressBar = document.getElementById('checklist-progress-bar');
  const progressPct = document.getElementById('checklist-progress-pct');

  if (checklistItems.length > 0 && progressBar && progressPct) {
    function calculateProgress() {
      const checkedItems = document.querySelectorAll('.checklist-task-item.checked');
      const percentage = Math.round((checkedItems.length / checklistItems.length) * 100);
      
      progressBar.style.width = `${percentage}%`;
      progressPct.textContent = `${percentage}%`;
    }

    checklistItems.forEach(item => {
      item.addEventListener('click', () => {
        item.classList.toggle('checked');
        calculateProgress();
      });
    });

    calculateProgress(); // Initialize
  }

  // 8. Polaroid Image Lightbox Modal
  const lightbox = document.querySelector('.brutal-lightbox');
  
  if (lightbox) {
    const lightboxImg = lightbox.querySelector('.lightbox-img');
    const lightboxCaption = lightbox.querySelector('.lightbox-caption');
    const lightboxClose = lightbox.querySelector('.lightbox-close');

    // Attach zoom trigger to polaroids and gallery grids
    const triggerImages = document.querySelectorAll('.polaroid-img-wrapper img, .gallery-img-frame img, .viewer-media-frame img');

    triggerImages.forEach(img => {
      img.style.cursor = 'zoom-in';
      img.addEventListener('click', () => {
        const parentPolaroid = img.closest('.polaroid-item') || img.closest('.gallery-item');
        const captionText = parentPolaroid ? (parentPolaroid.querySelector('.polaroid-caption') || parentPolaroid.querySelector('.gallery-label')).textContent : 'Visualización de Casting';
        
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
  }

  // 9. Mobile Sidebar Navigation Slider toggle
  const sidebar = document.querySelector('.sidebar');
  const toggleBtn = document.querySelector('.mobile-nav-toggle');

  if (sidebar && toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      sidebar.classList.toggle('active');
      if (sidebar.classList.contains('active')) {
        toggleBtn.innerHTML = `&times;`;
        toggleBtn.style.fontSize = '2rem';
      } else {
        toggleBtn.innerHTML = `
          <svg style="width: 24px; height: 24px; fill: currentColor;" viewBox="0 0 24 24">
            <path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/>
          </svg>
        `;
        toggleBtn.style.fontSize = '';
      }
    });

    // Close sidebar on link click in mobile
    const menuLinks = document.querySelectorAll('.nav-link');
    menuLinks.forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 1100) {
          sidebar.classList.remove('active');
          toggleBtn.innerHTML = `
            <svg style="width: 24px; height: 24px; fill: currentColor;" viewBox="0 0 24 24">
              <path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/>
            </svg>
          `;
          toggleBtn.style.fontSize = '';
        }
      });
    });
  }

  // 10. Dynamic Reveal Animation for Scrolling
  const selectorsToAnimate = [
    '.section-title',
    '.card-brutal',
    '.card-brutal-dark',
    '.compare-grid',
    '.polaroid-item',
    '.sheet-card',
    '.prompt-container',
    '.prompt-builder',
    '.dossier-grid',
    '.term-bank',
    '.progress-container',
    '.angles-showcase-container'
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
