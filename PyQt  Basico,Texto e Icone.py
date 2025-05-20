import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CareVision")
        self.setGeometry(0, 0, 1500, 1000)
        self.setWindowIcon(QIcon(r"C:\Users\Pichau\PycharmProjects\PythonProject\CareVision.jpg"))
                                 #ESSE r antes do "C:\..." permite que o caminho seja lido pelo codigo!

        label = QLabel("Olá", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: black;"
                            "background-color: grey;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        #label.setAlignment(Qt.AlignTop)     #VERTICALLY TOP
        #label.setAlignment(Qt.AlignBottom)  #VERTICALLY BOTTOM
        #label.setAlignment(Qt.AlignVCenter) #VERTICALLY CENTER

        #label.setAlignment(Qt.AlignRight)    # HORIZONTALLY RIGHT
        #label.setAlignment(Qt.AlignHCenter)  # HORIZONTALLY CENTER
        #label.setAlignment(Qt.AlignLeft)     # HORIZONTALLY LEFT

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)      #CENTER & TOP
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)   # CENTER & BOTTOM
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # CENTER & CENTER
        #label.setAlignment(Qt.AlignCenter)                      # CENTER & CENTER (SHORTCUT)






def main():
     app = QApplication(sys.argv)
     window = MainWindow()
     window.show()
     sys.exit(app.exec_())

if __name__ == "__main__":
    main()
