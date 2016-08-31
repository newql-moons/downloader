# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(890, 522)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.index_list = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.index_list.sizePolicy().hasHeightForWidth())
        self.index_list.setSizePolicy(sizePolicy)
        self.index_list.setMinimumSize(QtCore.QSize(0, 0))
        self.index_list.setMaximumSize(QtCore.QSize(200, 16777215))
        self.index_list.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"font: 15pt;")
        self.index_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.index_list.setObjectName("index_list")
        self.verticalLayout.addWidget(self.index_list)
        self.btn_add = QtWidgets.QPushButton(Form)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout.addWidget(self.btn_add)
        self.btn_about = QtWidgets.QPushButton(Form)
        self.btn_about.setObjectName("btn_about")
        self.verticalLayout.addWidget(self.btn_about)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.downloading = DownloadingWidget(self.page)
        self.downloading.setObjectName("downloading")
        self.verticalLayout_2.addWidget(self.downloading)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.downloaded = DownloadedWidget(self.page_2)
        self.downloaded.setObjectName("downloaded")
        self.horizontalLayout_2.addWidget(self.downloaded)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_add.setText(_translate("Form", "添加任务"))
        self.btn_about.setText(_translate("Form", "关于"))

from widgets.lists import DownloadedWidget
from widgets.lists import DownloadingWidget
