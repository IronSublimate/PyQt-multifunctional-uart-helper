# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\NXP\2018NXP\2侯宇轩工具\PyQt5-SerialPort-smartcar\GUI\Loading.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_loading(object):
    def setupUi(self, Form_loading):
        Form_loading.setObjectName("Form_loading")
        Form_loading.setWindowModality(QtCore.Qt.NonModal)
        Form_loading.resize(901, 521)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icon_128.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_loading.setWindowIcon(icon)
        Form_loading.setAutoFillBackground(False)
        Form_loading.setStyleSheet("QWidget#Form_loading{background-image: url(:/img/loading.jpg)};")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_loading)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(876, 134, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Title = QtWidgets.QLabel(Form_loading)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        self.Title.setStyleSheet("QLabel#Title{\n"
"    font: 36pt \"华文楷体\";\n"
"    \n"
"    color: rgb(0, 0, 127);\n"
"}")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 0, 0, 1, 3)
        self.Author = QtWidgets.QLabel(Form_loading)
        self.Author.setStyleSheet("QLabel#Author{\n"
"    font: 20pt \"宋体\";    \n"
"    color: rgb(0, 0, 127);\n"
"}")
        self.Author.setObjectName("Author")
        self.gridLayout.addWidget(self.Author, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(876, 134, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 4, 0, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(97, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(97, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Form_loading)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 6, 0, 1, 3)
        self.label = QtWidgets.QLabel(Form_loading)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(Form_loading)
        QtCore.QMetaObject.connectSlotsByName(Form_loading)

    def retranslateUi(self, Form_loading):
        _translate = QtCore.QCoreApplication.translate
        Form_loading.setWindowTitle(_translate("Form_loading", "Form"))
        self.Title.setText(_translate("Form_loading", "PyQt智能车串口调试助手"))
        self.Author.setText(_translate("Form_loading", "作者：侯宇轩"))
        self.label.setText(_translate("Form_loading", "加载中..."))

import res_rc
