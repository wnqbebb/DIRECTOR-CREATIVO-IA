import os
import shutil
import re

# 1. Copy the cover image to public media directory
src_cover = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\BONUS 5 3 LANZAMIENTOS EDITORIALES COPIABLES\BONUS 5 3 LANZAMIENTOS EDITORIALES COPIABLES.png"
dest_cover = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\public\media\bonus_5_cover.png"
os.makedirs(os.path.dirname(dest_cover), exist_ok=True)
if os.path.exists(src_cover):
    shutil.copy(src_cover, dest_cover)
    print(f"Cover image copied to {dest_cover}")
else:
    print(f"Warning: Source cover image not found at {src_cover}")

# 2. Define Image Mappings
model1_refs = ["image1.jpg", "image40.jpg", "image3.jpg", "image2.jpg"]
camp1_imgs = ["image46.jpg", "image29.jpg", "image22.jpg", "image36.jpg", "image20.jpg", "image35.jpg", "image38.jpg", "image34.jpg", "image19.jpg", "image45.jpg"]
camp2_imgs = ["image15.jpg", "image12.jpg", "image30.jpg", "image33.jpg", "image8.jpg", "image10.jpg", "image37.jpg", "image21.jpg"]
model2_refs = ["image23.png", "image18.jpg", "image17.jpg", "image26.jpg"]
camp3_imgs = ["image9.jpg", "image39.jpg", "image32.jpg", "image44.jpg", "image28.jpg", "image14.jpg", "image13.jpg", "image5.jpg", "image4.jpg", "image43.jpg", "image11.jpg", "image16.jpg", "image31.jpg", "image24.jpg", "image25.jpg", "image41.jpg", "image27.jpg", "image6.jpg", "image42.jpg", "image7.jpg"]

# 3. Read raw text
text_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\BONUS_5_TEXT.txt"
with open(text_path, "r", encoding="utf-8", errors="ignore") as f:
    raw_lines = f.readlines()

print(f"Read {len(raw_lines)} lines of text.")

# Helper to slice text lines
def get_text_range(start_line, end_line):
    return "".join(raw_lines[start_line-1:end_line])

# Helper to format lines of text as paragraph HTML
def format_paragraphs(text_block, class_name=""):
    paras = text_block.strip().split('\n\n')
    formatted = []
    for p in paras:
        lines = [line.strip() for line in p.split('\n') if line.strip()]
        if lines:
            p_text = " ".join(lines)
            p_text = re.sub(r'Same ([^,]+) from the reference images', r'<strong>Same \1 from reference images</strong>', p_text)
            p_text = re.sub(r'Same female sportswear model from the new reference images', r'<strong>Same female model from reference images</strong>', p_text)
            # Add highlights to text key elements
            p_text = p_text.replace("modelo ancla", "<strong>modelo ancla</strong>")
            p_text = p_text.replace("lanzamientos copiables", "<strong>lanzamientos copiables</strong>")
            p_text = p_text.replace("percepción", "<strong>percepción</strong>")
            p_text = p_text.replace("crear deseo", "<strong>crear deseo</strong>")
            p_text = p_text.replace("coherencia visual", "<strong>coherencia visual</strong>")
            
            class_attr = f' class="{class_name}"' if class_name else ""
            formatted.append(f"<p{class_attr}>{p_text}</p>")
    return "\n".join(formatted)

# Helper to format bullet list
def format_bullet_list(text_block):
    lines = [l.strip() for l in text_block.strip().split('\n') if l.strip()]
    html_items = []
    for line in lines:
        cleaned = re.sub(r'^[\-\*\•\d\.\,\;\:]\s*', '', line).strip()
        if cleaned:
            html_items.append(f"<li>{cleaned}</li>")
    return f'<ul class="styled-list">{"".join(html_items)}</ul>'

# Helper to parse and format the consistency instructions in a beautiful grid of pink cards
def format_consistency_cards(text_block):
    lines = text_block.strip().split('\n')
    points = []
    current_point = None
    point_5_end_lines = []
    
    header_pattern = r'^(\d+)\.\s+(.*)$'
    
    for line in lines:
        s_line = line.strip()
        if not s_line:
            continue
            
        m = re.match(header_pattern, s_line)
        if m and m.group(1).isdigit() and 6 <= int(m.group(1)) <= 29:
            if current_point:
                points.append(current_point)
            current_point = {
                "num": m.group(1),
                "title": m.group(2),
                "lines": []
            }
        else:
            if current_point:
                current_point["lines"].append(s_line)
            else:
                point_5_end_lines.append(s_line)
                
    if current_point:
        points.append(current_point)
        
    html = '<div class="consistency-grid">'
    
    # Continuation of point 5 (Cejas)
    if point_5_end_lines:
        p5_html = ""
        for l in point_5_end_lines:
            p5_html += f"<p>{l}</p>"
        html += f"""
        <div class="card-consistency-pink">
          <div class="card-num">05</div>
          <h4>5. CEJAS (DETALLE EXTRA)</h4>
          <div class="text-editorial" style="font-size: 0.95rem;">
            {p5_html}
          </div>
        </div>
        """
        
    for p in points:
        num = p["num"]
        title = p["title"]
        p_lines = p["lines"]
        
        body_html = ""
        avoid_items = []
        bullet_items = []
        current_para = []
        
        is_prompt = False
        prompt_text = ""
        
        # Check if point is a prompt block (21 to 25)
        if int(num) in [21, 22, 23, 24, 25]:
            is_prompt = True
            prompt_text = "\n".join(p_lines)
            
        if is_prompt:
            body_html = f"""
            <div class="prompt-container" style="margin: 0; border-color: var(--fuchsia); box-shadow: none;">
              <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                <span class="prompt-label" style="color: var(--fuchsia);">PROMPT IA COPIABLE</span>
                <button class="copy-btn" type="button" style="padding: 0.2rem 0.6rem; font-size: 0.65rem;">
                  <svg style="width: 10px; height: 10px;"><use href="#copy-svg"></use></svg>
                  Copiar
                </button>
              </div>
              <pre class="prompt-text" style="font-size: 0.75rem; max-height: 150px; color: var(--white);">{prompt_text}</pre>
            </div>
            """
        else:
            for l in p_lines:
                l_lower = l.lower()
                is_avoid = False
                for prefix in ["no se siente", "no se ven", "no se ve", "no beauty", "no piel", "no cgi", "no cambiar", "no usar", "no borrar", "no hacer", "no es una", "no parece", "sin exceso", "sin sombra", "sin sonrisa"]:
                    if l_lower.startswith(prefix) or l_lower.startswith("- no ") or l_lower.startswith("* no "):
                        is_avoid = True
                        break
                
                is_bullet = False
                if l.startswith('-') or l.startswith('*') or l.startswith('•') or (',' in l and len(l) < 140 and not l.endswith('.')):
                    is_bullet = True
                
                l_cleaned = re.sub(r'^[\-\*\•\d\.\,\;\:]\s*', '', l).strip()
                
                if is_avoid:
                    avoid_items.append(l_cleaned)
                elif is_bullet:
                    bullet_items.append(l_cleaned)
                else:
                    if l.endswith('.') or len(l) > 100:
                        if current_para:
                            current_para.append(l)
                        else:
                            current_para = [l]
                    else:
                        bullet_items.append(l_cleaned)
                        
            if current_para:
                para_text = " ".join(current_para)
                # Add highlights
                para_text = para_text.replace("cejas gruesas", "<strong>cejas gruesas</strong>")
                para_text = para_text.replace("mirada de la modelo", "<strong>mirada de la modelo</strong>")
                para_text = para_text.replace("labios son", "<strong>labios son</strong>")
                para_text = para_text.replace("piel de la modelo", "<strong>piel de la modelo</strong>")
                para_text = para_text.replace("cabello", "<strong>cabello</strong>")
                para_text = para_text.replace("complexión", "<strong>complexión</strong>")
                para_text = para_text.replace("postura", "<strong>postura</strong>")
                para_text = para_text.replace("maquillaje", "<strong>maquillaje</strong>")
                para_text = para_text.replace("luz suave", "<strong>luz suave</strong>")
                para_text = para_text.replace("consistencia", "<strong>consistencia</strong>")
                body_html += f"<p>{para_text}</p>"
                
            if bullet_items:
                bullets_html = "".join([f"<li>{item}</li>" for item in bullet_items])
                body_html += f'<ul class="consistency-bullets">{bullets_html}</ul>'
                
            if avoid_items:
                avoid_html = "".join([f"<li>{item}</li>" for item in avoid_items])
                body_html += f'<div style="margin-top: 0.8rem; font-family: monospace; font-size: 0.75rem; color: #ff3366; text-transform: uppercase; font-weight: bold; letter-spacing: 0.5px;">EVITAR / CONSTRICCIONES:</div>'
                body_html += f'<ul class="avoid-list">{avoid_html}</ul>'
                
        html += f"""
        <div class="card-consistency-pink">
          <div class="card-num">{num}</div>
          <h4>{num}. {title}</h4>
          <div class="text-editorial" style="font-size: 0.95rem;">
            {body_html}
          </div>
        </div>
        """
        
    html += '</div>'
    return html

