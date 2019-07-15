# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Berat Badan Ideal")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 201, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 451, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Ltinggi = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Ltinggi.setFont(font)
        self.Ltinggi.setObjectName("Ltinggi")
        self.gridLayout_2.addWidget(self.Ltinggi, 0, 0, 1, 1)
        self.Lberat = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lberat.setFont(font)
        self.Lberat.setObjectName("Lberat")
        self.gridLayout_2.addWidget(self.Lberat, 1, 0, 1, 1)
        self.tinggi = QtWidgets.QLineEdit(self.layoutWidget)
        self.tinggi.setObjectName("tinggi")
        self.gridLayout_2.addWidget(self.tinggi, 0, 1, 1, 1)
        self.berat = QtWidgets.QLineEdit(self.layoutWidget)
        self.berat.setObjectName("berat")
        self.gridLayout_2.addWidget(self.berat, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.imt = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.imt.setFont(font)
        self.imt.setText("")
        self.imt.setObjectName("imt")
        self.gridLayout.addWidget(self.imt, 0, 0, 1, 1)
        self.tubuh = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tubuh.setFont(font)
        self.tubuh.setText("")
        self.tubuh.setObjectName("tubuh")
        self.gridLayout.addWidget(self.tubuh, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 1, 0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        T = self.tinggi.text()
        B = self.berat.text()
        Tinggi = eval(T)
        Berat = eval(B)
        Hasil =Tinggi/100
        Hasil2=Hasil*Hasil
        IMT = Berat/Hasil2

        if IMT>25:
            self.tubuh.setText("Harap Diet Lur")
            self.imt.setText("IBM Anda ="+str(IMT))
        elif IMT>23:
            self.imt.setText("IBM Anda "+str(IMT))
            self.tubuh.setText("Kegemukan")
        elif IMT > 18.5:
            self.imt.setText("IBM Anda"+str(IMT))
            self.tubuh.setText("SEDANG")
        elif IMT < 18.5:
            self.imt.setText("IBM Anda"+str(IMT))
            self.tubuh.setText("KEKURUSAN")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "BERAT BADAN IDEAL"))
        self.Ltinggi.setText(_translate("MainWindow", "Tinggi Badan (CM)"))
        self.Lberat.setText(_translate("MainWindow", "Berat Badan (KG)"))
        self.pushButton.setText(_translate("MainWindow", "Cek"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

