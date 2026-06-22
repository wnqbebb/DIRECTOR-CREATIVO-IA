import os

layout_path = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\bonus_5_layout_layout.txt"
if not os.path.exists(layout_path):
    print("File not found.")
    exit()

with open(layout_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

image_mappings = []
current_para = ""
current_idx = -1

for i, line in enumerate(lines):
    if line.startswith("["):
        parts = line.split("] P: ")
        if len(parts) > 1:
            current_idx = parts[0][1:]
            current_para = parts[1].strip()
    elif "IMAGES:" in line:
        images_str = line.split("IMAGES:")[1].strip()
        image_mappings.append({
            'idx': current_idx,
            'paragraph': current_para,
            'images': images_str
        })

print(f"Found {len(image_mappings)} image references:")
for m in image_mappings:
    print(f"Index {m['idx']} | Images: {m['images']}")
    print(f"   Para: {m['paragraph'][:120]}...")
    print("-" * 50)
