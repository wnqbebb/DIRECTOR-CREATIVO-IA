import re

text_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\BONUS_5_TEXT.txt"
with open(text_path, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

m1_details_lines = lines[610:906]  # Lines 611 to 906 (0-indexed 610 to 906)

headings = []
for idx, line in enumerate(m1_details_lines):
    line_num = 611 + idx
    stripped = line.strip()
    if not stripped:
        continue
    # Match headers starting with digits followed by dot (e.g. "6. OJOS Y MIRADA" or "20. DESCRIPCIÓN MAESTRA")
    if re.match(r'^\d+\.\s+[A-ZÁÉÍÓÚÑa-z]', stripped):
        headings.append((line_num, stripped))

print(f"Parsed {len(headings)} headings:")
for line_num, h in headings:
    print(f"  Line {line_num}: {h}")
