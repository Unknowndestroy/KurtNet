import random
import os

def generate_proxy():
    ip_parts = [str(random.randint(0, 255)) for _ in range(4)]
    ip_address = '.'.join(ip_parts)
    port = random.randint(1024, 65535)
    return f'http://{ip_address}:{port}'

def save_proxy(proxy):
    folder = 'proxies'
    file_path = os.path.join(folder, 'proxies.txt')
    
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    with open(file_path, 'a') as file:
        file.write(proxy + '\n')

def create_and_delete_folders():
    for i in range(1, 21):
        folder_name = f'folder_{i}'
        # Klasörü oluştur
        os.makedirs(folder_name, exist_ok=True)
        # Klasörü sil
        os.rmdir(folder_name)

# Proxy oluştur ve kaydet
for _ in range(5000):
    proxy = generate_proxy()
    save_proxy(proxy)

# Klasör oluştur ve sil
create_and_delete_folders()
