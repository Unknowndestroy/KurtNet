import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox,
    QMenuBar, QAction, QFileDialog, QTabWidget, QLineEdit, QHBoxLayout, QInputDialog
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import requests

class WebTab(QWidget):
    def __init__(self, search_engines):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)


        self.search_engine_selector = QComboBox()
        for name, url in search_engines:
            self.search_engine_selector.addItem(name, url)
        self.search_engine_selector.currentIndexChanged.connect(self.update_search_engine)

        self.web_view = QWebEngineView()
        self.layout.addWidget(self.search_engine_selector)
        self.layout.addWidget(self.web_view)


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


        self.setWindowTitle('Güvenli Tarayıcı')
        self.setGeometry(100, 100, 1024, 768)


        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)


        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)


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

      
        self.search_button = QPushButton('Arama Yap')
        self.search_button.clicked.connect(self.perform_search)
        self.layout.addWidget(self.search_button)

     
        self.menu_bar = self.menuBar()
        file_menu = self.menu_bar.addMenu('Ayarlar')

   
        open_file_action = QAction('Ayarları Aç', self)
        open_file_action.triggered.connect(self.open_settings_dialog)
        file_menu.addAction(open_file_action)

    
        self.add_new_tab_action = QAction('Yeni Sekme', self)
        self.add_new_tab_action.triggered.connect(self.add_new_tab)
        self.menu_bar.addAction(self.add_new_tab_action)

    


 
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
        error_data = {
            'timestamp': '2024-09-18T12:34:56',
            'browserVersion': 'PyQt5 Secure Browser',
            'errors': 'Örnek hata mesajı'  
        }
        api_url = 'http://localhost:5000/receive-error-report'  
        try:
            response = requests.post(api_url, json=error_data)
            if response.status_code == 200:
                print('Hata verileri başarıyla gönderildi.')
            else:
                print('Hata raporu gönderilemedi:', response.status_code)
        except Exception as e:
            print('Bağlantı hatası:', e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = SecureBrowser()
    browser.show()
    sys.exit(app.exec_())
