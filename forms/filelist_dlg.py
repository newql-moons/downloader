from ui import ui_filelist_dlg
from PyQt5.QtWidgets import *
from core import task
from PyQt5.QtCore import Qt
import tools


class FilelistDlg(QDialog):
    def __init__(self, link, path, parent=None):
        super().__init__(parent)
        self.ui = ui_filelist_dlg.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('添加任务')

        self.ui.path_edit.setText(path)
        self.load_filelist(link)

        self.ui.btn_download.clicked.connect(self.__on_btn_download_click)
        self.ui.btn_path.clicked.connect(self.__on_btn_path_click)

    def __on_btn_path_click(self):
        path = QFileDialog.getExistingDirectory()
        if path != '':
            self.ui.path_edit.setText(path)

    def __on_btn_download_click(self):
        if self.ui.path_edit.text() == '':
            QMessageBox.about(self, '提醒', '路径不能为空！')
        else:
            self.accept()

    def get_task(self):
        self.task.path = self.ui.path_edit.text()
        return self.task

    def load_filelist(self, link):
        self.task = task.create_task(link)
        filelist = self.task.filelist

        self.ui.file_list.setRowCount(len(filelist))
        self.ui.file_list.setColumnCount(2)
        self.ui.file_list.setHorizontalHeaderLabels(['文件', '大小'])
        self.ui.file_list.horizontalHeader().setStretchLastSection(True)
        self.ui.file_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.file_list.setEditTriggers(QAbstractItemView.NoEditTriggers)

        raw = 0
        for file in filelist:
            name = file['name']
            size = file['size']

            size = tools.sizeof(size)

            item_name = QTableWidgetItem(name)
            item_size = QTableWidgetItem(size)
            item_size.setTextAlignment(Qt.AlignCenter)
            self.ui.file_list.setItem(raw, 0, item_name)
            self.ui.file_list.setItem(raw, 1, item_size)
            raw += 1

    @property
    def filelist(self):
        return self.task.filelist
