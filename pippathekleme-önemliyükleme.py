import os
import subprocess
import tkinter as tk
from tkinter import messagebox
import threading
import ctypes
import win32api
import win32con
import win32gui

def run_batch_file():
    # `giteklemecalistir.bat` dosyasını çalıştır
    batch_file = "giteklemecalistir.bat"
    if os.path.exists(batch_file):
        subprocess.run([batch_file], check=True)
    else:
        raise FileNotFoundError(f"{batch_file} bulunamadı.")

def run_install_commands():
    update_progress_message("Git, Pip ve Python PATH'e ekleniyor...", "black", 'center')
    
    # `giteklemecalistir.bat` dosyasını çalıştır ve 15 saniye bekle
    run_batch_file()
    root.after(15000, install_libraries)  # 15 saniye sonra kütüphaneleri yükle

def install_libraries():
    update_progress_message("Önemli kütüphaneler indiriliyor...", "black", 'center')

    commands = [
        "pip install discord_webhook",
        "pip install pycryptodome",
        "pip install requests",
        "pip install pypiwin32",
        "pip install cryptography",
        "pip install wmi",
        "pip install tk",
        "pip install packaging",
        "pip install pyinstaller",
        "pip install pynput",
        "pip install dhooks",
        "pip install discord",
        "pip install asyncio",
        "pip install mss",
        "pip install browserhistory",
        "pip install pyautogui",
        "pip install pycaw",
        "pip install pywin32",
        "pip install pywin32-ctypes",
        "pip install tls_client",
        "pip install httpx",
        "pip install fade",
        "pip install ipaddress",
        "pip install urllib3",
        "pip install certifi",
        "pip install scapy",
        "pip install sputil",
        "pip install fade~=0.0.9",
        "pip install lxml~=4.9.2",
        "pip install colorama~=0.4.5",
        "pip install fake-useragent~=1.2.1",
        "pip install aiohttp~=3.8.4",
        "pip install requests~=2.31.0",
        "pip install beautifulsoup4~=4.11.1",
        "pip install pythonping~=1.1.4",
        "pip install httpagentparser~=1.9.5",
        "pip install cloudscraper~=1.2.69",
        "pip install opentele~=1.15.1",
        "pip install ua-parser~=0.16.1",
        "pip install PyQt5",
        "pip install selenium",
        "pip install pillow",
        "pip install pytesseract",
        "pip install logging",
        "pip install tkinter",
        "pip install subproccess",
        "pip install pyperclip",
        "pip install os",
        "pip install lxml",
        "pip install beatifulsoup",
        "pip install time"
    ]

    for command in commands:
        try:
            library_name = command.split()[2]
            update_progress_message(f"İndiriliyor: {library_name}", "green", 'top_left')
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode != 0:
                update_progress_message(f"HATA: İndirilemedi: {library_name}", "red", 'top_right')
            else:
                update_progress_message("", "green", 'top_left')  # Temizle
        except subprocess.CalledProcessError:
            update_progress_message(f"HATA: İndirilemedi: {library_name}", "red", 'top_right')

    update_progress_message("Önemli kütüphaneler indiriliyor...", "black", 'center')
    messagebox.showinfo("Bilgi", "İndirme tamamlandı!")
    root.destroy()

def update_progress_message(message, color, position):
    if position == 'center':
        label = progress_label_center
    elif position == 'top_left':
        label = progress_label_left
    elif position == 'top_right':
        label = progress_label_right
    else:
        raise ValueError("Geçersiz konum değeri. 'center', 'top_left' veya 'top_right' olmalıdır.")
    
    label.config(text=message, fg=color)
    root.update_idletasks()  # GUI'yi günceller

def create_fullscreen_gui():
    global root, progress_label_left, progress_label_right, progress_label_center
    root = tk.Tk()
    root.title("Kurulum")

    # Tam ekran modu
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda e: "break")  # ESC ile tam ekran modunu kapatmayı engeller

    # GUI öğeleri
    progress_label_center = tk.Label(root, text="Git, Pip ve Python PATH'e ekleniyor...", font=("Helvetica", 16), fg="black", bg="#f0f0f0")
    progress_label_center.pack(expand=True, fill=tk.BOTH)

    progress_label_left = tk.Label(root, text="", font=("Helvetica", 16), fg="green", bg="#f0f0f0")
    progress_label_left.place(x=10, y=10)

    progress_label_right = tk.Label(root, text="", font=("Helvetica", 16), fg="red", bg="#f0f0f0")
    progress_label_right.place(x=root.winfo_screenwidth() - 250, y=10)

    # Arka plan rengini biraz şeffaf yapma
    root.configure(bg='#f0f0f0')  # Hafif gri arka plan rengi
    root.update_idletasks()

    # GUI başlatma
    root.after(1000, run_install_commands)

    # Tam ekran ve pencere kontrol engellemeleri
    disable_close_button()
    disable_key_combinations()

def disable_close_button():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    ctypes.windll.user32.SetWindowLongW(hwnd, win32con.GWL_STYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE) & ~win32con.WS_SYSMENU)

def disable_key_combinations():
    # Windows'taki bazı kısayolları engellemeye çalışır
    ctypes.windll.user32.RegisterHotKey(None, 1, win32con.MOD_ALT, win32con.VK_TAB)  # ALT+TAB
    ctypes.windll.user32.RegisterHotKey(None, 2, win32con.MOD_ALT, win32con.VK_F4)  # ALT+F4
    ctypes.windll.user32.RegisterHotKey(None, 3, win32con.MOD_CONTROL | win32con.MOD_ALT, win32con.VK_DELETE)  # CTRL+ALT+DEL

if __name__ == "__main__":
    create_fullscreen_gui()
    root.mainloop()
