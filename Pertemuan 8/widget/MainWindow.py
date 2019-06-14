# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(485, 367)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 461, 331))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 50, 441, 241))
        self.calendarWidget.setObjectName("calendarWidget")
        self.dateEdit = QtWidgets.QDateEdit(self.tab)
        self.dateEdit.setGeometry(QtCore.QRect(10, 30, 441, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 171, 111))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 40, 111, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 60, 121, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(240, 0, 181, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.dial = QtWidgets.QDial(self.groupBox_2)
        self.dial.setGeometry(QtCore.QRect(9, 30, 61, 81))
        self.dial.setObjectName("dial")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber.setGeometry(QtCore.QRect(83, 40, 71, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 130, 201, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.fontComboBox = QtWidgets.QFontComboBox(self.groupBox_3)
        self.fontComboBox.setGeometry(QtCore.QRect(0, 20, 188, 21))
        self.fontComboBox.setObjectName("fontComboBox")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(0, 40, 191, 61))
        self.label.setText("")
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setGeometry(QtCore.QRect(17, 270, 421, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.radioButton_2.clicked.connect(self.progressBar.reset)
        self.fontComboBox.activated['QString'].connect(self.label.setText)
        self.dial.valueChanged['int'].connect(self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Widget 1"))
        self.groupBox.setTitle(_translate("MainWindow", "Chose Option"))
        self.radioButton.setText(_translate("MainWindow", "Default"))
        self.radioButton_2.setText(_translate("MainWindow", "Reset ProgressBar"))
        self.radioButton_3.setText(_translate("MainWindow", "Select ProgressBar"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Move To Dial"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Widget 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

