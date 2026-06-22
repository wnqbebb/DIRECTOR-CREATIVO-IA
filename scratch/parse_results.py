import re

text_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\BONUS_5_TEXT.txt"

with open(text_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

def scan_section(start, end, label):
    print(f"\n--- Scanning {label} (lines {start} to {end}) ---")
    for idx in range(start-1, min(end, len(lines))):
        line = lines[idx].strip()
        if re.search(r'^(IMAGEN|RESULTADO|RESULTADO\s+)\d+', line, re.IGNORECASE):
            print(f"Line {idx+1}: {line}")
            # Print next 5 lines
            for offset in range(1, 10):
                if idx+offset < len(lines):
                    next_line = lines[idx+offset].strip()
                    if next_line:
                        print(f"  + {next_line[:120]}")

# Campaña 1
scan_section(910, 1378, "Campaña 1")

# Campaña 2
scan_section(1384, 1845, "Campaña 2")
