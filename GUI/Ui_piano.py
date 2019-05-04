# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piano.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_settings = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_settings.sizePolicy().hasHeightForWidth())
        self.groupBox_settings.setSizePolicy(sizePolicy)
        self.groupBox_settings.setObjectName("groupBox_settings")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_settings)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox_settings)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.comboBox_transpose = QtWidgets.QComboBox(self.groupBox_settings)
        self.comboBox_transpose.setObjectName("comboBox_transpose")
        self.comboBox_transpose.addItem("")
        self.comboBox_transpose.addItem("")
        self.comboBox_transpose.addItem("")
        self.comboBox_transpose.addItem("")
        self.comboBox_transpose.addItem("")
        self.comboBox_transpose.addItem("")
        self.comboBox_transpose.addItem("")
        self.comboBox_transpose.addItem("")
        self.comboBox_transpose.addItem("")
        self.comboBox_transpose.addItem("")
        self.comboBox_transpose.addItem("")
        self.comboBox_transpose.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_transpose)
        self.gridLayout.addWidget(self.groupBox_settings, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(219, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(375, 208, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 2)

        self.retranslateUi(Form)
        self.comboBox_transpose.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_settings.setTitle(_translate("Form", "设置"))
        self.label_10.setText(_translate("Form", "transpose"))
        self.comboBox_transpose.setItemText(0, _translate("Form", "A"))
        self.comboBox_transpose.setItemText(1, _translate("Form", "A#"))
        self.comboBox_transpose.setItemText(2, _translate("Form", "B"))
        self.comboBox_transpose.setItemText(3, _translate("Form", "C"))
        self.comboBox_transpose.setItemText(4, _translate("Form", "C#"))
        self.comboBox_transpose.setItemText(5, _translate("Form", "D"))
        self.comboBox_transpose.setItemText(6, _translate("Form", "D#"))
        self.comboBox_transpose.setItemText(7, _translate("Form", "E"))
        self.comboBox_transpose.setItemText(8, _translate("Form", "F"))
        self.comboBox_transpose.setItemText(9, _translate("Form", "F#"))
        self.comboBox_transpose.setItemText(10, _translate("Form", "G"))
        self.comboBox_transpose.setItemText(11, _translate("Form", "G#"))


