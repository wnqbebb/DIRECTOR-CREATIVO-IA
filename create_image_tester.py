import os

images_dir = "public/media/bonus_5"
images = sorted([f for f in os.listdir(images_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))], key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualizador de Imágenes de Bonus 5</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #ffffff;
            margin: 20px;
        }
        h1 {
            border-bottom: 2px solid #ff007f;
            padding-bottom: 10px;
            color: #ff007f;
        }
        h2 {
            margin-top: 40px;
            color: #ec4899;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
        }
        .card {
            background-color: #1e1e1e;
            border: 2px solid #333;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
        }
        .card img {
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            aspect-ratio: 1;
            object-fit: cover;
        }
        .filename {
            margin-top: 10px;
            font-family: monospace;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <h1>Visualizador de Imágenes de Bonus 5</h1>
    
    <h2>Model 1 References (Index 516)</h2>
    <div class="grid">
"""

# Group 1: Model 1 Refs
model1_refs = ["image1.jpg", "image40.jpg", "image3.jpg", "image2.jpg"]
for img in model1_refs:
    html_content += f"""
        <div class="card">
            <img src="/media/bonus_5/{img}" alt="{img}">
            <div class="filename">{img}</div>
        </div>
    """

html_content += """
    </div>
    
    <h2>Campaña 1 Results (Index 907)</h2>
    <div class="grid">
"""

# Group 2: Campaña 1 Results
camp1_imgs = ["image46.jpg", "image29.jpg", "image22.jpg", "image36.jpg", "image20.jpg", "image35.jpg", "image38.jpg", "image34.jpg", "image19.jpg", "image45.jpg"]
for img in camp1_imgs:
    html_content += f"""
        <div class="card">
            <img src="/media/bonus_5/{img}" alt="{img}">
            <div class="filename">{img}</div>
        </div>
    """

html_content += """
    </div>
    
    <h2>Campaña 2 Results (Index 1381)</h2>
    <div class="grid">
"""

# Group 3: Campaña 2 Results
camp2_imgs = ["image15.jpg", "image12.jpg", "image30.jpg", "image33.jpg", "image8.jpg", "image10.jpg", "image37.jpg", "image21.jpg"]
for img in camp2_imgs:
    html_content += f"""
        <div class="card">
            <img src="/media/bonus_5/{img}" alt="{img}">
            <div class="filename">{img}</div>
        </div>
    """

html_content += """
    </div>
    
    <h2>Model 2 References (Index 1850)</h2>
    <div class="grid">
"""

# Group 4: Model 2 Refs
model2_refs = ["image23.png", "image18.jpg", "image17.jpg", "image26.jpg"]
for img in model2_refs:
    html_content += f"""
        <div class="card">
            <img src="/media/bonus_5/{img}" alt="{img}">
            <div class="filename">{img}</div>
        </div>
    """

html_content += """
    </div>
    
    <h2>Campaña 3 Results (Index 2217)</h2>
    <div class="grid">
"""

# Group 5: Campaña 3 Results
camp3_imgs = ["image9.jpg", "image39.jpg", "image32.jpg", "image44.jpg", "image28.jpg", "image14.jpg", "image13.jpg", "image5.jpg", "image4.jpg", "image43.jpg", "image11.jpg", "image16.jpg", "image31.jpg", "image24.jpg", "image25.jpg", "image41.jpg", "image27.jpg", "image6.jpg", "image42.jpg", "image7.jpg"]
for img in camp3_imgs:
    html_content += f"""
        <div class="card">
            <img src="/media/bonus_5/{img}" alt="{img}">
            <div class="filename">{img}</div>
        </div>
    """

html_content += """
    </div>
</body>
</html>
"""

with open("test_images.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("test_images.html written successfully.")
