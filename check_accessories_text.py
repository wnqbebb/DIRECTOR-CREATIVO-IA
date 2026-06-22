with open("BONUS_5_TEXT.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx in range(350, 515):
    if idx < len(lines):
        print(f"Line {idx+1}: {lines[idx]}", end="")
