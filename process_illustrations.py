import os
from PIL import Image, ImageDraw

def flood_fill_background(img_path, out_path, tolerance=25):
    # Load image and convert to RGBA
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    
    # We will perform a flood fill on a mask starting from the 4 corners
    # to identify the black background pixels.
    # Convert image to grayscale for easier thresholding
    gray = img.convert("L")
    pixels = gray.load()
    
    # Mask: 0 = unvisited, 1 = background, 2 = foreground
    mask = [[0 for _ in range(h)] for _ in range(w)]
    
    # Stack for DFS flood fill
    stack = []
    
    # Add corners to stack
    corners = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
    for x, y in corners:
        # Check if corner pixel is dark (black background)
        if pixels[x, y] < tolerance:
            stack.append((x, y))
            mask[x][y] = 1 # Mark as background
            
    # Also add elements from the outer boundary lines
    for x in range(w):
        for y in [0, h - 1]:
            if mask[x][y] == 0 and pixels[x, y] < tolerance:
                stack.append((x, y))
                mask[x][y] = 1
    for y in range(h):
        for x in [0, w - 1]:
            if mask[x][y] == 0 and pixels[x, y] < tolerance:
                stack.append((x, y))
                mask[x][y] = 1
                
    # DFS to find all connected background pixels
    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny < h:
                if mask[nx][ny] == 0:
                    # If neighbor is also dark, it's background
                    if pixels[nx, ny] < tolerance:
                        mask[nx][ny] = 1
                        stack.append((nx, ny))
                        
    # Create final transparent image
    datas = img.getdata()
    newData = []
    i = 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = datas[i]
            if mask[x][y] == 1:
                # Background -> Transparent
                newData.append((0, 0, 0, 0))
            else:
                # Foreground -> Keep original color
                newData.append((r, g, b, a))
            i += 1
            
    img.putdata(newData)
    img.save(out_path, "PNG")
    print(f"Saved processed transparent illustration: {out_path}")

def crop_eye(img_path, out_path):
    # The eye has a black border. We will find the bounding box of the inner cream rectangle.
    # We can detect it by thresholding for bright pixels (the cream paper).
    img = Image.open(img_path).convert("RGBA")
    gray = img.convert("L")
    
    # Cream is bright, let's find pixels with brightness > 80
    temp = gray.point(lambda p: 255 if p > 80 else 0)
    bbox = temp.getbbox()
    if bbox:
        # Pad bbox slightly to make sure we don't clip the illustration text or edges
        x0, y0, x1, y1 = bbox
        # Crop
        cropped = img.crop((x0, y0, x1, y1))
        cropped.save(out_path, "PNG")
        print(f"Saved cropped eye illustration: {out_path}")
    else:
        img.save(out_path, "PNG")
        print(f"Bbox failed for eye. Saved original: {out_path}")

def main():
    brain_dir = "C:/Users/Admin/.gemini/antigravity-ide/brain/68aca044-0357-4016-8ded-47a78f44aa27"
    media_dir = "public/media"
    os.makedirs(media_dir, exist_ok=True)
    
    # Source paths
    eye_src = os.path.join(brain_dir, "media__1782000915858.png")
    girl_src = os.path.join(brain_dir, "media__1782000930429.png")
    guy_sun_src = os.path.join(brain_dir, "media__1782000938195.png")
    guy_back_src = os.path.join(brain_dir, "media__1782000944349.png")
    
    # Destination paths
    eye_out = os.path.join(media_dir, "illustration_eye.png")
    girl_out = os.path.join(media_dir, "illustration_girl.png")
    guy_sun_out = os.path.join(media_dir, "illustration_guy_sunglasses.png")
    guy_back_out = os.path.join(media_dir, "illustration_guy_backpack.png")
    
    # Copy & Process
    crop_eye(eye_src, eye_out)
    flood_fill_background(girl_src, girl_out, tolerance=35)
    flood_fill_background(guy_sun_src, guy_sun_out, tolerance=35)
    flood_fill_background(guy_back_src, guy_back_out, tolerance=60)
    
    print("All illustrations successfully processed!")

if __name__ == "__main__":
    main()
