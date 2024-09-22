import os
import sys
import urllib.request
import subprocess
import ctypes

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

def download_and_install_nmap():
    # Nmap'in en son sürümünü indir
    nmap_url = "https://nmap.org/dist/nmap-7.95-setup.exe"
    download_path = "nmap-7.95-setup.exe"
    
    print("Nmap'i indiriyorum...")
    try:
        urllib.request.urlretrieve(nmap_url, download_path)
    except Exception as e:
        print(f"İndirme hatası: {e}")
        sys.exit(1)
    
    # Nmap'i kur
    print("Nmap'i kuruyorum...")
    try:
        run_as_admin([download_path, '/S'])  # /S ile sessiz kurulum
    except Exception as e:
        print(f"Kurulum hatası: {e}")
        sys.exit(1)
    
    # İndirilen dosyayı sil
    os.remove(download_path)

def download_and_install_npcap():
    # NPCAP'in en son sürümünü indir
    npcap_url = "https://npcap.com/dist/npcap-1.79.exe"
    download_path = "npcap-1.79.exe"
    
    print("NPCAP'i indiriyorum...")
    try:
        urllib.request.urlretrieve(npcap_url, download_path)
    except Exception as e:
        print(f"İndirme hatası: {e}")
        sys.exit(1)
    
    # NPCAP'i kur
    print("NPCAP'i kuruyorum...")
    try:
        run_as_admin([download_path, '/S'])  # /S ile sessiz kurulum
    except Exception as e:
        print(f"Kurulum hatası: {e}")
        sys.exit(1)
    
    # İndirilen dosyayı sil
    os.remove(download_path)

def download_and_install_git():
    # Git'in en son sürümünü indir
    git_url = "https://github.com/git-for-windows/git/releases/download/v2.40.0.windows.1/Git-2.40.0-64-bit.exe"  # Güncel URL'yi buraya ekleyin
    download_path = "git-setup.exe"
    
    print("Git'i indiriyorum...")
    try:
        urllib.request.urlretrieve(git_url, download_path)
    except Exception as e:
        print(f"İndirme hatası: {e}")
        sys.exit(1)
    
    # Git'i kur
    print("Git'i kuruyorum...")
    try:
        run_as_admin([download_path, '/VERYSILENT', '/NORESTART'])  # /VERYSILENT ile sessiz kurulum
    except Exception as e:
        print(f"Kurulum hatası: {e}")
        sys.exit(1)
    
    # İndirilen dosyayı sil
    os.remove(download_path)

def run_as_admin(cmd):
    # Yükseltilmiş yetkilerle bir komut çalıştır
    if ctypes.windll.shell32.IsUserAnAdmin():
        subprocess.run(cmd, check=True)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(cmd), None, 1)

def add_paths_to_system():
    # Python dizinlerini ekle
    print("Python ve Pip PATH'e ekleniyor...")
    add_python_and_pip_to_path()
    
    # Nmap dizinini indir ve kur
    print("Nmap yükleniyor...")
    download_and_install_nmap()
    
    # NPCAP'i indir ve kur
    print("NPCAP yükleniyor...")
    download_and_install_npcap()

    # Git'i indir ve kur
    print("Git yükleniyor...")
    download_and_install_git()

    # PATH'i güncellemek için os.system komutunu kullan
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
    print("Python ve Pip dizinleri PATH'e ekleniyor...")
    add_paths_to_system()
    print("Yeniden PATH dizinleri temizleniyor...")
    clear_redundant_paths()
    print("Python, Pip, Nmap, NPCAP ve Git PATH'e eklendi ve tekrar eden dizinler temizlendi.")
