import os
from PIL import Image

def process_black_bg(img, boost=1.5, threshold=15):
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        r, g, b, a = item
        v = max(r, g, b)
        if v < threshold:
            newData.append((0, 0, 0, 0))
        else:
            alpha = min(255, int(v * boost))
            # Keep original color but apply transparency
            newData.append((r, g, b, alpha))
    img.putdata(newData)
    return img

def process_white_bg(img, threshold=230):
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        r, g, b, a = item
        if r > threshold and g > threshold and b > threshold:
            # Scale alpha based on how close it is to white
            avg = (r + g + b) / 3.0
            if avg > 253:
                newData.append((0, 0, 0, 0))
            else:
                alpha = int((255 - avg) / (255 - threshold) * 255)
                alpha = max(0, min(255, alpha))
                # Set color to black or red depending on original tone
                newData.append((r, g, b, alpha))
        else:
            newData.append((r, g, b, 255))
    img.putdata(newData)
    return img

def main():
    media_dir = "public/media"
    out_dir = os.path.join(media_dir, "extracted")
    os.makedirs(out_dir, exist_ok=True)

    # 1. SLICE TAPES (brand_tapes.jpg) - 3 columns, 6 rows roughly
    # Image size is 1024x1024. Let's slice it into a 3x6 grid.
    print("Slicing tapes...")
    tapes_img = Image.open(os.path.join(media_dir, "brand_tapes.jpg"))
    cols, rows = 3, 6
    cell_w = 1024 // cols
    cell_h = 1024 // rows
    for r in range(rows):
        for c in range(cols):
            # Crop cell
            box = (c * cell_w, r * cell_h, (c + 1) * cell_w, (r + 1) * cell_h)
            cropped = tapes_img.crop(box)
            # Find actual content bounding box (to remove empty black space)
            # Find pixels > threshold
            temp_proc = process_black_bg(cropped, boost=2.0, threshold=10)
            bbox = temp_proc.getbbox()
            if bbox:
                final_img = temp_proc.crop(bbox)
                # Avoid saving tiny noise
                if final_img.width > 20 and final_img.height > 20:
                    final_img.save(os.path.join(out_dir, f"tape_{r}_{c}.png"))

    # 2. SLICE LINES (brand_lines.jpg) - 3 columns, 10 rows roughly
    print("Slicing lines...")
    lines_img = Image.open(os.path.join(media_dir, "brand_lines.jpg"))
    cols, rows = 3, 10
    cell_w = 1024 // cols
    cell_h = 1024 // rows
    for r in range(rows):
        for c in range(cols):
            box = (c * cell_w, r * cell_h, (c + 1) * cell_w, (r + 1) * cell_h)
            cropped = lines_img.crop(box)
            temp_proc = process_black_bg(cropped, boost=2.0, threshold=12)
            bbox = temp_proc.getbbox()
            if bbox:
                final_img = temp_proc.crop(bbox)
                if final_img.width > 20 and final_img.height > 5:
                    final_img.save(os.path.join(out_dir, f"line_{r}_{c}.png"))

    # 3. SLICE SPLATTERS (brand_splatters.jpg) - 3 columns, 6 rows roughly
    # Note: Top left corner has white text, let's bypass or crop around it
    print("Slicing splatters...")
    splatters_img = Image.open(os.path.join(media_dir, "brand_splatters.jpg"))
    cols, rows = 3, 6
    cell_w = 1024 // cols
    cell_h = 1024 // rows
    for r in range(rows):
        for c in range(cols):
            # Skip top-left text area if r == 0 and c == 0
            if r == 0 and c == 0:
                # We can crop it but offset down to avoid the text
                box = (c * cell_w, r * cell_h + 100, (c + 1) * cell_w, (r + 1) * cell_h)
            else:
                box = (c * cell_w, r * cell_h, (c + 1) * cell_w, (r + 1) * cell_h)
            cropped = splatters_img.crop(box)
            temp_proc = process_black_bg(cropped, boost=2.0, threshold=12)
            bbox = temp_proc.getbbox()
            if bbox:
                final_img = temp_proc.crop(bbox)
                if final_img.width > 15 and final_img.height > 15:
                    final_img.save(os.path.join(out_dir, f"splatter_{r}_{c}.png"))

    # 4. SLICE HALFTONES (brand_halftones.jpg) - 4 columns, 5 rows roughly
    print("Slicing halftones...")
    halftones_img = Image.open(os.path.join(media_dir, "brand_halftones.jpg"))
    cols, rows = 4, 5
    cell_w = 1024 // cols
    cell_h = 1024 // rows
    for r in range(rows):
        for c in range(cols):
            box = (c * cell_w, r * cell_h, (c + 1) * cell_w, (r + 1) * cell_h)
            cropped = halftones_img.crop(box)
            temp_proc = process_black_bg(cropped, boost=2.0, threshold=8)
            bbox = temp_proc.getbbox()
            if bbox:
                final_img = temp_proc.crop(bbox)
                if final_img.width > 15 and final_img.height > 15:
                    final_img.save(os.path.join(out_dir, f"halftone_{r}_{c}.png"))

    # 5. SLICE ARROWS (brand_arrows.png) - White background. 5 columns, 10 rows roughly
    print("Slicing arrows...")
    arrows_img = Image.open(os.path.join(media_dir, "brand_arrows.png"))
    cols, rows = 5, 10
    cell_w = 1024 // cols
    cell_h = 1024 // rows
    for r in range(rows):
        for c in range(cols):
            box = (c * cell_w, r * cell_h, (c + 1) * cell_w, (r + 1) * cell_h)
            cropped = arrows_img.crop(box)
            temp_proc = process_white_bg(cropped, threshold=240)
            bbox = temp_proc.getbbox()
            if bbox:
                final_img = temp_proc.crop(bbox)
                if final_img.width > 10 and final_img.height > 10:
                    final_img.save(os.path.join(out_dir, f"arrow_{r}_{c}.png"))

    print("Brand assets successfully extracted and saved in public/media/extracted/")

if __name__ == "__main__":
    main()
