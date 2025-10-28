"""
    Snake Browser is licensed under GPL-3.0.
    2025 Freakybob Team.
    For information on the LICENSE, read LICENSE or IMPORTANT_LICENSE.
"""

import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from PyQt6 import QtWebEngineWidgets
from PyQt6.QtCore import QUrl, QTimer
from PyQt6.QtGui import QAction
import sys
import re
import os
from settings import SettingsWindow
from pathlib import Path
import urllib.request, urllib.parse
try:
    from updatecheck import check
except:
    print("Update Checker not found.")

downloads_path = str(Path.home() / "Downloads")
version = "1.2" # the snake browser version, when updating the snake browser, please change this - mpax235
app = QApplication(sys.argv)
gpc_use = None

if not os.path.exists("settings/"):
    os.mkdir("settings")
if os.path.exists("downloads/"):
    os.rmdir("downloads")
if not os.path.exists("settings/gpc.txt"):
    with open("settings/gpc.txt", "w") as file:
        file.write("1")
if not os.path.exists("settings/aed.txt"):
    with open("settings/aed.txt", "w") as file:
        file.write("1")
with open("settings/gpc.txt", "r") as file:
    if file.read() == "1":
        gpc_use = True
    if file.read() == "0":
        gpc_use = False

print("Snake Browser is starting up! Have fun :) - Licensed under GPL-3.0, by Freakybob Team. (if you are reading this i managed to sneak this in hahaha)")
print("""  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.""")

home = "https://search.freakybob.site"
response = requests.get(home, headers={"Sec-GPC": "1", "User-Agent": f"SnakeBrowser/{version}"})
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
        try:
            check(version, self)
        except:
            print("Update Check not loaded, so Check was not run.")
        reload_action = QAction("Reload", self)
        reload_action.triggered.connect(self.reload_page)
        back_action = QAction("Back", self)
        back_action.triggered.connect(self.back)
        forward_action = QAction("Forward", self)
        forward_action.triggered.connect(self.forward)
        home_action = QAction("Home", self)
        home_action.triggered.connect(self.home)
        settings_action = QAction("Settings", self)
        settings_action.triggered.connect(self.settings)
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        toolbar = self.addToolBar("TBar")
        toolbar.addWidget(self.urlbar)
        toolbar.addAction(reload_action)
        toolbar.addAction(back_action)
        toolbar.addAction(forward_action)
        toolbar.addAction(home_action)
        toolbar.addAction(settings_action)
        try:
            with open('qss/amoled.qss', 'r') as f:
                style = f.read()
                app.setStyleSheet(style)
        except:
            print("QSS file not found. Styling will not be on.")
        timer = QTimer()
        timer.timeout.connect(self.checkforqss)
        timer.start(5)

    def reload_page(self):
        self.view.reload()

    def back(self):
        self.view.back()

    def forward(self):
        self.view.forward()

    def settings(self):
        settingswindow = SettingsWindow(self)
        settingswindow.exec()
        # jesus christ you type fast okay should be fixed works but the css is REALLY ugly

    def home(self):
        if gpc_use == True:
            response = requests.get(home, headers={"Sec-GPC": "1", "User-Agent": "SnakeBrowser/b1.1"})
        else:
            response = requests.get(home)
        rawhtml = response.text
        makeit(self, rawhtml, home)

    def checkforqss():
        if os.path.exists("COHQSS.txt"):
            print("File found")
            with open("COHQSS.txt", "r") as file:
                cqss = file.read()
                app.setStyleSheet(cqss)
                print("Stylesheet set!")
                file.close()

    def navigate_to_url(self):
        with open("settings/aed.txt", "r") as file:
            aedsetting = file.read()
        file_extensions = [".mp3", ".png", ".jpg", ".jpeg", ".zip", ".exe", ".dmg", ".mp4"]
        executable_extensions = [".exe", ".zip", ".dmg"]
        inputed = self.urlbar.text()
        path = urllib.parse.urlsplit(inputed).path
        extension = os.path.splitext(path)[-1] 
        filename = os.path.basename(path)
        if extension in file_extensions:
            if aedsetting == "0" and extension in executable_extensions:
                QMessageBox.warning(self, "Failed to download!", f"You attempted to download a file that is a .exe, .zip, or .dmg, and you have your Allow Executable Downloads off. To download this, turn it on.")
                return
            print("Downloading!")
            urllib.request.urlretrieve(inputed, str(downloads_path) + "/" + filename)
            QMessageBox.warning(self, "Downloaded!", f"A file was downloaded to your downloads folder. You can access it in your downloads folder. If you don't recognize it, please delete it!")
            return
        if not inputed.startswith("http"):
            newurl = "https://" + self.urlbar.text()
        else:
            newurl = inputed
        try:
            if gpc_use == True:
                response = requests.get(newurl, headers={"Sec-GPC": "1", "User-Agent": f"SnakeBrowser/{version}"})
            else:
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

window = MainWindow()
window.show()
sys.exit(app.exec())