import os
import subprocess
import urllib.request
import zipfile

# GitHub deposu
github_url = 'httpsgithub.comUnknowndestroyKurtNetKaynakKodv2'
zip_url = 'httpsgithub.comUnknowndestroyKurtNetKaynakKodv2archiverefsheadsmain.zip'
extract_dir = 'KurtNetKaynakKodv2'

# Projeyi indirme fonksiyonu
def download_project()
    # Eğer git yüklü değilse zip dosyasını indirip açalım
    try
        # `git clone` komutunu çalıştır
        print(Proje git ile indiriliyor...)
        subprocess.run(['git', 'clone', github_url], check=True)
        print(Proje başarıyla indirildi.)
    except FileNotFoundError
        # Git yoksa, zip dosyasını indir
        print(Git bulunamadı. Proje zip dosyası olarak indiriliyor...)
        zip_file = 'KurtNetKaynakKodv2.zip'
        
        # Zip dosyasını indir
        urllib.request.urlretrieve(zip_url, zip_file)
        print(f{zip_file} indirildi.)
        
        # Zip dosyasını çıkart
        with zipfile.ZipFile(zip_file, 'r') as zip_ref
            zip_ref.extractall(extract_dir)
        print(fDosyalar {extract_dir} klasörüne çıkarıldı.)
        
        # Zip dosyasını temizle
        os.remove(zip_file)

# Projeyi mevcut çalışma klasörüne ekleyin
if __name__ == '__main__'
    download_project()
    print(Proje indirildi ve klasöre eklendi.)
