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
        response = urllib.request.urlopen('https://raw.githubusercontent.com/Freakybob-Team/snake-browser/refs/heads/main/update/version.txt')
        content = response.read()
    except Exception as e:
        print(f"Whoa! The update server could not be reached, try again later {e}")
        return
    if content == "429: Too Many Requests For more on scraping GitHub and how it may affect your rights, please review our Terms of Service (https://docs.github.com/en/site-policy/github-terms/github-terms-of-service).":
        print("Your access to GitHub was blocked for some reason. Try disabling your VPN.")
    if int(content) > int(version):
        # do popup with pyqt?
        # sure just hold on
        print(content)
        # make it so this always runs on start
        # ok so theres an issue for devs
        # if update.txt is b1.0
        #ew
        # then do compare see whichone is bigger and get rid of the beta tag instead of just compairng which one 
        webbrowser.open("https://github.com/Freakybob-Team/snake-browser/releases/latest")
        print("You are already up-to-date")