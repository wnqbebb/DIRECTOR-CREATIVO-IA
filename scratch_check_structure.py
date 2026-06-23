import re

file_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\BONUS_6_TEXT.txt"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Let's search for lines containing "PROMPT" or "CAMPAÑA"
for idx, line in enumerate(lines):
    if "PROMPT" in line.upper() and len(line.strip()) < 100:
        print(f"Line {idx+1}: {line.strip()}")
    if "CAMPAÑA" in line.upper() and len(line.strip()) < 100:
        print(f"Line {idx+1}: {line.strip()}")
