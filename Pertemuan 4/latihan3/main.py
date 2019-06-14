import sys
from PyQt5.QtWidgets import QApplication
from MainForm import *

if __name__ == '__main__':
    a = QApplication(sys.argv)

    mainform = MainForm()
    mainform.show()

a.exec_()
