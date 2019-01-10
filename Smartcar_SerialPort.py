# 逻辑文件

import re
import sys
sys.path.append("GUI")
import binascii
import time
from PyQt5.QtCore import QTimer, Qt, QUrl
# from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QListWidgetItem, QMessageBox, QGraphicsScene
from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5 import QtGui
# from PyQt5.QtWebEngineWidgets import *
from GUI.Ui_SerialPort import Ui_Form
from PyQt5.QtCore import QDate
from GUI.ParaItem import Widget_ParaItem
from PyQt5.QtCore import QSize
import parameter
import bitarray
from OpenCV import OpenCVUse




# import numpy as np

class MyMainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # 设置实例
        # self.isOpenUART=False
        self.create_items()
        # 设置信号与槽
        self.create_signal_slot()

    # 设置实例
    def create_items(self):
        # Qt 串口类
        self.com = QSerialPort()
        self.comParity = (QSerialPort.NoParity, QSerialPort.EvenParity, QSerialPort.OddParity, QSerialPort.SpaceParity,
                          QSerialPort.MarkParity)
        # Qt 定时器类
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.show_time)  # 计时结束调用operate()方法
        self.timer.start(100)  # 设置计时间隔 100ms 并启动
        # Qt ListWidget 类
        self.paraWidgets = []
        self.imgrxData = bytearray()
        # self.imgbyte=bitarray.bitarray(endian='big')
        for i, para in enumerate(parameter.parameterList):
            para_widget = Widget_ParaItem(
                para, i, self.com, self.listWidget_para)
            # self.listWidget_para.addItem()
            self.paraWidgets.append(para_widget)
            para_listWidgetItem = QListWidgetItem(self.listWidget_para)
            self.listWidget_para.addItem(para_listWidgetItem)
            self.listWidget_para.setItemWidget(
                para_listWidgetItem, para_widget)
            size = para_widget.minimumSizeHint()
            para_listWidgetItem.setSizeHint(size)
            # para_widget.show()
        # self.listWidget_para.show()

        # 图像类
        self.img = QImage()
        self.label_img.label_position = self.label_position  # 为了在label_img能改label_pasition
        # 上位机改参数类
        self.readyToGetParas: bool = False

    # 设置信号与槽
    def create_signal_slot(self):
        self.Com_Open_Button.clicked.connect(self.com_open_button_clicked)
        self.Com_Close_Button.clicked.connect(self.com_close_button_clicked)
        self.Send_Button.clicked.connect(self.send_button_clicked)
        self.Com_Refresh_Button.clicked.connect(
            self.com_refresh_button_clicked)
        self.com.readyRead.connect(self.com_receive_data)  # 接收数据
        self.hexSending_checkBox.stateChanged.connect(self.hex_showing_clicked)
        self.hexSending_checkBox.stateChanged.connect(self.hex_sending_clicked)
        # self.About_Button.clicked.connect(self.Goto_GitHub)
        self.pushButton_readMCU.clicked.connect(self.send_read_mcu)
        self.checkBox_UseOpenCV.stateChanged.connect(self.on_open_cv_use_clicked)
        self.checkBox_showGrid.stateChanged.connect(self.on_show_grid_changed)

    # 跳转到 GitHub 查看源代码
    # def Goto_GitHub(self):
    #     self.browser = QWebEngineView()
    #     self.browser.load(QUrl('https://github.com/Oslomayor/PyQt5-SerialPort-Stable'))
    #     self.setCentralWidget(self.browser)

    # 显示时间
    def show_time(self):
        self.Time_Label.setText(time.strftime(
            "%B %d, %H:%M:%S", time.localtime()))

    # 串口发送数据
    def com_send_data(self):
        txData = self.textEdit_Send.toPlainText()
        if len(txData) == 0:
            return
        if self.hexSending_checkBox.isChecked() == False:
            self.com.write(txData.encode('UTF-8'))
        else:
            Data = txData.replace(' ', '')
            # 如果16进制不是偶数个字符, 去掉最后一个, [ ]左闭右开
            if len(Data) % 2 == 1:
                Data = Data[0:len(Data) - 1]
            # 如果遇到非16进制字符
            if Data.isalnum() is False:
                QMessageBox.critical(self, '错误', '包含非十六进制数')
            try:
                hexData = binascii.a2b_hex(Data)
            except:
                QMessageBox.critical(self, '错误', '转换编码错误')
                return
            # 发送16进制数据, 发送格式如 ‘31 32 33 41 42 43’, 代表'123ABC'
            try:
                self.com.write(hexData)
            except:
                QMessageBox.critical(self, '异常', '十六进制发送错误')
                return

    # 串口接收数据
    def com_receive_data(self):
        tabWidget_currentIndex = self.tabWidget.currentIndex()
        if tabWidget_currentIndex == 0:  # 收发模式
            try:
                rxData = bytes(self.com.readAll())
            except:
                QMessageBox.critical(self, '严重错误', '串口接收数据错误')
            if self.hexShowing_checkBox.isChecked() == False:
                try:
                    self.textEdit_Recive.insertPlainText(
                        rxData.decode('UTF-8'))
                except:
                    pass
            else:
                Data = binascii.b2a_hex(rxData).decode('ascii')
                # re 正则表达式 (.{2}) 匹配两个字母
                hexStr = ' 0x'.join(re.findall('(.{2})', Data))
                # 补齐第一个 0x
                hexStr = '0x' + hexStr
                self.textEdit_Recive.insertPlainText(hexStr)
                self.textEdit_Recive.insertPlainText(' ')
        elif tabWidget_currentIndex == 1:  # 图像模式
            if len(self.imgrxData) == 0:
                self.imgrxData = self.com.readAll()
                if self.imgrxData[:2] != b'\x01\xfe':  # 不是图像的起始位
                    self.imgrxData = bytearray()
                    return
                else:
                    # self.imgrxData=self.imgrxData[2:]
                    return
            else:
                self.imgrxData += self.com.readAll()
            # if self.imgrxData[:2]==b'\x01\xfe' and self.imgrxData[-2:]==b'\xfe\x01':

            if len(self.imgrxData) >= self.totalImgSize:
                self.com.clear()
                cb_index = self.comboBox_imgType.currentIndex()
                if self.cb_index == 0:  # 二值化图像
                    imgbits = bitarray.bitarray(endian='big')
                    imgbits.frombytes(bytes(self.imgrxData[2:]))
                    # print(self.imgrxData)
                    imgbytes = imgbits.unpack(zero=b'\x66', one=b'\x00')
                    # print(imgbytes)
                elif self.cb_index == 1:  # 灰度图像
                    imgbytes = bytes(self.imgrxData[2:])
                # OpenCVUse.process(imgbytes, self.imgHeight, self.imgWidth)
                self.img = QImage(imgbytes, self.imgWidth,
                                  self.imgHeight, QImage.Format_Grayscale8)
                # print(self.img.height())
                # print(self.img.width())
                # print(self.img.dotsPerMeterY())
                # print(self.img.dotsPerMeterX())
                # self.img=QPixmap.loadFromData()
                size = self.label_img.size()
                self.label_img.setPixmap(QPixmap.fromImage(self.img))
                self.imgrxData.clear()
        elif tabWidget_currentIndex == 2 and self.readyToGetParas:  # 调参模式 且 已发送 hyxr
            try:
                for i, item in enumerate(self.paraWidgets):
                    rxData = bytes(self.com.read(4))
                    value = int.from_bytes(
                        rxData, 'little', signed=item.paras.signed)
                    item.paras.value = value
                    # self.listWidget_para.setIndexWidget(i, item)
                    item.para_value.setText(str(value))
                    print(value)
            except:
                QMessageBox.critical(self, '严重错误', '串口接收数据错误')
            finally:
                self.readyToGetParas = False
        else:
            pass

    # 串口刷新
    def com_refresh_button_clicked(self):
        self.Com_Name_Combo.clear()
        com = QSerialPort()
        com_list = QSerialPortInfo.availablePorts()
        for info in com_list:
            com.setPort(info)
            if com.open(QSerialPort.ReadWrite):
                self.Com_Name_Combo.addItem(info.portName())
                com.close()

    # 16进制显示按下
    def hex_showing_clicked(self):
        if self.hexShowing_checkBox.isChecked() == True:
            # 接收区换行
            self.textEdit_Recive.insertPlainText('\n')

    # 16进制发送按下
    def hex_sending_clicked(self):
        if self.hexSending_checkBox.isChecked() == True:
            pass

    # 发送按钮按下
    def send_button_clicked(self):
        self.com_send_data()

    # 串口打开按钮按下
    def com_open_button_clicked(self):
        # 图像模式
        try:
            self.imgHeight = int(self.lineEdit_height.text())
            self.imgWidth = int(self.lineEdit_width.text())
            self.label_img.set_img_height_width(self.imgHeight, self.imgWidth)

        except ValueError:
            QMessageBox.warning(self, '错误', '图像长宽请输入整数')
            return
        self.cb_index = self.comboBox_imgType.currentIndex()
        if self.cb_index == 0:  # 二值化图像
            self.totalImgSize = self.imgHeight * self.imgWidth // 8
        elif self.cb_index == 1:  # 灰度图像
            self.totalImgSize = self.imgHeight * self.imgWidth

        #### com Open Code here ####
        comName = self.Com_Name_Combo.currentText()
        comBaud = int(self.Com_Baud_Combo.currentText())
        self.com.setPortName(comName)
        self.com.setBaudRate(comBaud)
        self.com.setParity(self.comParity[self.comboBox_parity.currentIndex()])
        self.com.setDataBits(int(self.comboBox_data.currentText()))
        self.com.setStopBits(int(self.comboBox_stop.currentText()))

        try:
            if self.com.open(QSerialPort.ReadWrite) == False:
                QMessageBox.critical(self, '严重错误', '串口打开失败')
                return
        except:
            QMessageBox.critical(self, '严重错误', '串口打开失败')
            return
        # self.Com_Close_Button.setEnabled(True)
        # self.Com_Open_Button.setEnabled(False)
        # self.Com_Refresh_Button.setEnabled(False)
        # self.Com_Name_Combo.setEnabled(False)
        # self.Com_Baud_Combo.setEnabled(False)

        self.Com_isOpenOrNot_Label.setText('  已打开')

        self.set_widgets_enabled(False)

    def com_close_button_clicked(self):
        self.com.close()
        # self.Com_Close_Button.setEnabled(False)
        # self.Com_Open_Button.setEnabled(True)
        # self.Com_Refresh_Button.setEnabled(True)
        # self.Com_Name_Combo.setEnabled(True)
        # self.Com_Baud_Combo.setEnabled(True)

        self.set_widgets_enabled(True)
        self.Com_isOpenOrNot_Label.setText('  已关闭')

    def send_read_mcu(self):
        if self.com.isOpen():
            self.com.write(b'hyxr')
            self.readyToGetParas = True

    def on_open_cv_use_clicked(self):
        if self.checkBox_UseOpenCV.isChecked():
            OpenCVUse.init()
            # self.test()
        else:
            OpenCVUse.close()

    def on_show_grid_changed(self, a0: int):
        # print(a0)
        if a0 == 0:  # 取消勾选
            self.label_img.enable_grid = False
            self.label_img.repaint()
        else:  # 勾选
            self.label_img.enable_grid = True
            self.label_img.calculate_grid_points()
            self.label_img.repaint()

    def set_widgets_enabled(self, enable: bool):  # 图像模式
        self.Com_Close_Button.setEnabled(not enable)
        self.Com_Open_Button.setEnabled(enable)
        self.Com_Refresh_Button.setEnabled(enable)
        self.Com_Name_Combo.setEnabled(enable)
        self.Com_Baud_Combo.setEnabled(enable)

        self.lineEdit_height.setEnabled(enable)
        self.lineEdit_width.setEnabled(enable)
        self.comboBox_imgType.setEnabled(enable)
        self.comboBox_data.setEnabled(enable)
        self.comboBox_parity.setEnabled(enable)
        self.comboBox_stop.setEnabled(enable)
        # self.checkBox_UseOpenCV.setEnabled(enable)
        # self.checkBox_showGrid.setEnabled(enable)

    # def clear_read_buffer(self):
    #     pass
    #
    # def clear_write_buffer(self):
    #     pass

    # def resizeEvent(self, a0: QtGui.QResizeEvent):
    #     #super(MyMainWindow, self).resizeEvent(a0)
    #     size = self.label_img.size()
    #     self.label_img.setPixmap(QPixmap.fromImage(self.img).scaled(size, Qt.KeepAspectRatio))

    # def paintEvent(self, a0: QtGui.QPaintEvent):
    #     # super(MyMainWindow, self).paintEvent(a0)
    #
    #     painter = QPainter(self.label_img)
    #     painter.drawPixmap(0, 0, self.label_img.width(),
    #                        self.label_img.height(), QPixmap.fromImage(self.img))

    def test(self):
        self.tabWidget.setCurrentIndex(1)
        self.imgWidth = 80
        self.imgHeight = 60
        testbytes = b'\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff' * \
                    16 + b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x0f' * 44
        imgbits = bitarray.bitarray(endian='big')
        imgbits.frombytes(testbytes)
        # print(self.imgrxData)
        imgbytes = imgbits.unpack(zero=b'\x66', one=b'\x00')
        # print(imgbytes)
        # self.label_img.setScaledContents(True)
        # self.label_img.setAlignment(Qt.AlignCenter)
        if self.checkBox_UseOpenCV.isChecked():
            OpenCVUse.process(imgbytes, self.imgHeight, self.imgWidth)
        self.img = QImage(imgbytes, self.imgWidth,
                          self.imgHeight, QImage.Format_Grayscale8)

        # print(self.img.height())
        # print(self.img.width())
        # print(self.img.dotsPerMeterY())
        # print(self.img.dotsPerMeterX())
        # self.img=QPixmap.loadFromData()
        # self.label_img.setScaledContents(False)
        size = self.label_img.size()
        self.label_img.setPixmap(QPixmap.fromImage(self.img))


def main():
    app = QApplication(sys.argv)
    my_win = MyMainWindow()
    # mywin
    # myWin.test()
    my_win.show()
    # myWin.showFullScreen()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()