from ui import ui_about
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, Qt


class AboutDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_about.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('关于')

        logo = QPixmap('res/logo.ico')
        self.ui.label_logo.setPixmap(logo)
        self.ui.label_logo.setAlignment(Qt.AlignCenter)
        self.ui.label_logo.setFixedSize(QSize(100, 100))
        self.ui.label_logo.setScaledContents(True)

        self.ui.label_name.setText('<h3>%s</h3>' % '下载器')
        self.ui.label_version.setText('v1.0')
        self.ui.label_author.setText('@author月梦书')
