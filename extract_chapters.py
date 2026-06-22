import re

with open("BONUS_5_TEXT.txt", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split('\n')
for idx, line in enumerate(lines):
    line_strip = line.strip()
    # Find headers (lines starting with numbers, CAPÍTULO, CAMPAÑA, or all uppercase short lines)
    if re.match(r'^\d+\.', line_strip) or line_strip.startswith("CAPÍTULO") or line_strip.startswith("CAMPAÑA") or (line_strip.isupper() and len(line_strip) < 60 and len(line_strip) > 3):
        print(f"Line {idx+1}: {line_strip}")
