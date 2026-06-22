document.addEventListener('DOMContentLoaded', () => {
  // 1. Copy Prompt/Text to Clipboard
  const copyButtons = document.querySelectorAll('.copy-btn');
  copyButtons.forEach(button => {
    button.addEventListener('click', (e) => {
      let textToCopy = '';
      const promptContainer = button.closest('.prompt-container');
      
      if (promptContainer) {
        const textElement = promptContainer.querySelector('.prompt-text');
        if (textElement) {
          textToCopy = textElement.innerText || textElement.textContent;
        }
      }

      if (textToCopy) {
        navigator.clipboard.writeText(textToCopy.trim()).then(() => {
          const originalText = button.innerHTML;
          button.classList.add('copied');
          button.innerHTML = `
            <svg style="width: 12px; height: 12px; fill: currentColor;" viewBox="0 0 24 24">
              <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
            </svg>
            ¡Copiado!
          `;
          setTimeout(() => {
            button.classList.remove('copied');
            button.innerHTML = originalText;
          }, 2000);
        }).catch(err => {
          console.error('Error copying text: ', err);
        });
      }
    });
  });

  // 2. Tab Navigation for Prompts
  const tabTriggers = document.querySelectorAll('.tab-trigger');
  const tabPanels = document.querySelectorAll('.tab-content-panel');
  
  tabTriggers.forEach(trigger => {
    trigger.addEventListener('click', () => {
      const targetId = trigger.getAttribute('data-target');
      
      tabTriggers.forEach(t => t.classList.remove('active'));
      trigger.classList.add('active');
      
      tabPanels.forEach(panel => {
        if (panel.id === targetId) {
          panel.classList.add('active');
        } else {
          panel.classList.remove('active');
        }
      });
    });
  });

  // 3. Accordion Toggle for Step 4 Methods
  const accordionHeaders = document.querySelectorAll('.accordion-header');
  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.closest('.accordion-item');
      const isActive = item.classList.contains('active');
      
      // Close other items
      document.querySelectorAll('.accordion-item').forEach(i => i.classList.remove('active'));
      
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });

  // 4. Model Profile Deck Selector (Step 4)
  const modelDeckTabs = document.querySelectorAll('.model-deck-tab');
  const modelDeckContents = document.querySelectorAll('.model-deck-content');
  
  modelDeckTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const targetId = tab.getAttribute('data-target');
      
      modelDeckTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      
      modelDeckContents.forEach(content => {
        if (content.id === targetId) {
          content.classList.add('active');
        } else {
          content.classList.remove('active');
        }
      });
    });
  });

  // 5. Filing Cabinet Folder Tabs (Step 5)
  const cabinetTabs = document.querySelectorAll('.cabinet-tab-btn');
  const cabinetPanes = document.querySelectorAll('.cabinet-pane');
  
  cabinetTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const targetId = tab.getAttribute('data-target');
      
      cabinetTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      
      cabinetPanes.forEach(pane => {
        if (pane.id === targetId) {
          pane.classList.add('active');
        } else {
          pane.classList.remove('active');
        }
      });
    });
  });

  // 6. Content Calendar Timeline Selector (Step 5)
  const calendarDayBtns = document.querySelectorAll('.calendar-day-btn');
  const calendarDayContents = document.querySelectorAll('.calendar-day-content');
  
  calendarDayBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-target');
      
      calendarDayBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      
      calendarDayContents.forEach(content => {
        if (content.id === targetId) {
          content.classList.add('active');
        } else {
          content.classList.remove('active');
        }
      });
    });
  });

  // 7. Stories Mobile Phone Simulator (Step 5)
  let currentSlide = 0;
  const phoneSliderTrack = document.querySelector('.phone-slider-track');
  const phoneIndicator = document.querySelector('.phone-indicator');
  const prevBtn = document.getElementById('phone-prev-btn');
  const nextBtn = document.getElementById('phone-next-btn');
  
  if (phoneSliderTrack && phoneIndicator && prevBtn && nextBtn) {
    const updatePhoneSlide = () => {
      phoneSliderTrack.style.transform = `translateX(-${currentSlide * 20}%)`;
      phoneIndicator.textContent = `HISTORIA ${currentSlide + 1} / 5`;
    };
    
    prevBtn.addEventListener('click', () => {
      if (currentSlide > 0) {
        currentSlide--;
        updatePhoneSlide();
      }
    });
    
    nextBtn.addEventListener('click', () => {
      if (currentSlide < 4) {
        currentSlide++;
        updatePhoneSlide();
      } else {
        // Loop back
        currentSlide = 0;
        updatePhoneSlide();
      }
    });
  }

  // 8. Copy WhatsApp message text
  const chatCopyButtons = document.querySelectorAll('.chat-copy-btn');
  chatCopyButtons.forEach(button => {
    button.addEventListener('click', () => {
      const chatBubble = button.closest('.chat-bubble');
      if (chatBubble) {
        // Clone bubble, remove copy button, and get clean text
        const bubbleClone = chatBubble.cloneNode(true);
        const btnToRemove = bubbleClone.querySelector('.chat-bubble-footer');
        if (btnToRemove) {
          btnToRemove.remove();
        }
        const textToCopy = bubbleClone.innerText || bubbleClone.textContent;
        
        navigator.clipboard.writeText(textToCopy.trim()).then(() => {
          const originalText = button.textContent;
          button.textContent = '¡Copiado!';
          button.style.backgroundColor = '#28a745';
          button.style.color = '#ffffff';
          setTimeout(() => {
            button.textContent = originalText;
            button.style.backgroundColor = '';
            button.style.color = '';
          }, 2000);
        });
      }
    });
  });

  // 9. Scroll Tracking for Sidebar Active Links
  const sections = document.querySelectorAll('section, header');
  const navLinks = document.querySelectorAll('.nav-link');

  const observerOptions = {
    root: null,
    rootMargin: '-30% 0px -50% 0px',
    threshold: 0
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        
        navLinks.forEach(link => {
          link.classList.remove('active');
          const href = link.getAttribute('href');
          if (href === `#${id}` || (id === 'hero' && href === '#')) {
            link.classList.add('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(section => {
    if (section.id) {
      observer.observe(section);
    }
  });
});
