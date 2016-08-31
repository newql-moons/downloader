import tools
from ui import ui_downloading_item
from ui import ui_downloaded_item
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QDesktopServices
from forms.del_dlg import DelDlg
from db import *


class DownloadingItem(QWidget):
    finished = QtCore.pyqtSignal(dict)
    removed = QtCore.pyqtSignal(dict)

    def __init__(self, task, parent=None):
        super().__init__(parent)
        self.ui = ui_downloading_item.Ui_Form()
        self.ui.setupUi(self)

        self.__task = task
        self.__last = task.downloaded

        # 初始化控件
        self.ui.label_title.setText('<h3>%s</h1>' % task.title)
        self.ui.label_speed.setText('暂停')
        self.ui.label_size.setText('<h4>%s</h4>' % tools.sizeof(task.size))
        self.ui.progressBar.setValue(task.downloaded / task.size * 100)

        # 初始化右键菜单选项
        self.a_start = QAction('开始任务', self)
        self.a_stop = QAction('暂停任务', self)
        self.a_rm = QAction('移除任务', self)
        self.a_start.triggered.connect(self.start)
        self.a_stop.triggered.connect(self.stop)
        self.a_rm.triggered.connect(self.remove)

        self.__timer = QtCore.QTimer()
        self.__timer.timeout.connect(self.refresh)

    def contextMenuEvent(self, event):
        menu = QMenu()
        menu.addAction(self.a_start)
        menu.addAction(self.a_stop)
        menu.addAction(self.a_rm)
        menu.exec(event.globalPos())

    def mouseDoubleClickEvent(self, event):
        if self.__task.is_stop():
            self.start()
        else:
            self.stop()

    def start(self):
        self.ui.label_speed.setText('正在开始')
        self.__task.start()
        self.__timer.start(500)

    def stop(self):
        self.ui.label_speed.setText('暂停')
        if self.__timer.isActive():
            self.__timer.stop()
        self.__task.stop()

    def remove(self):
        dlg = DelDlg('是否删除任务？', '同时删除文件')
        if dlg.exec():
            self.removed.emit(self.__task.info)
            if dlg.is_checked():
                tab3 = FilelistTab()

                files = tab3.select_by_link(self.__task.info['link'])
                for file in files:
                    if os.path.exists(file['path']):
                        os.remove(file['path'])
                    if os.path.exists(file['path'] + '.json'):
                        os.remove(file['path'] + '.json')
                tab3.delete_by_link(self.__task.info['link'])

                tab3.close()

    def refresh(self):
        task = self.__task
        p = task.downloaded / task.size * 100
        self.ui.progressBar.setValue(p)
        self.ui.label_speed\
            .setText(tools.sizeof((task.downloaded - self.__last) * 2) + '/s')
        print(task.downloaded / task.size)
        self.__last = task.downloaded
        if p == 100:
            self.__timer.stop()
            self.finished.emit(self.__task.info)
            self.__task.wait()


class DownloadedItem(QWidget):
    removed = QtCore.pyqtSignal(dict)

    def __init__(self, info, parent=None):
        super().__init__(parent)
        self.ui = ui_downloaded_item.Ui_Form()
        self.ui.setupUi(self)

        self.__info = info

        self.ui.title_label.setText('<h3>%s</h3>' % info['title'])
        self.__path = info['path']
        self.ui.date_label.setText(info['date'])

        self.ui.btn_open.clicked.connect(self.on_btn_open_click)
        self.ui.btn_rm.clicked.connect(self.on_btn_rm_click)

    def on_btn_open_click(self):
        QDesktopServices().openUrl(QtCore.QUrl(self.__path, QtCore.QUrl.TolerantMode))

    def on_btn_rm_click(self):
        dlg = DelDlg('是否删除记录？', '同时删除文件')
        if dlg.exec():
            self.removed.emit(self.__info)
            if dlg.is_checked():
                tab3 = FilelistTab()

                files = tab3.select_by_link(self.__info['link'])
                for file in files:
                    if os.path.exists(file['path']):
                        os.remove(file['path'])
                    if os.path.exists(file['path'] + '.json'):
                        os.remove(file['path'] + '.json')
                tab3.delete_by_link(self.__info['link'])

                tab3.close()
