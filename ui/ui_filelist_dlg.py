# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filelist_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(603, 422)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.path_edit = QtWidgets.QLineEdit(Dialog)
        self.path_edit.setObjectName("path_edit")
        self.horizontalLayout.addWidget(self.path_edit)
        self.btn_path = QtWidgets.QToolButton(Dialog)
        self.btn_path.setObjectName("btn_path")
        self.horizontalLayout.addWidget(self.btn_path)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_filelist = QtWidgets.QLabel(Dialog)
        self.label_filelist.setObjectName("label_filelist")
        self.verticalLayout.addWidget(self.label_filelist)
        self.file_list = QtWidgets.QTableWidget(Dialog)
        self.file_list.setObjectName("file_list")
        self.file_list.setColumnCount(0)
        self.file_list.setRowCount(0)
        self.verticalLayout.addWidget(self.file_list)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_download = QtWidgets.QPushButton(Dialog)
        self.btn_download.setDefault(True)
        self.btn_download.setObjectName("btn_download")
        self.horizontalLayout_2.addWidget(self.btn_download)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_path.setText(_translate("Dialog", "..."))
        self.label_filelist.setText(_translate("Dialog", "Filelist"))
        self.btn_download.setText(_translate("Dialog", "Download"))

