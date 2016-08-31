import sys
import re
from core import setting
from ui import ui_add_dlg
from PyQt5.QtWidgets import *


class AddDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_add_dlg.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('添加任务')
        self.resize(500, 100)

        path = setting.download_path
        if re.match(r'^./[\S\s]*$', path):
            path = sys.path[0] + path[1:]
        self.ui.path_edit.setText(path)

        self.ui.btn_next.clicked.connect(self.__on_btn_next_click)
        self.ui.btn_path.clicked.connect(self.__on_btn_path_click)

    def __on_btn_path_click(self):
        path = QFileDialog.getExistingDirectory()
        if path != '':
            self.ui.path_edit.setText(path)
            
    def __on_btn_next_click(self):
        if self.get_link() == '':
            QMessageBox.about(self, '提醒', '链接不能为空！')
        elif self.get_path() == '':
            QMessageBox.about(self, '提醒', '路径不能为空！')
        else:
            self.accept()
            
    def get_link(self):
        return self.ui.link_edit.text()
    
    def get_path(self):
        return self.ui.path_edit.text()
