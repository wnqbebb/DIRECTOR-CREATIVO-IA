import os
import re

def main():
    print("Reading text paragraphs...")
    with open("DE_PRENDA_A_CAMPANA_TEXT.txt", "r", encoding="utf-8") as f:
        paragraphs = [line.strip() for line in f]

    # Helper function to generate full-size brutalist frames
    def make_full_size_image(img, label="Captura de Pantalla"):
        return f"""
        <div class="full-size-image-container">
          <div class="image-label-bar">[{label.upper()}]</div>
          <img class="full-size-img" src="/media/de_prenda_a_campana/{img}" alt="{label}" />
        </div>
        """

    def make_two_col_images(img1, img2, label1="Muestra A", label2="Muestra B"):
        return f"""
        <div class="image-layout-two-col">
          <div class="full-size-image-container">
            <div class="image-label-bar">[{label1.upper()}]</div>
            <img class="full-size-img" src="/media/de_prenda_a_campana/{img1}" alt="{label1}" />
          </div>
          <div class="full-size-image-container">
            <div class="image-label-bar">[{label2.upper()}]</div>
            <img class="full-size-img" src="/media/de_prenda_a_campana/{img2}" alt="{label2}" />
          </div>
        </div>
        """

    html_content = []
    
    # Write header with correct font loading and styles
    html_content.append("""<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2L15.5 8.5L24 12L15.5 15.5L12 24L8.5 15.5L0 12L8.5 8.5Z' fill='%23F94A2C'/%3E%3C/svg%3E" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>DE PRENDA A CAMPAÑA — Sistema Editorial 360°</title>
    
    <!-- OpenGraph/SEO -->
    <meta name="description" content="Transforma una prenda o idea en una campaña de moda profesional con Inteligencia Artificial. Método Editorial 360 sin fotógrafos ni estudio." />
    <meta property="og:title" content="DE PRENDA A CAMPAÑA — Dirección de Moda con IA" />
    <meta property="og:description" content="Diseña tu universo visual, genera prompts y automatiza tu contenido de moda." />
    <meta property="og:image" content="/media/hero_prenda_a_campana.png" />
    
    <link rel="stylesheet" href="/src/prenda-campana.css" />
    <script type="module" src="/src/prenda-campana.js"></script>
  </head>
  <body>
    <div class="app-container">
      <!-- Sidebar Navigation -->
      <aside class="sidebar">
        <div class="logo-container">
          <div class="logo-title">DE PRENDA <span>A CAMPAÑA</span></div>
          <div class="logo-subtitle">SISTEMA EDITORIAL 360°</div>
        </div>
        
        <nav>
          <ul class="nav-menu">
            <li class="nav-item"><a href="#" class="nav-link active" id="nav-btn-hero"><span class="nav-number">00</span> Portada</a></li>
            <li class="nav-item"><a href="#problema" class="nav-link" id="nav-btn-problema"><span class="nav-number">01</span> El Problema</a></li>
            <li class="nav-item"><a href="#sistema-360" class="nav-link" id="nav-btn-sistema-360"><span class="nav-number">02</span> Sistema 360</a></li>
            <li class="nav-item"><a href="#paso-0" class="nav-link" id="nav-btn-paso-0"><span class="nav-number">03</span> Paso 0: Prenda Base</a></li>
            <li class="nav-item"><a href="#paso-1" class="nav-link" id="nav-btn-paso-1"><span class="nav-number">04</span> Paso 1: Mapa Visual</a></li>
            <li class="nav-item"><a href="#paso-2" class="nav-link" id="nav-btn-paso-2"><span class="nav-number">05</span> Paso 2: ADN Editorial</a></li>
            <li class="nav-item"><a href="#paso-3" class="nav-link" id="nav-btn-paso-3"><span class="nav-number">06</span> Paso 3: Producción IA</a></li>
            <li class="nav-item"><a href="#paso-4" class="nav-link" id="nav-btn-paso-4"><span class="nav-number">07</span> Paso 4: Modelos IA</a></li>
            <li class="nav-item"><a href="#paso-5" class="nav-link" id="nav-btn-paso-5"><span class="nav-number">08</span> Paso 5: Campaña Ventas</a></li>
          </ul>
        </nav>
        
        <div class="sidebar-footer">
          De Prenda a Campaña<br>
          © 2026 Start Grow Fast AI Agents. Todos los derechos reservados.
        </div>
      </aside>

      <!-- Main Content Area -->
      <main class="main-content">
        <!-- Top Announcement Bar -->
        <div class="top-announcement-bar">
          <span class="announcement-tag">PROCESO IA</span>
          <span>ENTRENAMIENTO PRINCIPAL DE DIRECCIÓN CREATIVA DE MODA</span>
        </div>

        <!-- Portada / Hero -->
        <header id="hero" class="hero-section">
          <div class="hero-banner-container">
            <img src="/media/hero_prenda_a_campana.png" alt="De Prenda a Campaña Banner" class="hero-banner-img" />
            <div class="tape-sticker tape-newspaper" style="bottom: 30px; left: 40px; transform: rotate(-2.5deg); opacity: 0.95;">
              SISTEMA EDITORIAL 360°
            </div>
            <div class="tape-sticker tape-rip tape-dark" style="top: 25px; right: 30px; transform: rotate(1.5deg);">
              AI ART DIRECTION
            </div>
          </div>
          
          <div style="padding: 5rem; background-color: var(--black); color: var(--paper-warm);">
            <h1 style="font-family: 'Anton', 'Bebas Neue', Impact, sans-serif; font-size: clamp(64px, 11vw, 170px); line-height: 0.82; font-weight: 900; letter-spacing: -0.05em; text-transform: uppercase; margin-bottom: 2rem;">
              DE PRENDA<br><span style="color: var(--red);">A CAMPAÑA</span>
            </h1>
            <p style="font-size: clamp(18px, 2vw, 30px); line-height: 1.05; font-weight: 700; text-transform: uppercase; letter-spacing: -0.02em; color: var(--paper); margin-bottom: 2rem; max-width: 860px;">
              El entrenamiento para transformar una prenda o una idea en contenido visual <span style="color: var(--red);">profesional</span> listo para publicar con IA.
            </p>
            <div style="display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
              <span class="handwritten" style="font-size: 1.5rem; transform: rotate(-3deg); margin-right: 2rem;">TU MARCA. TU VISIÓN. TU CAMPAÑA.</span>
              <a href="#problema" class="cta-button">QUIERO CREAR MI CAMPAÑA</a>
            </div>
          </div>
        </header>

        <!-- Sección 01: El Problema -->
        <section id="problema" style="background-color: var(--paper); color: var(--black); padding-bottom: 0;">
          <div class="section-meta">[ SECCIÓN 01 / EL MANIFIESTO ]</div>
          <h2 class="section-title" style="font-size: clamp(40px, 5vw, 76px); line-height: 0.85;">TU PRENDA NO VENDE SI NADIE LA DESEA</h2>
          <div class="text-editorial" style="margin-bottom: 4rem;">
            <p style="font-size: 1.25rem; font-weight: 700; margin-bottom: 2rem;">
              Este es el corazón del producto. Es el entrenamiento paso a paso donde aprendes a crear una campaña visual completa para tu marca de ropa usando IA. No se vende como curso de IA. Se vende como el proceso para transformar una prenda o una idea en contenido visual profesional listo para publicar.
            </p>
            
            <div style="display: grid; grid-template-columns: 1fr 1.2fr; gap: 3rem; align-items: center; margin: 3rem 0;">
              <div>
                <p>El error de la mayoría de marcas pequeñas es pensar que la ropa se vende sola. Suben fotos planas, arrugadas o tomadas a la rápida en una habitación oscura. Y luego se quejan de que no venden.</p>
                <p>La IA nos da el superpoder de crear mundos editoriales premium para nuestro producto sin gastar miles de dólares en producción.</p>
                <span class="handwritten" style="font-size: 1.5rem; display: block; margin-top: 1rem; transform: rotate(-1deg);">Estilo de cartel underground de moda.</span>
              </div>
              <div>
                <div class="full-size-image-container" style="margin: 0;">
                  <div class="image-label-bar">[REFERENCIA VISUAL EDITORIAL - B/W]</div>
                  <img class="full-size-img" src="/media/de_prenda_a_campana/image5.png" style="filter: grayscale(1) contrast(1.1);" alt="Moda" />
                </div>
              </div>
            </div>
          </div>
          

        </section>

        <!-- Sección 02: Sistema 360 -->
        <section id="sistema-360" class="dark-section">
          <div class="section-meta">[ SECCIÓN 02 / EL MÉTODO ]</div>
          <h2 class="section-title">SISTEMA EDITORIAL 360°</h2>
          <div class="text-editorial">
            <p>Un sistema de 5 pasos diseñado para transformar tu producto físico en un activo publicitario premium:</p>
            
            <div class="horizontal-cards-list">
              <div class="horizontal-card-item">
                <div class="card-num-box">01</div>
                <div class="card-content-box">
                  <h3>MAPA VISUAL DE MARCA</h3>
                  <p>Aprende a mirar Pinterest, Instagram y marcas globales con ojos de directora creativa. No para copiar, sino para decodificar poses, iluminación, fondos y composiciones profesionales.</p>
                </div>
              </div>
              <div class="horizontal-card-item">
                <div class="card-num-box">02</div>
                <div class="card-content-box">
                  <h3>ADN EDITORIAL</h3>
                  <p>Define la personalidad visual de tu campaña antes de generar: el tipo de modelo, el ambiente, la paleta de colores y la sensación que deseas proyectar.</p>
                </div>
              </div>
              <div class="horizontal-card-item">
                <div class="card-num-box">03</div>
                <div class="card-content-box">
                  <h3>PRODUCCIÓN IA SIN ESTUDIO</h3>
                  <p>Genera imágenes de moda de alta resolución (2K) sin fotógrafo, sin locación, sin modelos reales y a costo $0 con Google Flow.</p>
                </div>
              </div>
              <div class="horizontal-card-item">
                <div class="card-num-box">04</div>
                <div class="card-content-box">
                  <h3>MODELOS IA Y ROSTRO DE MARCA</h3>
                  <p>Crea modelos virtuales consistentes o utiliza tu propio rostro en la campaña para generar deseo, contexto y aspiración.</p>
                </div>
              </div>
              <div class="horizontal-card-item">
                <div class="card-num-box">05</div>
                <div class="card-content-box">
                  <h3>CAMPAÑA LISTA PARA VENDER</h3>
                  <p>Convierte las imágenes en un embudo de contenido útil: carruseles de Instagram, stories de preventa, anuncios de Meta Ads y catálogos de WhatsApp.</p>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Sección 03: Paso 0 -->
        <section id="paso-0">
          <div class="section-meta">[ PASO 00 / LA BASE ]</div>
          <h2 class="section-title">PASO CERO: PRENDA DE REFERENCIA</h2>
          <div class="text-editorial">
            <p>Para este entrenamiento, hemos escogido un buso/polo sencillo. El objetivo es que veas cómo convertimos esta prenda real en una campaña de moda profesional.</p>
            
            <div class="brutalist-block-red" style="margin: 2rem 0;">
              <span class="ocr-label">[ RECOMENDACIÓN TÉCNICA ]</span>
              <p style="font-weight: 800; font-size: 1.15rem; text-transform: uppercase;">
                IMPORTANTE: Sube la foto en la mejor calidad posible. Aunque la IA corrige arrugas y costuras, el producto real debe ser fiel al resultado final.
              </p>
            </div>

            <p>Este es el producto de referencia real que hemos elegido, fotografiado por ambos lados en un fondo básico:</p>
""")

    # We append the Step 0 photos (image67.png, image22.png)
    html_content.append(make_two_col_images("image67.png", "image22.png", "Prenda Frontal", "Prenda Trasera"))

    html_content.append("""
            <p><strong>LIMPIEZA INICIAL CON EL AGENTE:</strong></p>
            <p>Pegamos nuestras fotos de referencia en <strong>Google Flow</strong>, activamos el botón de <strong>Modo Agente</strong> y le damos una indicación muy sencilla:</p>
            
            <div style="background-color: var(--black); color: var(--red); font-family: 'Space Mono', monospace; padding: 1.5rem; border: var(--border-brutal-thin); margin: 2rem 0;">
              "Cambia el fondo de cada imagen de referencia por un fondo de color blanco neutro para una campaña de moda."
            </div>
""")

    # Google Flow load (image77.png) and thinking (image12.png)
    html_content.append(make_full_size_image("image77.png", "Cargando prenda en Google Flow"))
    html_content.append(make_full_size_image("image12.png", "Agente de Google Flow procesando"))

    html_content.append("""
            <p>El agente se coloca a pensar... ¡y BOOM! Ya tenemos imágenes en estilo editorial de moda con fondo blanco de catálogo, sin pagar y sin saber de edición técnica.</p>
""")

    # Result images (image24.png, image38.png, image5.png)
    html_content.append(make_full_size_image("image24.png", "Resultado inicial del Agente"))
    html_content.append(make_two_col_images("image38.png", "image5.png", "Resultado Catálogo Blanco 01", "Resultado Catálogo Blanco 02"))

    # Section 04: Paso 1
    html_content.append("""
        </section>

        <!-- Sección 04: Paso 1 -->
        <section id="paso-1" style="background-color: var(--paper);">
          <div class="section-meta">[ PASO 01 / ANÁLISIS DE REFERENCIAS ]</div>
          <h2 class="section-title">PASO 1: MAPA VISUAL DE MARCA</h2>
          <div class="text-editorial">
            <p>Aquí aprendemos a mirar Pinterest, Instagram y marcas globales con ojos de directora creativa. No para copiar, sino para decodificar poses, iluminación, actitud, texturas y encuadres.</p>
            <p>Fuimos a <strong>Pinterest</strong> y buscamos conceptos clave relacionados con nuestra prenda (polo de punto tejido o camisa de rugby para hombre de estilo Streetwear):</p>
            
            <ul class="editorial-list">
              <li><strong>Knit polo shirt streetwear</strong> (Polo de punto para moda urbana)</li>
              <li><strong>Oversized knit rugby shirt</strong> (Camisa de rugby tejida y holgada)</li>
              <li><strong>Vintage striped knit polo</strong> (Polo tejido a rayas estilo vintage)</li>
            </ul>
""")

    # Pinterest search (image50.png)
    html_content.append(make_full_size_image("image50.png", "Buscando inspiración en Pinterest"))

    html_content.append("""
            <p>Guardamos las referencias visuales que representan las poses, el estilo y la dirección de arte que nos gustaría replicar para nuestra campaña:</p>
            
            <div class="pinterest-slider-container">
              <div class="section-meta">[ PINES SELECCIONADOS COMO MAPA VISUAL ]</div>
              <div class="pinterest-slider">
    """)
    
    # 10 pins
    pins = ["image55.png", "image48.png", "image65.png", "image69.png", "image32.png", "image64.png", "image35.png", "image3.png", "image11.png", "image76.png"]
    for pin in pins:
        html_content.append(f"""
                <div class="pinterest-pin-card">
                  <img class="pinterest-pin-img" src="/media/de_prenda_a_campana/{pin}" alt="Pinterest Reference Pin" />
                  <div class="showcase-caption">Pin de Referencia</div>
                </div>
        """)
        
    html_content.append("""
              </div>
            </div>

            <p><strong>ALIMENTANDO NUESTRO DIRECTOR CREATIVO EN CHATGPT:</strong></p>
            <p>Pegamos estas 10 referencias en nuestro chat con el Director Creativo de ChatGPT y le dimos una instrucción muy sencilla:</p>
            
            <div style="background-color: var(--black); color: var(--red); font-family: 'Space Mono', monospace; padding: 1.5rem; border: var(--border-brutal-thin); margin: 2rem 0;">
              "Analiza cada una de las imágenes de referencia porque las vamos a replicar todas tal cual para mi producto de referencia que te daré después. Quiero replicar estas fotos pero aplicadas a mi producto, así que estudia cada imagen que vamos a recrear."
            </div>
    """)

    # ChatGPT input (image54.png) and ChatGPT response (image4.png)
    html_content.append(make_full_size_image("image54.png", "Enviando referencias a ChatGPT"))
    html_content.append(make_full_size_image("image4.png", "Análisis creativo de ChatGPT"))

    html_content.append("""
            <p>Luego adjuntamos las fotos de referencia de nuestro polo real y escribimos este prompt maestro:</p>
            <div style="background-color: var(--black); color: var(--red); font-family: 'Space Mono', monospace; padding: 1.5rem; border: var(--border-brutal-thin); margin: 2rem 0;">
              "Este es mi producto y quiero que me des todos los prompts para recrear la campaña completa de cada una de las imágenes que analizamos anteriormente. Las mismas posiciones, estilo y diferentes modelos."
            </div>
    """)

    # Second ChatGPT response (image7.png)
    html_content.append(make_full_size_image("image7.png", "Obteniendo los prompts optimizados"))

    # Reorganize prompts 1-10 into a grid of 5 rows, 2 columns (side by side)
    prompts_1_10 = [
        ("PROMPT 1 — Modelo + fondo madera cálido",
         "Fotografía editorial de moda masculina streetwear premium, modelo joven usando polo tejido oversized de manga corta con cuello, rayas horizontales azul denim y beige, textura knit gruesa, botones frontales, branding elegante en el pecho y texto central grande estilo club vintage, silueta boxy, modelo de medio cuerpo frente a pared de madera oscura, mirada hacia un lado, expresión seria y tranquila, manos cruzadas suavemente frente al abdomen, pantalón deportivo gris claro, iluminación cálida suave, estética rugby club urbano, composición vertical para Instagram, lujo casual, alta nitidez, textura visible de la prenda.",
         "Negativos: logos de marcas reales, texto mal escrito, manos deformes, prenda distorsionada, cuello torcido, rayas irregulares, piel artificial, fondo caótico, baja calidad."),
        ("PROMPT 2 — Catálogo limpio frontal",
         "Fotografía lookbook streetwear premium, modelo masculino joven usando polo tejido oversized de manga corta con cuello, rayas azul denim y beige, fit boxy amplio, textura de punto visible, botones frontales, gráfico elegante central en el pecho, modelo de pie frontal mirando a cámara, expresión neutra, una mano en el bolsillo y la otra relajada, pantalón denim oscuro desgastado, fondo blanco grisáceo minimalista, luz de estudio suave, encuadre desde muslos hasta cabeza, estética limpia de marca urbana premium, imagen comercial para ecommerce e Instagram.",
         "Negativos: marcas reales, texto ilegible, manos deformes, ropa deformada, rayas torcidas, exceso de contraste, fondo sucio, baja resolución."),
        ("PROMPT 3 — Producto solo textura premium",
         "Fotografía de producto premium sin modelo, polo tejido oversized de manga corta con cuello, rayas horizontales azul denim y beige, textura knit gruesa visible, botones frontales, branding frontal elegante, prenda colocada perfectamente centrada sobre fondo crema cálido, luz suave lateral, sombras naturales, enfoque en tejido, cuello, mangas amplias y caída boxy, estética artesanal vintage de club, catálogo editorial, alta calidad, composición limpia.",
         "Negativos: maniquí, cuerpo humano, logos reales, texto deformado, prenda arrugada en exceso, rayas desalineadas, fondo caótico, baja calidad."),
        ("PROMPT 4 — Modelo mirando abajo estilo rugby",
         "Fotografía editorial streetwear, modelo masculino joven usando polo tejido oversized rayado azul denim y beige, cuello polo con botones, textura knit pesada, fit boxy, gráfico central elegante, modelo mirando hacia abajo con actitud relajada, una mano detrás o dentro del bolsillo, jeans claros lavados, fondo blanco limpio, iluminación de estudio suave, encuadre medio desde cintura hasta cabeza, estética rugby heritage moderna, composición minimalista, prenda protagonista.",
         "Negativos: logos reales, texto inventado mal escrito, manos deformes, cuello deformado, rayas rotas, prenda pegada al cuerpo, fondo recargado."),
        ("PROMPT 5 — Producto frontal ecommerce",
         "Fotografía ecommerce premium de prenda, polo tejido oversized de manga corta con cuello, rayas horizontales azul denim y beige, botones frontales, manga amplia, silueta boxy corta, textura de punto grueso visible, branding elegante en el pecho, prenda flotando o colgada invisible perfectamente centrada sobre fondo blanco puro, vista frontal plana, luz uniforme, sombra muy suave, catálogo de moda urbana premium.",
         "Negativos: modelo, maniquí visible, arrugas excesivas, rayas torcidas, texto mal escrito, logos de marcas reales, baja calidad."),
        ("PROMPT 6 — Lifestyle pareja",
         "Fotografía editorial lifestyle con pareja joven usando prendas coordinadas, ambos con polo tejido oversized de manga corta con cuello, rayas azul denim y beige, textura knit premium, fit boxy, estética rugby club vintage. Modelo masculino de espalda mostrando la parte trasera rayada de la prenda, modelo femenino al frente inclinando suavemente la cabeza hacia él, actitud íntima y relajada, jeans claros, fondo gris claro de estudio, luz suave natural, composición vertical, campaña streetwear premium para Instagram.",
         "Negativos: contacto incómodo, manos deformes, rostros artificiales, logos reales, texto deformado, rayas desalineadas, fondo caótico."),
        ("PROMPT 7 — Collage editorial de campaña",
         "Collage editorial de moda premium en tres imágenes, producto principal: polo tejido oversized de manga corta con cuello, rayas azul denim y beige, textura knit gruesa, fit boxy, branding frontal elegante. Imagen superior: prenda colgada en percha sobre estructura metálica, vista frontal limpia. Imagen inferior izquierda: modelo masculino de perfil usando la prenda, mirada seria, fondo gris. Imagen inferior derecha: modelo full body usando la prenda con pantalón gris amplio y sneakers blancos, manos en bolsillos, postura relajada. Paleta azul denim, beige, gris, iluminación suave de estudio, estética campaña streetwear club premium.",
         "Negativos: logos reales, texto ilegible, collage desordenado, cuerpos deformes, manos deformes, prenda distorsionada, baja resolución."),
        ("PROMPT 8 — Frente y espalda tipo drop limitado",
         "Composición de producto para lanzamiento streetwear, polo tejido oversized rayado azul denim y beige mostrado en dos vistas: vista frontal arriba con cuello, botones, branding frontal elegante y textura knit visible; vista trasera abajo mostrando rayas horizontales limpias sin gráfico grande, manga amplia, fit boxy. Fondo blanco limpio, iluminación uniforme, estética drop limitado premium, composición vertical de ecommerce editorial, alta nitidez, sombras suaves.",
         "Negativos: modelo, maniquí visible, rayas torcidas, texto mal escrito, logos reales, prenda deformada, baja calidad."),
        ("PROMPT 9 — Ficha técnica de diseño",
         "Ficha técnica editorial tipo tech pack para polo tejido oversized de manga corta con cuello, rayas azul denim y beige, ilustración frontal centrada de la prenda, medidas dibujadas con flechas, anotaciones de diseño, detalles de cuello, botones, rib en mangas y bajo, textura knit, etiquetas pequeñas, muestras de color azul denim y beige, notas de fabricación, layout blanco limpio con garabatos técnicos negros, estética diseñador streetwear premium, presentación de colección, imagen cuadrada para Instagram.",
         "Negativos: texto ilegible excesivo, logos reales, medidas con fusa, diseño sucios, prenda deformada, baja calidad."),
        ("PROMPT 10 — Producto sostenido por manos fondo oscuro",
         "Fotografía editorial dramática de producto, polo tejido oversized de manga corta con cuello, rayas azul denim y beige, sostenido horizontalmente por dos manos desde los extremos de los hombros o mangas, solo brazos visibles entrando desde los lados, fondo azul marino oscuro casi negro, iluminación dura lateral con contraste elegante, sombras profundas, textura knit muy visible, prenda protagonista flotando en el centro, estética campaña premium streetwear, sensación de drop exclusivo.",
         "Negativos: manos deformes, demasiados brazos, logos reales, texto mal escrito, prenda arrugada en exceso, rayas deformadas, fondo caótico, baja calidad.")
    ]

    grid_prompts_html = """
    <div class="prompts-grid-2col">
    """
    for title, prompt, neg in prompts_1_10:
        grid_prompts_html += f"""
      <div class="prompt-container" style="margin: 0;">
        <div class="prompt-header">
          <span class="prompt-label">{title.upper()}</span>
          <button class="copy-btn" type="button">
            <svg style="width: 12px; height: 12px; fill: currentColor;" viewBox="0 0 24 24">
              <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
            </svg>
            Copiar
          </button>
        </div>
        <pre class="prompt-text">{prompt}\n\n{neg}</pre>
      </div>
        """
    grid_prompts_html += """
    </div>
    """
    html_content.append(grid_prompts_html)

    # Section 05: Paso 2 ADN Editorial
    html_content.append("""
        </section>

        <!-- Sección 05: Paso 2 -->
        <section id="paso-2">
          <div class="section-meta">[ PASO 02 / LA IDENTIDAD VISUAL ]</div>
          <h2 class="section-title">PASO 2: ADN EDITORIAL</h2>
          <div class="text-editorial">
            <p>Antes de abrir la IA, debes decidir cómo quieres que se vea tu marca, qué sensación debe transmitir tu prenda y qué tipo de cliente quieres atraer. No es escribir prompts al azar.</p>
            <p>En nuestro caso, el ADN Editorial del polo sería algo así:</p>
            
            <div class="grid-editorial">
              <div class="editorial-card">
                <h4 style="color: var(--red); font-family: 'Bebas Neue', sans-serif; font-size: 1.5rem; margin-bottom: 0.5rem;">COLORES PRINCIPALES</h4>
                <p class="editorial-card-body">Azul denim, beige, blanco cálido, gris claro, crema.</p>
              </div>
              <div class="editorial-card">
                <h4 style="color: var(--red); font-family: 'Bebas Neue', sans-serif; font-size: 1.5rem; margin-bottom: 0.5rem;">ESTÉTICA & MOOD</h4>
                <p class="editorial-card-body">Rugby club vintage, streetwear premium, lookbook editorial. Sensación cómoda, costosa y relajada.</p>
              </div>
              <div class="editorial-card">
                <h4 style="color: var(--red); font-family: 'Bebas Neue', sans-serif; font-size: 1.5rem; margin-bottom: 0.5rem;">AMBIENTES</h4>
                <p class="editorial-card-body">Estudio beige, fondo blanco, cafetería minimalista, calle limpia, garaje premium, arquitectura moderna.</p>
              </div>
              <div class="editorial-card">
                <h4 style="color: var(--red); font-family: 'Bebas Neue', sans-serif; font-size: 1.5rem; margin-bottom: 0.5rem;">MODELOS</h4>
                <p class="editorial-card-body">Hombres y mujeres jóvenes, estilo natural, actitud seria o tranquila, nada exagerado ni artificial.</p>
              </div>
            </div>

            <h3 style="font-family: 'Anton', sans-serif; font-size: 2rem; margin: 3rem 0 1.5rem;">PLANTILLA PARA QUE EL ALUMNO CREATE SU ADN EDITORIAL</h3>
            <p>Para ayudarte a definir tu propia dirección visual, completa esta plantilla antes de generar:</p>
            
            <div style="background-color: var(--black-2); color: var(--paper-warm); padding: 2rem; border: var(--border-brutal); margin-bottom: 3rem;">
              <ul style="list-style: none; display: flex; flex-direction: column; gap: 1rem; font-family: 'Space Mono', monospace; font-size: 0.92rem;">
                <li><span style="color: var(--red);">[ MI PRODUCTO ES ]</span>: ______________ (Ej: polo tejido oversized azul denim y beige)</li>
                <li><span style="color: var(--red);">[ MI PRENDA SE DEBE SENTIR COMO ]</span>: ______________ (Ej: premium, relajada, vintage, urbana)</li>
                <li><span style="color: var(--red);">[ MI CLIENTE IDEAL ES ]</span>: ______________ (Ej: joven que quiere verse bien sin usar ropa llamativa)</li>
                <li><span style="color: var(--red);">[ MI CAMPAÑA DEBE PARECER ]</span>: ______________ (Ej: una colección streetwear premium inspirada en rugby)</li>
                <li><span style="color: var(--red);">[ MIS COLORES PRINCIPALES SON ]</span>: ______________</li>
                <li><span style="color: var(--red);">[ MIS FONDOS IDEALES SON ]</span>: ______________</li>
                <li><span style="color: var(--red);">[ LA PRENDA NUNCA DEBE PERDER ]</span>: ______________ (Ej: rayas, cuello polo beige, textura knit)</li>
              </ul>
            </div>

            <p><strong>PROMPT PARA CREAR EL ADN EDITORIAL CON CHATGPT:</strong></p>
            <p>Puedes copiar y pegar este prompt en ChatGPT para automatizar el análisis creativo:</p>
            
            <div class="prompt-container">
              <div class="prompt-header">
                <span class="prompt-label">PROMPT ADN EDITORIAL</span>
                <button class="copy-btn" type="button">
                  <svg style="width: 12px; height: 12px; fill: currentColor;" viewBox="0 0 24 24">
                    <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
                  </svg>
                  Copiar Prompt
                </button>
              </div>
              <pre class="prompt-text">Actúa como director creativo de moda. Voy a crear una campaña visual con IA para esta prenda: [describe la prenda o adjunta la imagen]. Necesito que me construyas el ADN Editorial de la campaña. Quiero que definas:\n1. Estética visual principal.\n2. Tipo de cliente que debe atraer.\n3. Sensación que debe transmitir.\n4. Tipo de modelos ideales.\n5. Fondos y locaciones recomendadas.\n6. Paleta de colores.\n7. Tipo de iluminación.\n8. Poses recomendadas.\n9. Reglas para mantener la prenda consistente.\n10. Errores que debo evitar al generar imágenes con IA.\nHazlo de manera clara, directa y aplicable a una campaña de moda.</pre>
            </div>
          </div>
        </section>

        <!-- Sección 06: Paso 3 Producción IA -->
        <section id="paso-3" style="background-color: var(--paper);">
          <div class="section-meta">[ PASO 03 / LA GENERACIÓN DE CAMPAÑA ]</div>
          <h2 class="section-title">PASO 3: PRODUCCIÓN IA SIN ESTUDIO</h2>
          <div class="text-editorial">
            <p>Aquí es donde la idea se convierte en imagen. Aprenderás el proceso exacto para generar, revisar, corregir e iterar hasta tener un banco visual completo.</p>
            
            <p><strong>PROMPT BASE DE CONSISTENCIA DE PRENDA:</strong></p>
            <p>Este prompt debe ir al inicio de casi todas tus generaciones para evitar que la IA desvíe o deforme tu producto:</p>
            
            <div class="prompt-container">
              <div class="prompt-header">
                <span class="prompt-label">PROMPT BASE DE CONSISTENCIA</span>
                <button class="copy-btn" type="button">
                  <svg style="width: 12px; height: 12px; fill: currentColor;" viewBox="0 0 24 24">
                    <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
                  </svg>
                  Copiar Prompt
                </button>
              </div>
              <pre class="prompt-text">Usar como referencia exacta un polo tejido oversized de manga corta, cuello polo beige, botones frontales oscuros, rayas horizontales azul denim y beige, textura knit gruesa, manga amplia, fit boxy corto y estética rugby club vintage. Mantener colores, proporciones, cuello, rayas, textura, caída y estructura de la prenda. No cambiar el diseño del producto.</pre>
            </div>

            <hr style="border: 0; border-top: 2px dashed var(--gray-metal); margin: 3rem 0;">

            <h3 id="manera-rapida" style="font-family: 'Anton', sans-serif; font-size: 2.2rem; margin-bottom: 1.5rem; text-transform: uppercase;">
              MANERA RÁPIDA: COPIAR Y PEGAR EN LOTE
            </h3>
            <p>Esta manera es perfecta para crear volumen rápido. Subimos las fotos de referencia del producto en Google Flow, presionamos <strong>@</strong> para añadirlas a la instrucción, y luego pegamos el bloque de prompts generado por ChatGPT.</p>
    """)

    # Manera rápida screenshots (image1.png, image57.png, image74.png, image45.png, image47.png)
    html_content.append(make_full_size_image("image1.png", "Abrir proyecto en Google Flow"))
    html_content.append(make_full_size_image("image57.png", "Menú de variables @ en barra de prompts"))
    html_content.append(make_full_size_image("image74.png", "Añadir imágenes de referencia al proyecto"))
    html_content.append(make_full_size_image("image45.png", "Pegar la lista de prompts en lote"))
    html_content.append(make_full_size_image("image47.png", "Generando imágenes en paralelo"))

    html_content.append("""
            <p><strong>RESULTADOS DE LA CAMPAÑA RÁPIDA:</strong></p>
    """)

    # Fast results (image78.png, image63.png)
    html_content.append(make_two_col_images("image78.png", "image63.png", "Resultado Rápido 01", "Resultado Rápido 02"))

    html_content.append("""
            <hr style="border: 0; border-top: 2px dashed var(--gray-metal); margin: 3rem 0;">

            <h3 id="manera-lenta" style="font-family: 'Anton', sans-serif; font-size: 2.2rem; margin-bottom: 1.5rem; text-transform: uppercase;">
              MANERA LENTA: SOLUCIÓN DE ERRORES E ITERACIÓN
            </h3>
            <p>La IA no es perfecta y a veces genera errores como distorsionar las rayas o deformar mangas.</p>
    """)

    # IA error (image61.png)
    html_content.append(make_full_size_image("image61.png", "Ejemplo de error o inconsistencia generado por IA"))

    html_content.append("""
            <p>Para solucionarlo, utilizamos la **Manera Lenta**: nos paramos encima de la foto, presionamos el botón de <strong>Reutilizar Prompt</strong>, deseleccionamos el modo agente, seleccionamos el formato y la cantidad de fotos a generar (<strong>x4</strong>) para tener más opciones de variantes, e iniciamos la iteración.</p>
    """)

    # Troubleshooting screenshots (image37, image58, image39, image15, image18, image60)
    html_content.append(make_full_size_image("image37.png", "Presionar botón de reutilización de prompt"))
    html_content.append(make_full_size_image("image58.png", "Ajustar texto del prompt base reutilizado"))
    html_content.append(make_full_size_image("image39.png", "Desactivar modo Agente para control manual"))
    html_content.append(make_full_size_image("image15.png", "Seleccionar formato 4:5 y cantidad x4 de fotos"))
    html_content.append(make_full_size_image("image18.png", "Hacer clic en generar variante"))
    html_content.append(make_full_size_image("image60.png", "Resultado con las 4 variantes de iteración"))

    html_content.append("""
            <p>Si aún así no mantiene la consistencia de forma soñada, copiamos el prompt y le decimos a ChatGPT qué está fallando para que nos devuelva una versión optimizada.</p>
    """)

    # Additional troubleshooting (image29, image53, and errors image10, image21, image43, image20, image6)
    html_content.append(make_two_col_images("image29.png", "image53.png", "Variante iterada exitosa 01", "Variante iterada exitosa 02"))
    
    html_content.append("""
            <p><strong>MUESTRAS COMPLEMENTARIAS DE ESTUDIO (RESULTADOS CORRECTOS):</strong></p>
    """)
    # Note: the user explicitly pointed out that image21, 43, 20, 6 are not errors nor variant corrections, they are successful consistency studies.
    # So we label them simply as general successful outputs.
    html_content.append(make_full_size_image("image10.png", "Estudio de Prenda con fondo lila"))
    html_content.append(make_two_col_images("image21.png", "image43.png", "Muestra de Consistencia A", "Muestra de Consistencia B"))
    html_content.append(make_two_col_images("image20.png", "image6.png", "Muestra de Consistencia C", "Muestra de Consistencia D"))

    # Individualized prompt-to-image tab layouts for the 30 prompts
    # 1:1 Prompt Sheet design
    tabs_html = """
            <hr style="border: 0; border-top: 2px dashed var(--gray-metal); margin: 4rem 0;">

            <h3 id="campana-30-prompts-inner" style="font-family: 'Anton', sans-serif; font-size: 2.5rem; margin-bottom: 1.5rem; text-transform: uppercase;">
              CAMPAÑA AMPLIADA: 30 PROMPTS AVANZADOS
            </h3>
            <p style="margin-bottom: 2rem;">Navega a través de las pestañas a continuación para ver las fichas creativas de los prompts y sus imágenes correspondientes en proporción 1:1.</p>

            <div class="prompts-tab-system">
              <div class="tabs-nav">
                <button class="tab-trigger active" data-target="tab-animales">01. Animales & Humanos</button>
                <button class="tab-trigger" data-target="tab-blancos">02. Fondos Blancos</button>
                <button class="tab-trigger" data-target="tab-carros">03. Carros Lujosos</button>
                <button class="tab-trigger" data-target="tab-web">04. Editorial Web</button>
                <button class="tab-trigger" data-target="tab-instagram">05. Instagram / Redes</button>
                <button class="tab-trigger" data-target="tab-anuncios">06. Anuncios & Venta</button>
              </div>

              <!-- Tab Animales -->
              <div class="tab-content-panel active" id="tab-animales">
                <div class="prompt-list-layout">
                  
                  <!-- Prompt 1 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>1. Caballo editorial luxury club</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Modelo masculino joven usando polo tejido oversized de rayas azul denim y beige, cuello polo beige, botones frontales, textura knit gruesa, fit boxy premium, parado junto a un caballo marrón elegante en una finca minimalista, actitud serena, pantalón beige amplio, luz dorada de tarde, estética rugby club aristocrático, composición editorial vertical, lujo casual, alta calidad.\nNegativos: logos reales, texto mal escrito, manos deformes, animal deformado, prenda distorsionada.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image44.png" alt="Caballo editorial" />
                    </div>
                  </div>

                  <!-- Prompt 2 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>2. Perro grande urbano premium</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Modelo masculino usando el polo tejido oversized rayado azul denim y beige, caminando con un perro grande tipo dóberman o labrador negro en una calle limpia de ciudad, actitud segura, jeans claros, sneakers blancos, luz natural suave, estética streetwear premium, encuadre cuerpo completo, campaña de moda urbana.\nNegativos: correas deformes, manos raras, prenda distorsionada, logos reales.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image28.png" alt="Perro urbano" />
                    </div>
                  </div>

                  <!-- Prompt 3 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>3. Gato editorial interior</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Modelo femenino usando el polo oversized como prenda principal, rayas azul denim y beige, textura knit visible, sentada en sofá minimalista beige con un gato elegante al lado, expresión calmada, luz de ventana, estética quiet luxury, lifestyle premium, formato vertical para campaña.\nNegativos: animal deformado, piel artificial, rayas torcidas, baja calidad.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image73.png" alt="Gato interior" />
                    </div>
                  </div>

                  <!-- Prompt 4 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>4. Caballo blanco en exterior</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Modelo masculino usando el polo tejido rayado azul denim y beige, parado de perfil junto a caballo blanco, fondo campestre limpio, pantalón crema, accesorios mínimos, luz suave de mañana, estética club ecuestre moderno, editorial de moda premium.\nNegativos: logos reales, anatomía deformada, texto ilegible, prenda mal formada.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image25.png" alt="Caballo blanco" />
                    </div>
                  </div>

                  <!-- Prompt 5 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>5. Pareja con perro en estudio</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Pareja joven usando styling coordinado, uno viste el polo tejido oversized rayado azul denim y beige, el otro lleva jeans y camiseta blanca, perro grande sentado entre ambos, fondo gris claro de estudio, poses relajadas, luz suave, estética campaña lifestyle streetwear premium.\nNegativos: manos deformes, animal extraño, exceso de filtros, fondo caótico.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image71.png" alt="Pareja perro" />
                    </div>
                  </div>
                  
                  <h4>Resultados Complementarios</h4>
                  <div class="image-layout-two-col">
                    <div class="full-size-image-container">
                      <div class="image-label-bar">[Campana Muestra 01]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image16.png" />
                    </div>
                    <div class="full-size-image-container">
                      <div class="image-label-bar">[Campana Muestra 02]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image40.png" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Tab Blancos -->
              <div class="tab-content-panel" id="tab-blancos">
                <div class="prompt-list-layout">
                  <!-- Prompt 6 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>6. Producto frontal limpio</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Fotografía ecommerce premium del polo tejido oversized manga corta, rayas horizontales azul denim y beige, cuello polo beige, botones frontales, textura knit gruesa, fit boxy corto, prenda centrada sobre fondo blanco puro, vista frontal plana, sombra suave, alta nitidez, catálogo profesional.\nNegativos: maniquí visible, arrugas excesivas, rayas torcidas, logos reales.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image38.png" alt="Frontal Blanco" />
                    </div>
                  </div>

                  <!-- Prompt 7 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>7. Producto espalda limpio</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Fotografía ecommerce premium vista trasera del polo tejido oversized, rayas azul denim y beige perfectamente alineadas, cuello beige, manga amplia, fit boxy, fondo blanco puro, iluminación uniforme, sombra ligera, imagen comercial de tienda online.\nNegativos: texto mal escrito, prenda deformada, manchas, baja calidad.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image36.png" alt="Espalda Blanco" />
                    </div>
                  </div>

                  <!-- Prompt 8 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>8. Modelo frontal fondo blanco</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Modelo masculino joven usando el polo tejido oversized rayado azul denim y beige, parado frontal mirando a cámara, jeans oscuros amplios, mano en bolsillo, expresión neutra, fondo blanco limpio, luz de estudio suave, lookbook premium, encuadre desde muslos.\nNegativos: manos deformes, rayas irregulares, logos reales.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image72.png" alt="Modelo Frontal" />
                    </div>
                  </div>

                  <!-- Prompt 9 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>9. Modelo femenino fondo blanco</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Modelo femenina usando el polo oversized rayado azul denim y beige como prenda protagonista, jeans claros tiro bajo, cabello natural, pose relajada, fondo blanco puro, luz suave editorial, estética unisex premium, imagen limpia para catálogo.\nNegativos: cuerpo deformado, prenda ajustada, texto ilegible, baja calidad.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image46.png" alt="Modelo Femenino" />
                    </div>
                  </div>

                  <!-- Prompt 10 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>10. Detalle textura fondo blanco</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Macro fotografía editorial del polo tejido, enfoque en cuello beige, botones frontales, textura knit gruesa, rayas azul denim y beige, bordados frontales elegantes, fondo blanco, luz suave lateral, imagen de detalle para ecommerce premium.\nNegativos: texto mal escrito, costuras falsas, baja nitidez.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image26.png" alt="Textura Zoom" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Tab Carros -->
              <div class="tab-content-panel" id="tab-carros">
                <div class="prompt-list-layout">
                  <!-- Prompt 11 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>11. Carro negro nocturno</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Modelo masculino usando polo tejido oversized rayado azul denim y beige, apoyado junto a carro lujoso negro sin logos visibles, calle nocturna elegante, luz de faros suave, jeans oscuros, actitud seria, estética street luxury, composición vertical, campaña premium.\nNegativos: logos de auto visibles, manos deformes, prenda distorsionada.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image51.png" alt="Auto Negro" />
                    </div>
                  </div>

                  <!-- Prompt 12 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>12. Convertible claro lifestyle</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Modelo femenino usando polo oversized rayado azul denim y beige, sentada en asiento de carro convertible beige sin logos visibles, gafas oscuras, jeans claros, luz de atardecer, estética resort luxury streetwear, encuadre medio, campaña aspiracional.\nNegativos: logos reales, volante deformado, texto mal escrito.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image30.png" alt="Convertible" />
                    </div>
                  </div>

                  <!-- Prompt 13 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>13. SUV lujo urbano</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Modelo masculino usando el polo tejido oversized, parado frente a SUV lujosa gris sin emblemas visibles, fondo arquitectura moderna, pantalón beige amplio, sneakers blancos, luz de mañana, estética urban club premium, foto vertical para redes.\nNegativos: marcas de carro, manos deformes, reflejos raros.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image75.png" alt="SUV" />
                    </div>
                  </div>

                  <!-- Prompt 14 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>14. Garaje premium</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Modelo joven usando polo rayado azul denim y beige, caminando en garaje minimalista con carro deportivo plateado sin logos visibles al fondo, iluminación cinematográfica, sombra elegante, pose natural, fit boxy visible, editorial streetwear de lujo.\nNegativos: logos reales, carro deformado, prenda torcida.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image59.png" alt="Garaje" />
                    </div>
                  </div>

                  <!-- Prompt 15 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>15. Detalle producto con carro</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Plano medio del polo tejido oversized rayado azul denim y beige, modelo sentado en capó de carro clásico crema sin logos visibles, manos relajadas, cuello y textura visibles, luz cálida, estética vintage club, campaña de lanzamiento.\nNegativos: rayas deformes, manos raras, texto ilegible.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image9.png" alt="Capó" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Tab Web -->
              <div class="tab-content-panel" id="tab-web">
                <div class="prompt-list-layout">
                  <!-- Prompt 16 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>16. Hero banner web</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Imagen editorial horizontal 16:9 para portada web, modelo masculino joven usando EXACTAMENTE el polo tejido oversized de referencia: rayas horizontales azul denim y beige, cuello polo beige, cuatro botones frontales oscuros, manga corta amplia, fit boxy corto, textura knit gruesa, logos bordados en pecho superior y lettering grande “Cartier” al frente, mantener la prenda frontal perfectamente visible y fiel. Modelo de pie en estudio beige cálido, mirada fuera de cámara, pose relajada, pantalón crema amplio, composición con espacio negativo elegante a la derecha para titulares, luz suave premium, estética rugby club vintage luxury, alta nitidez, campaña web de moda.\nNegativos: cambiar diseño del polo, borrar lettering frontal, rayas incorrectas, logos inventados diferentes, prenda deformada, cuello incorrecto, botones ausentes, baja calidad.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image62.png" alt="Web Banner" />
                    </div>
                  </div>

                  <!-- Prompt 17 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>17. Banner pareja web</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Imagen horizontal 16:9 para banner web, pareja joven con styling denim y beige, el modelo principal usando EXACTAMENTE el polo tejido oversized de referencia en vista frontal completa, rayas azul denim y beige, cuello beige, botones frontales, textura knit, lettering grande “Cartier” visible al frente, logos superiores y etiqueta inferior visibles. La segunda persona viste jeans claros y top básico crema, ambos en estudio gris cálido, pose cercana pero elegante, composición limpia con espacio lateral para copy, luz editorial suave, estética unisex premium club vintage.\nNegativos: ocultar frente del polo, cambiar colores, texto mal escrito, rayas torcidas, manos deformes, logos reales de otras marcas.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image70.png" alt="Pareja Web" />
                    </div>
                  </div>

                  <!-- Prompt 18 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>18. Editorial detalle web</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Fotografía horizontal macro editorial para sección web de calidad, primer plano del polo tejido de referencia sobre mesa crema, enfoque en cuello polo beige, cuatro botones oscuros, rayas azul denim y beige, textura knit gruesa, bordados superiores y lettering “Cartier” parcialmente visible pero limpio, manos acomodando suavemente el cuello y el pecho de la prenda, luz lateral suave, sombras premium, estética artesanal luxury streetwear.\nNegativos: texto deformado, botones incorrectos, manos deformes, textura plástica, cambiar rayas, baja nitidez.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image52.png" alt="Detalle Web" />
                    </div>
                  </div>

                  <!-- Prompt 19 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>19. Lookbook web full body</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Imagen horizontal lookbook web, modelo masculino full body usando EXACTAMENTE el polo tejido oversized de referencia, frente completamente visible, lettering grande “Cartier” claro, rayas azul denim y beige, cuello beige, botones frontales, manga amplia, fit boxy. Pantalón crema ancho, sneakers blancos, fondo beige minimalista, modelo caminando lentamente hacia cámara, actitud seria y segura, luz de estudio suave, estética club heritage moderno, fotografía premium para ecommerce editorial.\nNegativos: prenda ajustada, ocultar diseño frontal, cambiar lettering, rayas desalineadas, proporciones raras, logos de otras marcas.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image66.png" alt="Lookbook Web" />
                    </div>
                  </div>

                  <!-- Prompt 20 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>20. Portada colección web</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Fotografía editorial horizontal 16:9 para portada de colección, tres modelos diversos en styling premium azul denim, beige y blanco; modelo central usando EXACTAMENTE el polo tejido oversized de referencia en vista frontal, lettering “Cartier” visible, cuello beige, botones, rayas horizontales azul denim y beige, textura knit gruesa. Los modelos laterales usan prendas neutras que no compiten, fondo blanco cálido, actitud segura, composición limpia con espacio superior para título web, estética rugby club vintage premium.\nNegativos: tapar el polo, cambiar diseño frontal, texto defectuoso, logos de marcas externas, manos deformes, fondo saturado.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image13.png" alt="Colección Web" />
                    </div>
                  </div>
                  
                  <h4>Resultados Complementarios</h4>
                  <div class="image-layout-two-col">
                    <div class="full-size-image-container">
                      <div class="image-label-bar">[Campana Muestra 01]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image2.png" />
                    </div>
                    <div class="full-size-image-container">
                      <div class="image-label-bar">[Campana Muestra 02]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image31.png" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Tab Instagram -->
              <div class="tab-content-panel" id="tab-instagram">
                <div class="prompt-list-layout">
                  <!-- Prompt 21 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>21. Reel cover vertical</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Foto vertical 9:16 para portada de reel, modelo masculino joven caminando hacia cámara usando EXACTAMENTE el polo tejido oversized de referencia, frente totalmente visible, rayas azul denim y beige, cuello beige, cuatro botones, lettering grande “Cartier”, logos bordados superiores, textura knit realista, fit boxy. Jeans claros anchos, sneakers blancos, calle limpia con arquitectura minimalista, luz natural suave, actitud segura, espacio superior para frase corta, estética streetwear premium aspiracional.\nNegativos: texto mal escrito en la prenda, cambiar colores, tapar el frente, manos deformes, movimiento borroso, baja calidad.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image49.png" alt="Instagram vertical" />
                    </div>
                  </div>

                  <!-- Prompt 22 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>22. Story espejo editorial</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Story vertical 9:16 estilo espejo premium, modelo masculino usando EXACTAMENTE el polo tejido oversized de referencia, parte frontal visible en el reflejo, lettering “Cartier” claro, rayas azul denim y beige, cuello beige, botones, textura knit gruesa. Habitación minimalista beige, celular sin logo visible, pose casual segura, flash suave controlado, estética real pero editorial, jeans oscuros, composición limpia para story de marca.\nNegativos: celular deformado, tapar el logo frontal, texto ilegible, rayas torcidas, cuarto desordenado, piel artificial.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image19.png" alt="Espejo Story" />
                    </div>
                  </div>

                  <!-- Prompt 23 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>23. Carrusel slide producto</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Imagen vertical 4:5 para carrusel Instagram, polo tejido oversized de referencia colgado en percha de madera premium, vista frontal exacta, rayas horizontales azul denim y beige, cuello polo beige, cuatro botones, lettering grande “Cartier”, logos bordados superiores, etiqueta inferior visible, textura knit gruesa, fondo crema cálido, luz suave lateral, sombra elegante, estética drop premium.\nNegativos: cambiar lettering, borrar logos, rayas mal alineadas, arrugas excesivas, percha barata, baja resolución.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image68.png" alt="Carrusel Producto" />
                    </div>
                  </div>

                  <!-- Prompt 24 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>24. Lifestyle calle premium</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Foto vertical 4:5, modelo masculino sentado en escalones de concreto limpio usando EXACTAMENTE el polo tejido oversized de referencia, frente visible, lettering “Cartier” completo, rayas azul denim y beige, cuello beige, botones frontales, manga amplia, fit boxy. Jeans claros anchos, gafas oscuras, sneakers blancos, luz dorada de tarde, actitud relajada, estética urbana premium club vintage, composición aspiracional para Instagram.\nNegativos: fondo caótico, tapar el frente del polo, texto deformado, manos deformes, prenda distorsionada.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image42.png" alt="Calle Lifestyle" />
                    </div>
                  </div>

                  <!-- Prompt 25 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>25. UGC premium cafetería</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Foto vertical 4:5 estilo contenido orgánico premium, modelo joven usando EXACTAMENTE el polo tejido oversized de referencia sentado en cafetería minimalista, frente del polo visible, lettering “Cartier” claro, rayas azul denim y beige, cuello beige, botones y textura knit realista. Café en mano, jeans oscuros, luz natural de ventana, ambiente beige y madera, estética aspiracional cercana pero de marca premium.\nNegativos: logos de cafetería, tapar lettering, texto mal escrito, manos deformes, fondo sucio, baja calidad.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image14.png" alt="Cafetería UGC" />
                    </div>
                  </div>
                  
                  <h4>Resultados Complementarios</h4>
                  <div class="full-size-image-container">
                    <div class="image-label-bar">[Campana Muestra Extra]</div>
                    <img class="full-size-img" src="/media/de_prenda_a_campana/image17.png" />
                  </div>
                </div>
              </div>

              <!-- Tab Anuncios -->
              <div class="tab-content-panel" id="tab-anuncios">
                <div class="prompt-list-layout">
                  <!-- Prompt 26 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>26. Anuncio precio limpio</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Anuncio publicitario vertical 4:5 premium, modelo masculino frontal usando EXACTAMENTE el polo tejido oversized de referencia, frente perfectamente visible, lettering grande “Cartier”, rayas azul denim y beige, cuello beige, cuatro botones, textura knit gruesa, fit boxy. Fondo blanco cálido, luz suave de estudio, composición limpia. Generar texto elegante integrado en la imagen con tipografía serif premium y sans minimalista: “POLO TEJIDO OVERSIZED” arriba, “$79.900” grande y elegante abajo, “DROP LIMITADO” pequeño. Estética luxury streetwear accesible.\nNegativos: texto mal escrito, precio incorrecto, cambiar prenda, logos de otras marcas, manos deformes, baja calidad.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image23.png" alt="Ads 4:5" />
                    </div>
                  </div>

                  <!-- Prompt 27 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>27. Anuncio urgencia drop</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Imagen publicitaria vertical 9:16 estilo drop limitado, modelo usando EXACTAMENTE el polo tejido oversized de referencia, frente visible y protagonista, lettering “Cartier”, rayas azul denim y beige, cuello beige, botones, textura knit. Fondo gris oscuro premium, luz dramática lateral, mirada seria. Generar texto elegante en la imagen: “NUEVO DROP” en serif fina, “POLO TEJIDO” en mayúsculas, “$79.900” destacado, “UNIDADES LIMITADAS” pequeño. Composición de anuncio streetwear premium.\nNegativos: precio mal escrito, texto torcido, ocultar frente del polo, rayas incorrectas, logos externos.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image27.png" alt="Ads vertical 9:16" />
                    </div>
                  </div>

                  <!-- Prompt 28 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>28. Anuncio ecommerce conversion</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Anuncio cuadrado 1:1 para ecommerce, producto frontal del polo tejido oversized de referencia sobre fondo blanco puro, vista frontal exacta, rayas azul denim y beige, cuello beige, cuatro botones, logos superiores, lettering grande “Cartier”, etiqueta inferior visible, textura knit nítida, sombra suave. Generar texto comercial elegante alrededor sin tapar la prenda: “POLO TEJIDO OVERSIZED”, “TEXTURA PREMIUM”, “$79.900”, “COMPRA HOY”. Tipografía limpia, premium, legible, azul marino y beige.\nNegativos: tapar producto, texto mal escrito, precio incorrecto, maniquí visible, rayas torcidas, baja calidad.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image56.png" alt="Ad ecommerce 1:1" />
                    </div>
                  </div>

                  <!-- Prompt 29 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>29. Anuncio lifestyle precio valor</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Anuncio vertical 4:5 lifestyle premium, modelo masculino caminando en zona urbana elegante usando EXACTAMENTE el polo tejido oversized de referencia, frente visible, lettering “Cartier” claro, rayas azul denim y beige, cuello beige, botones, manga amplia, fit boxy. Pantalón beige, sneakers blancos, luz de atardecer, estética prenda costosa a precio alcanzable. Generar texto elegante en la imagen: “ESTILO PREMIUM” arriba, “POLO TEJIDO OVERSIZED” medio lateral, “$79.900” grande, “DISPONIBLE AHORA” pequeño.\nNegativos: texto ilegible, ocultar diseño frontal, logos de marcas reales, manos deformes, fondo caótico.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image8.png" alt="Ad lifestyle" />
                    </div>
                  </div>

                  <!-- Prompt 30 -->
                  <div class="prompt-card-individual">
                    <div>
                      <h4>30. Anuncio WhatsApp ventas</h4>
                      <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                        <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                          <span class="prompt-label">PROMPT</span>
                          <button class="copy-btn" type="button">Copiar</button>
                        </div>
                        <pre class="prompt-text" style="color: var(--black); max-height: none;">Imagen cuadrada 1:1 para WhatsApp e Instagram ads, polo tejido oversized de referencia doblado parcialmente pero con parte frontal visible: rayas azul denim y beige, cuello beige, botones, textura knit y lettering “Cartier” reconocible. Fondo crema con luz cálida, composición premium, etiqueta minimalista sin marca externa. Generar texto elegante dentro de la imagen: “POLO TEJIDO OVERSIZED”, “$79.900”, “PIDE EL TUYO POR WHATSAPP”, “TALLAS DISPONIBLES”. Tipografía serif elegante combinada con sans minimalista, color azul marino.\nNegativos: precio incorrecto, texto mal escrito, tapar prenda, logos externos, baja resolución.</pre>
                      </div>
                    </div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[Resultado 1:1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image41.png" alt="WhatsApp Ad" />
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <p><strong>PROCESO DE ITERACIÓN CONSTANTE:</strong></p>
            <p>No sale perfecto a la primera, por eso iteramos y refinamos constantemente con el Agente.</p>
    """
    
    tabs_html += make_full_size_image("image33.png", "Proceso de iteración y re-generación constante")
    
    # We append Paso 3 other text paragraphs: volume generation, troubleshooting, quality check.
    # Styled visually with clean brutalist components, process lists, checklists, copyable examples.
    step3_body = """
            <!-- 3.4.1 Workflow de Proceso Rápido -->
            <div class="brutalist-block" style="margin: 3.5rem 0; padding: 2.5rem; background-color: var(--paper-warm); border: var(--border-brutal); box-shadow: var(--shadow-brutal-red);">
              <h4 style="font-family: 'Archivo Black', 'Anton', sans-serif; font-size: 1.8rem; margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: -0.06em;">EL PROCESO DE GENERACIÓN EN LOTE:</h4>
              <div class="grid-editorial" style="margin-top: 1.5rem;">
                <div class="editorial-card" style="background-color: #fff; border: var(--border-brutal-thin); padding: 1.5rem;">
                  <span class="card-num-box" style="font-family: 'Space Mono', monospace; font-weight: bold; color: var(--red); font-size: 1.2rem; border-bottom: 2px solid var(--black); display: inline-block; margin-bottom: 0.8rem; padding-bottom: 0.2rem;">01 / REFERENCIAS</span>
                  <p>Subes las imágenes de referencia del producto real (frente y espalda).</p>
                </div>
                <div class="editorial-card" style="background-color: #fff; border: var(--border-brutal-thin); padding: 1.5rem;">
                  <span class="card-num-box" style="font-family: 'Space Mono', monospace; font-weight: bold; color: var(--red); font-size: 1.2rem; border-bottom: 2px solid var(--black); display: inline-block; margin-bottom: 0.8rem; padding-bottom: 0.2rem;">02 / AGENTE IA</span>
                  <p>Activas el modo agente o el sistema de referencias de marca en Google Flow.</p>
                </div>
                <div class="editorial-card" style="background-color: #fff; border: var(--border-brutal-thin); padding: 1.5rem;">
                  <span class="card-num-box" style="font-family: 'Space Mono', monospace; font-weight: bold; color: var(--red); font-size: 1.2rem; border-bottom: 2px solid var(--black); display: inline-block; margin-bottom: 0.8rem; padding-bottom: 0.2rem;">03 / LOTES</span>
                  <p>Pegas el bloque de prompts de campaña y generas varias imágenes en paralelo.</p>
                </div>
              </div>
              <p style="margin-top: 2rem; font-weight: 900; font-size: 1.15rem; text-transform: uppercase; color: var(--red); letter-spacing: -0.02em;">
                Esta manera es perfecta para crear volumen rápido.
              </p>
              
              <div style="background-color: var(--black); color: var(--paper-warm); padding: 1.8rem; margin-top: 1.8rem; border: var(--border-brutal-thin);">
                <p style="font-family: 'Space Mono', monospace; font-size: 0.8rem; margin-bottom: 1.2rem; color: var(--red); font-weight: bold;">[ DISTRIBUCIÓN RECOMENDADA DE GENERACIÓN DE CAMPAÑA ]</p>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; font-family: 'Bebas Neue', sans-serif; font-size: 1.6rem;">
                  <div style="border-bottom: 1px dashed var(--gray-metal); padding-bottom: 0.5rem;">5 FOTOS DE PRODUCTO LIMPIO (CATÁLOGO)</div>
                  <div style="border-bottom: 1px dashed var(--gray-metal); padding-bottom: 0.5rem;">5 FOTOS CON MODELO EN ESTUDIO</div>
                  <div style="border-bottom: 1px dashed var(--gray-metal); padding-bottom: 0.5rem;">5 FOTOS LIFESTYLE (CON MASCOTAS / PAREJA)</div>
                  <div style="border-bottom: 1px dashed var(--gray-metal); padding-bottom: 0.5rem;">5 FOTOS HORIZONTALES PARA BANNER WEB</div>
                  <div style="border-bottom: 1px dashed var(--gray-metal); padding-bottom: 0.5rem;">5 FOTOS EDITORIALES PARA REDES</div>
                  <div style="padding-bottom: 0.5rem;">5 FOTOS ENFOCADAS EN ANUNCIOS Y VENTA</div>
                </div>
              </div>
              
              <p style="margin-top: 1.5rem; font-style: italic; font-size: 0.95rem;">
                Así, en vez de quedarte pensando imagen por imagen, produces una campaña completa y después seleccionas las mejores fotos.
              </p>
            </div>

            <!-- 3.5. Producción lenta: corregir lo que no salió bien -->
            <div id="produccion-lenta-seccion" style="margin: 4.5rem 0;">
              <h3 style="font-family: 'Archivo Black', 'Anton', sans-serif; font-size: 2.2rem; margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: -0.06em;">
                3.5. PRODUCCIÓN LENTA: CORREGIR LO QUE NO SALIÓ BIEN
              </h3>
              <p style="margin-bottom: 2rem;">La IA no siempre respeta la consistencia completa de la prenda en el primer intento. Es totalmente normal encontrarse con inconsistencias en el diseño.</p>
              
              <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 3rem; margin-bottom: 3.5rem; align-items: start;">
                <div class="brutalist-block-red" style="padding: 2rem; margin: 0; background-color: rgba(249, 74, 44, 0.04); border-color: var(--red);">
                  <span class="ocr-label" style="background-color: var(--red); color: white;">[ ERRORES E INCOHERENCIAS HABITUALES ]</span>
                  <ul class="editorial-list" style="margin-top: 1.2rem; font-family: 'Space Mono', monospace; font-size: 0.88rem; list-style: none;">
                    <li style="margin-bottom: 0.6rem;">• Puede distorsionar las rayas horizontales.</li>
                    <li style="margin-bottom: 0.6rem;">• Puede deformar o cambiar el cuello polo.</li>
                    <li style="margin-bottom: 0.6rem;">• Puede inventar textos o logos extraños en el pecho.</li>
                    <li style="margin-bottom: 0.6rem;">• Puede omitir botones o hacer la caída demasiado ajustada.</li>
                    <li style="margin-bottom: 0.6rem;">• Puede dañar las manos de los modelos o cambiar la textura tejida.</li>
                  </ul>
                  <p style="margin-top: 1.5rem; font-size: 0.95rem; font-weight: bold; text-transform: uppercase; color: var(--red);">
                    *Esto es normal. No significa que el proceso falló. Significa que hay que iterar.*
                  </p>
                </div>
                
                <div>
                  <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1.2rem; color: var(--black); text-transform: uppercase;">La manera lenta para corregir es esta:</h4>
                  <ol style="margin-left: 1.2rem; display: flex; flex-direction: column; gap: 0.8rem; font-size: 0.98rem; line-height: 1.5;">
                    <li><strong>Tomas la imagen</strong> que casi funciona pero tiene un fallo.</li>
                    <li><strong>Reutilizas el prompt</strong> base en Google Flow.</li>
                    <li><strong>Le indicas a la IA</strong> qué salió mal específicamente.</li>
                    <li><strong>Refuerzas las reglas</strong> de consistencia (mismas rayas, cuello, fit).</li>
                    <li><strong>Generas 4 variaciones</strong> (x4) para aumentar tus opciones.</li>
                    <li><strong>Escoges la mejor</strong> del lote e iteras de nuevo si es preciso.</li>
                  </ol>
                </div>
              </div>

              <!-- Ejemplo de corrección -->
              <div class="prompt-container" style="margin: 2rem 0; border: var(--border-brutal-thin); padding: 1.5rem; background-color: var(--black);">
                <div class="prompt-header" style="border-bottom: 1px dashed rgba(244,240,230,0.2); padding-bottom: 0.8rem; margin-bottom: 1rem;">
                  <span class="prompt-label" style="color: var(--red); font-family: 'Space Mono', monospace; font-weight: bold;">[ EJEMPLO REAL DE PROMPT DE ITERACIÓN / CORRECCIÓN ]</span>
                  <button class="copy-btn" type="button">Copiar Prompt</button>
                </div>
                <pre class="prompt-text" style="color: var(--paper-warm) !important; background-color: transparent !important; border: none !important; padding: 0 !important; white-space: pre-wrap; font-family: 'Space Mono', monospace; font-size: 0.9rem; line-height: 1.5;">El resultado anterior no mantuvo bien la prenda. Corrige la generación manteniendo exactamente el polo de referencia: mismas rayas azul denim y beige, mismo cuello beige, mismos botones frontales, misma manga amplia, misma textura knit y mismo fit boxy. No inventes otra prenda. No cambies la distribución de las rayas. El modelo debe usar el polo de frente y la prenda debe verse completa.</pre>
              </div>
            </div>

            <!-- 3.6. Tipos de imágenes que debe producir la campaña -->
            <div id="tipos-imagenes-seccion" style="margin: 4.5rem 0;">
              <h3 style="font-family: 'Archivo Black', 'Anton', sans-serif; font-size: 2.2rem; margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: -0.06em;">
                3.6. TIPOS DE IMÁGENES QUE DEBE PRODUCIR LA CAMPAÑA
              </h3>
              <p style="margin-bottom: 2.5rem;">Una campaña útil no puede tener solo fotos bonitas. Necesita imágenes para diferentes usos de tu marca. Para este producto, mínimo deberíamos producir:</p>
              
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
                <!-- Tarjeta 1 -->
                <div class="editorial-card" style="background-color: #fff; border: var(--border-brutal-thin); padding: 2rem; box-shadow: var(--shadow-brutal);">
                  <span style="font-family: 'Space Mono', monospace; font-weight: bold; color: var(--red); font-size: 1.1rem; border-bottom: 2px solid var(--black); padding-bottom: 0.2rem;">01 / CATÁLOGO</span>
                  <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.6rem; margin: 1rem 0 0.5rem 0; text-transform: uppercase;">Fotos de producto limpio</h4>
                  <p style="font-size: 0.9rem; line-height: 1.5; color: var(--black-2);">Muestra el producto con máxima claridad. Incluye vista frontal, vista trasera, detalle de textura knit, detalle del cuello polo beige, y polo doblado o colgado.</p>
                </div>
                <!-- Tarjeta 2 -->
                <div class="editorial-card" style="background-color: #fff; border: var(--border-brutal-thin); padding: 2rem; box-shadow: var(--shadow-brutal);">
                  <span style="font-family: 'Space Mono', monospace; font-weight: bold; color: var(--red); font-size: 1.1rem; border-bottom: 2px solid var(--black); padding-bottom: 0.2rem;">02 / CON MODELO</span>
                  <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.6rem; margin: 1rem 0 0.5rem 0; text-transform: uppercase;">Calce y volumen real</h4>
                  <p style="font-size: 0.9rem; line-height: 1.5; color: var(--black-2);">Sirve para que el cliente entienda cómo queda puesta la prenda. Modelo de frente, caminando, sentado, mirando abajo, en estudio limpio o en locación urbana.</p>
                </div>
                <!-- Tarjeta 3 -->
                <div class="editorial-card" style="background-color: #fff; border: var(--border-brutal-thin); padding: 2rem; box-shadow: var(--shadow-brutal);">
                  <span style="font-family: 'Space Mono', monospace; font-weight: bold; color: var(--red); font-size: 1.1rem; border-bottom: 2px solid var(--black); padding-bottom: 0.2rem;">03 / LIFESTYLE</span>
                  <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.6rem; margin: 1rem 0 0.5rem 0; text-transform: uppercase;">Deseo y estilo de vida</h4>
                  <p style="font-size: 0.9rem; line-height: 1.5; color: var(--black-2);">Vende contexto y aspiración de marca. Cafeterías minimalistas, calles limpias de ciudad, fotos en pareja, con mascotas (perros), carros lujosos y garajes premium.</p>
                </div>
                <!-- Tarjeta 4 -->
                <div class="editorial-card" style="background-color: #fff; border: var(--border-brutal-thin); padding: 2rem; box-shadow: var(--shadow-brutal);">
                  <span style="font-family: 'Space Mono', monospace; font-weight: bold; color: var(--red); font-size: 1.1rem; border-bottom: 2px solid var(--black); padding-bottom: 0.2rem;">04 / EDITORIAL WEB</span>
                  <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.6rem; margin: 1rem 0 0.5rem 0; text-transform: uppercase;">Banners y home horizontal</h4>
                  <p style="font-size: 0.9rem; line-height: 1.5; color: var(--black-2);">Piezas en formato horizontal para la tienda online. Hero banner principal de web, fotos de textura en gran tamaño, lookbooks horizontales y portadas de colección.</p>
                </div>
                <!-- Tarjeta 5 -->
                <div class="editorial-card" style="background-color: #fff; border: var(--border-brutal-thin); padding: 2rem; box-shadow: var(--shadow-brutal);">
                  <span style="font-family: 'Space Mono', monospace; font-weight: bold; color: var(--red); font-size: 1.1rem; border-bottom: 2px solid var(--black); padding-bottom: 0.2rem;">05 / INSTAGRAM</span>
                  <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.6rem; margin: 1rem 0 0.5rem 0; text-transform: uppercase;">Contenido de redes</h4>
                  <p style="font-size: 0.9rem; line-height: 1.5; color: var(--black-2);">Formateado para captar atención en el feed. Portadas de reels 9:16, imágenes de carrusel 4:5, stories tomadas frente al espejo, y fotos estilo UGC premium.</p>
                </div>
                <!-- Tarjeta 6 -->
                <div class="editorial-card" style="background-color: #fff; border: var(--border-brutal-thin); padding: 2rem; box-shadow: var(--shadow-brutal);">
                  <span style="font-family: 'Space Mono', monospace; font-weight: bold; color: var(--red); font-size: 1.1rem; border-bottom: 2px solid var(--black); padding-bottom: 0.2rem;">06 / ANUNCIOS</span>
                  <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.6rem; margin: 1rem 0 0.5rem 0; text-transform: uppercase;">Venta y conversión</h4>
                  <p style="font-size: 0.9rem; line-height: 1.5; color: var(--black-2);">Dirigidas a la compra directa. Imágenes con precios superpuestos, llamadas de urgencia comercial, imágenes optimizadas para WhatsApp y avisos de drops limitados.</p>
                </div>
              </div>
            </div>

            <!-- 3.7. Prompt para pedir una campaña completa de 30 imágenes -->
            <div id="prompt-30-completo-seccion" style="margin: 4.5rem 0;">
              <h3 style="font-family: 'Archivo Black', 'Anton', sans-serif; font-size: 2.2rem; margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: -0.06em;">
                3.7. PROMPT MAESTRO PARA PEDIR UNA CAMPAÑA COMPLETA DE 30 IMÁGENES
              </h3>
              <p style="margin-bottom: 2rem;">El alumno puede copiar y usar este prompt completo para indicarle al Director Creativo de ChatGPT la producción completa de su drop:</p>
              
              <div class="prompt-container" style="border: var(--border-brutal-thin); padding: 1.5rem; background-color: var(--black);">
                <div class="prompt-header" style="border-bottom: 1px dashed rgba(244,240,230,0.2); padding-bottom: 0.8rem; margin-bottom: 1rem;">
                  <span class="prompt-label" style="color: var(--red); font-family: 'Space Mono', monospace; font-weight: bold;">[ PROMPT GENERADOR DE CAMPAÑA COMPLETA (30 PROMPTS) ]</span>
                  <button class="copy-btn" type="button">Copiar Prompt</button>
                </div>
                <pre class="prompt-text" style="color: var(--paper-warm) !important; background-color: transparent !important; border: none !important; padding: 0 !important; white-space: pre-wrap; font-family: 'Space Mono', monospace; font-size: 0.9rem; line-height: 1.55;">Actúa como director creativo de moda y generador de prompts para campañas visuales con IA.

Voy a darte una prenda de referencia. Quiero que me crees una campaña completa de 30 imágenes manteniendo la consistencia del producto.

Producto:
Polo tejido oversized de manga corta, cuello polo beige, botones frontales oscuros, rayas horizontales azul denim y beige, textura knit gruesa, manga amplia, fit boxy corto, estética rugby club vintage streetwear premium.

Quiero que dividas la campaña así:
5 imágenes de producto limpio para catálogo.
5 imágenes con modelos en fondo blanco.
5 imágenes lifestyle con animales o pareja.
5 imágenes con carros o ambientes premium.
5 imágenes editoriales para web en formato horizontal.
5 imágenes para Instagram, anuncios y venta.

Cada prompt debe incluir:
- Descripción exacta del producto.
- Modelo o escena.
- Fondo o ambiente.
- Pose.
- Iluminación.
- Formato recomendado.
- Estética.
- Negativos para evitar errores.

Muy importante:
La IA debe mantener la prenda fiel al producto original. No cambiar rayas, cuello, textura, colores, botones, silueta ni fit oversized.</pre>
              </div>
            </div>

            <!-- 3.8. Control de calidad de cada imagen -->
            <div id="control-calidad-seccion" style="margin: 4.5rem 0;">
              <h3 style="font-family: 'Archivo Black', 'Anton', sans-serif; font-size: 2.2rem; margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: -0.06em;">
                3.8. CONTROL DE CALIDAD DE CADA IMAGEN
              </h3>
              <p style="margin-bottom: 2rem;">Después de generar, no se publica todo directamente. Cada imagen producida por la IA debe superar un filtro estricto de control:</p>
              
              <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 3rem; align-items: start;">
                <div class="brutalist-block" style="padding: 2rem; background-color: #fff; border: var(--border-brutal); margin: 0; box-shadow: var(--shadow-brutal);">
                  <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1rem; text-transform: uppercase;">Lista de chequeo de la prenda:</h4>
                  <ul class="editorial-list" style="display: flex; flex-direction: column; gap: 0.8rem; font-size: 0.95rem; list-style: none;">
                    <li><strong>✓ Parecido:</strong> ¿La prenda se parece fielmente al producto real?</li>
                    <li><strong>✓ Colores:</strong> ¿Los colores siguen siendo azul denim y beige exactos?</li>
                    <li><strong>✓ Rayas:</strong> ¿Las rayas están correctamente ubicadas y alineadas?</li>
                    <li><strong>✓ Cuello & Botones:</strong> ¿El cuello polo beige se ve bien y mantiene los botones oscuros?</li>
                    <li><strong>✓ Fit & Textura:</strong> ¿Conserva la silueta boxy oversized y la textura de punto knit grueso?</li>
                    <li><strong>✓ Naturalidad:</strong> ¿El modelo tiene poses naturales y las manos correctas?</li>
                    <li><strong>✓ Identidad:</strong> ¿La foto se siente de la misma marca y sirve directamente para vender?</li>
                  </ul>
                </div>
                
                <div style="display: flex; flex-direction: column; gap: 1rem;">
                  <div class="brutalist-block-red" style="margin: 0; padding: 1.5rem;">
                    <h5 style="font-family: 'Space Mono', monospace; font-weight: bold; margin-bottom: 0.5rem; color: var(--red); text-transform: uppercase;">Filtro de Descarte</h5>
                    <p style="font-size: 0.85rem; line-height: 1.4;">Si una imagen es bonita pero no vende, o cambia sustancialmente los detalles del producto: <strong>se descarta de inmediato</strong>.</p>
                  </div>
                  <div style="background-color: var(--black); color: var(--paper-warm); padding: 1.5rem; border: var(--border-brutal-thin);">
                    <h5 style="font-family: 'Space Mono', monospace; font-weight: bold; margin-bottom: 0.5rem; color: var(--cement); text-transform: uppercase;">Iteración y Ajustes</h5>
                    <p style="font-size: 0.85rem; line-height: 1.4; color: var(--cement);">Si la imagen es casi perfecta pero tiene un error corregible de la prenda, se toma de base y se itera en la Manera Lenta.</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- 3.9. Resultado final del Paso 3 -->
            <div class="brutalist-block-red" style="margin: 4.5rem 0; padding: 2.5rem; background-color: var(--black); color: var(--paper-warm); border: var(--border-brutal); box-shadow: var(--shadow-brutal-red);">
              <span class="ocr-label" style="background-color: var(--red); color: white;">[ RESULTADO FINAL DEL PASO 3 ]</span>
              <h4 style="font-family: 'Archivo Black', 'Anton', sans-serif; font-size: 1.8rem; margin: 1rem 0; text-transform: uppercase; letter-spacing: -0.04em;">TU PRIMER BANCO VISUAL DE DROP:</h4>
              <p style="margin-bottom: 1.5rem; color: var(--cement);">Al terminar este proceso, la persona debe poseer una carpeta completa de activos de campaña:</p>
              
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; font-family: 'Bebas Neue', sans-serif; font-size: 1.5rem; color: var(--red); margin-bottom: 2rem;">
                <div style="background-color: var(--black-2); padding: 1rem; border: 1px dashed var(--gray-metal);">• 10 IMÁGENES EXCELENTES (DIRECTAS PARA PUBLICACIÓN)</div>
                <div style="background-color: var(--black-2); padding: 1rem; border: 1px dashed var(--gray-metal);">• 15 IMÁGENES ACEPTABLES DE APOYO</div>
                <div style="background-color: var(--black-2); padding: 1rem; border: 1px dashed var(--gray-metal);">• 5 IMÁGENES PARA DETALLES / CORRECCIONES</div>
              </div>
              
              <p style="font-weight: 800; text-transform: uppercase; color: var(--paper);">
                ¡Ya no dependes de un costoso estudio fotográfico! Tienes un sistema replicable para producir contenido visual de moda desde una prenda real.
              </p>
            </div>
    """
    html_content.append(tabs_html)
    html_content.append(step3_body)

    # Section 07: Paso 4 Modelos IA
    # Render with high-interactivity:
    # 1. Accordion for "3 formas de trabajar modelos"
    # 2. Model Profile selector deck showing the 4 profiles
    html_content.append("""
        </section>

        <!-- Sección 07: Paso 4 -->
        <section id="paso-4">
          <div class="section-meta">[ PASO 04 / CUERPO Y ACTITUD ]</div>
          <h2 class="section-title">PASO 4: MODELOS IA Y ROSTRO DE MARCA</h2>
          
          <div class="text-editorial">
            <p>Una prenda sola puede verse bonita. Pero una prenda en una persona genera deseo. El cliente no compra únicamente tela. Compra cómo cree que se va a ver usando esa prenda.</p>
            
            <p><strong>TRES FORMAS DE TRABAJAR MODELOS CON IA:</strong></p>
            
            <div class="accordion-wrapper">
              <div class="accordion-item active">
                <div class="accordion-header">
                  <span>Forma 1: Modelos virtuales creados desde cero</span>
                  <span class="accordion-icon">+</span>
                </div>
                <div class="accordion-content">
                  <p>Aquí la persona no usa fotos propias. Simplemente le pide a la IA un modelo que encaje con la marca.</p>
                  <p><em>Ejemplo:</em> "Modelo masculino joven de 24 a 28 años, estilo urbano limpio, cabello oscuro natural, rostro realista, expresión tranquila, cuerpo promedio, actitud segura, usando polo tejido oversized azul denim y beige, jeans claros amplios y sneakers blancos, estética streetwear premium."</p>
                </div>
              </div>
              <div class="accordion-item">
                <div class="accordion-header">
                  <span>Forma 2: Modelos de marca repetibles</span>
                  <span class="accordion-icon">+</span>
                </div>
                <div class="accordion-content">
                  <p>Aquí no queremos un modelo diferente en cada foto. Queremos crear un rostro que se repita, como si fuera parte de la identidad de la marca. Para eso se define una ficha fija.</p>
                  <p><em>Ficha de Ejemplo:</em> Modelo masculino principal, 25 años, cabello castaño oscuro ondulado, piel realista natural, actitud seria y segura, estilo urbano premium. Le pedimos a la IA que use siempre este perfil en todas las imágenes.</p>
                </div>
              </div>
              <div class="accordion-item">
                <div class="accordion-header">
                  <span>Forma 3: La persona como rostro de su propia marca</span>
                  <span class="accordion-icon">+</span>
                </div>
                <div class="accordion-content">
                  <p>Esta es una opción poderosa para emprendedores y marcas personales. La persona puede aparecer usando su propia prenda, generando más cercanía.</p>
                  <p><em>Regla de control:</em> Solo se debe usar la imagen propia o la de alguien que haya dado permiso explícito.</p>
                </div>
              </div>
            </div>

            <h3 style="font-family: 'Anton', sans-serif; font-size: 2.2rem; margin: 3.5rem 0 1.5rem; text-transform: uppercase;">
              VISUALIZADOR DE PERFILES DE MODELOS
            </h3>
            <p>Selecciona un perfil a continuación para revelar la dirección y prompts recomendados para esta campaña:</p>

            <div class="model-deck-wrapper">
              <div class="model-deck-nav">
                <button class="model-deck-tab active" data-target="model-masc">01. Masculino Principal</button>
                <button class="model-deck-tab" data-target="model-fem">02. Femenino Unisex</button>
                <button class="model-deck-tab" data-target="model-pareja">03. Pareja Editorial</button>
                <button class="model-deck-tab" data-target="model-propio">04. Rostro Propio</button>
              </div>

              <!-- Masculino -->
              <div class="model-deck-content active" id="model-masc">
                <div class="prompt-item-row">
                  <div>
                    <h4 style="color: var(--red);">Modelo Streetwear Masculino</h4>
                    <p style="margin-bottom: 1.5rem;"><strong>Uso:</strong> lookbook, anuncios, catálogo. <strong>Energía:</strong> segura, limpia, natural.</p>
                    
                    <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                      <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                        <span class="prompt-label">PROMPT RECOMENDADO</span>
                        <button class="copy-btn" type="button">Copiar</button>
                      </div>
                      <pre class="prompt-text" style="color: var(--black); max-height: none;">Fotografía editorial de moda masculina streetwear premium. Modelo masculino joven de 25 años, rostro realista, piel natural, cabello oscuro ligeramente ondulado, expresión tranquila y segura. Usa exactamente el polo tejido oversized de referencia: rayas horizontales azul denim y beige, cuello polo beige, botones frontales, textura knit gruesa, manga amplia y fit boxy corto. Combinar con jeans claros anchos y sneakers blancos. Fondo beige minimalista, luz suave de estudio, composición limpia, estética rugby club vintage urbano.\nNegativos: piel artificial, manos deformes, cambiar la prenda, rayas torcidas, logos externos, pose exagerada, fondo caótico.</pre>
                    </div>
                  </div>
                  <div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[PERFIL MASCULINO - ESTUDIO]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image72.png" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Femenino -->
              <div class="model-deck-content" id="model-fem">
                <div class="prompt-item-row">
                  <div>
                    <h4 style="color: var(--red);">Modelo Unisex Femenina</h4>
                    <p style="margin-bottom: 1.5rem;"><strong>Uso:</strong> campaña unisex, catálogo editorial. <strong>Energía:</strong> sofisticada, calmada, natural.</p>
                    
                    <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                      <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                        <span class="prompt-label">PROMPT RECOMENDADO</span>
                        <button class="copy-btn" type="button">Copiar</button>
                      </div>
                      <pre class="prompt-text" style="color: var(--black); max-height: none;">Fotografía editorial unisex premium. Modelo femenina joven usando el polo tejido oversized de referencia como prenda protagonista, rayas azul denim y beige, cuello beige, botones frontales, textura knit visible, fit boxy amplio. Jeans claros, cabello natural, accesorios mínimos, expresión calmada, fondo blanco cálido, luz suave editorial, estética quiet luxury streetwear.\nNegativos: prenda ajustada, rayas deformadas, piel plástica, manos raras, cambiar colores, fondo saturado.</pre>
                    </div>
                  </div>
                  <div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[PERFIL FEMENINO - UNISEX]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image46.png" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Pareja -->
              <div class="model-deck-content" id="model-pareja">
                <div class="prompt-item-row">
                  <div>
                    <h4 style="color: var(--red);">Pareja Lifestyle Editorial</h4>
                    <p style="margin-bottom: 1.5rem;"><strong>Uso:</strong> Instagram feed, branding, carruseles de deseo. <strong>Energía:</strong> íntima, relajada, compartida.</p>
                    
                    <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                      <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                        <span class="prompt-label">PROMPT RECOMENDADO</span>
                        <button class="copy-btn" type="button">Copiar</button>
                      </div>
                      <pre class="prompt-text" style="color: var(--black); max-height: none;">Fotografía lifestyle editorial con pareja joven. Uno de los modelos usa exactamente el polo tejido oversized de referencia, vista frontal clara, rayas azul denim y beige, cuello beige, botones frontales, textura knit gruesa, manga amplia y fit boxy. La otra persona lleva styling neutro en denim, blanco y beige. Ambos en estudio gris cálido, pose cercana pero natural, actitud relajada, luz suave, estética campaña premium unisex.\nNegativos: contacto incómodo, manos deformes, ocultar la prenda, cambiar colores, texto deformado, fondo caótico.</pre>
                    </div>
                  </div>
                  <div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[PERFIL PAREJA - LIFESTYLE]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image70.png" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Rostro Propio -->
              <div class="model-deck-content" id="model-propio">
                <div class="prompt-item-row">
                  <div>
                    <h4 style="color: var(--red);">Personalización de Rostro</h4>
                    <p style="margin-bottom: 1.5rem;"><strong>Uso:</strong> marca personal, contenido orgánico, credibilidad. <strong>Energía:</strong> cercana, auténtica.</p>
                    
                    <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                      <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                        <span class="prompt-label">PROMPT RECOMENDADO</span>
                        <button class="copy-btn" type="button">Copiar</button>
                      </div>
                      <pre class="prompt-text" style="color: var(--black); max-height: none;">Usar a la persona de referencia como modelo principal de una campaña de moda. Mantener su identidad facial, rasgos naturales, cabello, piel y proporciones. Vestirla con el polo tejido oversized de referencia: rayas azul denim y beige, cuello polo beige, botones frontales, textura knit gruesa, manga amplia y fit boxy corto. Crear una fotografía editorial premium en fondo beige minimalista, pose relajada, mirada fuera de cámara, luz suave, estética streetwear limpio y aspiracional.\nNegativos: cambiar el rostro, piel artificial, deformar manos, cambiar la prenda, alterar colores, rayas incorrectas, fondo caótico.</pre>
                    </div>
                  </div>
                  <div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[PERFIL CUSTOM ROSTRO]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image49.png" />
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <p><strong>CÓMO MANTENER LA CONSISTENCIA DEL MODELO:</strong></p>
            <p>Para evitar que la IA cambie el rostro de tus personajes entre tomas, repite siempre la misma ficha técnica del modelo al final del prompt y reutiliza una imagen que ya haya salido bien como referencia facial.</p>
          </div>
        </section>

        <!-- Sección 08: Paso 5 Campaña Ventas -->
        <!-- Extremely visual and interactive -->
        <section id="paso-5" style="background-color: var(--paper);">
          <div class="section-meta">[ PASO 05 / EL SISTEMA DE VENTAS ]</div>
          <h2 class="section-title">PASO 5: CAMPAÑA LISTA PARA VENDER</h2>
          
          <div class="text-editorial">
            <p>Una imagen bonita no siempre vende. Para convertir tus imágenes en ingresos reales, debes organizarlas por funciones comerciales y usarlas en un sistema estructurado.</p>
            
            <p><strong>1. GABINETE DE ARCHIVOS DEL CONTENIDO:</strong></p>
            <p>Haz clic en las carpetas a continuación para ver cómo debes clasificar tus fotos de campaña para su uso comercial:</p>

            <!-- Cabinet Folder Tabs -->
            <div class="cabinet-wrapper">
              <div class="cabinet-tabs">
                <button class="cabinet-tab-btn active" data-target="folder-prod">📁 01. Catálogo</button>
                <button class="cabinet-tab-btn" data-target="folder-mod">📁 02. Modelo</button>
                <button class="cabinet-tab-btn" data-target="folder-life">📁 03. Lifestyle</button>
                <button class="cabinet-tab-btn" data-target="folder-web">📁 04. Web</button>
                <button class="cabinet-tab-btn" data-target="folder-sale">📁 05. Conversión</button>
              </div>

              <!-- Folder Prod -->
              <div class="cabinet-pane active" id="folder-prod">
                <h4 style="margin-bottom: 1rem; color: var(--red);">Fotos de Catálogo de Prenda</h4>
                <p style="margin-bottom: 1rem;"><strong>Qué piezas contiene:</strong> Frente limpio, espalda limpia, macro-detalle de textura, detalles de botones y cuello.</p>
                <p><strong>Uso principal:</strong> Ficha técnica en e-commerce, historias de WhatsApp y detalles técnicos de costura para clientes exigentes.</p>
              </div>

              <!-- Folder Mod -->
              <div class="cabinet-pane" id="folder-mod">
                <h4 style="margin-bottom: 1rem; color: var(--red);">Fotos de Modelo en Poses</h4>
                <p style="margin-bottom: 1rem;"><strong>Qué piezas contiene:</strong> Modelo de pie, de perfil, caminando, sentado, en fondo gris o de estudio.</p>
                <p><strong>Uso principal:</strong> Anuncios principales de Meta Ads, e-commerce lookbook y portadas destacadas de Instagram.</p>
              </div>

              <!-- Folder Life -->
              <div class="cabinet-pane" id="folder-life">
                <h4 style="margin-bottom: 1rem; color: var(--red);">Fotos de Estilo de Vida (Lifestyle)</h4>
                <p style="margin-bottom: 1rem;"><strong>Qué piezas contiene:</strong> Pareja en estudio, modelo en cafetería minimalista, calle urbana elegante, garaje premium.</p>
                <p><strong>Uso principal:</strong> Contenido orgánico de Instagram/Pinterest para generar identidad, aspiración y deseo en la audiencia.</p>
              </div>

              <!-- Folder Web -->
              <div class="cabinet-pane" id="folder-web">
                <h4 style="margin-bottom: 1rem; color: var(--red);">Piezas Banners Horizontales</h4>
                <p style="margin-bottom: 1rem;"><strong>Qué piezas contiene:</strong> Banners 16:9 horizontales con espacio negativo elegante para texto y llamadas a la acción.</p>
                <p><strong>Uso principal:</strong> Portada de la página web de lanzamiento, banners de colecciones y cabeceras de correos electrónicos.</p>
              </div>

              <!-- Folder Sale -->
              <div class="cabinet-pane" id="folder-sale">
                <h4 style="margin-bottom: 1rem; color: var(--red);">Imágenes de Conversión Directa</h4>
                <p style="margin-bottom: 1rem;"><strong>Qué piezas contiene:</strong> Anuncios 1:1 o 9:16 con indicación del precio ($79.900), leyendas de "Drop Limitado" o "Unidades Limitadas".</p>
                <p><strong>Uso principal:</strong> Meta Ads de venta directa (conversión) y estados de WhatsApp de urgencia comercial.</p>
              </div>
            </div>

            <h3 style="font-family: 'Anton', sans-serif; font-size: 2.2rem; margin: 4rem 0 1.5rem; text-transform: uppercase;">
              2. CALENDARIO DE CONTENIDOS (7 DÍAS EN INSTAGRAM)
            </h3>
            <p>Haz clic en cada día del calendario a continuación para desplegar la pieza de campaña recomendada, la foto asociada y el copy comercial listo para copiar y publicar:</p>

            <!-- Calendar Board -->
            <div class="calendar-board">
              <div class="calendar-header-nav">
                <button class="calendar-day-btn active" data-target="cal-lunes">LUN</button>
                <button class="calendar-day-btn" data-target="cal-martes">MAR</button>
                <button class="calendar-day-btn" data-target="cal-miercoles">MIÉ</button>
                <button class="calendar-day-btn" data-target="cal-jueves">JUE</button>
                <button class="calendar-day-btn" data-target="cal-viernes">VIE</button>
                <button class="calendar-day-btn" data-target="cal-sabado">SÁB</button>
                <button class="calendar-day-btn" data-target="cal-domingo">DOM</button>
              </div>

              <!-- Lunes -->
              <div class="calendar-day-content active" id="cal-lunes">
                <div class="prompt-item-row">
                  <div>
                    <h4 style="color: var(--red);">Día 1: Teaser de Lanzamiento</h4>
                    <p style="margin-bottom: 1rem;"><strong>Objetivo:</strong> Generar expectativa (hype) sin revelar toda la prenda.</p>
                    <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                      <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                        <span class="prompt-label">COPY PARA INSTAGRAM</span>
                        <button class="copy-btn" type="button">Copiar Copy</button>
                      </div>
                      <pre class="prompt-text" style="color: var(--black); max-height: none;">Textura, peso y silueta.\n\nNuevo drop en camino. Separa el tuyo antes de que se agoten.</pre>
                    </div>
                  </div>
                  <div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[FOTO DÍA 1]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image26.png" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Martes -->
              <div class="calendar-day-content" id="cal-martes">
                <div class="prompt-item-row">
                  <div>
                    <h4 style="color: var(--red);">Día 2: Revelación de Producto</h4>
                    <p style="margin-bottom: 1rem;"><strong>Objetivo:</strong> Mostrar el diseño frontal de la prenda con total claridad.</p>
                    <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                      <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                        <span class="prompt-label">COPY PARA INSTAGRAM</span>
                        <button class="copy-btn" type="button">Copiar Copy</button>
                      </div>
                      <pre class="prompt-text" style="color: var(--black); max-height: none;">Polo tejido oversized.\n\nRayas azul denim + beige. Fit boxy. Manga amplia. Estética club vintage. Un básico elevado para el diario.</pre>
                    </div>
                  </div>
                  <div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[FOTO DÍA 2]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image38.png" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Miercoles -->
              <div class="calendar-day-content" id="cal-miercoles">
                <div class="prompt-item-row">
                  <div>
                    <h4 style="color: var(--red);">Día 3: Modelo Puesta en Escena</h4>
                    <p style="margin-bottom: 1rem;"><strong>Objetivo:</strong> Demostrar cómo queda la prenda en cuerpo real.</p>
                    <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                      <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                        <span class="prompt-label">COPY PARA INSTAGRAM</span>
                        <button class="copy-btn" type="button">Copiar Copy</button>
                      </div>
                      <pre class="prompt-text" style="color: var(--black); max-height: none;">Así se ve puesto.\n\nUna prenda fácil de combinar, pero con presencia de sobra. Estilo sin esfuerzo.</pre>
                    </div>
                  </div>
                  <div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[FOTO DÍA 3]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image72.png" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Jueves -->
              <div class="calendar-day-content" id="cal-jueves">
                <div class="prompt-item-row">
                  <div>
                    <h4 style="color: var(--red);">Día 4: Estilo de Vida y Contexto</h4>
                    <p style="margin-bottom: 1rem;"><strong>Objetivo:</strong> Vender la vibra de la marca a través de un escenario cotidiano.</p>
                    <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                      <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                        <span class="prompt-label">COPY PARA INSTAGRAM</span>
                        <button class="copy-btn" type="button">Copiar Copy</button>
                      </div>
                      <pre class="prompt-text" style="color: var(--black); max-height: none;">Para salir, para fotos, para elevar un outfit simple.\n\nEl tipo de prenda que hace que todo tu estilo se vea más pensado y premium.</pre>
                    </div>
                  </div>
                  <div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[FOTO DÍA 4]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image42.png" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Viernes -->
              <div class="calendar-day-content" id="cal-viernes">
                <div class="prompt-item-row">
                  <div>
                    <h4 style="color: var(--red);">Día 5: Detalle de Textura y Calidad</h4>
                    <p style="margin-bottom: 1rem;"><strong>Objetivo:</strong> Justificar el valor y calidad textil de la prenda.</p>
                    <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                      <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                        <span class="prompt-label">COPY PARA INSTAGRAM</span>
                        <button class="copy-btn" type="button">Copiar Copy</button>
                      </div>
                      <pre class="prompt-text" style="color: var(--black); max-height: none;">Textura knit premium visible, cuello polo y rayas azul denim. Una pieza cuidada con estética retro premium desde el primer vistazo.</pre>
                    </div>
                  </div>
                  <div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[FOTO DÍA 5]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image26.png" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Sabado -->
              <div class="calendar-day-content" id="cal-sabado">
                <div class="prompt-item-row">
                  <div>
                    <h4 style="color: var(--red);">Día 6: Oferta Directa de Conversión</h4>
                    <p style="margin-bottom: 1rem;"><strong>Objetivo:</strong> Cerrar la venta del drop.</p>
                    <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                      <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                        <span class="prompt-label">COPY PARA INSTAGRAM</span>
                        <button class="copy-btn" type="button">Copiar Copy</button>
                      </div>
                      <pre class="prompt-text" style="color: var(--black); max-height: none;">Polo tejido oversized disponible por $79.900.\n\nUnidades limitadas para este drop. Pídelo ya por WhatsApp en el link de la bio.</pre>
                    </div>
                  </div>
                  <div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[FOTO DÍA 6]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image23.png" />
                    </div>
                  </div>
                </div>
              </div>

              <!-- Domingo -->
              <div class="calendar-day-content" id="cal-domingo">
                <div class="prompt-item-row">
                  <div>
                    <h4 style="color: var(--red);">Día 7: Cierre de Urgencia</h4>
                    <p style="margin-bottom: 1rem;"><strong>Objetivo:</strong> Provocar las últimas compras por escasez de existencias.</p>
                    <div class="prompt-container" style="box-shadow: none; margin: 0; padding: 0; background: transparent;">
                      <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                        <span class="prompt-label">COPY PARA INSTAGRAM</span>
                        <button class="copy-btn" type="button">Copiar Copy</button>
                      </div>
                      <pre class="prompt-text" style="color: var(--black); max-height: none;">Últimas unidades del drop.\n\nSi quieres una prenda diferente para elevar cualquier outfit, escríbenos por WhatsApp y separa la tuya.</pre>
                    </div>
                  </div>
                  <div>
                    <div class="full-size-image-container" style="margin: 0;">
                      <div class="image-label-bar">[FOTO DÍA 7]</div>
                      <img class="full-size-img" src="/media/de_prenda_a_campana/image8.png" />
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <h3 style="font-family: 'Anton', sans-serif; font-size: 2.2rem; margin: 4rem 0 1.5rem; text-transform: uppercase;">
              3. SIMULADOR DE HISTORIAS DE INSTAGRAM (EMBUDO DE VENTAS)
            </h3>
            <p>Utiliza las flechas debajo del teléfono para ver cómo se compone la secuencia adictiva de 5 historias de venta en Instagram:</p>

            <!-- Stories Mobile Phone Simulator -->
            <div class="phone-simulator-container">
              <div class="mobile-phone-frame">
                <div class="phone-screen">
                  <div class="phone-slider-track">
                    <!-- Slide 1 -->
                    <div class="phone-slide">
                      <img src="/media/de_prenda_a_campana/image72.png" />
                      <div class="phone-slide-text">
                        <h4>HISTORIA 1</h4>
                        <p><strong>EL DESEO:</strong> Nuevo polo tejido oversized con estética club vintage. Disponible ya.</p>
                      </div>
                    </div>
                    <!-- Slide 2 -->
                    <div class="phone-slide">
                      <img src="/media/de_prenda_a_campana/image26.png" />
                      <div class="phone-slide-text">
                        <h4>HISTORIA 2</h4>
                        <p><strong>EL DETALLE:</strong> Textura knit premium con rayas azul denim y beige.</p>
                      </div>
                    </div>
                    <!-- Slide 3 -->
                    <div class="phone-slide">
                      <img src="/media/de_prenda_a_campana/image42.png" />
                      <div class="phone-slide-text">
                        <h4>HISTORIA 3</h4>
                        <p><strong>EL CALCE:</strong> Oversized, cómodo y extremadamente fácil de combinar.</p>
                      </div>
                    </div>
                    <!-- Slide 4 -->
                    <div class="phone-slide">
                      <img src="/media/de_prenda_a_campana/image38.png" />
                      <div class="phone-slide-text">
                        <h4>HISTORIA 4</h4>
                        <p><strong>EL PRECIO:</strong> Hazlo tuyo por $79.900. Pocas unidades disponibles.</p>
                      </div>
                    </div>
                    <!-- Slide 5 -->
                    <div class="phone-slide">
                      <img src="/media/de_prenda_a_campana/image8.png" />
                      <div class="phone-slide-text">
                        <h4>HISTORIA 5</h4>
                        <p><strong>LLAMADA A LA ACCIÓN:</strong> Desliza o haz clic para pedir directamente por WhatsApp.</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="phone-controls">
                  <button class="phone-nav-btn" id="phone-prev-btn">Anterior</button>
                  <span class="phone-indicator">HISTORIA 1 / 5</span>
                  <button class="phone-nav-btn" id="phone-next-btn">Siguiente</button>
                </div>
              </div>
            </div>

            <h3 style="font-family: 'Anton', sans-serif; font-size: 2.2rem; margin: 4rem 0 1.5rem; text-transform: uppercase;">
              4. DIÁLOGOS DE CIERRE EN WHATSAPP (CONVERSACIONES DE ANUNCIOS)
            </h3>
            <p>Utiliza estos guiones exactos de WhatsApp representados en burbujas interactivas para cerrar las ventas sin sonar desesperado ni agresivo:</p>

            <!-- WhatsApp Chat Mockups -->
            <div class="whatsapp-chat-container">
              <!-- Thread 1 -->
              <div class="chat-bubble received">
                <p>Hola, ¿qué precio tiene el polo tejido y qué tallas quedan?</p>
              </div>
              <div class="chat-bubble sent">
                <p>Hola, ¡claro! 🙌</p>
                <p>Tenemos disponible el polo tejido oversized en rayas azul denim + beige en tallas S, M y L.</p>
                <p>Es una prenda con textura premium, fit boxy, manga amplia y estética club vintage. Queda perfecta para elevar outfits casuales, urbanos y más producidos.</p>
                <p>Su precio es de <strong>$79.900</strong>.</p>
                <p>¿Te gustaría que te envíe las medidas de las tallas para que elijas la ideal?</p>
                <div class="chat-bubble-footer">
                  <button class="chat-copy-btn">Copiar Respuesta</button>
                </div>
              </div>
              
              <!-- Thread 2 -->
              <div class="chat-bubble received">
                <p>Vale, me gusta pero lo voy a pensar un poco.</p>
              </div>
              <div class="chat-bubble sent">
                <p>Dale, ¡sin ningún problema! 🙌</p>
                <p>Solo te aviso que es un drop limitado de pocas unidades y algunas tallas se pueden agotar pronto.</p>
                <p>Si quieres, te puedo enviar una foto de cómo queda puesto para que lo mires con calma.</p>
                <div class="chat-bubble-footer">
                  <button class="chat-copy-btn">Copiar Respuesta</button>
                </div>
              </div>
            </div>

            <h3 style="font-family: 'Anton', sans-serif; font-size: 2.2rem; margin: 4rem 0 1.5rem; text-transform: uppercase;">
              5. CHECKLIST FINAL DE CAMPAÑA
            </h3>
            <p>Antes de lanzar tu campaña y gastar un solo peso en anuncios, asegúrate de marcar cada casilla:</p>
            
            <div style="background-color: var(--black-2); color: var(--paper-warm); padding: 2rem; border: var(--border-brutal); margin-bottom: 3rem;">
              <ul style="list-style: none; display: flex; flex-direction: column; gap: 1rem; font-family: 'Space Mono', monospace; font-size: 0.92rem;">
                <li><input type="checkbox"> [ ] ¿Tengo foto frontal y trasera limpia del producto?</li>
                <li><input type="checkbox"> [ ] ¿Tengo al menos 3 imágenes consistentes con modelo?</li>
                <li><input type="checkbox"> [ ] ¿Tengo imágenes lifestyle que representen el ADN Editorial?</li>
                <li><input type="checkbox"> [ ] ¿Tengo el banner horizontal para mi e-commerce o landing?</li>
                <li><input type="checkbox"> [ ] ¿Tengo anuncios estructurados con el precio exacto ($79.900)?</li>
                <li><input type="checkbox"> [ ] ¿Tengo los copies de venta y respuestas de WhatsApp listos?</li>
                <li><input type="checkbox"> [ ] ¿Las imágenes mantienen la prenda fiel al producto real?</li>
              </ul>
            </div>
            
            <div class="brutalist-block-red" style="margin: 3rem 0;">
              <span class="ocr-label">[ CIERRE DEL ENTRENAMIENTO ]</span>
              <p style="font-weight: 800; font-size: 1.25rem; text-transform: uppercase; line-height: 1.45;">
                NO APRENDES A HACER IMÁGENES CON IA. CONSTRUYES UN SISTEMA CREATIVO DE MODA QUE TRANSFORMA PRENDAS FÍSICAS EN UNA CAMPAÑA DE ALTO IMPACTO LISTA PARA LA CALLE.
              </p>
            </div>
          </div>
        </section>
      </main>
    </div>
  </body>
</html>
""")

    full_html = "".join(html_content)

    # Clean list tagging: wrap continuous lists in <ul> tags
    full_html = re.sub(r'(<li>.*?</li>)+', lambda m: f"<ul>{m.group(0)}</ul><br>", full_html)

    # Save to file
    print("Writing HTML file...")
    with open("de-prenda-a-campana.html", "w", encoding="utf-8") as f:
        f.write(full_html)
    print("Done! Page successfully built at C:\\Users\\Admin\\Documents\\PRODUCTO DIGITAL\\de-prenda-a-campana.html")

if __name__ == "__main__":
    main()
