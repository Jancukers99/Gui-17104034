import sys
from PyQt5.QtWidgets import QApplication
from tooltip import *

if __name__ == '__main__':
    a = QApplication(sys.argv)

    mainform = tooltip()
    mainform.show()

a.exec_()
