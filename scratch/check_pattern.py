import re

text_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\BONUS_5_TEXT.txt"

with open(text_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

pattern = r'^\d+\.\s+(IMAGEN|RESULTADO|RESULTADO\s+)\d+'

for i in range(1080, 1090):
    line = lines[i]
    stripped = line.strip()
    match = re.match(pattern, stripped)
    print(f"Line {i+1}: {repr(line)} | Stripped: {repr(stripped)} | Match: {bool(match)}")
