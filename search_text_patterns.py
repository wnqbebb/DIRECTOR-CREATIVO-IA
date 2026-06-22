with open("BONUS_5_TEXT.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    l = line.strip()
    if "IMAGEN " in l.upper() or "RESULTADO " in l.upper() or "MUNDO " in l.upper():
        print(f"Line {idx+1}: {l}")
