from PyQt5.QtWidgets import (QWidget, QPushButton, QToolTip)
from PyQt5.QtGui import QFont

class tooltip(QWidget):
    def __init__ (self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(400, 300)
        self.move(300, 300)
        self.setWindowTitle('Latihan Menampilkan Tooltip')

        QToolTip.setFont(QFont('SansSerif',12))

        self.button =QPushButton('OtherForm')
        self.button.move(140, 100)
        self.button.setParent(self)
        self.button.setToolTip('''<font color=red>Tombol untuk</font><b>membuka form lain</b>''')
        self.button1 =QPushButton('Exit')
        self.button1.move(140, 140)
        self.button1.setParent(self)
        self.button.clicked.connect(self.buttonClick)
        self.button1.clicked.connect(self.buttonClick1)

    def buttonClick(self):
        self.form = OtherForm()
        self.form.show()

    def buttonClick1(self):
        self.close()
