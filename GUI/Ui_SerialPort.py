# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SerialPort.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1142, 771)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_msg = QtWidgets.QWidget()
        self.tab_msg.setObjectName("tab_msg")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_msg)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit_Recive = QtWidgets.QTextEdit(self.tab_msg)
        self.textEdit_Recive.setStyleSheet("/*background-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);*/")
        self.textEdit_Recive.setObjectName("textEdit_Recive")
        self.gridLayout_3.addWidget(self.textEdit_Recive, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.tab_msg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.hexSending_checkBox = QtWidgets.QCheckBox(self.tab_msg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hexSending_checkBox.sizePolicy().hasHeightForWidth())
        self.hexSending_checkBox.setSizePolicy(sizePolicy)
        self.hexSending_checkBox.setObjectName("hexSending_checkBox")
        self.horizontalLayout.addWidget(self.hexSending_checkBox)
        self.Send_Button = QtWidgets.QPushButton(self.tab_msg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Send_Button.sizePolicy().hasHeightForWidth())
        self.Send_Button.setSizePolicy(sizePolicy)
        self.Send_Button.setObjectName("Send_Button")
        self.horizontalLayout.addWidget(self.Send_Button)
        self.pushButton_clearSendText = QtWidgets.QPushButton(self.tab_msg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_clearSendText.sizePolicy().hasHeightForWidth())
        self.pushButton_clearSendText.setSizePolicy(sizePolicy)
        self.pushButton_clearSendText.setObjectName("pushButton_clearSendText")
        self.horizontalLayout.addWidget(self.pushButton_clearSendText)
        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.textEdit_Send = QtWidgets.QTextEdit(self.tab_msg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_Send.sizePolicy().hasHeightForWidth())
        self.textEdit_Send.setSizePolicy(sizePolicy)
        self.textEdit_Send.setStyleSheet("/*background-color: rgb(0, 0, 0);*/")
        self.textEdit_Send.setObjectName("textEdit_Send")
        self.gridLayout_3.addWidget(self.textEdit_Send, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.tab_msg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.hexShowing_checkBox = QtWidgets.QCheckBox(self.tab_msg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hexShowing_checkBox.sizePolicy().hasHeightForWidth())
        self.hexShowing_checkBox.setSizePolicy(sizePolicy)
        self.hexShowing_checkBox.setObjectName("hexShowing_checkBox")
        self.horizontalLayout_2.addWidget(self.hexShowing_checkBox)
        self.ClearButton = QtWidgets.QPushButton(self.tab_msg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClearButton.sizePolicy().hasHeightForWidth())
        self.ClearButton.setSizePolicy(sizePolicy)
        self.ClearButton.setObjectName("ClearButton")
        self.horizontalLayout_2.addWidget(self.ClearButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.tab_msg)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.comboBox_codetype = QtWidgets.QComboBox(self.tab_msg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_codetype.sizePolicy().hasHeightForWidth())
        self.comboBox_codetype.setSizePolicy(sizePolicy)
        self.comboBox_codetype.setObjectName("comboBox_codetype")
        self.comboBox_codetype.addItem("")
        self.comboBox_codetype.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_codetype)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_msg, "")
        self.tab_img = QtWidgets.QWidget()
        self.tab_img.setObjectName("tab_img")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_img)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_showGrid = QtWidgets.QCheckBox(self.tab_img)
        self.checkBox_showGrid.setObjectName("checkBox_showGrid")
        self.gridLayout_2.addWidget(self.checkBox_showGrid, 1, 7, 1, 1)
        self.comboBox_imgType = QtWidgets.QComboBox(self.tab_img)
        self.comboBox_imgType.setObjectName("comboBox_imgType")
        self.comboBox_imgType.addItem("")
        self.comboBox_imgType.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_imgType, 0, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.tab_img)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 5, 1, 2)
        self.lineEdit_width = QtWidgets.QLineEdit(self.tab_img)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_width.sizePolicy().hasHeightForWidth())
        self.lineEdit_width.setSizePolicy(sizePolicy)
        self.lineEdit_width.setInputMask("")
        self.lineEdit_width.setObjectName("lineEdit_width")
        self.gridLayout_2.addWidget(self.lineEdit_width, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(269, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 5, 1, 2)
        self.lineEdit_height = QtWidgets.QLineEdit(self.tab_img)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_height.sizePolicy().hasHeightForWidth())
        self.lineEdit_height.setSizePolicy(sizePolicy)
        self.lineEdit_height.setObjectName("lineEdit_height")
        self.gridLayout_2.addWidget(self.lineEdit_height, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_img)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_position = QtWidgets.QLabel(self.tab_img)
        self.label_position.setObjectName("label_position")
        self.gridLayout_2.addWidget(self.label_position, 2, 7, 1, 1)
        self.checkBox_UseOpenCV = QtWidgets.QCheckBox(self.tab_img)
        self.checkBox_UseOpenCV.setObjectName("checkBox_UseOpenCV")
        self.gridLayout_2.addWidget(self.checkBox_UseOpenCV, 0, 7, 1, 1)
        self.pushButton_saveImg = QtWidgets.QPushButton(self.tab_img)
        self.pushButton_saveImg.setObjectName("pushButton_saveImg")
        self.gridLayout_2.addWidget(self.pushButton_saveImg, 2, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 2, 5, 1, 1)
        self.label_extra14bytes = QtWidgets.QLabel(self.tab_img)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_extra14bytes.sizePolicy().hasHeightForWidth())
        self.label_extra14bytes.setSizePolicy(sizePolicy)
        self.label_extra14bytes.setText("")
        self.label_extra14bytes.setObjectName("label_extra14bytes")
        self.gridLayout_2.addWidget(self.label_extra14bytes, 0, 3, 1, 1)
        self.label_pause = QtWidgets.QLabel(self.tab_img)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pause.sizePolicy().hasHeightForWidth())
        self.label_pause.setSizePolicy(sizePolicy)
        self.label_pause.setText("")
        self.label_pause.setObjectName("label_pause")
        self.gridLayout_2.addWidget(self.label_pause, 2, 3, 1, 1)
        self.label_img = WidgetPainter(self.tab_img)
        self.label_img.setMouseTracking(True)
        self.label_img.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label_img.setObjectName("label_img")
        self.gridLayout_2.addWidget(self.label_img, 3, 0, 1, 8)
        self.tabWidget.addTab(self.tab_img, "")
        self.tab_other = QtWidgets.QWidget()
        self.tab_other.setObjectName("tab_other")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_other)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget_other = QtWidgets.QTabWidget(self.tab_other)
        self.tabWidget_other.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_other.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_other.setObjectName("tabWidget_other")
        self.tab_watch_parameter = QtWidgets.QWidget()
        self.tab_watch_parameter.setObjectName("tab_watch_parameter")
        self.tabWidget_other.addTab(self.tab_watch_parameter, "")
        self.tab_change_parameter = QtWidgets.QWidget()
        self.tab_change_parameter.setObjectName("tab_change_parameter")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_change_parameter)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidget_para = QtWidgets.QListWidget(self.tab_change_parameter)
        self.listWidget_para.setObjectName("listWidget_para")
        self.gridLayout_5.addWidget(self.listWidget_para, 1, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(570, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 2, 0, 1, 1)
        self.pushButton_readMCU = QtWidgets.QPushButton(self.tab_change_parameter)
        self.pushButton_readMCU.setObjectName("pushButton_readMCU")
        self.gridLayout_5.addWidget(self.pushButton_readMCU, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_change_parameter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 2)
        self.tabWidget_other.addTab(self.tab_change_parameter, "")
        self.tab_wave = QtWidgets.QWidget()
        self.tab_wave.setObjectName("tab_wave")
        self.tabWidget_other.addTab(self.tab_wave, "")
        self.tab_piano = QtWidgets.QWidget()
        self.tab_piano.setObjectName("tab_piano")
        self.tabWidget_other.addTab(self.tab_piano, "")
        self.horizontalLayout_5.addWidget(self.tabWidget_other)
        self.tabWidget.addTab(self.tab_other, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1142, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_uart = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_uart.setObjectName("dockWidget_uart")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_2 = QtWidgets.QFrame(self.dockWidgetContents_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.About_Button = QtWidgets.QPushButton(self.dockWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("方正兰亭中黑_GBK")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.About_Button.setFont(font)
        self.About_Button.setObjectName("About_Button")
        self.verticalLayout.addWidget(self.About_Button)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.Com_Name_Label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.Com_Name_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Com_Name_Label.setObjectName("Com_Name_Label")
        self.gridLayout.addWidget(self.Com_Name_Label, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.comboBox_data = QtWidgets.QComboBox(self.dockWidgetContents_2)
        self.comboBox_data.setObjectName("comboBox_data")
        self.comboBox_data.addItem("")
        self.comboBox_data.addItem("")
        self.comboBox_data.addItem("")
        self.comboBox_data.addItem("")
        self.gridLayout.addWidget(self.comboBox_data, 5, 1, 1, 1)
        self.comboBox_stop = QtWidgets.QComboBox(self.dockWidgetContents_2)
        self.comboBox_stop.setObjectName("comboBox_stop")
        self.comboBox_stop.addItem("")
        self.comboBox_stop.addItem("")
        self.gridLayout.addWidget(self.comboBox_stop, 6, 1, 1, 1)
        self.Com_Baud_Combo = QtWidgets.QComboBox(self.dockWidgetContents_2)
        self.Com_Baud_Combo.setEditable(True)
        self.Com_Baud_Combo.setDuplicatesEnabled(False)
        self.Com_Baud_Combo.setModelColumn(0)
        self.Com_Baud_Combo.setObjectName("Com_Baud_Combo")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.Com_Baud_Combo.addItem("")
        self.gridLayout.addWidget(self.Com_Baud_Combo, 3, 1, 1, 1)
        self.Com_Refresh_Label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.Com_Refresh_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Com_Refresh_Label.setObjectName("Com_Refresh_Label")
        self.gridLayout.addWidget(self.Com_Refresh_Label, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.Com_Refresh_Button = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.Com_Refresh_Button.setObjectName("Com_Refresh_Button")
        self.gridLayout.addWidget(self.Com_Refresh_Button, 0, 1, 1, 1)
        self.Com_Open_Button = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.Com_Open_Button.setObjectName("Com_Open_Button")
        self.gridLayout.addWidget(self.Com_Open_Button, 7, 1, 1, 1)
        self.comboBox_parity = QtWidgets.QComboBox(self.dockWidgetContents_2)
        self.comboBox_parity.setObjectName("comboBox_parity")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.comboBox_parity.addItem("")
        self.gridLayout.addWidget(self.comboBox_parity, 4, 1, 1, 1)
        self.Com_isOpenOrNot_Label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.Com_isOpenOrNot_Label.setText("")
        self.Com_isOpenOrNot_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Com_isOpenOrNot_Label.setObjectName("Com_isOpenOrNot_Label")
        self.gridLayout.addWidget(self.Com_isOpenOrNot_Label, 9, 0, 1, 1)
        self.Com_State_Label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.Com_State_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Com_State_Label.setObjectName("Com_State_Label")
        self.gridLayout.addWidget(self.Com_State_Label, 7, 0, 1, 1)
        self.Com_Name_Combo = QtWidgets.QComboBox(self.dockWidgetContents_2)
        self.Com_Name_Combo.setObjectName("Com_Name_Combo")
        self.gridLayout.addWidget(self.Com_Name_Combo, 2, 1, 1, 1)
        self.Com_Close_Button = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.Com_Close_Button.setDefault(False)
        self.Com_Close_Button.setObjectName("Com_Close_Button")
        self.gridLayout.addWidget(self.Com_Close_Button, 9, 1, 1, 1)
        self.Com_Baud_Label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.Com_Baud_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Com_Baud_Label.setObjectName("Com_Baud_Label")
        self.gridLayout.addWidget(self.Com_Baud_Label, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 115, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.Time_Label = QtWidgets.QLabel(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Time_Label.sizePolicy().hasHeightForWidth())
        self.Time_Label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("方正兰亭中黑_GBK")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Time_Label.setFont(font)
        self.Time_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Time_Label.setObjectName("Time_Label")
        self.verticalLayout.addWidget(self.Time_Label)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setStyleSheet("/*alternate-background-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);*/")
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.dockWidget_uart.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_uart)
        self.action_uart = QtWidgets.QAction(MainWindow)
        self.action_uart.setCheckable(True)
        self.action_uart.setChecked(True)
        self.action_uart.setObjectName("action_uart")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setShortcutVisibleInContextMenu(True)
        self.action_exit.setObjectName("action_exit")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.menu.addAction(self.action_exit)
        self.menu_2.addAction(self.actionAbout_Qt)
        self.menu_3.addAction(self.action_uart)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_other.setCurrentIndex(0)
        self.comboBox_data.setCurrentIndex(3)
        self.comboBox_stop.setCurrentIndex(0)
        self.Com_Baud_Combo.setCurrentIndex(10)
        self.pushButton_clearSendText.clicked.connect(self.textEdit_Send.clear)
        self.ClearButton.clicked.connect(self.textEdit_Recive.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt5 智能车串口调试助手"))
        self.textEdit_Recive.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "发送区"))
        self.hexSending_checkBox.setText(_translate("MainWindow", "16进制发送"))
        self.Send_Button.setText(_translate("MainWindow", "发送"))
        self.pushButton_clearSendText.setText(_translate("MainWindow", "清除"))
        self.label.setText(_translate("MainWindow", "接收区"))
        self.hexShowing_checkBox.setText(_translate("MainWindow", "16进制显示"))
        self.ClearButton.setText(_translate("MainWindow", "清除"))
        self.label_9.setText(_translate("MainWindow", "编码方式："))
        self.comboBox_codetype.setItemText(0, _translate("MainWindow", "utf-8"))
        self.comboBox_codetype.setItemText(1, _translate("MainWindow", "gb2312"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_msg), _translate("MainWindow", "接收发送数据"))
        self.checkBox_showGrid.setText(_translate("MainWindow", "显示网格线"))
        self.comboBox_imgType.setItemText(0, _translate("MainWindow", "二值化图像"))
        self.comboBox_imgType.setItemText(1, _translate("MainWindow", "灰度图像(单片机解压)"))
        self.label_5.setText(_translate("MainWindow", "高"))
        self.lineEdit_width.setText(_translate("MainWindow", "80"))
        self.lineEdit_height.setText(_translate("MainWindow", "60"))
        self.label_6.setText(_translate("MainWindow", "宽"))
        self.label_position.setText(_translate("MainWindow", "鼠标位置 x:  0,y:  0"))
        self.checkBox_UseOpenCV.setText(_translate("MainWindow", "使用OpenCV查看图像"))
        self.pushButton_saveImg.setText(_translate("MainWindow", "保存图像"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_img), _translate("MainWindow", "查看图像"))
        self.tabWidget_other.setTabText(self.tabWidget_other.indexOf(self.tab_watch_parameter), _translate("MainWindow", "查看参数"))
        self.pushButton_readMCU.setText(_translate("MainWindow", "更新上位机数据"))
        self.label_4.setText(_translate("MainWindow", "参数"))
        self.tabWidget_other.setTabText(self.tabWidget_other.indexOf(self.tab_change_parameter), _translate("MainWindow", "修改参数"))
        self.tabWidget_other.setTabText(self.tabWidget_other.indexOf(self.tab_wave), _translate("MainWindow", "显示波形"))
        self.tabWidget_other.setTabText(self.tabWidget_other.indexOf(self.tab_piano), _translate("MainWindow", "弹琴"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_other), _translate("MainWindow", "附加功能"))
        self.menu.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_2.setTitle(_translate("MainWindow", "关于(&A)"))
        self.menu_3.setTitle(_translate("MainWindow", "视图(&V)"))
        self.dockWidget_uart.setWindowTitle(_translate("MainWindow", "串口设置"))
        self.About_Button.setText(_translate("MainWindow", "Made by PyQt5 - 查看源代码"))
        self.label_3.setText(_translate("MainWindow", "奇偶位"))
        self.Com_Name_Label.setText(_translate("MainWindow", "串口选择"))
        self.label_8.setText(_translate("MainWindow", "停止位"))
        self.comboBox_data.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox_data.setItemText(1, _translate("MainWindow", "6"))
        self.comboBox_data.setItemText(2, _translate("MainWindow", "7"))
        self.comboBox_data.setItemText(3, _translate("MainWindow", "8"))
        self.comboBox_stop.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_stop.setItemText(1, _translate("MainWindow", "2"))
        self.Com_Baud_Combo.setCurrentText(_translate("MainWindow", "115200"))
        self.Com_Baud_Combo.setItemText(0, _translate("MainWindow", "1200"))
        self.Com_Baud_Combo.setItemText(1, _translate("MainWindow", "2400"))
        self.Com_Baud_Combo.setItemText(2, _translate("MainWindow", "4800"))
        self.Com_Baud_Combo.setItemText(3, _translate("MainWindow", "9600"))
        self.Com_Baud_Combo.setItemText(4, _translate("MainWindow", "14400"))
        self.Com_Baud_Combo.setItemText(5, _translate("MainWindow", "19200"))
        self.Com_Baud_Combo.setItemText(6, _translate("MainWindow", "38400"))
        self.Com_Baud_Combo.setItemText(7, _translate("MainWindow", "43000"))
        self.Com_Baud_Combo.setItemText(8, _translate("MainWindow", "57600"))
        self.Com_Baud_Combo.setItemText(9, _translate("MainWindow", "76800"))
        self.Com_Baud_Combo.setItemText(10, _translate("MainWindow", "115200"))
        self.Com_Baud_Combo.setItemText(11, _translate("MainWindow", "128000"))
        self.Com_Baud_Combo.setItemText(12, _translate("MainWindow", "230400"))
        self.Com_Baud_Combo.setItemText(13, _translate("MainWindow", "256000"))
        self.Com_Baud_Combo.setItemText(14, _translate("MainWindow", "460800"))
        self.Com_Baud_Combo.setItemText(15, _translate("MainWindow", "921600"))
        self.Com_Baud_Combo.setItemText(16, _translate("MainWindow", "1382400"))
        self.Com_Refresh_Label.setText(_translate("MainWindow", "串口搜索"))
        self.label_7.setText(_translate("MainWindow", "数据位"))
        self.Com_Refresh_Button.setText(_translate("MainWindow", "刷新"))
        self.Com_Open_Button.setText(_translate("MainWindow", "Open"))
        self.comboBox_parity.setItemText(0, _translate("MainWindow", "无校验"))
        self.comboBox_parity.setItemText(1, _translate("MainWindow", "偶校验"))
        self.comboBox_parity.setItemText(2, _translate("MainWindow", "奇校验"))
        self.comboBox_parity.setItemText(3, _translate("MainWindow", "空校验"))
        self.comboBox_parity.setItemText(4, _translate("MainWindow", "标志校验"))
        self.Com_State_Label.setText(_translate("MainWindow", "串口操作"))
        self.Com_Close_Button.setText(_translate("MainWindow", "Close"))
        self.Com_Baud_Label.setText(_translate("MainWindow", "波特率"))
        self.Time_Label.setText(_translate("MainWindow", "Time"))
        self.action_uart.setText(_translate("MainWindow", "串口设置(&U)"))
        self.action_exit.setText(_translate("MainWindow", "退出(&T)"))
        self.action_exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))


from widgetpainter import WidgetPainter
import res_rc
