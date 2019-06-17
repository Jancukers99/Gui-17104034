from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
class VBoxLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.verticalUi()
    def verticalUi(self):
        self.resize(300, 200)
        self.move(300,300)
        self.setWindowTitle('Latihan 1')

        self.Label1 = QLabel('<h3><font color = purple>Fakultas Teknologi Industri & Informatika</font></h3>')
        self.button1 =QPushButton('S1 Rekayasa Perangkat Lunak')
        self.button2 =QPushButton('S1 Desain Komunikasi Visual')
        self.button3 =QPushButton('S1 Sistem Informatika')
        self.button4 =QPushButton('S1 Teknik Industri')
        self.button5 =QPushButton('S1 Informatika')

        layout =QVBoxLayout()
        layout.addWidget(self.Label1)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)

        self.setLayout(layout)
