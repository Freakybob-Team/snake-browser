import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLineEdit, QMessageBox
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl
import sys

print("Snake Browser is starting up! Have fun :) - Licensed under GPL-3.0, by Freakybob Team.")
home = "https://freakybob.site"
response = requests.get(home)
rawhtml = response.text
def makeit(self, rawhtml, newurl):
        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.setHtml(rawhtml, baseUrl=QUrl(newurl))
        self.setCentralWidget(self.view)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Snake Browser - By Freakybob Team")
        makeit(self, rawhtml, newurl=home)
        reload_action = QAction("Reload", self)
        reload_action.triggered.connect(self.reload_page)
        back_action = QAction("Back", self)
        back_action.triggered.connect(self.back)
        forward_action = QAction("Forward", self)
        forward_action.triggered.connect(self.forward)
        home_action = QAction("Home", self)
        home_action.triggered.connect(self.home)
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        toolbar = self.addToolBar("TBar")
        toolbar.addWidget(self.urlbar)
        toolbar.addAction(reload_action)
        toolbar.addAction(back_action)
        toolbar.addAction(forward_action)
        toolbar.addAction(home_action)
        #view = QtWebEngineWidgets.QWebEngineView()
        #view.setHtml(rawhtml, baseUrl=QUrl("https://freakybob.site/"))
        #self.setCentralWidget(view)

    def reload_page(self):
        self.view.reload()
    def back(self):
        self.view.back()
    def forward(self):
        self.view.forward()
    def home(self):
        response = requests.get(home)
        rawhtml = response.text
        makeit(self, rawhtml, home)
    def navigate_to_url(self):
        inputed = self.urlbar.text()
        if not inputed.startswith("http"):
            newurl = "https://" + self.urlbar.text()
        else:
            newurl = self.urlbar.text()
        try:
            response = requests.get(newurl)
        except Exception as e:
            QMessageBox.warning(self, "Error accessing URL", f"URL not found. More information: {str(e)}")
            return
        rawhtml = response.text
        makeit(self, rawhtml, newurl)
        print(rawhtml)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec_())