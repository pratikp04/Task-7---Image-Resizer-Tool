import os
from PIL import Image

input_folder = "images"       
output_folder = "resized"     

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

new_size = (300, 300)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        resized_img = img.resize(new_size)

        new_filename = os.path.splitext(filename)[0] + ".jpg"
        save_path = os.path.join(output_folder, new_filename)
        resized_img.save(save_path, "JPEG")

        print(f"Resized and saved: {save_path}")

print(" All images resized successfully!")
