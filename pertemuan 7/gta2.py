# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desingui2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 287)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 30, 181, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.namaEdit = QtWidgets.QLineEdit(Form)
        self.namaEdit.setGeometry(QtCore.QRect(140, 60, 331, 21))
        self.namaEdit.setObjectName("namaEdit")
        self.hallo = QtWidgets.QPushButton(Form)
        self.hallo.setGeometry(QtCore.QRect(180, 100, 75, 23))
        self.hallo.setObjectName("hallo")
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(290, 100, 75, 23))
        self.clear.setObjectName("clear")
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(230, 140, 75, 23))
        self.exit.setObjectName("exit")

        self.retranslateUi(Form)
        self.exit.clicked.connect(Form.close)
        self.clear.clicked.connect(self.namaEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Masukan Nama Anda :</span></p></body></html>"))
        self.hallo.setText(_translate("Form", "Hallo"))
        self.clear.setText(_translate("Form", "Clear"))
        self.exit.setText(_translate("Form", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

