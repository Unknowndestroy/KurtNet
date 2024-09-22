import os

def list_path_directories_and_files():
    # PATH ortam değişkenini al
    path_variable = os.environ.get("PATH", "")

    # PATH değişkenindeki dizinleri ayır
    paths = path_variable.split(os.pathsep)

    for path in paths:
        if os.path.isdir(path):
            print(f"Dizin: {path}")
            try:
                # Dizindeki dosyaları ve alt dizinleri listele
                for item in os.listdir(path):
                    item_path = os.path.join(path, item)
                    if os.path.isfile(item_path):
                        print(f"    Dosya: {item}")
                    elif os.path.isdir(item_path):
                        print(f"    Alt Dizin: {item}")
            except PermissionError:
                print(f"    Erişim Reddedildi: {path}")
        else:
            print(f"Geçersiz Dizin: {path}")

if __name__ == "__main__":
    list_path_directories_and_files()
