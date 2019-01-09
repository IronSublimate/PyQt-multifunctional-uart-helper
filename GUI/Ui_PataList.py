# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\NXP\2018NXP\2侯宇轩工具\PyQt5-SerialPort-smartcar\GUI\PataList.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PataList(object):
    def setupUi(self, PataList):
        PataList.setObjectName("PataList")
        PataList.resize(588, 145)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PataList.sizePolicy().hasHeightForWidth())
        PataList.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(PataList)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(PataList)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 0, 1, 4)
        self.label = QtWidgets.QLabel(PataList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(PataList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.para_name = QtWidgets.QLabel(PataList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.para_name.sizePolicy().hasHeightForWidth())
        self.para_name.setSizePolicy(sizePolicy)
        self.para_name.setObjectName("para_name")
        self.gridLayout.addWidget(self.para_name, 2, 0, 1, 1)
        self.para_value = QtWidgets.QLineEdit(PataList)
        self.para_value.setObjectName("para_value")
        self.gridLayout.addWidget(self.para_value, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(127, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.send_to_MCU = QtWidgets.QCommandLinkButton(PataList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_to_MCU.sizePolicy().hasHeightForWidth())
        self.send_to_MCU.setSizePolicy(sizePolicy)
        self.send_to_MCU.setObjectName("send_to_MCU")
        self.gridLayout.addWidget(self.send_to_MCU, 2, 3, 1, 1)
        self.line = QtWidgets.QFrame(PataList)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 4)

        self.retranslateUi(PataList)
        QtCore.QMetaObject.connectSlotsByName(PataList)

    def retranslateUi(self, PataList):
        _translate = QtCore.QCoreApplication.translate
        PataList.setWindowTitle(_translate("PataList", "Form"))
        self.label.setText(_translate("PataList", "参数"))
        self.label_2.setText(_translate("PataList", "值"))
        self.para_name.setText(_translate("PataList", "TextLabel"))
        self.send_to_MCU.setText(_translate("PataList", "发送到单片机"))