# Helper to parse and format the closure instructions of Campaign 1 into beautiful circled-marker fuchsia cards
def format_c1_closure(text_block):
    lines = text_block.strip().split('\n')
    points = []
    current_point = None
    
    header_pattern = r'^(\d+)\.\s+(.*)$'
    
    for line in lines:
        s_line = line.strip()
        if not s_line:
            continue
            
        m = re.match(header_pattern, s_line)
        if m and m.group(1).isdigit() and 28 <= int(m.group(1)) <= 33:
            if current_point:
                points.append(current_point)
            current_point = {
                "num": m.group(1),
                "title": m.group(2),
                "lines": []
            }
        else:
            if current_point:
                current_point["lines"].append(s_line)
                
    if current_point:
        points.append(current_point)
        
    html = '<div style="display: flex; flex-direction: column; gap: 2rem; margin-top: 2rem; width: 100%;">'
    
    for p in points:
        num = p["num"]
        title = p["title"]
        p_lines = p["lines"]
        
        body_html = ""
        is_prompt = False
        prompt_text = ""
        
        if int(num) in [28, 29, 30, 31]:
            is_prompt = True
            
        if is_prompt:
            desc_lines = []
            prompt_lines = []
            for l in p_lines:
                if "same female" in l.lower() or "create a" in l.lower() or "wearing" in l.lower() or "mood is" in l.lower() or "photography" in l.lower() or "natural skin" in l.lower() or "real skin" in l.lower() or "organic" in l.lower():
                    prompt_lines.append(l)
                else:
                    desc_lines.append(l)
                    
            desc_html = ""
            if desc_lines:
                desc_text = " ".join(desc_lines)
                desc_html = f"<p>{desc_text}</p>"
                
            prompt_text_val = " ".join(prompt_lines)
            
            body_html = f"""
            {desc_html}
            <div class="prompt-container" style="margin-top: 1rem; border-color: var(--fuchsia); box-shadow: none;">
              <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                <span class="prompt-label" style="color: var(--fuchsia);">PROMPT IA COPIABLE</span>
                <button class="copy-btn" type="button" style="padding: 0.2rem 0.6rem; font-size: 0.65rem;">
                  <svg style="width: 10px; height: 10px;"><use href="#copy-svg"></use></svg>
                  Copiar Prompt
                </button>
              </div>
              <pre class="prompt-text" style="font-size: 0.75rem; max-height: 150px; color: var(--white);">{prompt_text_val}</pre>
            </div>
            """
        elif int(num) == 32:
            error_list = []
            for l in p_lines:
                l_cleaned = re.sub(r'^(Error\s+\d+\:?)\s*', '', l).strip()
                m_err = re.match(r'^([eE]rror\s+\d+\:?\s*[a-zA-ZÁÉÍÓÚÑa-zñáéíóú\s]+)(.*)$', l)
                if m_err:
                    error_title = m_err.group(1)
                    error_desc = m_err.group(2)
                    error_list.append(f"<li><strong>{error_title}</strong>: {error_desc}</li>")
                else:
                    error_list.append(f"<li>{l_cleaned}</li>")
                    
            body_html = f'<ul class="avoid-list" style="background: rgba(255, 0, 127, 0.05); border-left-color: var(--fuchsia); padding: 1rem 1.5rem;">' + "".join(error_list) + '</ul>'
        else:
            paragraphs = []
            for l in p_lines:
                paragraphs.append(l)
            body_html = "".join([f"<p>{para}</p>" for para in paragraphs])
            
        html += f"""
        <div class="card-marker-pink">
          <div class="card-num">{num}</div>
          <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.6rem; color: var(--fuchsia); text-transform: uppercase; margin-bottom: 1rem; border-bottom: 1px dashed rgba(255, 0, 127, 0.2); padding-bottom: 0.4rem; padding-right: 2.2rem;">
            {num}. {title}
          </h4>
          <div class="text-editorial" style="font-size: 0.95rem;">
            {body_html}
          </div>
        </div>
        """
        
    html += '</div>'
    return html

