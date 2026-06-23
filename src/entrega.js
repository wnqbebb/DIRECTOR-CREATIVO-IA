// JavaScript para la página de entrega del producto

document.addEventListener("DOMContentLoaded", () => {
  // 1. Barra de progreso de scroll dinámica
  const progressBar = document.createElement("div");
  progressBar.className = "scroll-progress-bar";
  document.body.appendChild(progressBar);

  window.addEventListener("scroll", () => {
    const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
    progressBar.style.width = scrolled + "%";
  });

  // 2. Navegación rápida con Scroll Suave
  const quickNavLinks = document.querySelectorAll(".quick-nav-btn");
  
  quickNavLinks.forEach(link => {
    link.addEventListener("click", (e) => {
      const targetId = link.getAttribute("href");
      if (targetId && targetId.startsWith("#")) {
        e.preventDefault();
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          targetElement.scrollIntoView({
            behavior: "smooth",
            block: "start"
          });
        }
      }
    });
  });

  // 3. Indicador activo de sección al hacer Scroll (IntersectionObserver)
  const sections = document.querySelectorAll(".deliverable-section");
  
  if ("IntersectionObserver" in window) {
    const observerOptions = {
      root: null,
      rootMargin: "-20% 0px -60% 0px", // Ajustado para detectar mejor la sección en pantalla
      threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const activeId = entry.target.getAttribute("id");
          
          quickNavLinks.forEach(link => {
            const href = link.getAttribute("href");
            if (href === `#${activeId}`) {
              link.style.backgroundColor = "var(--color-accent-red)";
              link.style.borderColor = "var(--color-accent-red)";
              link.style.color = "var(--color-text-light)";
              link.style.boxShadow = "4px 4px 0px rgba(250, 248, 245, 0.9)";
            } else {
              link.style.backgroundColor = "transparent";
              link.style.borderColor = "rgba(250, 248, 245, 0.15)";
              link.style.color = "var(--color-text-light)";
              link.style.boxShadow = "none";
            }
          });
        }
      });
    }, observerOptions);

    sections.forEach(section => {
      observer.observe(section);
    });
  }

  // 4. Lazy loading de imágenes usando IntersectionObserver
  const lazyImages = document.querySelectorAll("img[loading='lazy']");
  
  if ("IntersectionObserver" in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const image = entry.target;
          if (image.dataset.src) {
            image.src = image.dataset.src;
          }
          imageObserver.unobserve(image);
        }
      });
    });

    lazyImages.forEach(image => {
      imageObserver.observe(image);
    });
  }
});
