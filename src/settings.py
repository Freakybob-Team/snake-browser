from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QMessageBox, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt
import sys
try:
    import accentcolordetect # this module only supports windows & mac according to the github ig? good thing you dont need it to run
except: 
    print("Accentcolordetect wasn't installed. Settings buttons won't use your system accent color.")
# uhhh idk how to launch ts in the app itself
# centered buttons would also be nice
# not aligned
try:
    accentsource = accentcolordetect.accent()
    hex_color = accentsource.split(",")[-1].strip()
    hex_color = hex_color.strip(" )'\"") 
    QPushButton.setStyleSheet(
        "background-color:" + hex_color + ";"
    )
except:
    print("Accent couldn't be found! Using default.")
app = QApplication(sys.argv)

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        
        self.resize(500, 300)
        self.setWindowTitle("Settings - Snake Browser, by Freakybob Team.")

        # hold on
        layout = QVBoxLayout()
        layout_1 = QHBoxLayout()
        # ok now im gonna push after ur done with this line
        with open('qss/settings.qss', 'r') as f:
            style = f.read()
            app.setStyleSheet(style)
        
    def gpc(self):
        with open("settings/gpc.txt", "r") as file:
            gpccontrol = file.read()

        with open("settings/gpc.txt", "w") as file:
            if gpccontrol == "1":
                file.write("0")
                QMessageBox.warning(self, "GPC Setting Changed", "Your GPC setting has changed to off.")
            else:
                file.write("1")
                QMessageBox.warning(self, "GPC Setting Changed", "Your GPC setting has changed to on.")

# i tested and the settings window just closes
# yeah hold on
# i see
# i tested and dont see anything