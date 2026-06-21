import os
import sys
from PIL import Image

try:
    from rembg import remove
except ImportError:
    print("rembg is not installed. Run 'pip install rembg' first.")
    sys.exit(1)

def process_image(src_path, dest_path):
    print(f"AI background removal on {src_path}...")
    try:
        input_image = Image.open(src_path)
        output_image = remove(input_image)
        output_image.save(dest_path, "PNG")
        print(f"Successfully saved to {dest_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    brain_dir = "C:/Users/Admin/.gemini/antigravity-ide/brain/68aca044-0357-4016-8ded-47a78f44aa27"
    media_dir = "public/media"
    
    # New assets
    assets = {
        "media__1782003344879.png": "woman_tech_coat.png",
        "media__1782003344899.png": "guy_sitting_tech.png",
        "media__1782003344916.png": "girl_helmet.png",
        "media__1782003344946.png": "guy_tech_walking.png"
    }
    
    for brain_name, local_name in assets.items():
        src = os.path.join(brain_dir, brain_name)
        dest = os.path.join(media_dir, local_name)
        if os.path.exists(src):
            process_image(src, dest)
        else:
            print(f"Source file {src} not found in brain directory!")

if __name__ == "__main__":
    main()
