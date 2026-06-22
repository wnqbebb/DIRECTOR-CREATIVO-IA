import './radar.css'

document.addEventListener('DOMContentLoaded', () => {
  // 1. Terms Bank Database
  const termsDatabase = [
    // General
    { text: "fashion campaign editorial", category: "general" },
    { text: "fashion editorial photography", category: "general" },
    { text: "clothing brand campaign", category: "general" },
    { text: "fashion lookbook campaign", category: "general" },
    { text: "modern fashion campaign", category: "general" },
    { text: "premium fashion campaign", category: "general" },
    { text: "minimal fashion campaign", category: "general" },
    { text: "urban fashion campaign", category: "general" },
    { text: "studio fashion editorial", category: "general" },
    { text: "street fashion editorial", category: "general" },
    { text: "luxury fashion campaign", category: "general" },
    { text: "fashion brand photoshoot editorial", category: "general" },
    { text: "clothing photography", category: "general" },
    { text: "fashion campaign inspiration", category: "general" },
    { text: "fashion advertising campaign", category: "general" },
    { text: "fashion campaign poses", category: "general" },
    { text: "fashion campaign composition", category: "general" },
    { text: "fashion campaign moodboard", category: "general" },
    { text: "fashion campaign color palette", category: "general" },
    { text: "fashion brand visual identity", category: "general" },
    { text: "fashion photoshoot concept", category: "general" },
    { text: "fashion photography campaign ideas", category: "general" },
    { text: "high fashion campaign photography", category: "general" },
    { text: "clean fashion campaign", category: "general" },
    { text: "modern clothing brand photoshoot", category: "general" },
    { text: "fashion campaign with negative space", category: "general" },
    { text: "fashion campaign studio lighting", category: "general" },
    { text: "fashion campaign natural light", category: "general" },
    { text: "fashion lookbook poses", category: "general" },
    { text: "fashion product campaign", category: "general" },
    { text: "brand campaign fashion editorial", category: "general" },

    // Streetwear
    { text: "streetwear campaign", category: "streetwear" },
    { text: "streetwear editorial photoshoot", category: "streetwear" },
    { text: "streetwear lookbook", category: "streetwear" },
    { text: "urban streetwear campaign", category: "streetwear" },
    { text: "oversized hoodie campaign", category: "streetwear" },
    { text: "streetwear fashion photography", category: "streetwear" },
    { text: "streetwear model poses", category: "streetwear" },
    { text: "streetwear brand photoshoot", category: "streetwear" },
    { text: "streetwear campaign ideas", category: "streetwear" },
    { text: "streetwear editorial campaign", category: "streetwear" },
    { text: "streetwear fashion moodboard", category: "streetwear" },
    { text: "urban clothing brand campaign", category: "streetwear" },
    { text: "streetwear hoodie photoshoot", category: "streetwear" },
    { text: "streetwear denim campaign", category: "streetwear" },
    { text: "streetwear studio campaign", category: "streetwear" },
    { text: "streetwear concrete background", category: "streetwear" },
    { text: "streetwear night photoshoot", category: "streetwear" },
    { text: "streetwear city campaign", category: "streetwear" },
    { text: "streetwear fashion editorial male", category: "streetwear" },
    { text: "streetwear fashion editorial female", category: "streetwear" },
    { text: "streetwear oversized t shirt campaign", category: "streetwear" },
    { text: "streetwear brand visual identity", category: "streetwear" },
    { text: "streetwear ad campaign", category: "streetwear" },
    { text: "streetwear lookbook photography", category: "streetwear" },
    { text: "streetwear campaign composition", category: "streetwear" },
    { text: "streetwear fashion campaign poses", category: "streetwear" },
    { text: "streetwear urban background", category: "streetwear" },
    { text: "streetwear grunge editorial", category: "streetwear" },
    { text: "streetwear luxury campaign", category: "streetwear" },
    { text: "premium streetwear campaign", category: "streetwear" },

    // Hoodies
    { text: "oversized hoodie campaign", category: "hoodies" },
    { text: "hoodie fashion editorial", category: "hoodies" },
    { text: "hoodie streetwear photoshoot", category: "hoodies" },
    { text: "hoodie lookbook", category: "hoodies" },
    { text: "hoodie brand campaign", category: "hoodies" },
    { text: "hoodie model poses", category: "hoodies" },
    { text: "hoodie urban photoshoot", category: "hoodies" },
    { text: "premium hoodie campaign", category: "hoodies" },
    { text: "minimal hoodie campaign", category: "hoodies" },
    { text: "hoodie studio photography", category: "hoodies" },
    { text: "hoodie lifestyle campaign", category: "hoodies" },
    { text: "hoodie streetwear editorial", category: "hoodies" },
    { text: "hoodie fashion campaign male", category: "hoodies" },
    { text: "hoodie fashion campaign female", category: "hoodies" },
    { text: "hoodie concrete background photoshoot", category: "hoodies" },
    { text: "hoodie winter campaign", category: "hoodies" },
    { text: "hoodie fall fashion editorial", category: "hoodies" },
    { text: "hoodie oversized outfit photoshoot", category: "hoodies" },
    { text: "hoodie campaign photography", category: "hoodies" },
    { text: "hoodie fashion moodboard", category: "hoodies" },

    // Camisetas
    { text: "t shirt fashion campaign", category: "t-shirts" },
    { text: "oversized t shirt editorial", category: "t-shirts" },
    { text: "minimal t shirt campaign", category: "t-shirts" },
    { text: "premium t shirt photoshoot", category: "t-shirts" },
    { text: "basic t shirt fashion editorial", category: "t-shirts" },
    { text: "t shirt lookbook photography", category: "t-shirts" },
    { text: "t shirt brand campaign", category: "t-shirts" },
    { text: "t shirt studio photoshoot", category: "t-shirts" },
    { text: "white t shirt fashion campaign", category: "t-shirts" },
    { text: "graphic t shirt streetwear campaign", category: "t-shirts" },
    { text: "t shirt model poses", category: "t-shirts" },
    { text: "t shirt lifestyle photography", category: "t-shirts" },
    { text: "t shirt editorial campaign", category: "t-shirts" },
    { text: "t shirt fashion ads", category: "t-shirts" },
    { text: "t shirt product photography model", category: "t-shirts" },
    { text: "clean t shirt photoshoot", category: "t-shirts" },
    { text: "t shirt campaign inspiration", category: "t-shirts" },
    { text: "oversized tee campaign", category: "t-shirts" },
    { text: "t shirt streetwear photoshoot", category: "t-shirts" },
    { text: "fashion basics campaign", category: "t-shirts" },

    // Premium Masculino
    { text: "men polo fashion campaign", category: "premium-men" },
    { text: "knit polo editorial photoshoot", category: "premium-men" },
    { text: "old money fashion campaign men", category: "premium-men" },
    { text: "quiet luxury menswear campaign", category: "premium-men" },
    { text: "premium menswear campaign", category: "premium-men" },
    { text: "men fashion editorial polo", category: "premium-men" },
    { text: "men linen shirt campaign", category: "premium-men" },
    { text: "men shirt fashion photoshoot", category: "premium-men" },
    { text: "classic menswear editorial", category: "premium-men" },
    { text: "men summer fashion campaign", category: "premium-men" },
    { text: "men resort wear campaign", category: "premium-men" },
    { text: "luxury casual menswear", category: "premium-men" },
    { text: "men smart casual campaign", category: "premium-men" },
    { text: "men fashion lookbook", category: "premium-men" },
    { text: "premium men polo shirt photoshoot", category: "premium-men" },
    { text: "men fashion campaign neutral colors", category: "premium-men" },
    { text: "old money menswear photoshoot", category: "premium-men" },
    { text: "men fashion campaign natural light", category: "premium-men" },
    { text: "men editorial fashion photography", category: "premium-men" },
    { text: "premium basics menswear campaign", category: "premium-men" },

    // Denim
    { text: "denim fashion campaign", category: "denim" },
    { text: "denim editorial photoshoot", category: "denim" },
    { text: "jeans fashion campaign", category: "denim" },
    { text: "denim lookbook", category: "denim" },
    { text: "denim brand campaign", category: "denim" },
    { text: "denim streetwear editorial", category: "denim" },
    { text: "denim studio photoshoot", category: "denim" },
    { text: "denim lifestyle campaign", category: "denim" },
    { text: "denim on denim editorial", category: "denim" },
    { text: "jeans model poses", category: "denim" },
    { text: "premium denim campaign", category: "denim" },
    { text: "urban denim photoshoot", category: "denim" },
    { text: "denim fashion photography", category: "denim" },
    { text: "denim campaign inspiration", category: "denim" },
    { text: "blue denim editorial", category: "denim" },
    { text: "denim jacket campaign", category: "denim" },
    { text: "denim brand lookbook", category: "denim" },
    { text: "denim fashion ads", category: "denim" },
    { text: "denim editorial male", category: "denim" },
    { text: "denim editorial female", category: "denim" },

    // Vestidos / Femenino
    { text: "dress fashion campaign", category: "dress-female" },
    { text: "summer dress editorial", category: "dress-female" },
    { text: "dress lookbook photography", category: "dress-female" },
    { text: "feminine fashion campaign", category: "dress-female" },
    { text: "romantic dress photoshoot", category: "dress-female" },
    { text: "dress editorial campaign", category: "dress-female" },
    { text: "dress campaign natural light", category: "dress-female" },
    { text: "dress fashion photography", category: "dress-female" },
    { text: "premium dress campaign", category: "dress-female" },
    { text: "dress brand photoshoot", category: "dress-female" },
    { text: "dress model poses", category: "dress-female" },
    { text: "dress campaign inspiration", category: "dress-female" },
    { text: "flowy dress editorial", category: "dress-female" },
    { text: "elegant dress campaign", category: "dress-female" },
    { text: "minimal dress campaign", category: "dress-female" },
    { text: "resort dress campaign", category: "dress-female" },
    { text: "beach dress photoshoot", category: "dress-female" },
    { text: "dress fashion moodboard", category: "dress-female" },
    { text: "women dress campaign", category: "dress-female" },
    { text: "luxury dress editorial", category: "dress-female" },
    { text: "women fashion campaign", category: "dress-female" },
    { text: "feminine fashion editorial", category: "dress-female" },
    { text: "women clothing brand photoshoot", category: "dress-female" },
    { text: "soft feminine fashion campaign", category: "dress-female" },
    { text: "women casual fashion editorial", category: "dress-female" },
    { text: "women fashion lookbook", category: "dress-female" },
    { text: "women fashion campaign poses", category: "dress-female" },
    { text: "women lifestyle fashion photography", category: "dress-female" },
    { text: "premium women fashion campaign", category: "dress-female" },
    { text: "minimal women fashion campaign", category: "dress-female" },

    // Activewear
    { text: "activewear campaign", category: "activewear" },
    { text: "activewear editorial photoshoot", category: "activewear" },
    { text: "fitness fashion campaign", category: "activewear" },
    { text: "sportswear campaign", category: "activewear" },
    { text: "premium activewear photoshoot", category: "activewear" },
    { text: "activewear model poses", category: "activewear" },
    { text: "activewear running campaign", category: "activewear" },
    { text: "gym clothing campaign", category: "activewear" },
    { text: "yoga wear campaign", category: "activewear" },
    { text: "athleisure campaign", category: "activewear" },
    { text: "sportswear editorial photography", category: "activewear" },
    { text: "activewear brand campaign", category: "activewear" },
    { text: "fitness clothing photoshoot", category: "activewear" },
    { text: "activewear campaign ideas", category: "activewear" },
    { text: "activewear studio photoshoot", category: "activewear" },
    { text: "activewear outdoor campaign", category: "activewear" },
    { text: "running apparel campaign", category: "activewear" },
    { text: "training wear campaign", category: "activewear" },
    { text: "premium sportswear campaign", category: "activewear" },
    { text: "athletic fashion editorial", category: "activewear" },

    // Swimwear
    { text: "swimwear campaign", category: "swimwear" },
    { text: "swimwear editorial photoshoot", category: "swimwear" },
    { text: "beachwear campaign", category: "swimwear" },
    { text: "summer fashion campaign", category: "swimwear" },
    { text: "resort wear campaign", category: "swimwear" },
    { text: "swimwear lookbook", category: "swimwear" },
    { text: "swimwear model poses", category: "swimwear" },
    { text: "premium swimwear campaign", category: "swimwear" },
    { text: "beach fashion editorial", category: "swimwear" },
    { text: "swimwear natural light photoshoot", category: "swimwear" },
    { text: "luxury swimwear campaign", category: "swimwear" },
    { text: "swimwear brand photoshoot", category: "swimwear" },
    { text: "resort fashion editorial", category: "swimwear" },
    { text: "vacation fashion campaign", category: "swimwear" },
    { text: "summer clothing brand campaign", category: "swimwear" },
    { text: "beachwear lookbook", category: "swimwear" },
    { text: "swimwear campaign inspiration", category: "swimwear" },
    { text: "coastal fashion campaign", category: "swimwear" },
    { text: "beach editorial fashion photography", category: "swimwear" },
    { text: "summer resort wear photoshoot", category: "swimwear" },

    // Kidswear
    { text: "kids fashion campaign", category: "kidswear" },
    { text: "kidswear campaign", category: "kidswear" },
    { text: "children clothing photoshoot", category: "kidswear" },
    { text: "kids fashion editorial", category: "kidswear" },
    { text: "kids clothing brand campaign", category: "kidswear" },
    { text: "kidswear lookbook", category: "kidswear" },
    { text: "children fashion campaign ideas", category: "kidswear" },
    { text: "kids lifestyle photography", category: "kidswear" },
    { text: "kids clothing studio photoshoot", category: "kidswear" },
    { text: "kids fashion natural light", category: "kidswear" },
    { text: "premium kidswear campaign", category: "kidswear" },
    { text: "minimal kids fashion campaign", category: "kidswear" },
    { text: "children clothing brand photoshoot", category: "kidswear" },
    { text: "kids fashion moodboard", category: "kidswear" },
    { text: "kidswear editorial photography", category: "kidswear" },
    { text: "family fashion campaign", category: "kidswear" },
    { text: "children outfit photoshoot", category: "kidswear" },
    { text: "kids fashion campaign inspiration", category: "kidswear" },
    { text: "kids clothing ads", category: "kidswear" },
    { text: "kidswear brand visual identity", category: "kidswear" },

    // Minimalista
    { text: "minimal fashion campaign", category: "minimalist" },
    { text: "minimalist clothing brand", category: "minimalist" },
    { text: "clean fashion editorial", category: "minimalist" },
    { text: "neutral fashion campaign", category: "minimalist" },
    { text: "premium basics campaign", category: "minimalist" },
    { text: "minimal studio photoshoot", category: "minimalist" },
    { text: "minimal fashion photography", category: "minimalist" },
    { text: "minimal fashion lookbook", category: "minimalist" },
    { text: "minimal clothing campaign", category: "minimalist" },
    { text: "neutral colors fashion editorial", category: "minimalist" },
    { text: "clean studio fashion campaign", category: "minimalist" },
    { text: "minimalist fashion brand photoshoot", category: "minimalist" },
    { text: "quiet luxury fashion campaign", category: "minimalist" },
    { text: "minimal fashion campaign poses", category: "minimalist" },
    { text: "minimal fashion moodboard", category: "minimalist" },
    { text: "premium neutral clothing campaign", category: "minimalist" },
    { text: "clean clothing brand campaign", category: "minimalist" },
    { text: "minimal font campaign ads", category: "minimalist" },
    { text: "minimal fashion composition", category: "minimalist" },
    { text: "modern minimal fashion campaign", category: "minimalist" },

    // Lujo / Old Money
    { text: "old money fashion campaign", category: "old-money" },
    { text: "quiet luxury fashion campaign", category: "old-money" },
    { text: "old money aesthetic fashion", category: "old-money" },
    { text: "luxury casual fashion campaign", category: "old-money" },
    { text: "premium lifestyle fashion campaign", category: "old-money" },
    { text: "old money menswear campaign", category: "old-money" },
    { text: "old money women fashion campaign", category: "old-money" },
    { text: "country club fashion editorial", category: "old-money" },
    { text: "tennis club fashion campaign", category: "old-money" },
    { text: "polo club fashion editorial", category: "old-money" },
    { text: "luxury resort wear campaign", category: "old-money" },
    { text: "classic fashion editorial", category: "old-money" },
    { text: "heritage fashion campaign", category: "old-money" },
    { text: "elegant fashion campaign", category: "old-money" },
    { text: "old money fashion photoshoot", category: "old-money" },
    { text: "quiet luxury editorial", category: "old-money" },
    { text: "luxury basics campaign", category: "old-money" },
    { text: "premium knitwear campaign", category: "old-money" },
    { text: "classic menswear photoshoot", category: "old-money" },
    { text: "sophisticated fashion campaign", category: "old-money" },

    // Lanzamiento
    { text: "fashion launch campaign", category: "launch" },
    { text: "new collection fashion campaign", category: "launch" },
    { text: "clothing collection launch", category: "launch" },
    { text: "fashion drop campaign", category: "launch" },
    { text: "capsule collection campaign", category: "launch" },
    { text: "fashion campaign teaser", category: "launch" },
    { text: "clothing brand launch campaign", category: "launch" },
    { text: "new drop streetwear campaign", category: "launch" },
    { text: "fashion collection photoshoot", category: "launch" },
    { text: "product launch fashion editorial", category: "launch" },
    { text: "fashion campaign announcement", category: "launch" },
    { text: "new season fashion campaign", category: "launch" },
    { text: "fashion brand launch visuals", category: "launch" },
    { text: "clothing drop photoshoot", category: "launch" },
    { text: "capsule wardrobe campaign", category: "launch" },
    { text: "fashion collection moodboard", category: "launch" },
    { text: "fashion launch editorial", category: "launch" },
    { text: "new clothing brand campaign", category: "launch" },
    { text: "fashion campaign social media", category: "launch" },
    { text: "collection release campaign", category: "launch" },

    // E-commerce
    { text: "fashion ecommerce photography", category: "ecommerce" },
    { text: "ecommerce fashion editorial", category: "ecommerce" },
    { text: "clothing product photography model", category: "ecommerce" },
    { text: "fashion product photoshoot", category: "ecommerce" },
    { text: "clean product fashion photography", category: "ecommerce" },
    { text: "studio ecommerce fashion", category: "ecommerce" },
    { text: "fashion catalog photography", category: "ecommerce" },
    { text: "clothing catalog photoshoot", category: "ecommerce" },
    { text: "fashion product campaign", category: "ecommerce" },
    { text: "model product photography", category: "ecommerce" },
    { text: "fashion ecommerce clothing brand", category: "ecommerce" },
    { text: "fashion product detail photography", category: "ecommerce" },
    { text: "premium ecommerce fashion photography", category: "ecommerce" },
    { text: "minimal ecommerce clothing photography", category: "ecommerce" },
    { text: "fashion product page images", category: "ecommerce" },
    { text: "fashion web banner campaign", category: "ecommerce" },
    { text: "fashion ecommerce campaign", category: "ecommerce" },
    { text: "fashion product model poses", category: "ecommerce" },
    { text: "clean fashion catalog", category: "ecommerce" },
    { text: "modern ecommerce fashion photoshoot", category: "ecommerce" },

    // Web / Banners
    { text: "fashion website hero banner", category: "web-banners" },
    { text: "fashion web campaign", category: "web-banners" },
    { text: "clothing brand website banner", category: "web-banners" },
    { text: "fashion hero image", category: "web-banners" },
    { text: "fashion landing page campaign", category: "web-banners" },
    { text: "fashion banner photography", category: "web-banners" },
    { text: "fashion campaign negative space website", category: "web-banners" },
    { text: "fashion editorial banner", category: "web-banners" },
    { text: "fashion web hero section", category: "web-banners" },
    { text: "fashion brand homepage campaign", category: "web-banners" },
    { text: "clothing website hero image", category: "web-banners" },
    { text: "fashion campaign horizontal", category: "web-banners" },
    { text: "fashion editorial banner", category: "web-banners" },
    { text: "fashion website visual direction", category: "web-banners" },
    { text: "fashion campaign with space for text", category: "web-banners" },
    { text: "fashion landing page hero image", category: "web-banners" },
    { text: "fashion collection web banner", category: "web-banners" },
    { text: "fashion ecommerce hero campaign", category: "web-banners" },
    { text: "premium fashion website banner", category: "web-banners" },
    { text: "minimal fashion hero banner", category: "web-banners" }
  ];

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
          <div style="grid-column: 1/-1; text-align: center; padding: 2rem; color: var(--color-pinterest-light); font-family: var(--font-mono); font-size: 0.9rem;">
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
          <button class="copy-btn mini-copy" type="button" style="margin-top: 0.5rem; width: fit-content; align-self: flex-end;">
            <svg style="width: 12px; height: 12px; fill: currentColor;" viewBox="0 0 24 24">
              <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
            </svg>
            Copiar
          </button>
        `;

        // Register copy listener on the mini-button
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

    // Initial render
    renderTerms();
  }

  // 2. Clipboard Copy Functionality with Particle Sparks
  const copyButtons = document.querySelectorAll('.copy-btn:not(.mini-copy)');
  
  copyButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const parent = btn.closest('.prompt-container') || btn.closest('.card-brutal') || btn.closest('.compare-box') || btn.closest('.sheet-card') || btn.closest('.checklist-output-sheet') || btn.parentElement;
      const textEl = parent.querySelector('.prompt-text') || parent.querySelector('code') || parent.querySelector('.copy-target') || parent.querySelector('pre') || parent.querySelector('.term-text');
      
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

  // 3. Active Sidebar Links on Scroll (Scrollspy)
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

  // 4. Live Prompt Builder (Interactive Customizer)
  const builderInputs = document.querySelectorAll('.builder-input');
  const livePromptCode = document.getElementById('live-prompt-code');
  
  if (builderInputs.length > 0 && livePromptCode) {
    function updateLivePrompt() {
      const product = document.getElementById('bp-product').value || '[chaqueta sastre / vestido largo / hoodie]';
      const color = document.getElementById('bp-color').value || '[negro / blanco roto / azul denim]';
      const material = document.getElementById('bp-material').value || '[tejido knit / cuero sintético / lino]';
      const silueta = document.getElementById('bp-silueta').value || '[oversized / cropped / ajustada]';
      const publico = document.getElementById('bp-publico').value || '[mujeres de 22 a 35 años / hombres urbanos]';
      const estilo = document.getElementById('bp-estilo').value || '[lujo minimalista / streetwear premium / old money]';
      const emocion = document.getElementById('bp-emocion').value || '[deseo / seguridad / estatus silencioso]';
      
      const promptText = `Crea una campaña editorial de moda para una marca de estilo ${estilo}, mostrando un ${product} en color ${color}, material ${material} en silueta ${silueta}, diseñado para un público de ${publico}, con un modelo que transmita actitud natural y expresión de ${emocion}, en un entorno de estudio limpio o locación cuidada, con iluminación suave de tarde y sombras sutiles, composición con espacio negativo horizontal para texto, estética editorial premium, texturas detalladas visibles, fotografía profesional de moda urbana, sin logos inventados, sin distorsión, sin texto.`;
      
      livePromptCode.textContent = promptText;
    }
    
    builderInputs.forEach(input => {
      input.addEventListener('input', updateLivePrompt);
    });
    
    // Initial run
    updateLivePrompt();
  }

  // 5. Interactive Creative Direction Checklist Builder
  const selectBtns = document.querySelectorAll('.option-select-btn');
  const finalEstilo = document.getElementById('out-estilo');
  const finalCliente = document.getElementById('out-cliente');
  const finalFondo = document.getElementById('out-fondo');
  const finalActitud = document.getElementById('out-actitud');
  const finalColor = document.getElementById('out-color');
  const finalComposicion = document.getElementById('out-composicion');
  const finalEmocion = document.getElementById('out-emocion');
  const finalChecklistPrompt = document.getElementById('checklist-prompt-code');

  if (selectBtns.length > 0) {
    // Set default selections
    const defaults = {
      estilo: 'Premium',
      cliente: 'Aspiracional',
      fondo: 'Estudio Limpio',
      actitud: 'Segura',
      color: 'Neutra',
      composicion: 'Anuncio Vertical',
      emocion: 'Deseo'
    };

    // Initialize selections on load
    selectBtns.forEach(btn => {
      const group = btn.getAttribute('data-group');
      const val = btn.getAttribute('data-val');
      if (defaults[group] && defaults[group].toLowerCase() === val.toLowerCase()) {
        btn.classList.add('selected');
      }

      btn.addEventListener('click', () => {
        // Toggle/Select in group
        const groupBtns = document.querySelectorAll(`.option-select-btn[data-group="${group}"]`);
        groupBtns.forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');
        
        updateChecklistOutputs();
      });
    });

    function updateChecklistOutputs() {
      const selections = {};
      
      ['estilo', 'cliente', 'fondo', 'actitud', 'color', 'composicion', 'emocion'].forEach(group => {
        const selected = document.querySelector(`.option-select-btn[data-group="${group}"].selected`);
        selections[group] = selected ? selected.getAttribute('data-val') : '---';
      });

      // Update card outputs
      if (finalEstilo) finalEstilo.textContent = selections.estilo;
      if (finalCliente) finalCliente.textContent = selections.cliente;
      if (finalFondo) finalFondo.textContent = selections.fondo;
      if (finalActitud) finalActitud.textContent = selections.actitud;
      if (finalColor) finalColor.textContent = selections.color;
      if (finalComposicion) finalComposicion.textContent = selections.composicion;
      if (finalEmocion) finalEmocion.textContent = selections.emocion;

      // Update checklist generated prompt
      if (finalChecklistPrompt) {
        const generatedPrompt = `Crea una campaña editorial de moda para una marca de estilo ${selections.estilo}, mostrando una colección diseñada para un cliente ${selections.cliente}, en un entorno de ${selections.fondo}, con modelos de actitud ${selections.actitud}, usando una paleta de color ${selections.color}, encuadre idóneo para ${selections.composicion}, iluminación editorial y una emoción central de ${selections.emocion}, fotografía profesional`;
        finalChecklistPrompt.textContent = generatedPrompt;
      }
    }

    // Run once on load
    updateChecklistOutputs();
  }

  // 6. Polaroid Image Lightbox Modal
  const polaroidImgs = document.querySelectorAll('.polaroid-img-wrapper img');
  
  // Create Modal element programmatically if not exists
  let lightbox = document.querySelector('.brutal-lightbox');
  if (!lightbox) {
    lightbox = document.createElement('div');
    lightbox.className = 'brutal-lightbox';
    lightbox.innerHTML = `
      <div class="lightbox-content">
        <span class="lightbox-close">&times;</span>
        <img src="" alt="Zoom" class="lightbox-img">
        <div class="lightbox-caption"></div>
      </div>
    `;
    document.body.appendChild(lightbox);
  }
  
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

  // 7. Dynamic Reveal and Intersection Observer for Scroll Animations
  const selectorsToAnimate = [
    '.section-title',
    '.card-brutal',
    '.card-brutal-dark',
    '.compare-grid',
    '.table-brutal-wrapper',
    '.step-item',
    '.polaroid-item',
    '.sheet-card',
    '.prompt-container',
    '.bento-grid',
    '.term-bank',
    '.checklist-builder-container'
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
