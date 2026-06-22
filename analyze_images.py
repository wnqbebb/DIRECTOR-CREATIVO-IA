import os
import struct

def get_image_info(filepath):
    if not os.path.exists(filepath):
        return None
        
    _, ext = os.path.splitext(filepath.lower())
    if ext == '.png':
        with open(filepath, 'rb') as f:
            header = f.read(24)
            if len(header) < 24:
                return None
            if header[:8] != b'\x89PNG\r\n\x1a\n':
                return None
            width, height = struct.unpack('>II', header[16:24])
            return width, height
    elif ext in ('.jpg', '.jpeg'):
        with open(filepath, 'rb') as f:
            f.read(2)
            while True:
                marker = f.read(2)
                if len(marker) < 2:
                    break
                if marker[0] != 0xFF:
                    break
                mtype = marker[1]
                if mtype in (0xC0, 0xC1, 0xC2, 0xC3):
                    f.read(3)
                    height, width = struct.unpack('>HH', f.read(4))
                    return width, height
                else:
                    len_bytes = f.read(2)
                    if len(len_bytes) < 2:
                        break
                    length = struct.unpack('>H', len_bytes)[0]
                    f.read(length - 2)
    return None

def analyze_all_images():
    image_dir = r"C:\Users\Admin\Documents\PRODUCTO DIGITAL\public\media\bonus_4"
    print("Analyzing all 24 images...")
    for i in range(1, 25):
        for ext in ('.png', '.jpg'):
            filename = f"image{i}{ext}"
            filepath = os.path.join(image_dir, filename)
            if os.path.exists(filepath):
                info = get_image_info(filepath)
                if info:
                    width, height = info
                    aspect_ratio = width / height
                    print(f"File: {filename} -> Size: {width}x{height} (Aspect: {aspect_ratio:.2f})")
                break

if __name__ == "__main__":
    analyze_all_images()
