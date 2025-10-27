# Developed by wish and mpax235 and freakbob
# Snake Browser Settings, from Freakybob Team. Licensed under GPL-3.0.

from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QMessageBox, QPushButton, QLabel, QHBoxLayout, QSizePolicy
from PyQt6.QtCore import Qt
import sys
try:
    import accentcolordetect # this module only supports windows & mac according to the github ig? good thing you dont need it to run
except: 
    print("Accentcolordetect wasn't installed. Settings buttons won't use your system accent color.")
    
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

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        mainLabel = QLabel("Settings")
        mainLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLabel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        mainLabel.setFixedHeight(30)
        layout.addWidget(mainLabel)

        layout_1 = QHBoxLayout()

        self.gpcbtn = QPushButton("Toggle GPC", self)
        self.gpcbtn.clicked.connect(self.gpc)
        layout_1.addWidget(self.gpcbtn)
        
        layout.addLayout(layout_1)

        self.setLayout(layout)
        try:
            with open('qss/settings.qss', 'r') as f:
                style = f.read()
                app.setStyleSheet(style)
        except:
            print("QSS file not found. Styling will not be on.")
        
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