"""
    Snake Browser is licensed under GPL-3.0.
    2025 Freakybob Team.
    For information on the LICENSE, read LICENSE or IMPORTANT_LICENSE.
"""
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLineEdit, QMessageBox
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl
import sys
import re

print("Snake Browser is starting up! Have fun :) - Licensed under GPL-3.0, by Freakybob Team.")
print("""  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.""")
home = "https://freakybob.site"
response = requests.get(home)
rawhtml = response.text
def makeit(self, rawhtml, newurl):
        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.setHtml(rawhtml, baseUrl=QUrl(newurl))
        self.setCentralWidget(self.view)
def changeTitle(self, title):
    if title:
        if title == "Snake Browser, by Freakybob Team.":
            self.setWindowTitle("Snake Browser, by Freakybob Team.")
        else:
            self.setWindowTitle(f"{title} - Snake Browser, by Freakybob Team.")
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        changeTitle(self, title="FreakySearch")
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
            newurl = inputed
        try:
            response = requests.get(newurl)
        except Exception as e:
            QMessageBox.warning(self, "Error accessing URL", f"URL not found. More information: {str(e)}")
            return
        rawhtml = response.text
        match = re.search(r"<title>(.*?)</title>", rawhtml, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1).strip()
            changeTitle(self, title)
            changeTitle(self, title)
        else:
           changeTitle(self, title="Snake Browser, by Freakybob Team.")
        makeit(self, rawhtml, newurl)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec_())