import sys
from PyQt5.QtWidgets import QApplication
from html import *

if __name__ == '__main__':
    a = QApplication(sys.argv)

    mainform = html()
    mainform.show()

a.exec_()
