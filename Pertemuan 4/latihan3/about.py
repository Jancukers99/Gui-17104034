from PyQt5.QtWidgets import QWidget, QPushButton, QLabel

class about (QWidget):
    def __init__(self):
                super().__init__()
                self.setupUi()

    def setupUi(self):
            self.resize(150, 100)
            self.move(100, 100)
            self.setWindowTitle('About')

            self.label1 =QLabel('Dibuat Oleh Tim RPL')
            self.label1.move(10, 40)
            self.label1.setParent(self)

            self.label2 =QLabel('Versi 1.0')
            self.label2.move(10, 50)
            self.label2.setParent(self)

            self.label3 =QLabel('Copyright@2019')
            self.label3.move(10, 60)
            self.label3.setParent(self)

            self.button =QPushButton('OK')
            self.button.move(60, 75)
            self.button.setParent(self)

            self.button.clicked.connect(self.buttonClick)
    def buttonClick(self):
            self.close()
