import urllib.request
import sys
from PyQt6.QtWidgets import QMessageBox
import webbrowser
# after settings we maybe do this
# to like check for updates and maybe even update itself? idk
# amazing update checker
def check(version):
    print("Snake is checking for updates...")
    response = urllib.request.urlopen('https://github.com/freakybob-team/snake-browser/refs/heads/main/update/version.txt?raw=true')
    content = response.read()
    
    if not content == version:
        # do popup with pyqt?
        # sure just hold on
        # make it so this always runs on start
        QMessageBox.warning("Update Notice", "Snake Browser has an update. The download page has been opened in your default web browser.")
        webbrowser.open("https://github.com/Freakybob-Team/snake-browser/releases/latest")
    else:
        print("You are on the latesti version!")