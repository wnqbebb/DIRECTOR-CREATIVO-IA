import os
from PIL import Image

def main():
    media_dir = "public/media"
    out_dir = os.path.join(media_dir, "extracted")
    os.makedirs(out_dir, exist_ok=True)
    
    # Load sheet
    sheet_path = os.path.join(media_dir, "asset_sheet_20.png")
    sheet = Image.open(sheet_path).convert("RGBA")
    w, h = sheet.size
    
    # Grid parameters
    # The header is roughly the top 90 pixels
    grid_top = 90
    grid_h = h - grid_top
    cols, rows = 4, 5
    
    cell_w = w // cols
    cell_h = grid_h // rows
    
    print(f"Slicing brutalist sheet: {w}x{h}, cells of {cell_w}x{cell_h} starting from y={grid_top}")
    
    for r in range(rows):
        for c in range(cols):
            # Calculate box
            x0 = c * cell_w
            y0 = grid_top + (r * cell_h)
            x1 = (c + 1) * cell_w
            y1 = grid_top + ((r + 1) * cell_h)
            
            # Crop cell
            cropped = sheet.crop((x0, y0, x1, y1))
            
            # Remove title/labels by cropping the bottom ~15 pixels of the cell
            # because each cell has text labels like "1. CIRCULAR HALFTONE" at the bottom
            cropped_no_label = cropped.crop((0, 0, cell_w, cell_h - 15))
            
            # Find content bounding box
            bbox = cropped_no_label.getbbox()
            if bbox:
                final_img = cropped_no_label.crop(bbox)
                # Save if it has meaningful size
                if final_img.width > 10 and final_img.height > 10:
                    final_img.save(os.path.join(out_dir, f"brutalist_texture_{r}_{c}.png"))
                    
    print("Brutalist textures successfully extracted!")

if __name__ == "__main__":
    main()
