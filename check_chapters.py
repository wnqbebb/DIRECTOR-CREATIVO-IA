import os

layout_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\bonus_5_layout_layout.txt"
with open(layout_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

def print_around(index, window=10):
    idx_str = f"[{index}]"
    found = -1
    for i, line in enumerate(lines):
        if line.startswith(idx_str):
            found = i
            break
            
    if found != -1:
        start = max(0, found - 2)
        end = min(len(lines), found + window)
        print(f"=== Around Index {index} ===")
        for j in range(start, end):
            print(lines[j], end="")
        print("=" * 40)

# Check the surrounding paragraphs for each image block
print_around(513)
print_around(905)
print_around(1379)
print_around(1846)
print_around(2217)
