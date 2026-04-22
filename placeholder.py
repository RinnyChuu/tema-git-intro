import os
from PIL import Image, ImageDraw

def genereaza_imagini_test():
    
    categorii = {
        "height": [("scund.png", "bisque"), ("inalt.png", "tan")],
        "clothes": [("tricou_rosu.png", "red"), ("tricou_albastru.png", "blue")],
        "eyes": [("ochi_verzi.png", "green"), ("ochi_negri.png", "black")],
        "hair": [("par_maro.png", "brown"), ("par_galben.png", "yellow")]
    }

    if not os.path.exists("assets"):
        os.makedirs("assets")

    for folder, fisiere in categorii.items():
        cale_folder = os.path.join("assets", folder)
        os.makedirs(cale_folder, exist_ok=True)

        for nume_fisier, culoare in fisiere:
            # Cream o imagine transparenta
            img = Image.new("RGBA", (200, 400), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)

            
            if folder == "height":
                draw.rectangle([50, 100, 150, 350], fill=culoare) # Corpul
            elif folder == "clothes":
                draw.rectangle([50, 180, 150, 280], fill=culoare) # Haina
            elif folder == "eyes":
                draw.ellipse([75, 130, 90, 145], fill=culoare)   # Ochi stang
                draw.ellipse([110, 130, 125, 145], fill=culoare) # Ochi drept
            elif folder == "hair":
                draw.rectangle([50, 90, 150, 130], fill=culoare)  # Parul

            img.save(os.path.join(cale_folder, nume_fisier))
            print(f"Generat: {folder}/{nume_fisier}")

if __name__ == "__main__":
    genereaza_imagini_test()