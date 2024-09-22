import os
import sys
import subprocess

def add_to_path(new_path):
    # Mevcut PATH'i al
    current_path = os.environ['PATH']

    # Yeni yolun PATH'te olup olmadığını kontrol et
    if new_path not in current_path:
        updated_path = current_path + os.pathsep + new_path
        
        # Kalıcı olarak güncelle (Windows için)
        subprocess.run(['setx', 'PATH', updated_path])
        print("PATH başarıyla güncellendi.")
    else:
        print("Dizin zaten PATH'te mevcut.")

if __name__ == "__main__":
    new_path = r'C:\YeniDizin'  # Eklemek istediğiniz dizini buraya yazın
    add_to_path(new_path)
