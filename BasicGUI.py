from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        print("Clicked")
        self.label.setText("You Pressed The Button")
        self.update()

    def update(self):
        self.label.adjustSize()

    def initUI(self):
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Basic GUI")

        self.label =QtWidgets.QLabel(self)
        self.label.setText("My First Label")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me!")
        self.b1.clicked.connect(self.button_clicked)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()