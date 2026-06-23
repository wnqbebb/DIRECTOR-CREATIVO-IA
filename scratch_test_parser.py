import re

file_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\BONUS_6_TEXT.txt"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines read: {len(lines)}")

prompts = []
campaigns = []

current_mode = None
current_item = None
in_pack_maestro = False

def clean_text(t):
    return t.replace(chr(8212), "-").strip()

for line_idx, raw_line in enumerate(lines):
    line = raw_line.strip()
    if not line:
        if current_item and current_mode == 'prompt' and 'prompt_lines' in current_item:
            current_item['prompt_lines'].append("")
        continue
        
    line_clean = clean_text(line)
    
    # Track when we enter PACK MAESTRO
    if "PACK MAESTRO" in line_clean.upper():
        in_pack_maestro = True
        # Save previous if any
        if current_item:
            if current_mode == 'prompt':
                prompts.append(current_item)
            elif current_mode == 'campaign':
                campaigns.append(current_item)
            current_item = None
            current_mode = None
        continue
    
    # Check if this line starts a detailed prompt: "PROMPT X - TITLE"
    if line_clean.upper().startswith("PROMPT "):
        match = re.match(r"^PROMPT\s+(\d+)\s*[-—]\s*(.*)$", line_clean, re.IGNORECASE)
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
            
    # Check if this line starts a campaign: "X. Campaña TITLE" (ONLY in Pack Maestro)
    if in_pack_maestro:
        match_camp = re.match(r"^(\d+)\.\s*Campa[ñn]a\s+(.*)$", line_clean, re.IGNORECASE)
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

    # If we are parsing a prompt
    if current_mode == 'prompt' and current_item:
        if line_clean.upper() in ["SIRVE PARA", "SIRVE PARA:", "PARA QUÉ SERVIRÁ", "PARA QUÉ SIRVE", "PARA QUÉ SIRVE:"]:
            current_item["current_field"] = 'sirve'
        elif line_clean.upper() in ["PROMPT", "PROMPT:", "PROMPT EN INGLÉS", "PROMPT DE GENERACIÓN", "PROMPT DE GENERACIÓN:"]:
            current_item["current_field"] = 'prompt'
        elif line_clean.upper() in ["QUÉ MODIFICAR", "QUÉ MODIFICAR:", "QUÉ SE PUEDE MODIFICAR", "QUÉ SE PUEDE MODIFICAR:"]:
            current_item["current_field"] = 'modificar'
        elif line_clean.upper() in ["QUÉ NO TOCAR", "QUÉ NO TOCAR:", "QUÉ NO SE DEBE TOCAR", "QUÉ NO SE DEBE TOCAR:"]:
            current_item["current_field"] = 'tocar'
        elif line_clean.upper() in ["NOTA", "NOTA:", "NOTA DE DIRECCIÓN CREATIVA", "NOTA DE DIRECCIÓN CREATIVA:"]:
            current_item["current_field"] = 'nota'
        else:
            field = current_item["current_field"]
            if field == 'sirve':
                current_item["sirve_lines"].append(line_clean)
            elif field == 'prompt':
                current_item["prompt_lines"].append(raw_line.rstrip('\r\n')) # keep spaces
            elif field == 'modificar':
                current_item["modificar_lines"].append(line_clean)
            elif field == 'tocar':
                current_item["tocar_lines"].append(line_clean)
            elif field == 'nota':
                current_item["nota_lines"].append(line_clean)
                
    # If we are parsing a campaign
    elif current_mode == 'campaign' and current_item:
        if line_clean.upper() in ["NOMBRE DE CAMPAÑA", "NOMBRE DE CAMPAÑA:", "NOMBRE", "NOMBRE DE LA CAMPAÑA", "NOMBRE DE LA CAMPAÑA:"]:
            current_item["current_field"] = 'name'
        elif line_clean.upper() in ["IDEA CENTRAL", "IDEA CENTRAL:", "CONCEPTO", "CONCEPTO:"]:
            current_item["current_field"] = 'idea'
        elif line_clean.upper() in ["IDEAL PARA", "IDEAL PARA:", "PRENDAS IDEALES", "PRENDAS IDEALES:"]:
            current_item["current_field"] = 'ideal'
        elif line_clean.upper() in ["ADN VISUAL", "ADN VISUAL:", "DIRECCIÓN DE ARTE", "DIRECCIÓN DE ARTE:"]:
            current_item["current_field"] = 'adn'
        elif line_clean.upper() in ["DIRECCIÓN DE STYLING", "DIRECCIÓN DE STYLING:", "STYLING", "STYLING:"]:
            current_item["current_field"] = 'styling'
        elif line_clean.upper() in ["STORYBOARD", "STORYBOARD:", "ESCENAS", "ESCENAS:"]:
            current_item["current_field"] = 'storyboard'
        elif line_clean.upper().startswith("PROMPT"):
            current_item["current_field"] = f"prompt:{line_clean}"
            current_item["prompts"].append({
                "label": line_clean,
                "lines": []
            })
        elif line_clean.upper() in ["COPY DE VENTA", "COPY DE VENTA:", "COPY DE ANUNCIO", "COPY DE ANUNCIO:", "COPY DE VENTA RÁPIDA", "COPY DE VENTA RÁPIDA:"]:
            current_item["current_field"] = 'copy'
        elif line_clean.upper() in ["CTA", "CTA:", "CALL TO ACTION", "CALL TO ACTION:"]:
            current_item["current_field"] = 'cta'
        else:
            field = current_item["current_field"]
            if field == 'name':
                current_item["name"] = line_clean
            elif field == 'idea':
                current_item["idea"] += (" " if current_item["idea"] else "") + line_clean
            elif field == 'ideal':
                current_item["ideal"] += (" " if current_item["ideal"] else "") + line_clean
            elif field == 'adn':
                current_item["adn"] += (" " if current_item["adn"] else "") + line_clean
            elif field == 'styling':
                current_item["styling"] += (" " if current_item["styling"] else "") + line_clean
            elif field == 'storyboard':
                current_item["storyboard_lines"].append(line_clean)
            elif field and field.startswith("prompt:"):
                current_item["prompts"][-1]["lines"].append(raw_line.rstrip('\r\n'))
            elif field == 'copy':
                current_item["copy_lines"].append(line_clean)
            elif field == 'cta':
                current_item["cta_lines"].append(line_clean)

# Add last item
if current_item:
    if current_mode == 'prompt':
        prompts.append(current_item)
    elif current_mode == 'campaign':
        campaigns.append(current_item)

# Post-processing: clean up lists of lines
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

print(f"Parsed {len(prompts)} detailed prompts.")
print(f"Parsed {len(campaigns)} campaigns.")

if campaigns:
    print("\n--- SAMPLE CAMPAIGN 1 ---")
    c1 = campaigns[0]
    print(f"Num: {c1['num']}")
    print(f"Type: {c1['type']}")
    print(f"Name: {c1['name']}")
    print(f"Idea: {c1['idea']}")
    print(f"Storyboard: {c1['storyboard']}")
    print(f"Copy: {c1['copy']}")
    print(f"CTA: {c1['cta']}")
    print(f"Prompts count: {len(c1['prompts'])}")
    for pr in c1['prompts']:
        print(f"  {pr['label']}: {pr['value'][:60]}...")
