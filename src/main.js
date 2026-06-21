import './style.css'

document.addEventListener('DOMContentLoaded', () => {
  // 1. Copy to Clipboard Functionality
  const copyButtons = document.querySelectorAll('.copy-btn');
  
  copyButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const parent = btn.closest('.prompt-container') || btn.closest('.editorial-card') || btn.parentElement;
      const textEl = parent.querySelector('.prompt-text') || parent.querySelector('.copy-target') || parent.querySelector('code') || parent.querySelector('.copy-source');
      
      if (textEl) {
        // Get raw text (preserving line breaks)
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

  // 2. Active Sidebar Links on Scroll (Scrollspy)
  const sections = document.querySelectorAll('section, header');
  const navLinks = document.querySelectorAll('.nav-link');
  
  function updateActiveLink() {
    let scrollPosition = window.scrollY || document.documentElement.scrollTop;
    let currentSectionId = '';
    
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      
      // If we scrolled past the top of the section (minus some padding)
      if (scrollPosition >= (sectionTop - 200)) {
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

  // 3. Interactive Tabs for Campaign Deliverables
  const tabButtons = document.querySelectorAll('.tab-btn');
  
  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const tabsContainer = btn.closest('.tabs-container');
      const tabGroup = btn.getAttribute('data-group');
      const targetPanelId = btn.getAttribute('data-tab');
      
      // Deactivate all buttons in this group
      tabsContainer.querySelectorAll(`.tab-btn[data-group="${tabGroup}"]`).forEach(b => {
        b.classList.remove('active');
      });
      
      // Deactivate all panels in this group
      tabsContainer.querySelectorAll(`.tab-panel[data-group="${tabGroup}"]`).forEach(p => {
        p.classList.remove('active');
      });
      
      // Activate selected button and panel
      btn.classList.add('active');
      const targetPanel = tabsContainer.querySelector(`#${targetPanelId}`);
      if (targetPanel) {
        targetPanel.classList.add('active');
      }
    });
  });
});
