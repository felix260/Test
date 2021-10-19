#!/usr/bin/python3
import sys
from Ui_untitled import Ui_Dialog

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = QMainWindow()
    w = Ui_Dialog()
    w.setupUi(mw)
    mw.show()
    sys.exit(app.exec_())
