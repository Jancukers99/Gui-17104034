from PyQt5.QtWidgets import QWidget, QLabel


class html (QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 200)
        self.move(300, 300)
        self.setWindowTitle('Latihan 2 <Tag HTML')

        self.label1 =QLabel('<h1><font color = Black>Rekayasa</font><font color = red> Perangkat </font><font color = blue>Lunak</font></h1>')
        self.label1.move(10, 10)
        self.label1.setParent(self)

        self.label2 = QLabel('<b>Peserta Praktikum Pemprograman Gui</b>')
        self.label3 = QLabel(' 1. Monkey D Luffy')
        self.label4 = QLabel(' 2. Roronoa Zoro')
        self.label5 = QLabel(' 3. Takiya Genji')
        self.label2.move(10, 50)
        self.label2.setParent(self)
        self.label3.move(10, 70)
        self.label3.setParent(self)
        self.label4.move(10, 80)
        self.label4.setParent(self)
        self.label5.move(10, 90)
        self.label5.setParent(self)
