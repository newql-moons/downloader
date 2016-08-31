import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, pyqtSignal
from .items import DownloadingItem, DownloadedItem
from db import *


class DownloadingWidget(QListWidget):
    stopAll = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def addTask(self, task):
        w = DownloadingItem(task)
        item = QListWidgetItem()
        self.addItem(item)
        item.setSizeHint(QSize(0, 60))
        self.setItemWidget(item, w)

        w.finished.connect(self.rm_task_slot(item, self.count() - 1))
        w.finished.connect(self.parent().parent().parent().ui.downloaded.addRecord)
        w.removed.connect(self.rm_task_slot(item, self.count() - 1))
        self.stopAll.connect(w.stop)

        tab = DownloadingTab()
        tab.insert(task.info)
        tab.close()

        tab3 = FilelistTab()
        for file in task.filelist:
            f = {
                'link': task.link,
                'path': task.path + file['name']
            }
            tab3.insert(f)
        tab3.close()

    def rm_task_slot(self, item, index):
        def slot(info):
            print(info)

            tab1 = DownloadingTab()
            tab1.delete(info['link'])
            tab1.close()

            self.removeItemWidget(item)
            self.takeItem(index)
        return slot


class DownloadedWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def addRecord(self, info):
        t = time.localtime()
        info['date'] = '%s/%s/%s' % (t.tm_year, t.tm_mon, t.tm_mday,)

        w = DownloadedItem(info)
        item = QListWidgetItem()
        self.addItem(item)
        item.setSizeHint(QSize(0, 60))
        self.setItemWidget(item, w)

        tab2 = DownloadedTab()
        tab2.insert(info)
        tab2.close()

        w.removed.connect(self.rm_record_slot(item, self.count() - 1))

    def rm_record_slot(self, item, index):
        def slot(info):
            print(info)
            tab = DownloadedTab()
            tab.delete(info['link'])
            tab.close()

            self.removeItemWidget(item)
            self.takeItem(index)
        return slot
