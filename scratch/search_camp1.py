text_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\BONUS_5_TEXT.txt"

with open(text_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Print lines 910 to 1100 to inspect Campaña 1 structure
for idx in range(910 - 1, min(1100, len(lines))):
    line = lines[idx].strip()
    if line:
        print(f"Line {idx+1}: {line[:120]}")
