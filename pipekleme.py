import os
import subprocess
import sys

def add_to_path(directory):
    if directory not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + directory

def add_python_and_pip_to_path():
    python_dir = os.path.dirname(sys.executable)
    scripts_dir = os.path.join(python_dir, 'Scripts')

    # PATH'e Python ve Scripts dizinlerini ekle
    add_to_path(python_dir)
    add_to_path(scripts_dir)

    # PATH'i güncellemek için os.system komutunu kullan
    # `setx` komutunu kullanarak PATH'i güncelleyin
    new_path = os.environ["PATH"]
    os.system(f'setx PATH "{new_path}"')

def clear_redundant_paths():
    # PATH değişkenini al
    path = os.environ["PATH"]
    # PATH'teki tekrar eden dizinleri kaldır
    path_list = list(dict.fromkeys(path.split(os.pathsep)))
    # Yeni PATH değeri oluştur
    new_path = os.pathsep.join(path_list)
    os.system(f'setx PATH "{new_path}"')

if __name__ == "__main__":
    add_python_and_pip_to_path()
    clear_redundant_paths()
    print("Python ve Pip PATH'e eklendi ve tekrar eden dizinler temizlendi.")
