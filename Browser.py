import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.broswer = QWebEngineView()
        self.broswer.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.broswer)
        self.showMaximized()

        # Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back',self)
        back_btn.triggered.connect(self.broswer.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forwad',self)
        forward_btn.triggered.connect(self.broswer.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Relaod',self)
        reload_btn.triggered.connect(self.broswer.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.broswer.urlChanged.connect(self.update_url)


    def navigate_home(self):
        self.broswer.setUrl(QUrl('http://google.com'))
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.broswer.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("Harsh Broswer")
window = MainWindow()
app.exec()
