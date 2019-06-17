import sys
from PyQt5.QtWidgets import QApplication

from BoxLayout import*
if __name__ == '__main__':
        a =QApplication(sys.argv)
        form =BoxLayout()
        form.show()
        a.exec_()
