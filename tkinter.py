import os
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class CharacterCreatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Generator de Personaje AI")
        self.root.geometry("400x600")

        self.assets_path = "assets"
        self.layers = ["height", "clothes", "eyes", "hair"]

        # Titlu
        self.label_titlu = tk.Label(root, text="Apasă butonul pentru un personaj nou", font=("Arial", 12))
        self.label_titlu.pack(pady=10)

        # Zona de afișare imagine
        self.canvas = tk.Canvas(root, width=200, height=400, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.pack(pady=20)

        # Buton Generare
        self.btn_generate = tk.Button(root, text="Generează Personaj", command=self.generate, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=20, pady=10)
        self.btn_generate.pack(pady=20)

        self.current_tk_image = None # Păstrăm referința imaginii pentru a nu fi ștearsă de garbage collector

    def generate(self):
        try:
            # 1. Alegerea pieselor
            selected_paths = []
            for layer in self.layers:
                folder = os.path.join(self.assets_path, layer)
                files = [f for f in os.listdir(folder) if f.endswith(".png")]
                selected_paths.append(os.path.join(folder, random.choice(files)))

            # 2. Compunerea imaginii
            combined_img = Image.new("RGBA", (200, 400), (255, 255, 255, 0))
            for path in selected_paths:
                layer_img = Image.open(path).convert("RGBA")
                combined_img.alpha_composite(layer_img)

            # 3. Afișarea în interfață
            self.current_tk_image = ImageTk.PhotoImage(combined_img)
            self.canvas.delete("all")
            self.canvas.create_image(100, 200, image=self.current_tk_image)
            
            print("Personaj generat cu succes!")

        except FileNotFoundError:
            messagebox.showerror("Eroare", "Asigură-te că folderul 'assets' există și conține imagini!")
        except Exception as e:
            messagebox.showerror("Eroare", f"A apărut o problemă: {e}")

if __name__ == "__main__":
    # Verificăm dacă există assets înainte de a porni
    if not os.path.exists("assets"):
        print("Rulează mai întâi scriptul de generare imagini de test!")
    else:
        root = tk.Tk()
        app = CharacterCreatorGUI(root)
        root.mainloop()