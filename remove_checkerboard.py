import os
from PIL import Image

def is_checkerboard_color(r, g, b, tolerance=15):
    # 1. White square check
    if r > 240 and g > 240 and b > 240:
        return True
    # 2. Light grey square check (usually around 180-220, low saturation)
    if 170 <= r <= 225 and 170 <= g <= 225 and 170 <= b <= 225:
        if abs(r - g) < tolerance and abs(g - b) < tolerance and abs(r - b) < tolerance:
            return True
    return False

def remove_checkerboard(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    pixels = img.load()
    
    # Mask: 0 = unvisited, 1 = background (transparent), 2 = foreground
    mask = [[0 for _ in range(h)] for _ in range(w)]
    stack = []
    
    # Add corners and borders
    corners = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
    for x, y in corners:
        r, g, b, a = pixels[x, y]
        if is_checkerboard_color(r, g, b):
            stack.append((x, y))
            mask[x][y] = 1
            
    # Add borders
    for x in range(w):
        for y in [0, h - 1]:
            if mask[x][y] == 0:
                r, g, b, a = pixels[x, y]
                if is_checkerboard_color(r, g, b):
                    stack.append((x, y))
                    mask[x][y] = 1
    for y in range(h):
        for x in [0, w - 1]:
            if mask[x][y] == 0:
                r, g, b, a = pixels[x, y]
                if is_checkerboard_color(r, g, b):
                    stack.append((x, y))
                    mask[x][y] = 1
                    
    # Flood fill
    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny < h:
                if mask[nx][ny] == 0:
                    nr, ng, nb, na = pixels[nx, ny]
                    if is_checkerboard_color(nr, ng, nb):
                        mask[nx][ny] = 1
                        stack.append((nx, ny))
                        
    # Save image with transparent background
    datas = img.getdata()
    newData = []
    i = 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = datas[i]
            if mask[x][y] == 1:
                newData.append((0, 0, 0, 0))
            else:
                newData.append((r, g, b, a))
            i += 1
            
    img.putdata(newData)
    img.save(out_path, "PNG")
    print(f"Checkerboard removed successfully. Saved to: {out_path}")

def main():
    img_path = "public/media/guy_tech_jacket.png"
    remove_checkerboard(img_path, img_path)

if __name__ == "__main__":
    main()
