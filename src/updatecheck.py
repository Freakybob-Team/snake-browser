import urllib.request
import sys
from PyQt6.QtWidgets import QMessageBox
import webbrowser
# after settings we maybe do this
# to like check for updates and maybe even update itself? idk
# amazing update checker
def check(version, self):
    print("Snake is checking for updates...")
    try:
        response = urllib.request.urlopen('https://freakybob-team.github.io/snake-browser/update/version.txt')
        content = response.read().decode().strip()
    except Exception as e:
        print(f"Whoa! The update server could not be reached, try again later {e}")
        return
    if content > version:
        print(content)
        QMessageBox.warning(self, "Update recommended", "An update was found. I'll launch the download page in your default browser now. Snake will still work, but this message will show at startup unless you update.")
        webbrowser.open("https://github.com/Freakybob-Team/snake-browser/releases/latest")
    else:
        print("You are already up-to-date")