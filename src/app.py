import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl
import sys

response = requests.get("https://freakybob.site")
rawhtml = response.text

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Snake Browser - By Freakybob Team")

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.setHtml(rawhtml, baseUrl=QUrl("https://freakybob.site/"))
        self.setCentralWidget(self.view)

        reload_action = QAction("Reload", self)
        reload_action.triggered.connect(self.reload_page)
        back_action = QAction("Back", self)
        back_action.triggered.connect(self.back)
        forward_action = QAction("Forward", self)
        forward_action.triggered.connect(self.forward)

        toolbar = self.addToolBar("TBar")
        toolbar.addAction(reload_action)
        toolbar.addAction(back_action)
        toolbar.addAction(forward_action)

        #view = QtWebEngineWidgets.QWebEngineView()
        #view.setHtml(rawhtml, baseUrl=QUrl("https://freakybob.site/"))
        #self.setCentralWidget(view)

    def reload_page(self):
        self.view.reload()
    def back(self):
        self.view.back()
    def forward(self):
        self.view.forward()

app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec_())