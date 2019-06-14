from PyQt5.QtWidgets import QWidget, QLabel

class FormSederhana(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 200)
        self.move(400, 450)
        self.setWindowTitle('Praktikum Pemrograman GUI')

        self.label = QLabel('Dosen Pengampu :')
        self.label1 = QLabel('Afandi Nur Aziz Thohari, S.T.,M.Cs')
        self.label.move(70, 70)
        self.label1.move(70, 80)
        self.label.setParent(self)
        self.label1.setParent(self)
