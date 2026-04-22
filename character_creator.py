import os
import random
from PIL import Image

def create_random_character():
    
    assets_path = "assets"
    layers = ["height", "clothes", "eyes", "hair"] 
    
    selected_parts = {}

    
    for layer in layers:
        folder_path = os.path.join(assets_path, layer)
        
        if not os.path.exists(folder_path):
            print(f"Eroare: Folderul {folder_path} nu există!")
            return

        files = [f for f in os.listdir(folder_path) if f.endswith(".png")]
        if not files:
            print(f"Eroare: Nu sunt imagini PNG în {folder_path}!")
            return

        selected_parts[layer] = os.path.join(folder_path, random.choice(files))

    
    base_img = None

    for layer in layers:
        img_path = selected_parts[layer]
        current_img = Image.open(img_path).convert("RGBA")

        if base_img is None:
            # Prima imagine (modelul de înălțime/corp) devine baza
            base_img = current_img
        else:
            # Suprapunem următoarea trăsătură peste bază
            base_img.alpha_composite(current_img)

    
    output_name = f"character_{random.randint(1000, 9999)}.png"
    base_img.save(output_name)
    print(f" Personaj creat cu succes: {output_name}")
    print(f"Piese folosite: {selected_parts}")

if __name__ == "__main__":
    create_random_character()