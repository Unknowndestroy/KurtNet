import sys
import random
import os
import zipfile
import urllib.request
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox,
    QMenuBar, QAction, QFileDialog, QTabWidget, QInputDialog
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

# Geckodriver indirme URL'si ve varsayılan konum
geckodriver_url = 'https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-win32.zip'
geckodriver_zip_path = 'geckodriver.zip'
geckodriver_extract_path = 'geckodriver'

# Proxy'leri dosyadan okuma fonksiyonu
def load_proxies(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            proxies = f.readlines()
            proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
            return proxies
    else:
        print(f"Proxy dosyası bulunamadı: {file_path}")
        return []

# Random bir proxy seç
def get_random_proxy(proxies):
    if proxies:
        return random.choice(proxies)
    else:
        print("Proxy listesi boş!")
        return None

# Firefox ayarlarını proxy ile yapılandırma
def setup_firefox_with_proxy(proxy):
    firefox_profile = FirefoxProfile()

    if ':' in proxy:
        proxy_host, proxy_port = proxy.split(':')
        try:
            proxy_port = int(proxy_port)  # Proxy portunu tam sayıya dönüştür
        except ValueError:
            print(f"Geçersiz port numarası: {proxy_port}")
            return None
    else:
        print(f"Geçersiz proxy formatı: {proxy}")
        return None

    # Proxy ayarları (HTTP ve HTTPS için aynı proxy'yi kullan)
    firefox_profile.set_preference('network.proxy.type', 1)
    firefox_profile.set_preference('network.proxy.http', proxy_host)
    firefox_profile.set_preference('network.proxy.http_port', proxy_port)
    firefox_profile.set_preference('network.proxy.ssl', proxy_host)
    firefox_profile.set_preference('network.proxy.ssl_port', proxy_port)
    firefox_profile.set_preference('network.proxy.share_proxy_settings', True)
    
    return firefox_profile

# Geckodriver'ı indirme fonksiyonu
def download_geckodriver():
    if not os.path.exists(geckodriver_extract_path):
        print("Geckodriver indiriliyor...")
        urllib.request.urlretrieve(geckodriver_url, geckodriver_zip_path)
        
        # Zip dosyasını çıkart
        with zipfile.ZipFile(geckodriver_zip_path, 'r') as zip_ref:
            zip_ref.extractall(geckodriver_extract_path)
        print("Geckodriver indirildi ve çıkarıldı.")
    else:
        print("Geckodriver zaten mevcut.")

# VPN'e bağlanma fonksiyonu
def connect_vpn():
    proxies_file = 'proxies/proxies.txt'
    proxies = load_proxies(proxies_file)

    proxy = get_random_proxy(proxies)
    if proxy:
        firefox_profile = setup_firefox_with_proxy(proxy)
        
        if firefox_profile is not None:
            options = Options()
            gecko_path = os.path.join(geckodriver_extract_path, 'geckodriver.exe')
            service = Service(gecko_path)

            # Firefox'u başlat
            driver = webdriver.Firefox(service=service, options=options, firefox_profile=firefox_profile)
            driver.get("https://www.whatismyip.com")  # IP kontrolü için
            driver.implicitly_wait(10)
            print(f"Bağlanılan proxy: {proxy}")
        else:
            print("Proxy ayarları yapılandırılamadı.")
    else:
        print("Geçerli bir proxy bulunamadı.")

class WebTab(QWidget):
    def __init__(self, search_engines):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Arama motoru seçici ve web tarayıcı
        self.search_engine_selector = QComboBox()
        for name, url in search_engines:
            self.search_engine_selector.addItem(name, url)
        self.search_engine_selector.currentIndexChanged.connect(self.update_search_engine)

        self.web_view = QWebEngineView()
        self.layout.addWidget(self.search_engine_selector)
        self.layout.addWidget(self.web_view)

        # Varsayılan arama motorunu yükle
        self.update_search_engine()

    def update_search_engine(self):
        current_url = self.search_engine_selector.currentData()
        if current_url:
            self.web_view.setUrl(QUrl(current_url))

    def search(self, query):
        search_query = self.search_engine_selector.currentData() + "/search?q=" + query
        self.web_view.setUrl(QUrl(search_query))

    def load_url(self, url):
        self.web_view.setUrl(QUrl(url))

class SecureBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Pencere başlığı ve boyutu
        self.setWindowTitle('Güvenli Tarayıcı')
        self.setGeometry(100, 100, 1024, 768)

        # Ana widget ve düzen
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Sekme widget'ı
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        # Arama motorları
        self.search_engines = [
            ("DuckDuckGo", "https://duckduckgo.com"),
            ("Google", "https://www.google.com"),
            ("Bing", "https://www.bing.com"),
            ("Yahoo", "https://search.yahoo.com"),
            ("Startpage", "https://www.startpage.com"),
            ("Qwant", "https://www.qwant.com"),
            ("Ecosia", "https://www.ecosia.org"),
            ("Searx", "https://searx.org"),
            ("Brave Search", "https://search.brave.com"),
            ("Swisscows", "https://swisscows.com")
        ]

        self.theme_selector = QComboBox()
        self.theme_selector.addItem("Klasik", "classic")
        self.theme_selector.addItem("Karanlık", "dark")
        self.theme_selector.currentIndexChanged.connect(self.apply_theme)

        # Arama yapma butonu
        self.search_button = QPushButton('Arama Yap')
        self.search_button.clicked.connect(self.perform_search)
        self.layout.addWidget(self.search_button)

        # VPN'e bağlan butonu
        self.vpn_button = QPushButton('VPN\'e Bağlan')
        self.vpn_button.clicked.connect(connect_vpn)
        self.layout.addWidget(self.vpn_button)

        # Menü çubuğu
        self.menu_bar = self.menuBar()
        file_menu = self.menu_bar.addMenu('Ayarlar')

        # Ayarlar menüsü öğeleri
        open_file_action = QAction('Ayarları Aç', self)
        open_file_action.triggered.connect(self.open_settings_dialog)
        file_menu.addAction(open_file_action)

        # Yeni sekme açma
        self.add_new_tab_action = QAction('Yeni Sekme', self)
        self.add_new_tab_action.triggered.connect(self.add_new_tab)
        self.menu_bar.addAction(self.add_new_tab_action)

        # Hata raporlama butonu
        self.report_button = QPushButton('Hata Verilerini Gönder')
        self.report_button.clicked.connect(self.send_error_report)
        self.layout.addWidget(self.report_button)

        # Başlangıç sekmesini ekle
        self.add_new_tab()

    def add_new_tab(self):
        new_tab = WebTab(self.search_engines)
        self.tab_widget.addTab(new_tab, "Yeni Sekme")
        self.tab_widget.setCurrentWidget(new_tab)

    def perform_search(self):
        search_query, ok = QInputDialog.getText(self, 'Arama', 'Arama terimini girin:')
        if ok and search_query:
            for i in range(self.tab_widget.count()):
                tab = self.tab_widget.widget(i)
                if isinstance(tab, WebTab):
                    tab.search(search_query)

    def apply_theme(self):
        theme = self.theme_selector.currentData()
        if theme == 'dark':
            self.central_widget.setStyleSheet("background-color: #333; color: #FFF;")
        else:
            self.central_widget.setStyleSheet("background-color: #FFF; color: #000;")

    def open_settings_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Ayarlar Dosyasını Aç", "", "JSON Dosyaları (*.json);;Tüm Dosyalar (*)", options=options)
        if file_name:
            print(f"Seçilen dosya: {file_name}")

    def send_error_report(self):
        # Burada hata verilerini gönderme işlemi yapılacak
        print("Hata raporu gönderiliyor...")

# Ana fonksiyon
def main():
    app = QApplication(sys.argv)
    
    download_geckodriver()  # Geckodriver'ı indir
    browser = SecureBrowser()
    browser.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
