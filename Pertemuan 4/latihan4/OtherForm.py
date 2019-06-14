from PyQt5.QtWidgets import QWidget, QPushButton
class OtherForm(QWidget):
    def __init__(self):
            super().__init__()
            self.setupUi()

    def setupUi(self):
            self.resize(400, 300)
            self.move(300, 300)
            self.setWindowTitle('Form Liane')

            self.button =QPushButton('Tutup')
            self.button.move(150, 130)
            self.button.setParent(self)

            self.button1.clicked.connect(self.buttonClick1)
    def buttonClick1(self):
            self.close()
