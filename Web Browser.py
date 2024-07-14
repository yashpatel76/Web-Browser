import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

#MainClass
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar) 

        #backward button
        back_button = QAction('🠈', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        #Forward button
        forward_button = QAction('🠊', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        #Reload button
        reload_button = QAction('⟳', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        #Home button
        home_button = QAction('⌂', self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        #Searchbar 
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_URL)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url) 

    def navigate_home(self):
         self.browser.setUrl(QUrl('http://google.com'))
    
    def navigate_to_URL(self):
        url = self.url_bar.text()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://www.google.com/search?q=' + url.replace(' ', '+')
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText('')

#TheExecutioncode
app = QApplication(sys.argv)
QApplication.setApplicationName('Google Browser')
window = MainWindow()
app.exec_()