import sys
from forms.mainform import MainForm
from PyQt5.QtWidgets import QApplication
from db import pre_db


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pre_db()
    w = MainForm()
    w.show()
    app.exec()
