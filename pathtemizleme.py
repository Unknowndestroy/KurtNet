import os

def remove_from_path(keyword):
    # Mevcut PATH'i al
    path = os.environ["PATH"]
    # PATH'teki dizinleri ayır
    path_list = path.split(os.pathsep)
    # Belirtilen anahtar kelimeyi içeren dizinleri filtrele
    new_path_list = [p for p in path_list if keyword.lower() not in p.lower()]
    # Yeni PATH değerini oluştur
    new_path = os.pathsep.join(new_path_list)
    # PATH'i güncelle
    os.environ["PATH"] = new_path
    # PATH'i kalıcı olarak güncellemek için setx komutunu kullan
    os.system(f'setx PATH "{new_path}"')

if __name__ == "__main__":
    # Python, pip ve git ile ilgili dizinleri PATH'ten çıkar
    remove_from_path("python")
    remove_from_path("pip")
    remove_from_path("git")

    print("Python, Pip ve Git PATH'ten çıkarıldı.")
