# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desingui1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 468)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 652, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menucopy = QtWidgets.QMenu(self.menufile)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Who I Am/Pictures/IMG_0192.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menucopy.setIcon(icon)
        self.menucopy.setObjectName("menucopy")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Who I Am/Pictures/0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionnew.setIcon(icon1)
        self.actionnew.setObjectName("actionnew")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionexit_2 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/Who I Am/Pictures/Light Yagami.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionexit_2.setIcon(icon2)
        self.actionexit_2.setObjectName("actionexit_2")
        self.actionsleep = QtWidgets.QAction(MainWindow)
        self.actionsleep.setObjectName("actionsleep")
        self.actionselebgram = QtWidgets.QAction(MainWindow)
        self.actionselebgram.setObjectName("actionselebgram")
        self.menucopy.addAction(self.actionsleep)
        self.menucopy.addAction(self.actionselebgram)
        self.menufile.addAction(self.actionnew)
        self.menufile.addAction(self.menucopy.menuAction())
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionexit_2)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())

        self.retranslateUi(MainWindow)
        self.actionexit_2.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menucopy.setTitle(_translate("MainWindow", "copy"))
        self.menuedit.setTitle(_translate("MainWindow", "edit"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionexit_2.setText(_translate("MainWindow", "exit"))
        self.actionexit_2.setStatusTip(_translate("MainWindow", "Klik Untuk Keluar"))
        self.actionsleep.setText(_translate("MainWindow", "sleep"))
        self.actionselebgram.setText(_translate("MainWindow", "selebgram"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

