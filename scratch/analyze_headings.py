import re

text_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\BONUS_5_TEXT.txt"

with open(text_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        stripped = line.strip()
        if not stripped:
            continue
        # Check if line looks like a header (uppercase, short, or containing numbers/sections)
        if stripped.isupper() and len(stripped) < 100:
            print(f"Line {i+1}: {stripped}")
        elif re.match(r'^\d+\..*', stripped):
            print(f"Line {i+1}: {stripped}")
