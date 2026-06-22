import os
import shutil
import re

print("Starting complete generation of biblioteca-de-prompts.html...")

# 1. Ensure cover image is copied to public/media
src_cover = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\public\media\bonus_6_cover.png"
if not os.path.exists(src_cover):
    print("Cover image copy check...")
    fallback_src = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\BONUS 6 BIBLIOTECA COPIAR-PEGAR DE PROMPTS\BONUS 6 BIBLIOTECA COPIAR-PEGAR DE PROMPTS.png"
    if os.path.exists(fallback_src):
        os.makedirs(r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\public\media", exist_ok=True)
        shutil.copy(fallback_src, src_cover)
        print("Successfully verified and copied cover image.")

# 2. Define structured data for the 20 Categories (remains hardcoded for custom Bad/Good compare box format)
categories_data = [
    {
        "num": "01",
        "title": "Producto limpio para tienda online",
        "bad": "Foto de un pantalón para vender.",
        "good": "Fotografía limpia de producto para tienda online, pantalón beige de lino sobre fondo blanco, iluminación suave, prenda bien planchada, textura visible, composición centrada, estilo ecommerce premium.",
        "pro": "Clean ecommerce product photography of beige linen wide-leg pants, perfectly arranged on a pure white background, visible fabric texture, natural folds, soft studio lighting, centered composition, premium online store aesthetic, high resolution, no model, no fake logos, no wrinkles, no shadows too harsh, no distorted garment.",
        "why": "Define producto, fondo, textura, luz, uso comercial y errores a evitar de manera directa."
    },
    {
        "num": "02",
        "title": "Producto premium tipo lujo silencioso",
        "bad": "Pantalón elegante con fondo bonito.",
        "good": "Imagen premium de pantalón sastre negro sobre fondo piedra, luz suave lateral, estética lujo silencioso, textura elegante, composición minimalista.",
        "pro": "Luxury product image of black tailored trousers placed on a warm stone surface, quiet luxury aesthetic, soft side lighting, refined shadows, elegant fabric texture, minimal composition, neutral color palette, high-end fashion catalog style, no text, no logo, no messy background, no harsh contrast.",
        "why": "Vende precio alto sin exagerar; usa materiales, luz y composición premium para inspirar estatus."
    },
    {
        "num": "03",
        "title": "Editorial femenina de moda",
        "bad": "Mujer bonita usando ropa.",
        "good": "Modelo femenina usando pantalón sastre negro, pose segura, fondo gris, iluminación editorial, estética elegante y moderna.",
        "pro": "High-fashion editorial image of a female model wearing black high-waisted tailored trousers, elegant fitted top, confident standing pose, one hand in pocket, minimal gray studio background, soft diffused lighting, full body shot, modern luxury fashion campaign, sophisticated attitude, vertical 4:5, no deformed hands, no fake logos, no distorted clothing, no plastic skin.",
        "why": "No solo muestra la prenda de forma plana; construye la personalidad e identidad aspiracional de la marca."
    },
    {
        "num": "04",
        "title": "Editorial masculina",
        "bad": "Hombre con outfit urbano.",
        "good": "Modelo masculino usando pantalón cargo negro, camiseta blanca, fondo urbano limpio, pose relajada, luz natural, estética streetwear premium.",
        "pro": "Men’s fashion editorial campaign featuring a male model wearing black cargo pants, oversized white t-shirt, minimal sneakers, relaxed confident pose, clean urban concrete background, natural daylight, premium streetwear aesthetic, full body composition, vertical Instagram format, no fake brand logos, no distorted limbs, no chaotic background.",
        "why": "Mezcla de forma equilibrada moda masculina, calle, limpieza visual y efectividad de venta."
    },
    {
        "num": "05",
        "title": "Streetwear urbano",
        "bad": "Ropa urbana cool.",
        "good": "Campaña streetwear con modelo usando hoodie oversize and pantalón cargo, fondo de ciudad, luz dura, actitud desafiante.",
        "pro": "Urban streetwear fashion campaign, model wearing oversized charcoal hoodie and black cargo pants, confident rebellious pose, clean city street background, concrete walls, afternoon hard light, strong shadows, cinematic street style, low angle full body shot, edgy commercial look for Instagram drop, no graffiti text, no fake logos, no distorted hands, no messy outfit.",
        "why": "Tiene energía, actitud rebelde, locación limpia y el lenguaje visual característico de un drop exclusivo."
    },
    {
        "num": "06",
        "title": "Pantalones / jeans",
        "bad": "Foto de jeans para vender.",
        "good": "Modelo usando jeans rectos azul oscuro, camiseta blanca, pose caminando, fondo neutro, luz natural, enfoque en fit y silueta.",
        "pro": "Fashion campaign image focused on dark blue straight-leg jeans, model wearing a clean white t-shirt, walking pose, natural relaxed attitude, neutral beige background, soft daylight, full body shot emphasizing fit, waist, leg shape and denim texture, clean commercial fashion photography, vertical 4:5, no distorted legs, no fake logos, no unrealistic body proportions.",
        "why": "En pantalones, lo que realmente vende es el fit, la caída de la tela, la cintura y el largo de pierna."
    },
    {
        "num": "07",
        "title": "Vestidos",
        "bad": "Vestido bonito en modelo.",
        "good": "Modelo femenina usando vestido satinado negro, pose elegante, fondo nocturno minimalista, luz suave, estética sensual premium.",
        "pro": "Elegant evening fashion editorial of a female model wearing a black satin midi dress, soft fluid silhouette, graceful standing pose, minimal dark background, subtle cinematic lighting, refined sensual mood, premium partywear campaign, three-quarter full body shot, vertical 4:5, no distorted fabric, no extra fingers, no fake jewelry logos, no overexposed skin.",
        "why": "El vestido necesita movimiento, fluidez, emoción y una clara sugerencia de la ocasión de uso."
    },
    {
        "num": "08",
        "title": "Chaquetas y blazers",
        "bad": "Foto de blazer moderno.",
        "good": "Modelo usando blazer oversize color marfil, pantalón recto, fondo minimalista, pose poderosa, luz de estudio premium.",
        "pro": "Luxury fashion editorial featuring a model wearing an ivory oversized blazer with straight tailored pants, powerful confident pose, minimal warm studio background, soft sculptural lighting, sharp shoulder silhouette, elegant business-luxury aesthetic, full body editorial composition, premium campaign for social media and catalog, no fake logos, no distorted lapels, no messy wrinkles.",
        "why": "Resalta la estructura rígida de la prenda, la forma de los hombros, el poder y la categoría premium."
    },
    {
        "num": "09",
        "title": "Hoodies y sudaderas",
        "bad": "Hoodie urbano.",
        "good": "Modelo joven usando hoodie oversize gris, pantalón cargo, fondo urbano limpio, luz natural, estética casual premium.",
        "pro": "Premium casual streetwear campaign, young model wearing an oversized heather gray hoodie, black cargo pants, relaxed pose, clean urban background, soft natural daylight, cozy yet confident mood, focus on hoodie volume, hood shape and fabric texture, vertical 4:5 for Instagram, no fake logos, no distorted hood, no bad hands, no cluttered background.",
        "why": "Vende comodidad, volumen de la prenda, peso de la tela y estilo de vida moderno."
    },
    {
        "num": "10",
        "title": "Camisetas y básicos premium",
        "bad": "Camiseta blanca en modelo.",
        "good": "Modelo usando camiseta blanca premium, jeans rectos, fondo beige, luz suave, estética minimalista y limpia.",
        "pro": "Minimal premium basics campaign, model wearing a high-quality white cotton t-shirt with straight blue jeans, relaxed natural pose, warm beige studio background, soft daylight, clean composition, focus on fit, neckline, sleeve length and cotton texture, quiet luxury casual aesthetic, vertical 4:5, no transparent fabric, no fake logos, no distorted neckline, no plastic skin.",
        "why": "En básicos no vendes diseño complejo, vendes calidad percibida, caída, cuello y textura del algodón."
    },
    {
        "num": "11",
        "title": "Bolsos",
        "bad": "Bolso bonito elegante.",
        "good": "Fotografía premium de bolso negro estructurado sobre fondo beige, luz lateral suave, sombras elegantes, estética lujo moderno.",
        "pro": "Luxury handbag product photography, structured black leather handbag placed on a warm beige pedestal, soft side lighting, refined shadows, visible leather texture, minimal editorial composition, modern luxury aesthetic, high-end catalog image, square 1:1 format, no fake logos, no text, no distorted handles, no messy reflections.",
        "why": "Los bolsos necesitan estructura firme, textura del material visible, sombra real y sensación de deseo premium."
    },
    {
        "num": "12",
        "title": "Gafas y accesorios pequeños",
        "bad": "Foto de gafas fashion.",
        "good": "Close-up editorial de gafas negras sobre rostro de modelo, luz dura elegante, fondo claro, estética moderna.",
        "pro": "Close-up fashion editorial of a model wearing black rectangular sunglasses, clean skin texture, strong elegant pose, minimal light background, sharp shadow, premium accessory campaign, focus on eyewear shape, reflection control and facial attitude, high-end commercial photography, no fake logos, no distorted eyes, no warped sunglasses, no overfiltered skin.",
        "why": "En accesorios pequeños el plano cerrado (close-up) y la nitidez extrema son cruciales para vender."
    },
    {
        "num": "13",
        "title": "Activewear / fitness",
        "bad": "Mujer con ropa deportiva.",
        "good": "Modelo fitness usando conjunto deportivo negro, pose dinámica, fondo de estudio claro, luz limpia, estética fuerte y saludable.",
        "pro": "Premium activewear campaign featuring an athletic female model wearing a black seamless workout set, dynamic stretching pose, clean light gray studio background, crisp natural lighting, strong healthy body language, focus on fabric support, fit and movement, modern fitness brand aesthetic, vertical 4:5, no unrealistic body, no distorted hands, no fake logos, no oversexualized pose.",
        "why": "Vende rendimiento deportivo, elasticidad, soporte de tela, fit y confianza en el movimiento."
    },
    {
        "num": "14",
        "title": "Anuncio de venta directa",
        "bad": "Imagen para vender ropa.",
        "good": "Imagen publicitaria de pantalón beige, modelo elegante, fondo limpio, espacio libre para texto promocional, luz premium.",
        "pro": "Commercial fashion ad image for beige wide-leg pants, elegant female model standing confidently, minimal warm background, soft premium lighting, clean composition with empty space on the left for promotional text, full body shot, stylish but clear product visibility, Instagram ad format 4:5, no text inside image, no fake logos, no distorted garment, no clutter.",
        "why": "Deja espacio limpio para el copy del anuncio publicitario y mantiene la prenda totalmente visible."
    },
    {
        "num": "15",
        "title": "Stories y Reels verticales",
        "bad": "Imagen vertical de outfit.",
        "good": "Imagen vertical 9:16 de modelo caminando con outfit urbano, composición dinámica, espacio arriba para texto, luz natural.",
        "pro": "Vertical 9:16 fashion story image, model walking toward camera wearing black cargo pants and oversized white shirt, dynamic urban background, natural daylight, strong sense of movement, clean top area for story headline, commercial streetwear aesthetic, mobile-first composition, no text, no fake logos, no distorted legs, no busy background.",
        "why": "Está estructurado en proporción 9:16 nativa pensada para móviles, con espacio superior libre para títulos."
    },
    {
        "num": "16",
        "title": "Catálogo de colección",
        "bad": "Fotos de colección de ropa.",
        "good": "Serie de catálogo minimalista con modelos usando prendas coordinadas en tonos neutros, fondo blanco cálido, poses limpias, luz suave.",
        "pro": "Minimal fashion collection catalog image, three models wearing coordinated neutral outfits: beige trousers, white cotton shirt, black tailored pants, ivory blazer, warm white studio background, soft even lighting, clean standing poses, consistent styling, premium boutique aesthetic, full body composition, no fake logos, no distorted clothes, no chaotic styling.",
        "why": "Crea coherencia estética inmediata para presentar varias prendas juntas como una sola colección."
    },
    {
        "num": "17",
        "title": "Lanzamiento de colección / drop",
        "bad": "Campaña de lanzamiento de ropa.",
        "good": "Imagen teaser para lanzamiento de colección urbana, modelo parcialmente en sombra, prenda protagonista, luz dramática, ambiente misterioso.",
        "pro": "Fashion drop launch teaser, model wearing an oversized black hoodie and cargo pants, partially hidden in dramatic shadow, minimal dark urban background, cinematic side lighting, mysterious premium streetwear mood, focus on silhouette and anticipation, vertical 4:5 campaign image, no readable text, no fake logos, no distorted hands, no low quality.",
        "why": "No revela toda la prenda; crea misterio, deseo y una fuerte expectativa de lanzamiento."
    },
    {
        "num": "18",
        "title": "Campaña editorial de lujo",
        "bad": "Foto lujosa de ropa.",
        "good": "Campaña editorial de lujo con modelo elegante, blazer negro, fondo arquitectónico minimalista, luz cinematográfica, pose sofisticada.",
        "pro": "High-end luxury fashion editorial campaign, model wearing a black tailored blazer and wide-leg trousers, standing in a minimal architectural interior, sculptural cinematic lighting, elegant shadows, refined posture, quiet confidence, monochrome palette, premium magazine-style composition, vertical 4:5, no fake logos, no distorted tailoring, no excessive filters, no chaotic background.",
        "why": "Usa códigos de editorial clásica: arquitectura minimalista, sombras marcadas y silencio visual."
    },
    {
        "num": "19",
        "title": "Campaña casual lifestyle",
        "bad": "Chica casual con ropa bonita.",
        "good": "Modelo usando outfit casual premium, jeans rectos y camiseta blanca, caminando en una cafetería minimalista, luz natural cálida.",
        "pro": "Casual lifestyle fashion campaign, model wearing straight-leg blue jeans and a premium white cotton t-shirt, walking outside a minimal coffee shop, warm natural morning light, relaxed confident smile, effortless style, clean urban lifestyle aesthetic, full body shot, vertical 4:5 for Instagram, no fake logos, no distorted body, no messy background, no overposed expression.",
        "why": "Vende un estilo de vida diario aspiracional que conecta emocionalmente con el cliente, no solo la tela."
    },
    {
        "num": "20",
        "title": "Campaña con maniquí sin modelo",
        "bad": "Ropa sin persona.",
        "good": "Imagen de prenda en maniquí invisible, fondo blanco, luz suave, fit claro, estilo tienda online premium.",
        "pro": "Premium ghost mannequin product photography of black tailored pants, invisible mannequin effect, pure white background, soft even studio lighting, realistic garment shape, clear waistline and leg silhouette, ecommerce catalog style, high resolution, no human body, no fake logos, no distorted fabric, no harsh shadows, no wrinkles.",
        "why": "Ideal para tiendas online cuando no se cuenta con modelo o producción presencial, enseñando la silueta perfecta."
    }
]

# 3. Read and Parse the raw document BONUS_6_TEXT.txt
text_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\BONUS_6_TEXT.txt"
with open(text_path, "r", encoding="utf-8") as f:
    text_lines = f.readlines()

print(f"Read {len(text_lines)} lines from BONUS_6_TEXT.txt")

# Helper functions to clean and locate lines
def clean_line(l):
    return l.strip().replace(chr(8212), "-")

# Clean text replacements for common typos or encoding variations
text_content = []
for line in text_lines:
    cl = clean_line(line)
    # Replace common issues
    cl = cl.replace("Campaa", "Campaña")
    cl = cl.replace("salo", "Úsalo")
    cl = cl.replace("Cmo", "Cómo")
    cl = cl.replace("Sabas", "Sabías")
    text_content.append(cl)

prompts = []
campaigns = []
current_mode = None
current_item = None
in_pack_maestro = False

for idx, line in enumerate(text_content):
    raw_line = text_lines[idx].rstrip('\r\n')
    
    if "PACK MAESTRO" in line.upper():
        in_pack_maestro = True
        if current_item:
            if current_mode == 'prompt':
                prompts.append(current_item)
            elif current_mode == 'campaign':
                campaigns.append(current_item)
            current_item = None
            current_mode = None
        continue
        
    # Check for detailed prompt headers (e.g. PROMPT 11 - TITLE)
    if line.upper().startswith("PROMPT "):
        match = re.match(r"^PROMPT\s+(\d+)\s*[-—]\s*(.*)$", line, re.IGNORECASE)
        if match:
            if current_item:
                if current_mode == 'prompt':
                    prompts.append(current_item)
                elif current_mode == 'campaign':
                    campaigns.append(current_item)
            num = match.group(1)
            title = match.group(2).strip()
            current_mode = 'prompt'
            current_item = {
                "num": num,
                "title": title,
                "sirve_lines": [],
                "prompt_lines": [],
                "modificar_lines": [],
                "tocar_lines": [],
                "nota_lines": [],
                "current_field": None
            }
            continue
            
    # Check for campaign headers (e.g. 1. Campaña Editorial Blanca Premium)
    if in_pack_maestro:
        match_camp = re.match(r"^(\d+)\.\s*Campa[ñn]a\s+(.*)$", line, re.IGNORECASE)
        if match_camp:
            if current_item:
                if current_mode == 'prompt':
                    prompts.append(current_item)
                elif current_mode == 'campaign':
                    campaigns.append(current_item)
            num = match_camp.group(1)
            type_title = match_camp.group(2).strip()
            current_mode = 'campaign'
            current_item = {
                "num": num,
                "type": type_title,
                "name": "",
                "idea": "",
                "ideal": "",
                "adn": "",
                "styling": "",
                "storyboard_lines": [],
                "prompts": [],
                "copy_lines": [],
                "cta_lines": [],
                "current_field": None
            }
            continue
            
    # Field state tracker for prompts
    if current_mode == 'prompt' and current_item:
        if line.upper() in ["SIRVE PARA", "SIRVE PARA:", "PARA QUÉ SERVIRÁ", "PARA QUÉ SIRVE", "PARA QUÉ SIRVE:"]:
            current_item["current_field"] = 'sirve'
        elif line.upper() in ["PROMPT", "PROMPT:", "PROMPT EN INGLÉS", "PROMPT DE GENERACIÓN", "PROMPT DE GENERACIÓN:"]:
            current_item["current_field"] = 'prompt'
        elif line.upper() in ["QUÉ MODIFICAR", "QUÉ MODIFICAR:", "QUÉ SE PUEDE MODIFICAR", "QUÉ SE PUEDE MODIFICAR:"]:
            current_item["current_field"] = 'modificar'
        elif line.upper() in ["QUÉ NO TOCAR", "QUÉ NO TOCAR:", "QUÉ NO SE DEBE TOCAR", "QUÉ NO SE DEBE TOCAR:"]:
            current_item["current_field"] = 'tocar'
        elif line.upper() in ["NOTA", "NOTA:", "NOTA DE DIRECCIÓN CREATIVA", "NOTA DE DIRECCIÓN CREATIVA:"]:
            current_item["current_field"] = 'nota'
        else:
            field = current_item["current_field"]
            if field == 'sirve':
                current_item["sirve_lines"].append(line)
            elif field == 'prompt':
                current_item["prompt_lines"].append(raw_line)
            elif field == 'modificar':
                current_item["modificar_lines"].append(line)
            elif field == 'tocar':
                current_item["tocar_lines"].append(line)
            elif field == 'nota':
                current_item["nota_lines"].append(line)
                
    # Field state tracker for campaigns
    elif current_mode == 'campaign' and current_item:
        if line.upper() in ["NOMBRE DE CAMPAÑA", "NOMBRE DE CAMPAÑA:", "NOMBRE", "NOMBRE DE LA CAMPAÑA", "NOMBRE DE LA CAMPAÑA:"]:
            current_item["current_field"] = 'name'
        elif line.upper() in ["IDEA CENTRAL", "IDEA CENTRAL:", "CONCEPTO", "CONCEPTO:"]:
            current_item["current_field"] = 'idea'
        elif line.upper() in ["IDEAL PARA", "IDEAL PARA:", "PRENDAS IDEALES", "PRENDAS IDEALES:"]:
            current_item["current_field"] = 'ideal'
        elif line.upper() in ["ADN VISUAL", "ADN VISUAL:", "DIRECCIÓN DE ARTE", "DIRECCIÓN DE ARTE:"]:
            current_item["current_field"] = 'adn'
        elif line.upper() in ["DIRECCIÓN DE STYLING", "DIRECCIÓN DE STYLING:", "STYLING", "STYLING:"]:
            current_item["current_field"] = 'styling'
        elif line.upper() in ["STORYBOARD", "STORYBOARD:", "ESCENAS", "ESCENAS:"]:
            current_item["current_field"] = 'storyboard'
        elif line.upper().startswith("PROMPT"):
            current_item["current_field"] = f"prompt:{line}"
            current_item["prompts"].append({
                "label": line,
                "lines": []
            })
        elif line.upper() in ["COPY DE VENTA", "COPY DE VENTA:", "COPY DE ANUNCIO", "COPY DE ANUNCIO:", "COPY DE VENTA RÁPIDA", "COPY DE VENTA RÁPIDA:"]:
            current_item["current_field"] = 'copy'
        elif line.upper() in ["CTA", "CTA:", "CALL TO ACTION", "CALL TO ACTION:"]:
            current_item["current_field"] = 'cta'
        else:
            field = current_item["current_field"]
            if field == 'name':
                current_item["name"] = line
            elif field == 'idea':
                current_item["idea"] += (" " if current_item["idea"] else "") + line
            elif field == 'ideal':
                current_item["ideal"] += (" " if current_item["ideal"] else "") + line
            elif field == 'adn':
                current_item["adn"] += (" " if current_item["adn"] else "") + line
            elif field == 'styling':
                current_item["styling"] += (" " if current_item["styling"] else "") + line
            elif field == 'storyboard':
                current_item["storyboard_lines"].append(line)
            elif field and field.startswith("prompt:"):
                current_item["prompts"][-1]["lines"].append(raw_line)
            elif field == 'copy':
                current_item["copy_lines"].append(line)
            elif field == 'cta':
                current_item["cta_lines"].append(line)

# Add last item
if current_item:
    if current_mode == 'prompt':
        prompts.append(current_item)
    elif current_mode == 'campaign':
        campaigns.append(current_item)

# Post-process parsed lists to single strings
for p in prompts:
    p["sirve"] = " ".join(p["sirve_lines"]).strip()
    p["prompt"] = "\n".join(p["prompt_lines"]).strip()
    p["modificar"] = " ".join(p["modificar_lines"]).strip()
    p["tocar"] = " ".join(p["tocar_lines"]).strip()
    p["nota"] = " ".join(p["nota_lines"]).strip()

for c in campaigns:
    c["storyboard"] = "\n".join(c["storyboard_lines"]).strip()
    for pr in c["prompts"]:
        pr["value"] = "\n".join(pr["lines"]).strip()
    c["copy"] = "\n".join(c["copy_lines"]).strip()
    c["cta"] = "\n".join(c["cta_lines"]).strip()

print(f"Successfully structured {len(prompts)} Prompts and {len(campaigns)} Campaigns.")

# 4. Define text helper function to slice sections of the document
def extract_section_lines(start_header, end_header=None):
    start_idx = -1
    for idx, line in enumerate(text_content):
        if start_header.upper() in line.upper():
            start_idx = idx
            break
    if start_idx == -1:
        return []
    
    end_idx = len(text_content)
    if end_header:
        for idx in range(start_idx + 1, len(text_content)):
            if end_header.upper() in text_content[idx].upper():
                end_idx = idx
                break
    return [l for l in text_content[start_idx+1:end_idx] if l]

# 5. Extract Closing Sections and Guidelines
criterio_lines = extract_section_lines("19. CÓMO SABER QUÉ PROMPT USAR", "20. CÓMO MODIFICAR UN PROMPT SIN DAÑARLO")
modificar_guidelines_lines = extract_section_lines("20. CÓMO MODIFICAR UN PROMPT SIN DAÑARLO", "21. CÓMO PEDIR VARIACIONES AL AGENTE CREATIVO")
variaciones_lines = extract_section_lines("21. CÓMO PEDIR VARIACIONES AL AGENTE CREATIVO", "22. ERRORES COMUNES AL USAR PROMPTS DE MODA")
errores_lines = extract_section_lines("22. ERRORES COMUNES AL USAR PROMPTS DE MODA", "23. EJERCICIO FINAL DEL BONUS")
ejercicio_lines = extract_section_lines("23. EJERCICIO FINAL DEL BONUS", "24. TRANSFORMACIÓN FINAL DEL BONUS")
transformacion_lines = extract_section_lines("24. TRANSFORMACIÓN FINAL DEL BONUS", "25. CIERRE PARA EL ALUMNO")
cierre_lines = extract_section_lines("25. CIERRE PARA EL ALUMNO", "PACK MAESTRO")
checklist_lines = extract_section_lines("Checklist final de producción")

# 6. Format closing sections into HTML blocks
criterio_html = ""
for line in criterio_lines:
    if line.startswith("Si la persona tiene") or line.startswith("Si tiene") or line.startswith("Si quiere"):
        criterio_html += f"<p style='margin-top: 1rem; color: var(--color-cyan-glow); font-weight: bold;'>{line}</p>"
    else:
        criterio_html += f"<p style='margin-left: 1.5rem; opacity: 0.9;'>&bull; {line}</p>"

modificar_html = ""
for line in modificar_guidelines_lines:
    if "EJEMPLO" in line.upper() or "PROMPT BASE:" in line.upper() or "ADAPTACIÓN PARA MARCA" in line.upper():
        modificar_html += f"<pre style='font-family: var(--font-mono); font-size: 0.82rem; background: var(--color-bg-dark); padding: 0.8rem; border-left: 2px solid var(--color-cobalt-primary); margin: 0.5rem 0;'>{line}</pre>"
    elif "CAMBIÓ:" in line.upper() or "PERO SE MANTIENE:" in line.upper():
        modificar_html += f"<p style='color: var(--color-cyan-glow); margin-top: 0.8rem; font-weight: bold;'>{line}</p>"
    else:
        modificar_html += f"<p style='margin-bottom: 0.6rem;'>{line}</p>"

variaciones_html = ""
current_var_block = ""
for line in variaciones_lines:
    if line.startswith("Para "):
        if current_var_block:
            variaciones_html += f"<div class='copy-box' style='margin-bottom: 1.5rem;'><pre class='copy-target'>{current_var_block}</pre><button class='copy-btn copy-inline-btn' type='button'>Copiar Orden</button></div>"
        variaciones_html += f"<h4 style='color: var(--color-cyan-glow); font-family: var(--font-heavy); font-size: 1.1rem; text-transform: uppercase; margin: 1.5rem 0 0.5rem;'>{line}</h4>"
        current_var_block = ""
    else:
        current_var_block += ("\n" if current_var_block else "") + line
if current_var_block:
    variaciones_html += f"<div class='copy-box'><pre class='copy-target'>{current_var_block}</pre><button class='copy-btn copy-inline-btn' type='button'>Copiar Orden</button></div>"

errores_html = ""
for line in errores_lines:
    if line.startswith("Error "):
        errores_html += f"<h4 style='color: var(--color-red-light); font-family: var(--font-heavy); font-size: 1.1rem; margin-top: 1.5rem;'>{line}</h4>"
    elif line.startswith("Mejor:"):
        errores_html += f"<p style='color: var(--color-green-light); font-family: var(--font-mono); font-size: 0.9rem; padding-left: 0.8rem; border-left: 2px solid var(--color-green); margin: 0.5rem 0;'>{line}</p>"
    elif line.startswith("Siempre agrega:") or line.startswith("Define:") or line.startswith("Cambia solo:") or line.startswith("Siempre agrega:"):
        errores_html += f"<p style='font-weight: bold; margin-top: 0.8rem;'>{line}</p>"
    else:
        errores_html += f"<p style='margin-bottom: 0.5rem; opacity: 0.9;'>{line}</p>"

ejercicio_html = "<div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;'>"
curr_step = ""
step_num = 1
for line in ejercicio_lines:
    if line.startswith("Paso "):
        if curr_step:
            ejercicio_html += f"<div class='card-brutal' style='margin-bottom: 0; padding: 1.5rem;'><h4 style='color: var(--color-cyan-glow); margin-bottom: 0.5rem;'>PASO {step_num}</h4><p style='font-size: 0.9rem;'>{curr_step}</p></div>"
            step_num += 1
        curr_step = line
    else:
        curr_step += " &mdash; " + line
if curr_step:
    ejercicio_html += f"<div class='card-brutal' style='margin-bottom: 0; padding: 1.5rem;'><h4 style='color: var(--color-cyan-glow); margin-bottom: 0.5rem;'>PASO {step_num}</h4><p style='font-size: 0.9rem;'>{curr_step}</p></div>"
ejercicio_html += "</div>"

transformacion_html = ""
for line in transformacion_lines:
    if line.startswith("Antes:") or line.startswith("Después:") or line.startswith("Antes dependía") or line.startswith("Antes empezaba") or line.startswith("Antes generaba"):
        transformacion_html += f"<p style='font-family: var(--font-mono); font-size: 0.95rem; margin-bottom: 0.4rem; padding-left: 0.8rem; border-left: 2px solid var(--color-cobalt-primary);'>{line}</p>"
    else:
        transformacion_html += f"<p style='margin-bottom: 0.8rem;'>{line}</p>"

cierre_html = ""
for line in cierre_lines:
    cierre_html += f"<p style='margin-bottom: 0.8rem; line-height: 1.7;'>{line}</p>"

checklist_html = ""
for line in checklist_lines:
    if "?" in line:
        questions = line.split("?")
        checklist_html += "<ul class='styled-list' style='columns: 2; gap: 2rem; margin-top: 1rem;'>"
        for q in questions:
            q_s = q.strip()
            if q_s:
                checklist_html += f"<li style='margin-bottom: 0.8rem;'><strong>{q_s}?</strong></li>"
        checklist_html += "</ul>"
    else:
        checklist_html += f"<p style='margin-top: 1.2rem; font-style: italic; opacity: 0.8;'>{line}</p>"

# 7. Extract the Banco de Variables data (Section 18)
variables_lines = extract_section_lines("18. BANCO DE VARIABLES PARA ADAPTAR PROMPTS", "19. CÓMO SABER QUÉ PROMPT USAR")
variables_categories = {}
curr_var_cat = None
for line in variables_lines:
    if line in ["Modelos femeninos", "Modelos masculinos", "Fondos", "Luces", "Cámaras", "Poses", "Realismo", "Restricciones negativas"]:
        curr_var_cat = line
        variables_categories[curr_var_cat] = []
    elif curr_var_cat:
        variables_categories[curr_var_cat].append(line)

variables_table_html = "<div class='variables-table-container'><table class='variables-table'><thead><tr><th>Categoría</th><th>Valores / Fórmulas Adaptables (Haz click para copiar)</th></tr></thead><tbody>"
for cat, items in variables_categories.items():
    items_html = ""
    for item in items:
        items_html += f"<div class='prompt-container' style='margin: 0.4rem 0; display: inline-flex; width: 100%; align-items: center; justify-content: space-between; padding: 0.5rem 1rem;'><span class='copy-target' style='font-family: var(--font-mono); font-size: 0.8rem;'>{item}</span><button class='copy-btn copy-inline-btn' type='button' style='padding: 0.2rem 0.6rem; font-size: 0.65rem;'>Copiar</button></div>"
    variables_table_html += f"<tr><td><strong class='variable-tag'>{cat}</strong></td><td>{items_html}</td></tr>"
variables_table_html += "</tbody></table></div>"

# 8. Merge Prompts 1-10 into the hardcoded 10 Garments guides
garments_data = [
    {
        "num": 1,
        "title": "1. Camisetas, tops y básicos",
        "serves": "Marcas que venden camisetas, tops, crop tops, tank tops, polos o básicos de algodón.",
        "show": "Fit, caída, textura del algodón, terminación del cuello, mangas, largo y estampado si tiene.",
        "styles": "Fondo blanco de estudio, lookbook minimalista, editorial de calle, lifestyle casual.",
        "terms": "white t-shirt editorial, minimal fashion basics, premium cotton clothing lookbook.",
        "care": "Exigir arrugas de tela naturales, hombros relajados, cuello realista y proporciones humanas."
    },
    {
        "num": 2,
        "title": "2. Hoodies, buzos y sudaderas",
        "serves": "Buzos, hoodies, sweatshirts, drops de ropa urbana y colecciones cómodas.",
        "show": "Volumen, peso de la tela, capucha estructurada, mangas amplias, costuras y costados relajados.",
        "styles": "Streetwear editorial, fondo de concreto, estudio industrial brutalista, look nocturno.",
        "terms": "oversized hoodie campaign, streetwear lookbook, concrete background fashion shoot.",
        "care": "Pedir 'heavy cotton fleece', 'visible fabric weight' y 'hood structure visible'."
    },
    {
        "num": 3,
        "title": "3. Jeans, denim y pantalones",
        "serves": "Jeans, cargo pants, pantalones wide leg, joggers, chaquetas denim y sets coordinados.",
        "show": "Fit de piernas, talle de cintura, caída, costuras visibles, bolsillos y lavado del color.",
        "styles": "Cuerpo completo de estudio, calle editorial, plano de detalle de costuras.",
        "terms": "denim campaign photography, wide leg jeans editorial, cargo pants streetwear.",
        "care": "Forzar cuerpo completo o plano de 3/4. Pedir 'visible seams' y 'natural folds at knees'."
    },
    {
        "num": 4,
        "title": "4. Vestidos, faldas y siluetas femeninas",
        "serves": "Vestidos casuales, vestidos elegantes satinados, faldas fluidas y sets románticos.",
        "show": "Silueta general, caída fluida de la tela, vuelo, movimiento y largo relativo.",
        "styles": "Editorial femenino, luz natural suave, estudio minimalista, exterior mediterráneo.",
        "terms": "flowing dress campaign, minimal feminine editorial, romantic fashion photoshoot.",
        "care": "Pedir 'fabric movement', 'soft drape' y evitar poses rígidas que congelen la tela."
    },
    {
        "num": 5,
        "title": "5. Streetwear y drops urbanos",
        "serves": "Marcas de ropa urbana, camisetas gráficas gigantes, gorras, chaquetas y drops de stock limitado.",
        "show": "Actitud, capas de prendas (layering), fit oversized y estética urbana contemporánea.",
        "styles": "Calle brutalista, flash directo, estación de metro, parking urbano, pared de concreto.",
        "terms": "urban fashion drop, brutalist streetwear campaign, direct flash streetwear.",
        "care": "Pedir 'urban attitude', 'relaxed posture' y 'concrete background'. Evitar looks de disfraz."
    },
    {
        "num": 6,
        "title": "6. Fitness, activewear y athleisure",
        "serves": "Leggings, tops deportivos, shorts seamless, bikers y marcas deportivas urbanas.",
        "show": "Elasticidad, compresión, costuras reforzadas, ajuste al cuerpo y ergonomía del movimiento.",
        "styles": "Estudio fitness limpio, gimnasio premium, exterior de running, plano macro de textura.",
        "terms": "premium activewear campaign, fitness apparel editorial, sportswear model photography.",
        "care": "Pedir 'performance fabric', 'stretch texture', 'body in motion' y 'sweat glow natural'."
    },
    {
        "num": 7,
        "title": "7. Chaquetas, abrigos y capas exteriores",
        "serves": "Chaquetas denim, bombers, blazers, trench coats, puffers y abrigos pesados.",
        "show": "Estructura, hombros marcados, volumen, capas y la textura exterior (piel, plumas, nylon).",
        "styles": "Editorial de calle en invierno, estudio premium gris, fondo arquitectónico minimalista.",
        "terms": "jacket editorial campaign, outerwear fashion photography, trench coat editorial.",
        "care": "Pedir 'structured shoulders', 'visible garment volume' y 'outerwear silhouette'."
    },
    {
        "num": 8,
        "title": "8. Tejidos, knitwear y prendas texturizadas",
        "serves": "Sweaters, cardigans, polos tejidos, chalecos de punto y prendas crochet artesanales.",
        "show": "Trama del tejido, grosor del hilo, suavidad visual, relieve e imperfecciones de punto.",
        "styles": "Luz lateral suave, primer plano macro de tejido, cafetería de tarde, lookbook acogedor.",
        "terms": "knitwear editorial photography, sweater campaign studio, textured knit close-up.",
        "care": "Forzar 'visible knit texture', 'soft yarn fibers' y 'macro fabric detail'."
    },
    {
        "num": 9,
        "title": "9. Accesorios, bolsos y joyería",
        "serves": "Bolsos de cuero, collares, anillos, gafas de sol, gorras y accesorios pequeños.",
        "show": "Escala del producto respecto al cuerpo, textura del material, brillos metálicos y detalles.",
        "styles": "Still life sobre pedestales, close-up del modelo usando el accesorio, detalle macro.",
        "terms": "handbag editorial photography, jewelry close-up fashion, sunglasses campaign.",
        "care": "Pedir 'sharp product detail', 'natural hand placement' y 'realistic material texture'."
    },
    {
        "num": 10,
        "title": "10. Calzado, tenis y sandalias",
        "serves": "Tenis, sneakers urbanos, botas de cuero, tacones elegantes y calzado deportivo.",
        "show": "Forma y horma del zapato, suela, texturas (cuero, malla, goma) y costuras.",
        "styles": "Still life en estudio, modelo caminando en la calle, plano de cámara bajo.",
        "terms": "sneaker campaign photography, footwear editorial, low angle shoe photography.",
        "care": "Pedir 'low angle product focus', 'accurate shoe shape' y 'visible sole detail'."
    }
]

# Extract Prompts 1 to 10 from our parsed prompts list
prompt_map_1_10 = {int(p["num"]): p for p in prompts if int(p["num"]) <= 10}

garments_html = ""
for idx, gar in enumerate(garments_data):
    num_key = gar["num"]
    matching_prompt = prompt_map_1_10.get(num_key)
    prompt_snippet = ""
    
    if matching_prompt:
        prompt_snippet = f"""
        <div class="prompt-container" style="margin-top: 1.5rem;">
          <div class="prompt-header">
            <span class="prompt-label" style="color: var(--color-cyan-glow);">FÓRMULA DE PROMPT PRO COPIAR-PEGAR</span>
            <button class="copy-btn" type="button">
              <svg style="width: 12px; height: 12px; fill: currentColor;" viewBox="0 0 24 24">
                <use href="#copy-svg"></use>
              </svg>
              Copiar Prompt
            </button>
          </div>
          <pre class="prompt-text" style="font-size: 0.85rem;">{matching_prompt['prompt']}</pre>
        </div>
        """
    
    garments_html += f"""
    <div class="garment-card reveal-element">
      <h3 class="garment-title">{gar['title']}</h3>
      
      <div class="garment-section">
        <div class="garment-section-title">Para qué sirve:</div>
        <div class="garment-section-body">{gar['serves']}</div>
      </div>
      
      <div class="garment-section">
        <div class="garment-section-title">Qué necesita mostrar:</div>
        <div class="garment-section-body">{gar['show']}</div>
      </div>
      
      <div class="garment-section">
        <div class="garment-section-title">Estilos recomendados:</div>
        <div class="garment-section-body">{gar['styles']}</div>
      </div>
      
      <div class="garment-section">
        <div class="garment-section-title">Términos de búsqueda útiles (Inglés):</div>
        <div class="garment-section-body" style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--color-cobalt-light);">{gar['terms']}</div>
      </div>
      
      <div class="garment-section">
        <div class="garment-section-title">Qué cuidar en el prompt:</div>
        <div class="garment-section-body" style="border-left: 2.5px solid var(--color-cyan-glow); padding-left: 0.8rem; font-style: italic;">{gar['care']}</div>
      </div>
      
      {prompt_snippet}
    </div>
    """

# 9. Format Detailed Prompts 11 to 47
prompts_by_group = {
    "Modelos Femeninos (11-13)": [],
    "Modelos Masculinos (14-16)": [],
    "Fondos y Escenarios (17-21)": [],
    "Estilo Estudio (22-24)": [],
    "Fotos Editoriales (25-27)": [],
    "Piezas de Anuncios (28-31)": [],
    "Producto Solo (32-34)": [],
    "Campañas Completas (35-38)": [],
    "Pack Realista (39-47)": []
}

for p in prompts:
    num = int(p["num"])
    if 11 <= num <= 13:
        prompts_by_group["Modelos Femeninos (11-13)"].append(p)
    elif 14 <= num <= 16:
        prompts_by_group["Modelos Masculinos (14-16)"].append(p)
    elif 17 <= num <= 21:
        prompts_by_group["Fondos y Escenarios (17-21)"].append(p)
    elif 22 <= num <= 24:
        prompts_by_group["Estilo Estudio (22-24)"].append(p)
    elif 25 <= num <= 27:
        prompts_by_group["Fotos Editoriales (25-27)"].append(p)
    elif 28 <= num <= 31:
        prompts_by_group["Piezas de Anuncios (28-31)"].append(p)
    elif 32 <= num <= 34:
        prompts_by_group["Producto Solo (32-34)"].append(p)
    elif 35 <= num <= 38:
        prompts_by_group["Campañas Completas (35-38)"].append(p)
    elif 39 <= num <= 47:
        prompts_by_group["Pack Realista (39-47)"].append(p)

detailed_prompts_html = ""
for group_name, group_prompts in prompts_by_group.items():
    detailed_prompts_html += f"""
    <div style="margin-top: 3.5rem;">
      <h3 style="font-family: var(--font-heavy); font-size: 1.8rem; text-transform: uppercase; color: var(--color-cobalt-light); border-bottom: 2.5px solid var(--color-cobalt-primary); padding-bottom: 0.5rem; margin-bottom: 2rem;">{group_name}</h3>
      <div class="boveda-grid">
    """
    for p in group_prompts:
        meta_html = ""
        if p["modificar"]:
            meta_html += f"<p class='prompt-detail-meta'><strong>Qué modificar:</strong> {p['modificar']}</p>"
        if p["tocar"]:
            meta_html += f"<p class='prompt-detail-meta'><strong>Qué no tocar:</strong> {p['tocar']}</p>"
        if p["nota"]:
            meta_html += f"<p class='prompt-detail-note'><strong>Nota de Dirección Creativa:</strong> {p['nota']}</p>"
            
        detailed_prompts_html += f"""
        <div class="prompt-detail-card reveal-element">
          <div class="prompt-detail-header">
            <span class="prompt-detail-num">PROMPT {p['num']}</span>
            <h3 class="prompt-detail-title">{p['title']}</h3>
          </div>
          <div class="prompt-detail-body">
            <p class="prompt-detail-desc"><strong>Sirve para:</strong> {p['sirve']}</p>
            
            <div class="prompt-container">
              <div class="prompt-header">
                <span class="prompt-label" style="color: var(--color-cyan-glow);">FÓRMULA TÉCNICA</span>
                <button class="copy-btn" type="button">
                  <svg style="width: 12px; height: 12px; fill: currentColor;" viewBox="0 0 24 24">
                    <use href="#copy-svg"></use>
                  </svg>
                  Copiar Prompt
                </button>
              </div>
              <pre class="prompt-text" style="font-size: 0.85rem;">{p['prompt']}</pre>
            </div>
            {meta_html}
          </div>
        </div>
        """
    detailed_prompts_html += "</div></div>"

# 10. Format Pack Maestro (25 Campaigns Accordion)
campaigns_html = "<div class='accordion-container'>"
for c in campaigns:
    prompts_snippets = ""
    for pr in c["prompts"]:
        prompts_snippets += f"""
        <div class="prompt-container" style="margin: 0;">
          <div class="prompt-header">
            <span class="prompt-label" style="color: var(--color-cobalt-light);">{pr['label'].upper()}</span>
            <button class="copy-btn" type="button">
              <svg style="width: 12px; height: 12px; fill: currentColor;" viewBox="0 0 24 24">
                <use href="#copy-svg"></use>
              </svg>
              Copiar
            </button>
          </div>
          <pre class="prompt-text" style="font-size: 0.85rem; max-height: 250px; background-color: #010006;">{pr['value']}</pre>
        </div>
        """
        
    campaigns_html += f"""
    <div class="accordion-item reveal-element">
      <button class="accordion-trigger" type="button">
        <div>
          <span class="accordion-num">CAMPAÑA {c['num']}</span>
          <span class="accordion-title">{c['type']} &mdash; <span class="trends" style="color: var(--color-cyan-glow);">{c['name']}</span></span>
        </div>
        <span class="accordion-icon">+</span>
      </button>
      
      <div class="accordion-content">
        <div class="campaign-detail-grid">
          <div class="campaign-info">
            <p><strong>Idea central:</strong> {c['idea']}</p>
            <p><strong>Ideal para:</strong> {c['ideal']}</p>
            <p><strong>ADN visual:</strong> {c['adn']}</p>
            <p><strong>Dirección de styling:</strong> {c['styling']}</p>
          </div>
          <div class="campaign-storyboard">
            <h4>Storyboard / Escenas</h4>
            <pre>{c['storyboard']}</pre>
          </div>
        </div>
        
        <div class="campaign-prompts">
          <h4>Bóveda de Prompts de Campaña</h4>
          <div class="campaign-prompts-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
            {prompts_snippets}
          </div>
        </div>
        
        <div class="campaign-copies">
          <div class="copy-box">
            <h4>Copy de Venta Recomendado</h4>
            <pre class="copy-target" style="font-size: 0.88rem; opacity: 0.95;">{c['copy']}</pre>
            <button class="copy-btn copy-inline-btn" type="button">Copiar Copy</button>
          </div>
          <div class="cta-box">
            <h4>CTA (Call to Action)</h4>
            <pre class="copy-target" style="font-size: 0.88rem; opacity: 0.95;">{c['cta']}</pre>
            <button class="copy-btn copy-inline-btn" type="button">Copiar CTA</button>
          </div>
        </div>
      </div>
    </div>
    """
campaigns_html += "</div>"

# 11. Define structured data for the 20 Categories (first 20 categories HTML)
categories_html = ""
for cat in categories_data:
    categories_html += f"""
    <div class="library-card reveal-element">
      <div class="library-card-header">
        <span class="library-card-num">CATEGORÍA {cat['num']}</span>
        <h3 class="library-card-title">{cat['title']}</h3>
        <span class="library-card-tag">Editorial</span>
      </div>
      
      <div class="compare-grid" style="margin-bottom: 1.5rem;">
        <div class="compare-box bad">
          <div class="compare-badge bad">Mal Prompt</div>
          <div class="compare-title bad">Evitar simplicidad</div>
          <p class="text-editorial" style="font-size: 0.95rem; font-style: italic; color: #ff8a9a;">"{cat['bad']}"</p>
        </div>
        <div class="compare-box good">
          <div class="compare-badge good">Buen Prompt</div>
          <div class="compare-title good">Estructura descriptiva</div>
          <p class="text-editorial" style="font-size: 0.95rem; font-weight: 500; color: var(--color-green-light);">"{cat['good']}"</p>
        </div>
      </div>
      
      <div class="prompt-container">
        <div class="prompt-header">
          <span class="prompt-label" style="color: var(--color-cobalt-glow);">PROMPT PRO (INGLÉS / IA DIRECTO)</span>
          <button class="copy-btn" type="button">
            <svg style="width: 12px; height: 12px; fill: currentColor;" viewBox="0 0 24 24">
              <use href="#copy-svg"></use>
            </svg>
            Copiar Prompt
          </button>
        </div>
        <pre class="prompt-text">{cat['pro']}</pre>
      </div>
      
      <div class="library-card-why">
        <strong>Por qué funciona:</strong>
        {cat['why']}
      </div>
    </div>
    """

conceptos_html = """
<section id="manifiesto">
  <div class="sticker-cobalt">BONUS 6</div>
  
  <div class="section-meta">
    <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
    <span>[ SECCIÓN 01 / EL MANIFIESTO ]</span>
  </div>

  <h2 class="section-title">
    LA BÓVEDA DE PROMPTS PARA <span class="trends">DEJAR DE IMPROVISAR</span>
  </h2>
  
  <div class="text-editorial" style="display: flex; flex-direction: column; gap: 1.5rem; margin-bottom: 3.5rem;">
    <p style="font-size: 1.25rem; font-weight: 700; line-height: 1.6; border-left: 3.5px solid var(--color-cobalt-primary); padding-left: 1.2rem;">
      Este bonus existe para resolver un problema muy concreto: el bloqueo frente al generador de imágenes. Sabes qué quieres vender, tienes prendas y referencias, pero cuando llega el momento de escribir... la IA crea imágenes planas o plásticas que gritan "INTELIGENCIA ARTIFICIAL" y destruyen tu credibilidad comercial.
    </p>
    
    <p>
      La <strong>Biblioteca Copiar-Pegar de Prompts Editoriales</strong> es la respuesta a ese bloqueo. No es una lista decorativa de frases bonitas ni una colección de prompts al azar. Es un sistema de dirección creativa para que puedas pasar de tener una prenda física a producir una campaña visual completa y coherente con intención de venta, gratis y en minutos.
    </p>

    <div class="card-brutal" style="margin-top: 1.5rem;">
      <h3 style="font-family: var(--font-heavy); font-size: 1.4rem; color: var(--color-cobalt-light); margin-bottom: 1rem; text-transform: uppercase;">
        LO QUE LOGRARÁS CON ESTA BIBLIOTECA
      </h3>
      <ul class="styled-list">
        <li><strong>Crear imágenes de moda coherentes</strong> con prompts estructurados y ya probados.</li>
        <li><strong>Adaptar una misma base de prompt</strong> a diferentes prendas, modelos, fondos y estilos sin perder calidad.</li>
        <li><strong>Producir de forma organizada</strong> para campañas femeninas, masculinas, streetwear, activewear y bodegones.</li>
        <li><strong>Dejar de depender del azar</strong> y empezar a dirigir a la IA como una Directora Creativa Senior.</li>
      </ul>
    </div>
  </div>
</section>

<section id="prompt-engineering">
  <div class="section-meta">
    <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
    <span>[ SECCIÓN 02 / PROMPT ENGINEERING EN MODA ]</span>
  </div>
  
  <h2 class="section-title">¿Qué es realmente <span class="trends">Prompt Engineering</span> en moda?</h2>
  
  <div class="text-editorial" style="display: flex; flex-direction: column; gap: 1.5rem;">
    <p>
      Prompt engineering es aprender a darle instrucciones técnicas claras a una IA para que produzca una imagen con intención de marca. Escribir <em>“Modelo usando pantalón bonito”</em> es inútil. Un prompt profesional detalla:
    </p>
    <div style="font-family: var(--font-mono); font-size: 0.95rem; background-color: var(--color-bg-dark); padding: 1.5rem; border: var(--border-brutal-thin); border-radius: 4px; line-height: 1.8;">
      <span style="color: var(--color-cobalt-glow);">[FÓRMULA MADRE]:</span> Sujeto + Prenda + Estilo + Pose + Ambiente + Luz + Cámara + Composición + Emoción + Uso comercial + Formato + Negativos
    </div>
    
    <h3 style="font-family: var(--font-heavy); font-size: 1.6rem; margin-top: 2rem; color: var(--color-cobalt-light);">
      LOS FORMATOS DE PROMPTS QUE DEBES DOMINAR
    </h3>
    
    <div class="tab-container" style="margin-top: 1.5rem;">
      <div class="tab-nav">
        <button class="tab-btn active" type="button" data-target="format-es">Español Natural</button>
        <button class="tab-btn" type="button" data-target="format-en">Inglés Natural</button>
        <button class="tab-btn" type="button" data-target="format-sections">Por Secciones</button>
        <button class="tab-btn" type="button" data-target="format-json">Formato JSON</button>
        <button class="tab-btn" type="button" data-target="format-root">Palabra Raíz</button>
      </div>
      
      <div id="format-es" class="tab-pane active">
        <p style="margin-bottom: 1rem;"><strong>Prompt en Español Natural:</strong> Útil para maquetar ideas y estructurar bocetos rápidamente.</p>
        <div class="prompt-container">
          <div class="prompt-header"><span class="prompt-label">Español</span></div>
          <div class="prompt-text">Crea una imagen editorial de moda para un pantalón negro de tiro alto, con modelo femenina elegante, pose segura, fondo gris minimalista, iluminación suave de estudio, estética premium, composición limpia para anuncio de Instagram.</div>
        </div>
      </div>
      
      <div id="format-en" class="tab-pane">
        <p style="margin-bottom: 1rem;"><strong>Prompt en Inglés Natural:</strong> Las IA de imagen entienden mejor el vocabulario fotográfico en inglés debido a sus bases de entrenamiento.</p>
        <div class="prompt-container">
          <div class="prompt-header"><span class="prompt-label">Inglés</span></div>
          <div class="prompt-text">High-end fashion editorial image of a female model wearing black high-waisted tailored pants, confident pose, minimal gray studio background, soft diffused lighting, clean luxury aesthetic, full body composition, premium Instagram ad, vertical 4:5 format.</div>
        </div>
      </div>
      
      <div id="format-sections" class="tab-pane">
        <p style="margin-bottom: 1rem;"><strong>Prompt por Secciones:</strong> Organiza la instrucción en bloques técnicos para garantizar consistencia visual.</p>
        <div class="prompt-container">
          <div class="prompt-header"><span class="prompt-label">Secciones</span></div>
          <pre class="prompt-text">SUBJECT: Female fashion model
GARMENT: Black high-waisted tailored pants
POSE: Confident standing pose, one hand in pocket
LOCATION: Gray studio background
LIGHTING: Soft diffused studio light
CAMERA: Full body shot, 85mm fashion photography
MOOD: Sophisticated, premium
NEGATIVE: distorted hands, fake logos, messy background, low quality</pre>
        </div>
      </div>
      
      <div id="format-json" class="tab-pane">
        <p style="margin-bottom: 1rem;"><strong>Prompt en JSON:</strong> Permite controlar el estilo y la producción como si fuera una ficha técnica de fábrica.</p>
        <div class="prompt-container">
          <div class="prompt-header"><span class="prompt-label">JSON</span></div>
          <pre class="prompt-text">{
  "image_type": "fashion editorial campaign",
  "subject": "female model",
  "garment": "black high-waisted tailored pants",
  "silhouette": "elegant, structured",
  "pose": "standing confidently, one hand in pocket",
  "location": "minimal gray studio",
  "lighting": "soft diffused luxury lighting",
  "camera": "full body shot, 85mm lens",
  "negative_prompt": "deformed hands, fake logos, distorted clothing, messy background, low resolution"
}</pre>
        </div>
      </div>
      
      <div id="format-root" class="tab-pane">
        <p style="margin-bottom: 1rem;"><strong>Palabra Raíz (Ej: "NOCTURNA"):</strong> Una sola palabra que funciona como el ADN emocional del drop visual.</p>
        <div class="prompt-container">
          <div class="prompt-header"><span class="prompt-label">Palabra Raíz</span></div>
          <div class="prompt-text">Campaña inspirada en la palabra NOCTURNA: estética de noche, tonos negro profundo y plata, iluminación lateral dramática, fondo urbano nocturno limpio, prendas estructuradas, sensación de poder silencioso, lujo moderno.</div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

anatomia_html = """
<section id="anatomia">
  <div class="section-meta">
    <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
    <span>[ SECCIÓN 05 / ANATOMÍA DE UN PROMPT ]</span>
  </div>
  
  <h2 class="section-title">Anatomía de un <span class="trends">PROMPT EDITORIAL</span></h2>
  
  <div class="text-editorial" style="display: flex; flex-direction: column; gap: 1.5rem;">
    <p>
      Para dejar de improvisar, divide tus instrucciones en estas 11 capas de producción técnica:
    </p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
      <div class="card-brutal" style="padding: 1.5rem; margin-bottom: 0;">
        <h4 style="color: var(--color-cobalt-light); font-family: var(--font-mono); font-size: 0.95rem; margin-bottom: 0.5rem;">1. Task</h4>
        <p style="font-size: 0.88rem; opacity: 0.95;">Define qué debe hacer la IA (ej. generate, edit, create campaign image).</p>
      </div>
      <div class="card-brutal" style="padding: 1.5rem; margin-bottom: 0;">
        <h4 style="color: var(--color-cobalt-light); font-family: var(--font-mono); font-size: 0.95rem; margin-bottom: 0.5rem;">2. Subject</h4>
        <p style="font-size: 0.88rem; opacity: 0.95;">Define quién o qué aparece en la imagen (edad, complexión, etnicidad, expresión).</p>
      </div>
      <div class="card-brutal" style="padding: 1.5rem; margin-bottom: 0;">
        <h4 style="color: var(--color-cobalt-light); font-family: var(--font-mono); font-size: 0.95rem; margin-bottom: 0.5rem;">3. Wardrobe</h4>
        <p style="font-size: 0.88rem; opacity: 0.95;">Detalla las prendas, color exacto, fit (fitted, oversized) y la caída en el cuerpo.</p>
      </div>
      <div class="card-brutal" style="padding: 1.5rem; margin-bottom: 0;">
        <h4 style="color: var(--color-cobalt-light); font-family: var(--font-mono); font-size: 0.95rem; margin-bottom: 0.5rem;">4. Environment</h4>
        <p style="font-size: 0.88rem; opacity: 0.95;">Establece el fondo o entorno físico (estudio blanco, calle concreta, rooftop de tarde).</p>
      </div>
      <div class="card-brutal" style="padding: 1.5rem; margin-bottom: 0;">
        <h4 style="color: var(--color-cobalt-light); font-family: var(--font-mono); font-size: 0.95rem; margin-bottom: 0.5rem;">5. Lighting</h4>
        <p style="font-size: 0.88rem; opacity: 0.95;">Decide el esquema de iluminación (soft studio lighting, direct hard sunlight, flash).</p>
      </div>
      <div class="card-brutal" style="padding: 1.5rem; margin-bottom: 0;">
        <h4 style="color: var(--color-cobalt-light); font-family: var(--font-mono); font-size: 0.95rem; margin-bottom: 0.5rem;">6. Camera</h4>
        <p style="font-size: 0.88rem; opacity: 0.95;">Especificaciones fotográficas: tipo de cámara, lente (85mm para retratos, 35mm para calle).</p>
      </div>
      <div class="card-brutal" style="padding: 1.5rem; margin-bottom: 0;">
        <h4 style="color: var(--color-cobalt-light); font-family: var(--font-mono); font-size: 0.95rem; margin-bottom: 0.5rem;">7. Pose</h4>
        <p style="font-size: 0.88rem; opacity: 0.95;">La actitud corporal (standing relaxed, walking mid-step, hands in pockets).</p>
      </div>
      <div class="card-brutal" style="padding: 1.5rem; margin-bottom: 0;">
        <h4 style="color: var(--color-cobalt-light); font-family: var(--font-mono); font-size: 0.95rem; margin-bottom: 0.5rem;">8. Expression</h4>
        <p style="font-size: 0.88rem; opacity: 0.95;">La emoción facial que evita la rigidez de maniquí (neutral, confident, calm).</p>
      </div>
      <div class="card-brutal" style="padding: 1.5rem; margin-bottom: 0;">
        <h4 style="color: var(--color-cobalt-light); font-family: var(--font-mono); font-size: 0.95rem; margin-bottom: 0.5rem;">9. Composition</h4>
        <p style="font-size: 0.88rem; opacity: 0.95;">Disposición en el frame: espacio vacío (aire) para copy, centered, Rule of Thirds.</p>
      </div>
      <div class="card-brutal" style="padding: 1.5rem; margin-bottom: 0;">
        <h4 style="color: var(--color-cobalt-light); font-family: var(--font-mono); font-size: 0.95rem; margin-bottom: 0.5rem;">10. Realism constraints</h4>
        <p style="font-size: 0.88rem; opacity: 0.95;">Filtros restrictivos técnicos: visible pores, fabric wrinkles, no illustration, no cgi.</p>
      </div>
      <div class="card-brutal" style="padding: 1.5rem; margin-bottom: 0;">
        <h4 style="color: var(--color-cobalt-light); font-family: var(--font-mono); font-size: 0.95rem; margin-bottom: 0.5rem;">11. Post-processing</h4>
        <p style="font-size: 0.88rem; opacity: 0.95;">El acabado final que emula revelado químico (subtle film grain, raw capture look).</p>
      </div>
    </div>
  </div>
</section>
"""

# Compile the final layout using template placeholders
html_template = f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2L15.5 8.5L24 12L15.5 15.5L12 24L8.5 15.5L0 12L8.5 8.5Z' fill='%230055ff'/%3E%3C/svg%3E" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>BONUS 6: BIBLIOTECA COPIAR-PEGAR DE PROMPTS - Dirección Creativa & Moda con IA</title>
    
    <!-- OpenGraph/SEO -->
    <meta name="description" content="La bóveda de prompts completa para dejar de improvisar imágenes y empezar a producir campañas visuales con intención comercial y estilo profesional." />
    <meta property="og:title" content="BONUS 6: BIBLIOTECA COPIAR-PEGAR DE PROMPTS" />
    <meta property="og:description" content="Accede a 20 categorías de prompts, guías por prenda y 25 campañas estructuradas en Cobalt Blue Neon." />
    <meta property="og:image" content="/media/bonus_6_cover.png" />
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    
    <link rel="stylesheet" href="/src/biblioteca-prompts.css" />
    <script type="module" src="/src/biblioteca-prompts.js"></script>
  </head>
  <body>
    <!-- Background Grid Effect -->
    <div class="bg-grid"></div>

    <!-- SVG Definitions for icons -->
    <svg style="display: none;">
      <g id="sparkle-svg">
        <path d="M12 0C12 8.4 8.4 12 0 12c8.4 0 12 3.6 12 12 0-8.4 3.6-12 12-12-8.4 0-12-3.6-12-12z" fill="currentColor"/>
      </g>
      <g id="arrow-svg">
        <path d="M16.01 11H4v2h12.01v3L20 12l-3.99-4z" fill="currentColor"/>
      </g>
      <g id="crosshair-svg">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17.93c-3.95-.49-7-3.85-7.44-7.93H7v-2H5.56c.44-4.08 3.5-7.44 7.44-7.93V5h2v1.07c3.95.49 7 3.85 7.44 7.93H20v2h-1.56c-.44 4.08-3.5 7.44-7.44 7.93V19h-2v-.07z" fill="currentColor"/>
        <circle cx="12" cy="12" r="2" fill="currentColor"/>
      </g>
      <g id="copy-svg">
        <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z" fill="currentColor"/>
      </g>
    </svg>

    <div class="app-container">
      <!-- Sidebar Navigation -->
      <aside class="sidebar">
        <div class="logo-container">
          <div style="width: 100%; aspect-ratio: 2.1; overflow: hidden; border: 1.5px solid var(--color-cobalt-primary); margin-bottom: 1rem; border-radius: 4px; box-shadow: 0px 0px 8px rgba(0, 85, 255, 0.3);">
            <img src="/media/bonus_6_cover.png" alt="Mini cover" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
          </div>
          <div class="logo-title">BIBLIOTECA<span>PROMPTS</span></div>
          <div class="logo-subtitle">MÉTODO BONUS 06</div>
        </div>
        
        <nav style="flex: 1; display: flex; flex-direction: column; justify-content: center;">
          <ul class="nav-menu">
            <li class="nav-item">
              <a href="#" class="nav-link active">
                <span class="nav-number">00</span> Portada
              </a>
            </li>
            <li class="nav-item">
              <a href="#manifiesto" class="nav-link">
                <span class="nav-number">01</span> Manifiesto
              </a>
            </li>
            <li class="nav-item">
              <a href="#prompt-engineering" class="nav-link">
                <span class="nav-number">02</span> Engineering
              </a>
            </li>
            <li class="nav-item">
              <a href="#customizer" class="nav-link">
                <span class="nav-number">03</span> Customizador
              </a>
            </li>
            <li class="nav-item">
              <a href="#biblioteca" class="nav-link">
                <span class="nav-number">04</span> 20 Categorías
              </a>
            </li>
            <li class="nav-item">
              <a href="#anatomia" class="nav-link">
                <span class="nav-number">05</span> Anatomía
              </a>
            </li>
            <li class="nav-item">
              <a href="#garments" class="nav-link">
                <span class="nav-number">06</span> 10 Prendas
              </a>
            </li>
            <li class="nav-item">
              <a href="#boveda-detallada" class="nav-link">
                <span class="nav-number">07</span> Prompts 11-47
              </a>
            </li>
            <li class="nav-item">
              <a href="#plantillas-variables" class="nav-link">
                <span class="nav-number">08</span> Variables
              </a>
            </li>
            <li class="nav-item">
              <a href="#guia-criterio" class="nav-link">
                <span class="nav-number">09</span> Guía de Uso
              </a>
            </li>
            <li class="nav-item">
              <a href="#pack-maestro" class="nav-link">
                <span class="nav-number">10</span> Pack Maestro
              </a>
            </li>
          </ul>
        </nav>
        
        <div class="sidebar-footer">
          Biblioteca Prompts IA<br>
          © 2026 Start Grow Fast.
        </div>
      </aside>

      <!-- Main Content Area -->
      <main class="main-content">
        <!-- Hero / Portada (Solo Imagen Limpia) -->
        <header id="hero" class="hero-section">
          <div class="hero-banner-container">
            <img src="/media/bonus_6_cover.png" alt="Bonus 6 Cover" class="hero-banner-img" />
          </div>
        </header>

        <!-- Top Announcement Bar (Abajo del Hero) -->
        <div class="top-announcement-bar">
          <span class="announcement-tag">EXCLUSIVO B6</span>
          <span>SISTEMA DE DIRECCIÓN CREATIVA: BÓVEDA DE PROMPTS COPIAR-PEGAR</span>
        </div>

        <!-- Introducción de Campaña (Textos y Botones) -->
        <section id="intro" class="intro-section" style="border-bottom: var(--border-brutal); background-color: var(--color-bg-dark); padding: 4.5rem 5rem;">
          <div class="hero-badge" style="margin-bottom: 1rem;">BONUS 6 COMPLETO</div>
          <h1 class="hero-title" style="font-size: clamp(3rem, 5.5vw, 5.5rem); line-height: 0.9; text-transform: uppercase; letter-spacing: -2px; margin-bottom: 1.5rem; color: var(--color-white-editorial);">
            BIBLIOTECA <span>COPIAR-PEGAR</span> DE PROMPTS
          </h1>
          <p class="hero-subtitle" style="font-size: 1.25rem; line-height: 1.6; color: rgba(240, 243, 250, 0.85); margin-bottom: 2.2rem; max-width: 820px; border-left: 3px solid var(--color-cobalt-primary); padding-left: 1.2rem;">
            La bóveda técnica definitiva para dejar de improvisar imágenes visuales y empezar a producir campañas de moda con dirección, consistencia y fuerza comercial.
          </p>
          
          <div class="manifesto-box-banner" style="max-width: 820px; margin-bottom: 2.5rem;">
            <div class="manifesto-quote-text">
              <svg style="width: 20px; height: 20px; fill: currentColor;"><use href="#crosshair-svg"></use></svg>
              NO ES SUERTE. ES SISTEMA.
            </div>
            <span style="font-family: var(--font-mono); font-size: 0.65rem; color: var(--color-cobalt-light); font-weight: bold; letter-spacing: 1.5px;">ABOVE SYSTEM</span>
          </div>
          
          <div style="display: flex; gap: 1.5rem; flex-wrap: wrap;">
            <a href="#customizer" class="cta-button">
              Probar Customizador
              <svg style="width: 14px; height: 14px; fill: currentColor;"><use href="#arrow-svg"></use></svg>
            </a>
            <a href="#biblioteca" class="cta-button highlight-cta">
              Ver 20 Categorías
              <svg style="width: 14px; height: 14px; fill: currentColor;"><use href="#copy-svg"></use></svg>
            </a>
            <a href="#pack-maestro" class="cta-button" style="background-color: var(--color-green); box-shadow: 4px 4px 0px var(--color-bg-dark); border-color: var(--color-bg-dark);">
              Pack Maestro (25 Campañas)
              <svg style="width: 14px; height: 14px; fill: currentColor;"><use href="#arrow-svg"></use></svg>
            </a>
          </div>
        </section>

        <!-- Sección 01: El Manifiesto -->
        {conceptos_html}

        <!-- Sección 03: Customizador (Hero playground) -->
        <section id="customizer">
          <div class="section-meta">
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
            <span>[ SECCIÓN 03 / PLAYGROUND PERSONALIZABLE ]</span>
          </div>
          
          <h2 class="section-title">CUSTOMIZADOR DE <span class="trends">PROMPTS EN VIVO</span></h2>
          
          <div class="text-editorial">
            <p style="margin-bottom: 2rem;">
              Escribe las variables de tu prenda y tu marca en los campos de control a continuación. El sistema adaptará las estructuras técnicas y compilará el prompt final (Inglés) y su estructura JSON correspondiente listos para usar.
            </p>
          </div>
          
          <div class="prompt-builder">
            <div class="builder-grid">
              <div class="builder-field">
                <label for="layer-category">Tipo de Imagen / Campaña</label>
                <select id="layer-category" class="builder-input">
                  <option value="clean_product">Producto Ecommerce limpio (ecommerce lay flat)</option>
                  <option value="quiet_luxury" selected>Lujo Silencioso (quiet luxury composition)</option>
                  <option value="editorial_female">Editorial con Modelo (editorial fashion campaign)</option>
                  <option value="streetwear">Streetwear Urbano (streetwear drop campaign)</option>
                </select>
              </div>
              <div class="builder-field">
                <label for="layer-garment">Describe tu Prenda</label>
                <input type="text" id="layer-garment" class="builder-input" value="oversized denim jacket with silver buttons" />
              </div>
              <div class="builder-field">
                <label for="layer-silhouette">Silueta de la prenda</label>
                <input type="text" id="layer-silhouette" class="builder-input" value="structured oversized silhouette" />
              </div>
              <div class="builder-field">
                <label for="layer-model">Tipo de Modelo (Sujeto)</label>
                <input type="text" id="layer-model" class="builder-input" value="confident male model, defined jawline" />
              </div>
              <div class="builder-field">
                <label for="layer-background">Locación / Fondo</label>
                <input type="text" id="layer-background" class="builder-input" value="minimal light gray studio wall, natural floor shadows" />
              </div>
              <div class="builder-field">
                <label for="layer-lighting">Tipo de Iluminación</label>
                <input type="text" id="layer-lighting" class="builder-input" value="soft side studio light with gentle contrast" />
              </div>
              <div class="builder-field">
                <label for="layer-pose">Pose / Postura</label>
                <input type="text" id="layer-pose" class="builder-input" value="relaxed standing pose, hands in front pockets" />
              </div>
              <div class="builder-field">
                <label for="layer-color">Paleta de Color</label>
                <input type="text" id="layer-color" class="builder-input" value="indigo blue and soft gray" />
              </div>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 2rem;">
              <div class="prompt-container" style="margin: 0;">
                <div class="prompt-header">
                  <span class="prompt-label">PROMPT TEXTO GENERADO</span>
                  <button class="copy-btn" type="button">Copiar Prompt</button>
                </div>
                <div class="prompt-text" id="live-builder-prompt" style="font-size: 0.85rem; max-height: 250px; background-color: #010006;"></div>
              </div>
              <div class="prompt-container" style="margin: 0;">
                <div class="prompt-header">
                  <span class="prompt-label">ESTRUCTURA DE CAMPANA JSON</span>
                  <button class="copy-btn" type="button">Copiar JSON</button>
                </div>
                <pre class="prompt-text" id="live-builder-json" style="font-size: 0.78rem; max-height: 250px;"></pre>
              </div>
            </div>
          </div>
        </section>

        <!-- Sección 04: Biblioteca 20 Categorías -->
        <section id="biblioteca">
          <div class="section-meta">
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
            <span>[ SECCIÓN 04 / BÓVEDA DE CATEGORÍAS ]</span>
          </div>
          
          <h2 class="section-title">20 Categorías de <span class="trends">PROMPTS EDITORIALES</span></h2>
          
          <div class="text-editorial">
            <p>
              Explora las 20 estructuras base. Compara la debilidad del "Mal Prompt" frente a la riqueza descriptiva del "Buen Prompt" (español), y copia directamente la fórmula PRO de generación (inglés).
            </p>
          </div>
          
          <div class="library-grid">
            {categories_html}
          </div>
        </section>

        <!-- Sección 05: Anatomía de un Prompt -->
        {anatomia_html}

        <!-- Sección 06: 10 Guías de Prendas -->
        <section id="garments">
          <div class="section-meta">
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
            <span>[ SECCIÓN 06 / GUÍA TÉCNICA POR PRENDA ]</span>
          </div>
          
          <h2 class="section-title">10 Guías de Prompts <span class="trends">POR TIPO DE PRENDA</span></h2>
          
          <div class="text-editorial">
            <p>
              Cada categoría de prenda exige códigos visuales distintos para venderse con fuerza. Sigue estas 10 directrices para saber qué forzar y qué evitar al redactar tus prompts. Hemos integrado los prompts de prendas (Prompts 1-10) directamente para facilitar tu copia.
            </p>
          </div>
          
          <div class="garment-grid">
            {garments_html}
          </div>
        </section>

        <!-- Sección 07: Bóveda Detallada Prompts 11-47 -->
        <section id="boveda-detallada">
          <div class="section-meta">
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
            <span>[ SECCIÓN 07 / BÓVEDA DETALLADA ]</span>
          </div>
          
          <h2 class="section-title">BÓVEDA DETALLADA: PROMPTS <span class="trends">11 AL 47</span></h2>
          
          <div class="text-editorial">
            <p>
              Navega a través de las fórmulas detalladas del documento. Están estructuradas para controlar de forma precisa el modelo, el escenario, la iluminación, el encuadre editorial y el acabado realista para tu marca.
            </p>
          </div>
          
          {detailed_prompts_html}
        </section>

        <!-- Sección 08: Variables y Plantillas Rápidas -->
        <section id="plantillas-variables">
          <div class="section-meta">
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
            <span>[ SECCIÓN 08 / VARIABLES & PLANTILLAS ]</span>
          </div>
          
          <h2 class="section-title">BANCO DE VARIABLES & <span class="trends">PLANTILLAS DE ANUNCIOS</span></h2>
          
          <div class="text-editorial">
            <p style="margin-bottom: 2rem;">
              Combina y reemplaza estas variables técnicas en tus prompts. Copia las plantillas rápidas para estructurar anuncios de forma ágil según tus objetivos visuales.
            </p>
            
            <h3 style="font-family: var(--font-heavy); font-size: 1.5rem; text-transform: uppercase; color: var(--color-cobalt-light); margin-top: 2rem; border-bottom: 1.5px solid var(--color-cobalt-primary); padding-bottom: 0.5rem;">
              Plantillas Rápidas por Objetivo
            </h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
              <div class="card-brutal" style="margin-bottom: 0; padding: 1.5rem;">
                <h4 style="color: var(--color-cyan-glow); margin-bottom: 0.5rem;">CATÁLOGO LIMPIO</h4>
                <div class="prompt-container" style="margin: 0;"><pre class="prompt-text" style="font-size: 0.78rem;">Create a clean catalog fashion image of [PRENDA] on a [male/female] model, pure white studio background, realistic fabric texture, natural folds, accurate garment shape, soft studio lighting, full-frame photography, centered composition, no text, no logos, no CGI.</pre></div>
              </div>
              <div class="card-brutal" style="margin-bottom: 0; padding: 1.5rem;">
                <h4 style="color: var(--color-cyan-glow); margin-bottom: 0.5rem;">EDITORIAL PREMIUM</h4>
                <div class="prompt-container" style="margin: 0;"><pre class="prompt-text" style="font-size: 0.78rem;">Create a premium fashion editorial image of [PRENDA] on a [male/female] model, minimal warm background, soft diffused light, real skin texture, natural fabric movement, calm confident pose, medium format photography look, subtle grain, no text, no logos.</pre></div>
              </div>
              <div class="card-brutal" style="margin-bottom: 0; padding: 1.5rem;">
                <h4 style="color: var(--color-cyan-glow); margin-bottom: 0.5rem;">STREETWEAR</h4>
                <div class="prompt-container" style="margin: 0;"><pre class="prompt-text" style="font-size: 0.78rem;">Create a bold streetwear campaign image of [PRENDA] on a [male/female/unisex] model, oversized fit, concrete urban background, relaxed confident attitude, visible fabric weight, natural wrinkles, raw editorial lighting, no text, no logos.</pre></div>
              </div>
              <div class="card-brutal" style="margin-bottom: 0; padding: 1.5rem;">
                <h4 style="color: var(--color-cyan-glow); margin-bottom: 0.5rem;">FITNESS / ACTIVEWEAR</h4>
                <div class="prompt-container" style="margin: 0;"><pre class="prompt-text" style="font-size: 0.78rem;">Create a realistic activewear campaign image of [PRENDA] on an athletic but natural model, performance fabric, realistic compression, movement pose, clean gym or studio background, sporty lighting, real skin texture, no text, no logos.</pre></div>
              </div>
              <div class="card-brutal" style="margin-bottom: 0; padding: 1.5rem;">
                <h4 style="color: var(--color-cyan-glow); margin-bottom: 0.5rem;">BANNER WEB HERO 16:9</h4>
                <div class="prompt-container" style="margin: 0;"><pre class="prompt-text" style="font-size: 0.78rem;">Create a horizontal 16:9 fashion hero banner featuring [PRENDA/COLECCIÓN], model placed on the left, large negative space on the right for copy, premium minimal background, soft editorial lighting, realistic fabric, no text, no logos.</pre></div>
              </div>
              <div class="card-brutal" style="margin-bottom: 0; padding: 1.5rem;">
                <h4 style="color: var(--color-cyan-glow); margin-bottom: 0.5rem;">ANUNCIO VERTICAL 9:16</h4>
                <div class="prompt-container" style="margin: 0;"><pre class="prompt-text" style="font-size: 0.78rem;">Create a vertical 9:16 fashion ad image featuring [PRENDA], full outfit visible, clean negative space at the top for headline, realistic fabric texture, real skin, minimal background, no text, no logos.</pre></div>
              </div>
            </div>
            
            <h3 style="font-family: var(--font-heavy); font-size: 1.5rem; text-transform: uppercase; color: var(--color-cobalt-light); margin-top: 3.5rem; border-bottom: 1.5px solid var(--color-cobalt-primary); padding-bottom: 0.5rem; margin-bottom: 1.5rem;">
              Banco de Variables Técnicas
            </h3>
            {variables_table_html}
          </div>
        </section>

        <!-- Sección 09: Guías de Criterio y Ejercicio -->
        <section id="guia-criterio">
          <div class="section-meta">
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
            <span>[ SECCIÓN 09 / GUÍA DE CRITERIO Y EJERCICIO ]</span>
          </div>
          
          <h2 class="section-title">GUÍA DE CRITERIO Y <span class="trends">EJERCICIO DE PRODUCCIÓN</span></h2>
          
          <div class="text-editorial" style="display: flex; flex-direction: column; gap: 2rem;">
            
            <div class="card-brutal">
              <h3 style="color: var(--color-cyan-glow); margin-bottom: 1rem;">¿CÓMO SABER QUÉ PROMPT USAR?</h3>
              {criterio_html}
            </div>

            <div class="card-brutal" style="border-color: var(--color-cobalt-light); box-shadow: 4px 4px 0px var(--color-cobalt-light);">
              <h3 style="color: var(--color-cobalt-light); margin-bottom: 1rem;">CÓMO MODIFICAR UN PROMPT SIN DAÑARLO</h3>
              {modificar_html}
            </div>

            <div class="card-brutal">
              <h3 style="color: var(--color-cyan-glow); margin-bottom: 1rem;">CÓMO PEDIR VARIACIONES AL AGENTE CREATIVO</h3>
              {variaciones_html}
            </div>

            <div class="card-brutal" style="border-color: var(--color-red); box-shadow: 4px 4px 0px var(--color-red);">
              <h3 style="color: var(--color-red-light); margin-bottom: 1rem;">ERRORES COMUNES AL USAR PROMPTS DE MODA</h3>
              {errores_html}
            </div>

            <div class="card-brutal" style="border-color: var(--color-green); box-shadow: 4px 4px 0px var(--color-green);">
              <h3 style="color: var(--color-green-light); margin-bottom: 1rem;">EJERCICIO FINAL DE PRODUCCIÓN</h3>
              <p>Sigue esta guía paso a paso para entrenar tu dirección creativa con una prenda real:</p>
              {ejercicio_html}
            </div>

            <div class="card-brutal" style="background-color: var(--color-bg-dark);">
              <h3 style="color: var(--color-white); margin-bottom: 1rem; text-transform: uppercase;">Transformación Visual Final</h3>
              {transformacion_html}
            </div>

            <div class="card-brutal" style="border: var(--border-dashed); background: none; box-shadow: none;">
              <h3 style="color: var(--color-cobalt-light); margin-bottom: 1rem; text-transform: uppercase;">Mensaje de Cierre</h3>
              {cierre_html}
            </div>
            
          </div>
        </section>

        <!-- Sección 10: Pack Maestro (25 Campañas Fondo Blanco) -->
        <section id="pack-maestro" style="background-color: var(--color-bg-dark);">
          <div class="section-meta">
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
            <span>[ SECCIÓN 10 / PACK MAESTRO EN FONDO BLANCO ]</span>
          </div>
          
          <h2 class="section-title">PACK MAESTRO: 25 CAMPAÑAS <span class="trends">FONDO BLANCO</span></h2>
          
          <div class="text-editorial">
            <p>
              <strong>Regla visual global:</strong> Todas las campañas usan fondo blanco, pero no se ven iguales. El fondo blanco puede ser un ciclorama puro, cálido, lona, papel con texturas, sombras duras o luces naturales.
            </p>
            
            <div class="card-brutal-dark" style="margin-top: 1.5rem;">
              <h4 style="color: var(--color-cyan-glow); font-family: var(--font-heavy); font-size: 1.2rem; text-transform: uppercase; margin-bottom: 0.8rem;">Prompt Negativo Global (Anti-errores de IA)</h4>
              <p style="font-family: var(--font-mono); font-size: 0.82rem; line-height: 1.5; color: var(--color-red-light);">
                No deformed hands, no extra fingers, no distorted clothing, no fake logos, no unreadable text, no messy background, no low resolution, no artificial plastic skin, no overfiltered face, no bad anatomy, no warped fabric, no unrealistic body proportions, no duplicated limbs, no watermark.
              </p>
            </div>
          </div>
          
          {campaigns_html}
          
          <!-- Checklist final and Closing templates -->
          <div style="margin-top: 4.5rem; display: flex; flex-direction: column; gap: 2.5rem;">
            <div class="card-brutal" style="border-color: var(--color-cyan-glow); box-shadow: 4px 4px 0px var(--color-cyan-glow);">
              <h3 style="color: var(--color-cyan-glow); font-family: var(--font-heavy); font-size: 1.5rem; text-transform: uppercase; margin-bottom: 1.2rem;">Checklist final de producción</h3>
              {checklist_html}
            </div>
            
            <div class="card-brutal" style="border-color: var(--color-green); box-shadow: 4px 4px 0px var(--color-green);">
              <h3 style="color: var(--color-green-light); font-family: var(--font-heavy); font-size: 1.3rem; text-transform: uppercase; margin-bottom: 1.2rem;">Fórmula Comercial para Copies Recomendados</h3>
              <p>Utiliza esta estructura para redactar copies atractivos que complementen las campañas:</p>
              <pre style="font-family: var(--font-body); font-size: 0.9rem; padding: 1.2rem; background: var(--color-bg-dark); border-radius: 4px; line-height: 1.6; margin: 1rem 0;">
[Frase aspiracional]
[Beneficio de la prenda]
[Disponibilidad o urgencia]
[CTA / Llamada a la acción]
              </pre>
              <p style="font-weight: bold; margin-bottom: 0.5rem;">Ejemplo Aplicado:</p>
              <div class="copy-box" style="margin-top: 0.5rem;">
                <pre class="copy-target" style="font-size: 0.88rem; opacity: 0.95;">Elegancia que se nota sin esfuerzo.
Pantalón de caída amplia, cintura favorecedora y textura premium.
Disponible en pocas unidades.
Escríbenos para separar tu talla.</pre>
                <button class="copy-btn copy-inline-btn" type="button">Copiar Ejemplo</button>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  </body>
</html>
"""

# Write compiled html file
out_html_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\biblioteca-de-prompts.html"
with open(out_html_path, "w", encoding="utf-8") as f_out:
    f_out.write(html_template)

print(f"biblioteca-de-prompts.html generated successfully at {out_html_path}!")
