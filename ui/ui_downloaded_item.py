# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloaded_item.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(570, 67)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title_label = QtWidgets.QLabel(Form)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout_2.addWidget(self.title_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.date_label = QtWidgets.QLabel(Form)
        self.date_label.setObjectName("date_label")
        self.horizontalLayout.addWidget(self.date_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_open = QtWidgets.QPushButton(Form)
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout.addWidget(self.btn_open)
        self.btn_rm = QtWidgets.QPushButton(Form)
        self.btn_rm.setObjectName("btn_rm")
        self.horizontalLayout.addWidget(self.btn_rm)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_label.setText(_translate("Form", "TextLabel"))
        self.date_label.setText(_translate("Form", "TextLabel"))
        self.btn_open.setText(_translate("Form", "打开目录"))
        self.btn_rm.setText(_translate("Form", "删除"))

