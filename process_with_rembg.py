import os
import sys
from PIL import Image

try:
    from rembg import remove
except ImportError:
    print("rembg is not installed. Run 'pip install rembg' first.")
    sys.exit(1)

def clean_bg_ai(img_path, out_path):
    print(f"Removing background from {img_path} using AI (rembg)...")
    try:
        input_image = Image.open(img_path)
        # rembg automatic background removal
        output_image = remove(input_image)
        output_image.save(out_path, "PNG")
        print(f"Success! Saved to {out_path}")
    except Exception as e:
        print(f"Error processing {img_path}: {e}")

def main():
    brain_dir = "C:/Users/Admin/.gemini/antigravity-ide/brain/68aca044-0357-4016-8ded-47a78f44aa27"
    media_dir = "public/media"
    
    # Let's test on the newly uploaded guy_tech_jacket to compare the cutout quality!
    src = os.path.join(brain_dir, "media__1782002051269.png") # original guy tech jacket from brain
    dest = os.path.join(media_dir, "guy_tech_jacket_ai.png")
    
    clean_bg_ai(src, dest)
    print("AI background removal test finished.")

if __name__ == "__main__":
    main()