# Helper to format points/headings into beautiful pink circled cards (card-marker-pink)
def format_points_to_cards(text_block, force_card_marker=True, allowed_prompt_nums=None, avoid_nums=None):
    if allowed_prompt_nums is None:
        allowed_prompt_nums = []
    if avoid_nums is None:
        avoid_nums = []
        
    lines = text_block.strip().split('\n')
    intro_lines = []
    points = []
    current_point = None
    
    header_pattern = r'^(\d+)\.\s+(.*)$'
    
    for line in lines:
        s_line = line.strip()
        if not s_line:
            continue
            
        m = re.match(header_pattern, s_line)
        if m and m.group(1).isdigit():
            if current_point:
                points.append(current_point)
            current_point = {
                "num": int(m.group(1)),
                "title": m.group(2),
                "lines": []
            }
        else:
            if current_point:
                current_point["lines"].append(s_line)
            else:
                intro_lines.append(s_line)
                
    if current_point:
        points.append(current_point)
        
    html = ""
    
    # Format Intro
    if intro_lines:
        cleaned_intro = []
        for l in intro_lines:
            # Exclude metadata/header labels
            if not l.startswith("CAMPAÑA") and not l.startswith("SITIO WEB") and not l.startswith("RESULTADOS") and not l.startswith("LINK") and not l.startswith("FOTOS DE REFENECIA"):
                cleaned_intro.append(l)
        if cleaned_intro:
            intro_text = " ".join(cleaned_intro)
            html += f"""
            <div class="card-brutal-neon" style="margin-bottom: 2.5rem;">
              <h3 style="color: var(--white); font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1rem;">
                DIRECCIÓN DE ARTE & INTRODUCCIÓN
              </h3>
              <div class="text-editorial">
                <p>{intro_text}</p>
              </div>
            </div>
            """
            
    html += '<div style="display: flex; flex-direction: column; gap: 2rem; width: 100%;">'
    
    for p in points:
        num = p["num"]
        title = p["title"]
        p_lines = p["lines"]
        
        body_html = ""
        is_prompt = num in allowed_prompt_nums
        
        if "PROMPT" in title.upper() or "NEGATIVE PROMPT" in title.upper() or "EJEMPLO DE ADAPTACIÓN" in title.upper():
            is_prompt = True
            
        if is_prompt:
            desc_lines = []
            prompt_lines = []
            for l in p_lines:
                # English or prompt indicator
                l_lower = l.lower()
                if any(x in l_lower for x in ["same female", "same model", "create a", "wearing", "mood is", "photography", "natural skin", "real skin", "negative prompt", "no text", "no logos", "no watermark"]):
                    prompt_lines.append(l)
                else:
                    desc_lines.append(l)
                    
            desc_html = ""
            if desc_lines:
                desc_text = " ".join(desc_lines)
                desc_html = f"<p>{desc_text}</p>"
                
            prompt_val = "\n".join(prompt_lines) if "negative" in title.lower() or "madre" in title.lower() else " ".join(prompt_lines)
            
            body_html = f"""
            {desc_html}
            <div class="prompt-container" style="margin-top: 1rem; border-color: var(--fuchsia); box-shadow: none;">
              <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                <span class="prompt-label" style="color: var(--fuchsia);">PROMPT IA COPIABLE</span>
                <button class="copy-btn" type="button" style="padding: 0.2rem 0.6rem; font-size: 0.65rem;">
                  <svg style="width: 10px; height: 10px;"><use href="#copy-svg"></use></svg>
                  Copiar Prompt
                </button>
              </div>
              <pre class="prompt-text" style="font-size: 0.75rem; max-height: 150px; color: var(--white);">{prompt_val}</pre>
            </div>
            """
        elif num in avoid_nums or "EVITAR" in title.upper() or "ERRORES" in title.upper() or "NO SE DEBE" in title.upper():
            error_list = []
            for l in p_lines:
                l_cleaned = re.sub(r'^([eE]rror\s+\d+\:?|Paso\s+\d+\:?|[\-\*\•\d\.\,\;\:])\s*', '', l).strip()
                m_err = re.match(r'^([eE]rror\s+\d+\:?\s*[a-zA-ZÁÉÍÓÚÑa-zñáéíóú\s]+)(.*)$', l)
                if m_err:
                    error_title = m_err.group(1)
                    error_desc = m_err.group(2)
                    error_list.append(f"<li><strong>{error_title}</strong>: {error_desc}</li>")
                else:
                    error_list.append(f"<li>{l_cleaned}</li>")
            body_html = f'<ul class="avoid-list" style="background: rgba(255, 0, 127, 0.05); border-left-color: var(--fuchsia); padding: 1rem 1.5rem;">' + "".join(error_list) + '</ul>'
        else:
            avoid_items = []
            bullet_items = []
            current_para = []
            
            for l in p_lines:
                l_lower = l.lower()
                is_avoid = False
                for prefix in ["no se siente", "no se ven", "no se ve", "no beauty", "no piel", "no cgi", "no cambiar", "no usar", "no borrar", "no hacer", "no es una", "no parece", "sin exceso", "sin sombra", "sin sonrisa", "evitar", "no convertir", "no oscurecer", "no maquillar", "no deformar"]:
                    if l_lower.startswith(prefix) or l_lower.startswith("- no ") or l_lower.startswith("* no "):
                        is_avoid = True
                        break
                
                is_bullet = False
                if l.startswith('-') or l.startswith('*') or l.startswith('•') or (',' in l and len(l) < 140 and not l.endswith('.')) or l.startswith('Paso ') or l.startswith('Pieza ') or l.startswith('Mundo '):
                    is_bullet = True
                
                l_cleaned = re.sub(r'^([\-\*\•\d\.\,\;\:]|Paso\s+\d+\:|Pieza\s+\d+\:|Mundo\s+\d+\:)\s*', '', l).strip()
                
                if is_avoid:
                    avoid_items.append(l_cleaned)
                elif is_bullet:
                    if l.startswith('Paso') or l.startswith('Pieza') or l.startswith('Mundo'):
                        bullet_items.append(f"<strong>{l.split(':')[0]}:</strong> {l.split(':', 1)[1].strip() if ':' in l else l}")
                    else:
                        bullet_items.append(l_cleaned)
                else:
                    if l.endswith('.') or len(l) > 100:
                        current_para.append(l)
                    else:
                        bullet_items.append(l_cleaned)
                        
            if current_para:
                para_text = " ".join(current_para)
                # Highlight words
                para_text = para_text.replace("modelo ancla", "<strong>modelo ancla</strong>")
                para_text = para_text.replace("prenda protagonista", "<strong>prenda protagonista</strong>")
                para_text = para_text.replace("coherencia visual", "<strong>coherencia visual</strong>")
                para_text = para_text.replace("ropa deportiva", "<strong>ropa deportiva</strong>")
                para_text = para_text.replace("e-commerce", "<strong>e-commerce</strong>")
                para_text = para_text.replace("consistencia", "<strong>consistencia</strong>")
                para_text = para_text.replace("movimiento", "<strong>movimiento</strong>")
                body_html += f"<p>{para_text}</p>"
                
            if bullet_items:
                bullets_html = "".join([f"<li>{item}</li>" for item in bullet_items])
                body_html += f'<ul class="consistency-bullets">{bullets_html}</ul>'
                
            if avoid_items:
                avoid_html = "".join([f"<li>{item}</li>" for item in avoid_items])
                body_html += f'<div style="margin-top: 0.8rem; font-family: monospace; font-size: 0.75rem; color: #ff3366; text-transform: uppercase; font-weight: bold; letter-spacing: 0.5px;">EVITAR / CONSTRICCIONES:</div>'
                body_html += f'<ul class="avoid-list">{avoid_html}</ul>'
                
        card_class = "card-marker-pink" if force_card_marker else "card-consistency-pink"
        
        html += f"""
        <div class="{card_class}">
          <div class="card-num">{num:02d}</div>
          <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.6rem; color: var(--fuchsia); text-transform: uppercase; margin-bottom: 1rem; border-bottom: 1px dashed rgba(255, 0, 127, 0.2); padding-bottom: 0.4rem; padding-right: 2.2rem;">
            {num}. {title}
          </h4>
          <div class="text-editorial" style="font-size: 0.95rem;">
            {body_html}
          </div>
        </div>
        """
        
    html += '</div>'
    return html

# Parse campaign results/images dynamically from raw lines
def parse_campaign_blocks(start_l, end_l):
    block_lines = raw_lines[start_l-1:end_l]
    blocks = []
    current_block = None
    pattern = r'^\d+\.\s+(IMAGEN|RESULTADO)\s+\d+'
    
    for idx, line in enumerate(block_lines):
        s_line = line.strip()
        if re.match(pattern, s_line):
            if current_block:
                blocks.append(current_block)
            current_block = {
                "header": s_line,
                "lines": [],
                "line_num": start_l + idx
            }
        elif current_block is not None:
            current_block["lines"].append(s_line)
            
    if current_block:
        blocks.append(current_block)
        
    parsed_items = []
    for b in blocks:
        lines_list = [l for l in b["lines"] if l]
        if len(lines_list) >= 2:
            title = lines_list[0]
            # Find prompt divider
            prompt_idx = -1
            for idx, l in enumerate(lines_list):
                if "prompt" in l.lower():
                    prompt_idx = idx
                    break
            
            if prompt_idx != -1:
                desc_paras = lines_list[1:prompt_idx]
                prompt_lines = lines_list[prompt_idx+1:]
                
                desc = " ".join(desc_paras)
                prompt = " ".join(prompt_lines)
                
                parsed_items.append({
                    "header": b["header"],
                    "title": title,
                    "description": desc,
                    "prompt": prompt
                })
            else:
                desc = " ".join(lines_list[1:])
                parsed_items.append({
                    "header": b["header"],
                    "title": title,
                    "description": desc,
                    "prompt": ""
                })
    return parsed_items

