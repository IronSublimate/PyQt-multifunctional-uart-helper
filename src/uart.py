import binascii
import re
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPixmap,QBitmap, QPainter


class Uart:
    def __init__(self):
        # Qt 串口类
        self.com = QSerialPort()
        self.comParity = (QSerialPort.NoParity, QSerialPort.EvenParity, QSerialPort.OddParity, QSerialPort.SpaceParity,
                          QSerialPort.MarkParity)
        # 图像类
        self.img = QPixmap()
        self.label_img.label_position = self.label_position  # 为了在label_img能改label_pasition
        self.label_img.label_pause = self.label_pause  # 为了在label_img能改label_pause
        # 上位机改参数类
        self.ready_to_get_paras = False

        # 串口发送数据
    def com_send_data(self):
        txData = self.textEdit_Send.toPlainText()
        if len(txData) == 0:
            return
        if self.hexSending_checkBox.isChecked() == False:
            codetype = self.comboBox_codetype.currentText()
            self.com.write(txData.encode(codetype))
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
            self.com_receive_normal()
        elif tabWidget_currentIndex == 1:  # 图像模式
            self.com_receive_image()
        elif tabWidget_currentIndex == 2:  # 调参模式 且 已发送 hyxr
            self.com_receive_para()
        else:
            pass

    # 串口收发模式处理函数
    def com_receive_normal(self):
        try:
            rxData = bytes(self.com.readAll())
        except:
            QMessageBox.critical(self, '严重错误', '串口接收数据错误')
        if self.hexShowing_checkBox.isChecked() == False:
            codetype = self.comboBox_codetype.currentText()
            self.textEdit_Recive.insertPlainText(rxData.decode(codetype, errors='replace'))
        else:
            Data = binascii.b2a_hex(rxData).decode('ascii')
            # re 正则表达式 (.{2}) 匹配两个字母
            hexStr = ' 0x'.join(re.findall('(.{2})', Data))
            # 补齐第一个 0x
            hexStr = '0x' + hexStr
            self.textEdit_Recive.insertPlainText(hexStr)
            self.textEdit_Recive.insertPlainText(' ')

    # 串口图像模式处理函数
    def com_receive_image(self):
        if len(self.imgrxData) == 0:
            self.imgrxData = self.com.readAll()
            # print(type(self.imgrxData))
            if self.imgrxData[:2] != b'\x01\xfe':  # 不是图像的起始位
                self.imgrxData.clear()
                return
            else:
                # self.imgrxData=self.imgrxData[2:]
                return
        else:
            self.imgrxData += self.com.readAll()
        # if self.imgrxData[:2]==b'\x01\xfe' and self.imgrxData[-2:]==b'\xfe\x01':
        if len(self.imgrxData) >= self.totalImgSize + 2 + self.label_img.extra_bytes_len:  # 校验位两位，其余14位为传的数据
            self.com.clear()
            # cb_index = self.comboBox_imgType.currentIndex()
            self.label_img.extra_data = tuple(
                bytes(self.imgrxData[2:2 + self.label_img.extra_bytes_len]))  # 14位额外数据
            # print(type( self.label_img.extra_data[0]))
            # print(self.label_img.extra_data)
            if self.cb_index == 0:  # 二值化图像
                self.img = QBitmap.fromData(QSize(self.imgWidth, self.imgHeight),
                                            bytes(self.imgrxData[2 + self.label_img.extra_bytes_len:]),
                                            QImage.Format_Mono)
            elif self.cb_index == 1:  # 灰度图像
                # imgbytes = bytes(self.imgrxData[2:])
                # self.img = QImage(imgbytes, self.imgWidth,self.imgHeight, QImage.Format_Mono)
                imgbytes = bytes([255 if int.from_bytes(b, 'little') > 0 else 0 for b in
                                  self.imgrxData[2 + self.label_img.extra_bytes_len:]])
                self.img = QBitmap.fromImage(
                    QImage(imgbytes, self.imgWidth, self.imgHeight, QImage.Format_Grayscale8))
                # import numpy as np
                # a=np.frombuffer(bytes(self.imgrxData[2:]),dtype=np.uint8)*128
                # imgbytes=bytes(a)
            # OpenCVUse.process(imgbytes, self.imgHeight, self.imgWidth)
            self.label_img.setPixmap(self.img)
            self.imgrxData.clear()

    # 串口调参模式处理函数 且 已发送 hyxr
    def com_receive_para(self):
        if self.ready_to_get_paras:
            try:
                self.pararxData += self.com.readAll()
                if len(self.pararxData) >= len(self.paraWidgets) * 4:
                    # print(len(self.pararxData))
                    for i, item in enumerate(self.paraWidgets):
                        rxData = bytes(self.pararxData[0 + i * 4:3 + i * 4])
                        value = int.from_bytes(
                            rxData, 'little', signed=item.paras.signed)
                        item.paras.value = value
                        # self.listWidget_para.setIndexWidget(i, item)
                        item.para_value.setText(str(value))
                        print(i, value)
                    self.pararxData.clear()
                    self.ready_to_get_paras = False
            except:
                QMessageBox.critical(self, '严重错误', '串口接收数据错误')
                self.ready_to_get_paras = False
                self.pararxData.clear()

                # 串口刷新

    # 串口综合模式（改参数、波形、弹琴等）
    def com_receive_other(self):
        pass
