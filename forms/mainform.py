from ui import ui_mainform
from .add_dlg import AddDlg
from .filelist_dlg import FilelistDlg
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from db import *
from core import task
from forms import about


class MainForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_mainform.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('下载器')

        # 初始化导航条
        item1 = QListWidgetItem(QIcon('res/downloading.ico'), '正在下载')
        item2 = QListWidgetItem(QIcon('res/downloaded.ico'), '下载完成')
        item1.setSizeHint(QSize(60, 30))
        item2.setSizeHint(QSize(60, 30))
        self.ui.index_list.addItem(item1)
        self.ui.index_list.addItem(item2)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.btn_add.clicked.connect(self.on_btn_add_click)
        self.ui.btn_about.clicked.connect(self.on_btn_about_click)
        self.ui.index_list.doubleClicked.connect(self.change)

        # 根据数据数据初始化列表
        tab1 = DownloadingTab()
        for info in tab1.select():
            t = task.load_task(info)
            self.ui.downloading.addTask(t)
        tab1.close()
        tab2 = DownloadedTab()
        for info in tab2.select():
            self.ui.downloaded.addRecord(info)
        tab2.close()

    def closeEvent(self, QCloseEvent):
        self.ui.downloading.stopAll.emit()

    def on_btn_add_click(self):
        a = AddDlg()
        if a.exec():
            f = FilelistDlg(a.get_link(), a.get_path())
            if f.exec():
                self.ui.downloading.addTask(f.get_task())
                self.ui.downloading\
                    .itemWidget(self.ui.downloading.item(self.ui.downloading.count() - 1))\
                    .start()

    def on_btn_about_click(self):
        dlg = about.AboutDlg()
        dlg.exec()

    def change(self, index):
        self.ui.stackedWidget.setCurrentIndex(index.row())