# Generate side-by-side alternating layout for results
def generate_alternating_rows(items, images, folder_prefix="bonus_5"):
    html = ""
    for idx, item in enumerate(items):
        if idx >= len(images):
            break
        img_src = f"/media/{folder_prefix}/{images[idx]}"
        title = item["title"]
        desc = item["description"]
        prompt = item["prompt"]
        header = item["header"]
        
        # Clean desc and format paragraphs
        desc_html = ""
        # Split sentences by period followed by space
        sentences = [s.strip() for s in desc.split('.') if s.strip()]
        group_size = 2
        for i in range(0, len(sentences), group_size):
            para_text = ". ".join(sentences[i:i+group_size]) + "."
            desc_html += f"<p>{para_text}</p>"
            
        prompt_html = ""
        if prompt:
            prompt_html = f"""
            <div class="prompt-container">
              <div class="prompt-header">
                <span class="prompt-label">PROMPT IA COPIABLE</span>
                <button class="copy-btn" type="button">
                  <svg style="width: 14px; height: 14px;"><use href="#copy-svg"></use></svg>
                  Copiar Prompt
                </button>
              </div>
              <pre class="prompt-text">{prompt}</pre>
            </div>
            """
            
        html += f"""
        <div class="result-row">
          <div class="result-image-col">
            <div class="showcase-item">
              <img src="{img_src}" alt="{title}" />
              <div class="showcase-caption">{header} - {title}</div>
            </div>
          </div>
          <div class="result-prompt-col">
            <h3 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; color: var(--fuchsia); text-transform: uppercase; margin-bottom: 1rem;">
              {title}
            </h3>
            <div class="result-explanation">
              {desc_html}
            </div>
            {prompt_html}
          </div>
        </div>
        """
    return html

# Parse campaign data
c1_results = parse_campaign_blocks(1082, 1324) # 10 items
c2_results = parse_campaign_blocks(1577, 1715) # 9 items, we will map 8
c3_results = parse_campaign_blocks(2350, 2523) # 16 items

# Extract segments of text
manifiesto_1 = get_text_range(5, 25)
manifiesto_2 = get_text_range(26, 46)
manifiesto_3 = get_text_range(47, 72)
manifiesto_4 = get_text_range(73, 101)

m1_intro = get_text_range(518, 536)
m1_qes = get_text_range(537, 554)
m1_lectura = get_text_range(555, 568)
m1_edad = get_text_range(569, 588)
m1_rostro = get_text_range(589, 610)
m1_details = get_text_range(611, 906)
c1_theory = get_text_range(910, 1081)
c1_closure = get_text_range(1325, 1378)

c2_theory = get_text_range(1384, 1576)
c2_closure = get_text_range(1716, 1845)

c3_model_info = get_text_range(1852, 2216)
c3_theory = get_text_range(2219, 2349)
c3_closure = get_text_range(2524, 2652)

