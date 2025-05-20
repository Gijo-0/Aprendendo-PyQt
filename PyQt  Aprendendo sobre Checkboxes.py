import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CareVision")
        self.setGeometry(0, 0, 1500, 1000)
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10, 0, 750, 350)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font family: Arial;")
        self.checkbox.setChecked(False) #True = checkbox estara confirmada ao abrir o aplicativo
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You like food")
        else:
            print("you do NOT like food")

def main():
     app = QApplication(sys.argv)
     window = MainWindow()
     window.show()
     sys.exit(app.exec_())

if __name__ == "__main__":
    main()
