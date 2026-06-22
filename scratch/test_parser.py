import re

text_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\BONUS_5_TEXT.txt"

with open(text_path, "r", encoding="utf-8") as f:
    raw_lines = f.readlines()

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
            # Find prompt divider using simple check
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
                    "prompt": prompt,
                    "line_num": b["line_num"]
                })
            else:
                desc = " ".join(lines_list[1:])
                parsed_items.append({
                    "header": b["header"],
                    "title": title,
                    "description": desc,
                    "prompt": "",
                    "line_num": b["line_num"]
                })
                
    return parsed_items

# Test Campaña 2
c2_items = parse_campaign_blocks(1577, 1845)
print(f"Campaña 2 parsed: {len(c2_items)} items")
for item in c2_items[:2]:
    print(f"  Line: {item['line_num']} | Header: {item['header']} | Title: {item['title']}")
    print(f"    Desc: {item['description'][:100]}...")
    print(f"    Prompt: {item['prompt'][:100]}...")