# Generate HTML file
html_template = f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2L15.5 8.5L24 12L15.5 15.5L12 24L8.5 15.5L0 12L8.5 8.5Z' fill='%23FF007F'/%3E%3C/svg%3E" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>BONUS 5: 3 LANZAMIENTOS EDITORIALES COPIABLES - Dirección Creativa & Moda con IA</title>
    
    <!-- OpenGraph/SEO -->
    <meta name="description" content="Aprende a estructurar lanzamientos completos de moda con consistencia visual: Colección Femenina, Drop Streetwear y Campaña de Accesorios." />
    <meta property="og:title" content="BONUS 5: 3 LANZAMIENTOS EDITORIALES COPIABLES" />
    <meta property="og:description" content="Adapta tres estructuras de campañas de moda completas a tu marca usando inteligencia artificial." />
    <meta property="og:image" content="/media/bonus_5_cover.png" />
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    
    <link rel="stylesheet" href="/src/lanzamientos-editoriales.css" />
    <script type="module" src="/src/lanzamientos-editoriales.js"></script>
  </head>
  <body>
    <!-- SVG Definitions for icons -->
    <svg style="display: none;">
      <g id="sparkle-svg">
        <path d="M12 0C12 8.4 8.4 12 0 12c8.4 0 12 3.6 12 12 0-8.4 3.6-12 12-12-8.4 0-12-3.6-12-12z" fill="currentColor"/>
      </g>
      <g id="arrow-svg">
        <path d="M16.01 11H4v2h12.01v3L20 12l-3.99-4z" fill="currentColor"/>
      </g>
      <g id="copy-svg">
        <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z" fill="currentColor"/>
      </g>
      <g id="crosshair-svg">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17.93c-3.95-.49-7-3.85-7.44-7.93H7v-2H5.56c.44-4.08 3.5-7.44 7.44-7.93V5h2v1.07c3.95.49 7 3.85 7.44 7.93H20v2h-1.56c-.44 4.08-3.5 7.44-7.44 7.93V19h-2v-.07z" fill="currentColor"/>
        <circle cx="12" cy="12" r="2" fill="currentColor"/>
      </g>
    </svg>

    <div class="app-container">
      <!-- Sidebar Navigation -->
      <aside class="sidebar">
        <div class="logo-container">
          <div style="width: 100%; aspect-ratio: 2.1; overflow: hidden; border: 1.5px solid var(--fuchsia); margin-bottom: 1rem; border-radius: 4px; box-shadow: 0px 0px 8px rgba(255, 0, 127, 0.35);">
            <img src="/media/bonus_5_cover.png" alt="Mini cover" style="width: 100%; height: 100%; object-fit: cover; display: block;" />
          </div>
          <div class="logo-title">LANZAMIENTOS<span>EDITORIALES</span></div>
          <div class="logo-subtitle">MÉTODO BONUS 05</div>
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
              <a href="#modelo-ancla" class="nav-link">
                <span class="nav-number">02</span> Modelo Ancla
              </a>
            </li>
            <li class="nav-item">
              <a href="#mundo-1" class="nav-link">
                <span class="nav-number">03</span> Mundo 01: Naturaleza
              </a>
            </li>
            <li class="nav-item">
              <a href="#mundo-2" class="nav-link">
                <span class="nav-number">04</span> Mundo 02: Streetwear
              </a>
            </li>
            <li class="nav-item">
              <a href="#mundo-3" class="nav-link">
                <span class="nav-number">05</span> Mundo 03: Tennis Club
              </a>
            </li>
            <li class="nav-item">
              <a href="#prompt-generator" class="nav-link">
                <span class="nav-number">06</span> Herramienta IA
              </a>
            </li>
            <li class="nav-item">
              <a href="#checklist-audit" class="nav-link">
                <span class="nav-number">07</span> Checklist
              </a>
            </li>
          </ul>
        </nav>
        
        <div class="sidebar-footer">
          Lanzamientos Copiables IA<br>
          © 2026 Start Grow Fast AI Agents.
        </div>
      </aside>

      <!-- Main Content Area -->
      <main class="main-content">
        <!-- Hero / Portada -->
        <header id="hero" class="hero-section">
          <div class="hero-banner-container">
            <img src="/media/bonus_5_cover.png" alt="Bonus 5: 3 Lanzamientos Editoriales Copiables" class="hero-banner-img" />
          </div>
        </header>

        <!-- Sección 01: El Manifiesto -->
        <section id="manifiesto">
          <div class="sticker-fuchsia">BONUS 5</div>
          
          <div class="section-meta">
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
            <span>[ SECCIÓN 01 / EL MANIFIESTO ]</span>
          </div>

          <h2 class="section-title">
            3 CAMPAÑAS PARA QUE TU MARCA <span class="trends">DEJE DE VERSE IMPROVISADA</span>
          </h2>
          
          <div style="display: flex; flex-direction: column; gap: 2rem; margin-bottom: 3.5rem;">
            <!-- Chapter 1 -->
            <div class="card-brutal-neon">
              <h3 style="color: var(--fuchsia); font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1rem;">
                1. UNA PRENDA NO ES UNA CAMPAÑA
              </h3>
              <div class="text-editorial">
                {format_paragraphs(manifiesto_1)}
              </div>
            </div>

            <!-- Chapter 2 -->
            <div class="card-brutal">
              <h3 style="color: var(--white); font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1rem;">
                2. LA DIFERENCIA ENTRE MOSTRAR ROPA Y CREAR DESEO
              </h3>
              <div class="text-editorial">
                {format_paragraphs(manifiesto_2)}
              </div>
            </div>

            <!-- Chapter 3 -->
            <div class="card-brutal-neon">
              <h3 style="color: var(--fuchsia); font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1rem;">
                3. NO VAS A COPIAR FOTOS: VAS A ROBAR LA ESTRUCTURA
              </h3>
              <div class="text-editorial">
                {format_paragraphs(manifiesto_3)}
              </div>
            </div>

            <!-- Chapter 4 -->
            <div class="card-brutal">
              <h3 style="color: var(--white); font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1rem;">
                4. AQUÍ ES DONDE EL SISTEMA DEMUESTRA QUE FUNCIONA
              </h3>
              <div class="text-editorial">
                {format_paragraphs(manifiesto_4)}
              </div>
            </div>
          </div>
        </section>

        <!-- Sección 02: La Modelo Ancla -->
        <section id="modelo-ancla">
          <div class="section-meta">
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
            <span>[ SECCIÓN 02 / LA MODELO ANCLA ]</span>
          </div>

          <h2 class="section-title">
            LA MODELO ANCLA: EL ROSTRO QUE <span class="trends">SOSTIENE LA CAMPAÑA</span>
          </h2>

          <div class="card-brutal" style="margin-bottom: 3rem;">
            <div class="text-editorial">
              {format_paragraphs(m1_intro)}
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 2rem;">
              <div class="card-brutal-neon" style="margin: 0; padding: 1.5rem;">
                <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.4rem; color: var(--fuchsia); margin-bottom: 0.8rem;">1. QUÉ ES UNA MODELO ANCLA</h4>
                <div class="text-editorial" style="font-size: 0.95rem;">
                  {format_paragraphs(m1_qes)}
                </div>
              </div>
              <div class="card-brutal-neon" style="margin: 0; padding: 1.5rem;">
                <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.4rem; color: var(--fuchsia); margin-bottom: 0.8rem;">2. LECTURA GENERAL DE REFERENCIA</h4>
                <div class="text-editorial" style="font-size: 0.95rem;">
                  {format_paragraphs(m1_lectura)}
                </div>
              </div>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 2rem;">
              <div class="card-brutal-neon" style="margin: 0; padding: 1.5rem;">
                <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.4rem; color: var(--fuchsia); margin-bottom: 0.8rem;">3. EDAD VISUAL Y PRESENCIA</h4>
                <div class="text-editorial" style="font-size: 0.95rem;">
                  {format_paragraphs(m1_edad)}
                </div>
              </div>
              <div class="card-brutal-neon" style="margin: 0; padding: 1.5rem;">
                <h4 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.4rem; color: var(--fuchsia); margin-bottom: 0.8rem;">4. ROSTRO Y DETALLES DE IDENTIDAD</h4>
                <div class="text-editorial" style="font-size: 0.95rem;">
                  {format_paragraphs(m1_rostro)}
                </div>
              </div>
            </div>
          </div>

          <!-- Model 1 Gallery -->
          <div class="card-brutal-neon">
            <h3 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1.5rem; text-transform: uppercase;">
              FOTOS DE REFERENCIA — MODELO ANCLA FEMENINA 01 (ALEXANDRA P - CLON CON IA)
            </h3>
            <div class="showcase-grid">
              <div class="showcase-item">
                <img src="/media/bonus_5/image1.jpg" alt="Modelo 1 Ref 1" />
                <div class="showcase-caption">image1.jpg - Retrato Frontal</div>
              </div>
              <div class="showcase-item">
                <img src="/media/bonus_5/image40.jpg" alt="Modelo 1 Ref 2" />
                <div class="showcase-caption">image40.jpg - Styling Denim</div>
              </div>
              <div class="showcase-item">
                <img src="/media/bonus_5/image3.jpg" alt="Modelo 1 Ref 3" />
                <div class="showcase-caption">image3.jpg - Cuerpo Completo</div>
              </div>
              <div class="showcase-item">
                <img src="/media/bonus_5/image2.jpg" alt="Modelo 1 Ref 4" />
                <div class="showcase-caption">image2.jpg - Perfil / Tres Cuartos</div>
              </div>
            </div>
          </div>

          <!-- Model 1 Prompts -->
          <div class="card-brutal">
            <h3 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.6rem; color: var(--fuchsia); text-transform: uppercase; margin-bottom: 1.2rem;">
              PROMPTS DE IDENTIDAD BASE (MODELO ANCLA 01)
            </h3>
            
            <div class="prompt-container">
              <div class="prompt-header">
                <span class="prompt-label">PROMPT 1: RETRATO UNIVERSAL (ANCHOR PORTRAIT)</span>
                <button class="copy-btn" type="button">
                  <svg style="width: 14px; height: 14px;"><use href="#copy-svg"></use></svg>
                  Copiar Prompt
                </button>
              </div>
              <pre class="prompt-text">Universal identity anchor portrait of a female editorial fashion model, visual age 22-28, oval-long face shape, warm light-to-medium olive skin tone with realistic natural texture, thick dark natural eyebrows, almond brown eyes, full natural lips, straight proportional nose, defined but soft jawline, long elegant neck, slender tall editorial body proportions. Long dark brown straight hair with a clean center part and natural polished fall. Neutral calm confident expression, direct editorial gaze, minimal natural makeup, luminous realistic skin, visible subtle pores and natural details, no plastic skin, no excessive retouching. Wearing a simple black sleeveless top. Clean white or light gray studio background, soft editorial studio lighting, full-frame photography, 85mm lens, sharp focus on eyes and facial structure, fashion model test shoot aesthetic, no text, no logos, no CGI, no illustration, no beauty smoothing, retain natural imperfections.</pre>
            </div>

            <div class="prompt-container">
              <div class="prompt-header">
                <span class="prompt-label">PROMPT 2: CUERPO COMPLETO (FIT & LOOKBOOK)</span>
                <button class="copy-btn" type="button">
                  <svg style="width: 14px; height: 14px;"><use href="#copy-svg"></use></svg>
                  Copiar Prompt
                </button>
              </div>
              <pre class="prompt-text">Full-body model test shot of the same female editorial fashion model, visual age 22-28, warm olive skin tone, thick dark natural eyebrows, almond brown eyes, full natural lips, long dark brown straight hair with center part, slender tall editorial body proportions, long neck, relaxed straight posture, calm neutral expression. Wearing a simple black sleeveless fitted top and light blue straight-leg jeans, realistic fabric texture, natural folds, clean fit, black minimal heels. Standing front-facing in a clean white studio background, soft even editorial lighting, full-frame photography, 50mm lens, f/4, sharp focus on body proportions and outfit fit, no text, no logos, no CGI, no beauty smoothing, realistic fashion lookbook test image.</pre>
            </div>
            
            <div style="margin-top: 2rem;">
              <h3 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.5rem; color: var(--fuchsia); text-transform: uppercase; margin-bottom: 0.8rem;">
                INSTRUCCIONES Y DETALLES DE CONSISTENCIA
              </h3>
              {format_consistency_cards(m1_details)}
            </div>
          </div>

          <!-- Interactive Dossier Builder Component -->
          <div class="prompt-builder">
            <h3 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1.5rem; text-transform: uppercase;">
              DOSSIER CREATIVO INTERACTIVO DE MODELO ANCLA
            </h3>
            <p style="font-size: 0.95rem; margin-bottom: 2rem; opacity: 0.85;">
              Configura y edita los valores del Dossier del Modelo para visualizar la ficha técnica del Embajador de Marca y copiarla al portapapeles.
            </p>
            
            <div class="dossier-grid" style="margin: 0;">
              <!-- Left controls -->
              <div style="display: flex; flex-direction: column; gap: 1rem;">
                <div class="builder-field">
                  <label for="dos-input-name">Nombre Comercial</label>
                  <input type="text" id="dos-input-name" class="builder-input" value="Alexandra P (Clon con IA - No original)" />
                </div>
                <div class="builder-field">
                  <label for="dos-input-age">Edad Visual</label>
                  <input type="text" id="dos-input-age" class="builder-input" value="22 a 28 años" />
                </div>
                <div class="builder-field">
                  <label for="dos-input-origin">Etnicidad / Origen</label>
                  <input type="text" id="dos-input-origin" class="builder-input" value="Oliva Clara / Mediterránea" />
                </div>
                <div class="builder-field">
                  <label for="dos-input-role">Rol en Campaña</label>
                  <input type="text" id="dos-input-role" class="builder-input" value="Rostro Coherente de Colección" />
                </div>
                <div class="builder-field">
                  <label for="dos-input-essence">Rasgos Clave</label>
                  <textarea id="dos-input-essence" class="builder-input" rows="2" style="resize: none; font-family: inherit;">Rostro ovalado-alargado, cejas gruesas y oscuras, ojos almendrados marrones, labios carnosos.</textarea>
                </div>
                <div class="builder-field">
                  <label for="dos-input-thesis">Cabello</label>
                  <textarea id="dos-input-thesis" class="builder-input" rows="2" style="resize: none; font-family: inherit;">Largo castaño oscuro, liso, raya al centro con caída limpia y natural.</textarea>
                </div>
                <div class="builder-field">
                  <label for="dos-input-contradiction">Cuerpo y Altura</label>
                  <textarea id="dos-input-contradiction" class="builder-input" rows="2" style="resize: none; font-family: inherit;">Delgado, esbelto, proporciones editoriales, cuello largo y clavículas visibles.</textarea>
                </div>
                <div class="builder-field">
                  <label for="dos-input-quote">Viba / Energía</label>
                  <input type="text" id="dos-input-quote" class="builder-input" value="Expresión neutral, serena, segura y sofisticada" />
                </div>
              </div>

              <!-- Right dossier visual card -->
              <div class="dossier-portrait-card" style="box-shadow: 0 0 20px rgba(255, 0, 127, 0.1); border-color: var(--fuchsia);">
                <div class="dossier-title-bar">
                  <h3 class="dossier-name" id="dos-out-name">Alexandra P (Clon con IA - No original)</h3>
                  <span class="dossier-role" id="dos-out-role">Rostro Coherente de Colección</span>
                </div>
                
                <div style="display: grid; grid-template-columns: 180px 1fr; gap: 1.5rem; margin-bottom: 1.5rem;">
                  <div class="dossier-portrait-wrapper" style="border-color: var(--fuchsia);">
                    <img id="dos-portrait" src="/media/bonus_5/image1.jpg" alt="Dossier Portrait" />
                  </div>
                  
                  <div class="dossier-details" style="gap: 0.8rem;">
                    <div class="dossier-spec">
                      <span>Edad Visual</span>
                      <p id="dos-card-age">22 a 28 años</p>
                    </div>
                    <div class="dossier-spec">
                      <span>Etnicidad</span>
                      <p id="dos-card-origin">Oliva Clara / Mediterránea</p>
                    </div>
                    <div class="dossier-spec">
                      <span>Esencia Narrativa</span>
                      <p id="dos-out-essence">Rostro ovalado-alargado, cejas gruesas y oscuras, ojos almendrados marrones, labios carnosos.</p>
                    </div>
                  </div>
                </div>

                <div class="dossier-spec" style="margin-bottom: 0.8rem;">
                  <span>Estructura de Cabello</span>
                  <p id="dos-out-thesis">Largo castaño oscuro, liso, raya al centro con caída limpia y natural.</p>
                </div>
                <div class="dossier-spec" style="margin-bottom: 0.8rem;">
                  <span>Líneas Corporales</span>
                  <p id="dos-out-contradiction">Delgado, esbelto, proporciones editoriales, cuello largo y clavículas visibles.</p>
                </div>
                
                <div style="background-color: var(--black-deep); padding: 1rem; border-left: 3px solid var(--fuchsia); font-style: italic; font-size: 0.9rem; margin-top: auto; color: var(--fuchsia);" id="dos-out-quote">
                  "Expresión neutral, serena, segura y sofisticada"
                </div>

                <div class="prompt-container" style="margin-top: 1.5rem; border-color: rgba(255, 255, 255, 0.15); box-shadow: none; padding: 1rem;">
                  <div class="prompt-header" style="border: none; padding: 0; margin-bottom: 0.5rem;">
                    <span class="prompt-label">COMPILACIÓN NARRATIVA IA</span>
                    <button class="copy-btn" type="button" style="padding: 0.2rem 0.6rem; font-size: 0.65rem;">Copiar Ficha</button>
                  </div>
                  <pre class="prompt-text" id="dossier-output-text" style="font-size: 0.75rem; max-height: 120px; color: var(--white);"></pre>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Sección 03: Mundo 01 - Naturaleza Editorial -->
        <section id="mundo-1">
          <div class="section-meta">
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
            <span>[ MUNDO 01 / COLECCIÓN FEMENINA ]</span>
          </div>

          <h2 class="section-title">
            MUNDO 01: NATURALEZA EDITORIAL - <span class="trends">LA PRENDA NACE DEL ENTORNO</span>
          </h2>

          <div class="card-brutal" style="margin-bottom: 4rem;">
            <h3 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1.2rem; text-transform: uppercase;">
              DIRECCIÓN CREATIVA Y PRINCIPIOS DE MUNDO 01
            </h3>
            <div class="text-editorial">
              {format_paragraphs(c1_theory)}
            </div>
          </div>

          <h2 class="section-title" style="font-size: 2.2rem; margin-bottom: 3rem; border-bottom: 2px dashed var(--fuchsia); padding-bottom: 1rem;">
            RESULTADOS DE CAMPAÑA — 10 VISTAS DE NATURALEZA EDITORIAL (ALINEADOS CON PROMPTS)
          </h2>

          <!-- Campaign 1 Side-by-Side Results -->
          <div style="margin-bottom: 4rem;">
            {generate_alternating_rows(c1_results, camp1_imgs)}
          </div>

          <!-- Campaign 1 Closing -->
          <div style="margin-top: 4rem;">
            <h2 class="section-title" style="font-size: 2.2rem; margin-bottom: 2rem; border-bottom: 2px dashed var(--fuchsia); padding-bottom: 1rem;">
              CIERRE Y LECCIONES DE MUNDO 01
            </h2>
            {format_c1_closure(c1_closure)}
          </div>
        </section>

        <!-- Sección 04: Mundo 02 - Drop Streetwear -->
        <section id="mundo-2">
          <div class="section-meta">
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
            <span>[ MUNDO 02 / DROP STREETWEAR ]</span>
          </div>

          <h2 class="section-title">
            MUNDO 02: DROP STREETWEAR - <span class="trends">ACTITUD Y PESO VISUAL URBANO</span>
          </h2>

          <div class="card-brutal" style="margin-bottom: 4rem;">
            <h3 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1.2rem; text-transform: uppercase;">
              ACCESO DIRECTO A LA CAMPAÑA EN PRODUCCIÓN
            </h3>
            <p style="font-size: 1rem; margin-bottom: 1.5rem; opacity: 0.9;">
              Accede al entorno montado en vivo de este lanzamiento streetwear de e-commerce real con modelo ancla consistente:
            </p>
            <div class="direct-link-container">
              <a href="https://xrtawsv7e2vcg.ok.kimi.link/" target="_blank" class="direct-link-btn">
                ↗ ACCEDER AL DROP STREETWEAR EN VIVO
              </a>
            </div>
          </div>

          <div style="margin-bottom: 4rem;">
            {format_points_to_cards(c2_theory, force_card_marker=True, allowed_prompt_nums=[10], avoid_nums=[11])}
          </div>

          <h2 class="section-title" style="font-size: 2.2rem; margin-bottom: 3rem; border-bottom: 2px dashed var(--fuchsia); padding-bottom: 1rem;">
            RESULTADOS DE CAMPAÑA — 8 VISTAS DROP STREETWEAR URBANO (ALINEADOS CON PROMPTS)
          </h2>

          <!-- Campaign 2 Side-by-Side Results -->
          <div style="margin-bottom: 4rem;">
            {generate_alternating_rows(c2_results[:8], camp2_imgs)}
          </div>

          <!-- Campaign 2 Closing -->
          <div style="margin-top: 4rem;">
            <h2 class="section-title" style="font-size: 2.2rem; margin-bottom: 2rem; border-bottom: 2px dashed var(--fuchsia); padding-bottom: 1rem;">
              CIERRE Y LECCIONES DE MUNDO 02
            </h2>
            {format_points_to_cards(c2_closure, force_card_marker=True, allowed_prompt_nums=[25, 26, 27, 28], avoid_nums=[29])}
          </div>
        </section>

        <!-- Sección 05: Mundo 03 - Tennis Club Drop (Bárbara Palvin) -->
        <section id="mundo-3">
          <div class="section-meta">
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
            <span>[ MUNDO 03 / TENNIS CLUB DROP - BÁRBARA PALVIN ]</span>
          </div>

          <h2 class="section-title">
            MUNDO 03: TENNIS CLUB DROP - <span class="trends">ROPA DEPORTIVA REALISTA CON IA</span>
          </h2>

          <div class="card-brutal" style="margin-bottom: 4rem;">
            <h3 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1.2rem; text-transform: uppercase;">
              ACCESO DIRECTO A LA CAMPAÑA EN PRODUCCIÓN
            </h3>
            <p style="font-size: 1rem; margin-bottom: 1.5rem; opacity: 0.9;">
              Accede al entorno de la campaña deportiva completa del drop de tenis en vivo:
            </p>
            <div class="direct-link-container">
              <a href="https://czrdsgvw7axs2.ok.kimi.link/" target="_blank" class="direct-link-btn">
                ↗ ACCEDER AL TENNIS CLUB DROP EN VIVO
              </a>
            </div>
          </div>

          <!-- Model 2 References -->
          <div class="card-brutal-neon" style="margin-bottom: 4rem;">
            <h3 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1.5rem; text-transform: uppercase;">
              FOTOS DE REFERENCIA — MODELO ANCLA DEPORTIVA 02 (BÁRBARA PALVIN)
            </h3>
            <div class="showcase-grid">
              <div class="showcase-item">
                <img src="/media/bonus_5/image23.png" alt="Modelo 2 Ref 1" />
                <div class="showcase-caption">image23.png - Rostro Base</div>
              </div>
              <div class="showcase-item">
                <img src="/media/bonus_5/image18.jpg" alt="Modelo 2 Ref 2" />
                <div class="showcase-caption">image18.jpg - Enfoque Lentes</div>
              </div>
              <div class="showcase-item">
                <img src="/media/bonus_5/image17.jpg" alt="Modelo 2 Ref 3" />
                <div class="showcase-caption">image17.jpg - Mano / Carteras</div>
              </div>
              <div class="showcase-item">
                <img src="/media/bonus_5/image26.jpg" alt="Modelo 2 Ref 4" />
                <div class="showcase-caption">image26.jpg - Luz de Tarde</div>
              </div>
            </div>
          </div>

          <!-- Campaign 3 Theory & Model -->
          <div style="margin-bottom: 4rem;">
            {format_points_to_cards(c3_model_info, force_card_marker=True, allowed_prompt_nums=[12, 13, 14], avoid_nums=[5])}
          </div>

          <div style="margin-bottom: 4rem;">
            {format_points_to_cards(c3_theory, force_card_marker=True, allowed_prompt_nums=[8, 9])}
          </div>

          <h2 class="section-title" style="font-size: 2.2rem; margin-bottom: 3rem; border-bottom: 2px dashed var(--fuchsia); padding-bottom: 1rem;">
            RESULTADOS DE CAMPAÑA — 16 VISTAS TENNIS CLUB DROP (ALINEADOS CON PROMPTS)
          </h2>

          <!-- Campaign 3 Side-by-Side Results -->
          <div style="margin-bottom: 4rem;">
            {generate_alternating_rows(c3_results, camp3_imgs[:16])}
          </div>

          <!-- Additional images (the remaining 4 images out of the 20) -->
          <div class="card-brutal" style="margin-top: 4rem; margin-bottom: 4rem;">
            <h3 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; margin-bottom: 1.5rem; text-transform: uppercase;">
              ÁNGULOS Y DETALLES ADICIONALES DE LA COLECCIÓN
            </h3>
            <div class="showcase-grid" style="grid-template-columns: repeat(4, 1fr);">
              <div class="showcase-item">
                <img src="/media/bonus_5/image27.jpg" alt="Detalle Adicional 17" />
                <div class="showcase-caption">27. Billetera de Cuero</div>
              </div>
              <div class="showcase-item">
                <img src="/media/bonus_5/image6.jpg" alt="Detalle Adicional 18" />
                <div class="showcase-caption">06. Accesorio Pelo Sutil</div>
              </div>
              <div class="showcase-item">
                <img src="/media/bonus_5/image42.jpg" alt="Detalle Adicional 19" />
                <div class="showcase-caption">42. Llavero / Herraje Metal</div>
              </div>
              <div class="showcase-item">
                <img src="/media/bonus_5/image7.jpg" alt="Detalle Adicional 20" />
                <div class="showcase-caption">07. Puesta en Escena Calle</div>
              </div>
            </div>
          </div>

          <!-- Campaign 3 Closing -->
          <div style="margin-top: 4rem;">
            <h2 class="section-title" style="font-size: 2.2rem; margin-bottom: 2rem; border-bottom: 2px dashed var(--fuchsia); padding-bottom: 1rem;">
              CIERRE Y LECCIONES DE MUNDO 03
            </h2>
            {format_points_to_cards(c3_closure, force_card_marker=True, allowed_prompt_nums=[30], avoid_nums=[31])}
          </div>
        </section>

        <!-- Compiled Prompt Builder Component -->
        <section id="prompt-generator">
          <div class="section-meta">
            <span>[ HERRAMIENTA INTERACTIVA / GENERADOR DE PROMPTS ]</span>
          </div>
          <h2 class="section-title">COMPILADOR DE PROMPTS <span class="trends">EDITORIALES IA</span></h2>
          
          <div class="prompt-builder" style="background-color: var(--black-light); border-color: var(--fuchsia);">
            <div class="builder-grid">
              <div class="builder-field">
                <label for="layer-gender">Género del Modelo</label>
                <select id="layer-gender" class="builder-input">
                  <option value="female" selected>Femenino (Female)</option>
                  <option value="male">Masculino (Male)</option>
                  <option value="non-binary">No binario (Non-binary)</option>
                </select>
              </div>
              <div class="builder-field">
                <label for="layer-age">Edad Visual</label>
                <select id="layer-age" class="builder-input">
                  <option value="22-28" selected>22 a 28 años</option>
                  <option value="28-35">28 a 35 años</option>
                  <option value="18-22">18 a 22 años</option>
                </select>
              </div>
              <div class="builder-field">
                <label for="layer-ethnicity">Etnicidad / Origen</label>
                <input type="text" id="layer-ethnicity" class="builder-input" value="light-to-medium olive skin tone" />
              </div>
              <div class="builder-field">
                <label for="layer-face">Facciones del Rostro</label>
                <input type="text" id="layer-face" class="builder-input" value="oval face shape, thick dark eyebrows, almond brown eyes, full natural lips" />
              </div>
              <div class="builder-field">
                <label for="layer-hair">Estilo de Cabello</label>
                <input type="text" id="layer-hair" class="builder-input" value="long dark brown straight hair with center part" />
              </div>
              <div class="builder-field">
                <label for="layer-realism">Detalles de Realismo</label>
                <input type="text" id="layer-realism" class="builder-input" value="visible pores, natural skin texture, slight skin redness" />
              </div>
              <div class="builder-field">
                <label for="layer-energy">Expresión / Actitud</label>
                <input type="text" id="layer-energy" class="builder-input" value="calm serious editorial expression, confident gaze" />
              </div>
              <div class="builder-field">
                <label for="layer-wardrobe">Prenda / Outfit</label>
                <input type="text" id="layer-wardrobe" class="builder-input" value="flowing green slip dress, natural fabric wrinkles" />
              </div>
              <div class="builder-field">
                <label for="layer-environment">Entorno / Escenario</label>
                <input type="text" id="layer-environment" class="builder-input" value="lush tropical rainforest with wet leaves and mossy tree trunks" />
              </div>
              <div class="builder-field">
                <label for="layer-lighting">Esquema de Luz</label>
                <input type="text" id="layer-lighting" class="builder-input" value="natural sunlight filtering through the leaf canopy, soft organic shadows" />
              </div>
              <div class="builder-field">
                <label for="layer-camera">Cámara y Enfoque</label>
                <input type="text" id="layer-camera" class="builder-input" value="full-frame fashion photography, 50mm lens, f/2.8, sharp focus" />
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr; gap: 1.5rem; margin-top: 2rem;">
              <div class="prompt-container" style="margin: 0; border-color: var(--fuchsia); box-shadow: none;">
                <div class="prompt-header">
                  <span class="prompt-label" style="color: var(--fuchsia);">PROMPT DE TEXTO COMPILADO (EN INGLÉS)</span>
                  <button class="copy-btn" type="button">Copiar Prompt</button>
                </div>
                <pre class="prompt-text" id="live-builder-prompt" style="font-size: 0.85rem; max-height: 250px;"></pre>
              </div>
              <div class="prompt-container" style="margin: 0; border-color: var(--fuchsia); box-shadow: none;">
                <div class="prompt-header">
                  <span class="prompt-label" style="color: var(--fuchsia);">FICHA CONFIGURACIÓN JSON</span>
                  <button class="copy-btn" type="button">Copiar JSON</button>
                </div>
                <pre class="prompt-text" id="live-builder-json" style="font-family: monospace; font-size: 0.75rem; max-height: 250px;"></pre>
              </div>
            </div>
          </div>
        </section>

        <!-- Sección 06: Checklist de Auditoría -->
        <section id="checklist-audit">
          <div class="section-meta">
            <svg style="width: 14px; height: 14px; fill: currentColor; margin-right: 0.25rem;"><use href="#crosshair-svg"></use></svg>
            <span>[ SECCIÓN 06 / CIERRE Y AUDITORÍA ]</span>
          </div>

          <h2 class="section-title">
            DISEÑA LANZAMIENTOS, <span class="trends">CREA UNIVERSOS DESEABLES</span>
          </h2>

          <div class="text-editorial">
            <p>
              Al finalizar este bonus, el alumno deja de pensar en "imágenes perfectas sueltas" y pasa a coordinar un sistema visual completo para su marca.
            </p>
            
            <div class="card-brutal" style="margin-top: 2rem; border-color: var(--fuchsia); background-color: var(--black-deep);">
              <h3 style="font-family: 'Bebas Neue', sans-serif; font-size: 1.5rem; color: var(--fuchsia); margin-bottom: 1rem; text-transform: uppercase;">
                CHECKLIST PARA AUDITAR TU CAMPAÑA
              </h3>
              <ul style="margin-left: 1.5rem; font-size: 0.95rem; display: flex; flex-direction: column; gap: 0.6rem; list-style: square;">
                <li>¿Se entiende claramente el producto principal?</li>
                <li>¿Mantiene la modelo ancla consistencia facial en todos los planos?</li>
                <li>¿La paleta de color dialoga con el entorno y la prenda?</li>
                <li>¿Tienes fotos limpias de catálogo, detalles macro de costura y escenas lifestyle?</li>
                <li>¿Las imágenes están cortadas en los formatos correctos (anuncio vertical, banner web)?</li>
                <li>¿La piel se ve realista con textura y poros visibles en lugar de un alisado de muñeca plástica?</li>
              </ul>
            </div>
          </div>
        </section>
      </main>
    </div>

    <!-- Lightbox Zoom Modal Component -->
    <div class="brutal-lightbox">
      <div class="lightbox-content">
        <span class="lightbox-close">&times;</span>
        <img src="" alt="Ampliado" class="lightbox-img" />
        <div class="lightbox-caption">Detalle del Lanzamiento</div>
      </div>
    </div>
  </body>
</html>
"""

# Write out html file
out_html_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\3-lanzamientos-editoriales-copiables.html"
with open(out_html_path, "w", encoding="utf-8") as f_out:
    f_out.write(html_template)

print(f"Core landing page written successfully to {out_html_path}")
