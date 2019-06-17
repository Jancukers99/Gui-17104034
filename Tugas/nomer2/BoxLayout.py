from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLineEdit, QLabel

class BoxLayout(QWidget):
    def __init__(self):
        super(). __init__ ()
        self.horizontalUi ()

    def horizontalUi (self):
            self.resize(350, 100)
            self.move(300,300)
            self.setWindowTitle('Latihan 2')

            self.Label =QLabel('Masukan Nama Anda')
            self.LineEdit =QLineEdit()
            layout = QHBoxLayout()
            layout.addWidget(self.Label)
            layout.addWidget(self.LineEdit)

            self.setLayout(layout)
