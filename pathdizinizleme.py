import tkinter as tk
from tkinter import ttk
import os

class PathViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PATH Dizin Görüntüleyici")
        self.root.geometry("600x400")  # Pencere boyutu

        # Kaydırılabilir çerçeve oluştur
        self.canvas = tk.Canvas(root)
        self.scroll_y = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        # Scrollable frame yapılandırması
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scroll_y.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.config(yscrollcommand=self.scroll_y.set)

        # PATH dizinlerini listele
        self.list_path_directories()

        # PATH sınırı
        self.limit_label = tk.Label(root, text=f"Cihazınızın PATH Sınırı: {self.get_path_limit()}", font=("Helvetica", 12))
        self.limit_label.pack(side="bottom", pady=10)

    def list_path_directories(self):
        # PATH ortam değişkenini al
        path_variable = os.environ.get("PATH", "")
        paths = path_variable.split(os.pathsep)

        # Dizinleri listele
        for path in paths:
            if os.path.isdir(path):
                tk.Label(self.scrollable_frame, text=path, font=("Helvetica", 12)).pack(anchor="w")

    def get_path_limit(self):
        # PATH sınırını belirle (Windows'ta genellikle 2048 karakter)
        return "2048 karakter"

if __name__ == "__main__":
    root = tk.Tk()
    app = PathViewerApp(root)
    root.mainloop()
