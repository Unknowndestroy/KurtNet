import os
import sys

def add_to_path(directory):
    if directory not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + directory

def add_python_and_pip_to_path():
    python_dir = os.path.dirname(sys.executable)
    scripts_dir = os.path.join(python_dir, 'Scripts')
    
    paths_to_add = [python_dir, scripts_dir]
    
    # PATH'e Python ve Scripts dizinlerini ekle
    for path in paths_to_add:
        add_to_path(path)
    
    # PATH'i güncellemek için os.system komutunu kullan
    os.system('setx PATH "{}"'.format(os.environ["PATH"]))

if __name__ == "__main__":
    add_python_and_pip_to_path()
    print("Python ve Pip PATH'e eklendi.")
