import binascii
import re
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize, QByteArray
from PyQt5.QtGui import QImage, QPixmap, QBitmap, QPainter


class Uart:
    def __init__(self):
        # Qt 串口类
        self.com = QSerialPort()
        self.comParity = (QSerialPort.NoParity, QSerialPort.EvenParity, QSerialPort.OddParity, QSerialPort.SpaceParity,
                          QSerialPort.MarkParity)
        # 图像类
        self.img = QPixmap()
        self.imgHeight = 80
        self.imgWidth = 60
        self.imgrxData = QByteArray()
        self.totalImgSize = self.imgHeight * self.imgWidth
        # 上位机改参数类
        self.ready_to_get_paras = False

        self.imgrxData = bytearray()
        self.pararxData = bytearray()
        # 串口发送数据

    def com_send_data(self, tx_data: str, is_hex: bool, codetype: str):
        if len(tx_data) == 0:
            return
        if not is_hex:
            self.com.write(tx_data.encode(codetype))
        else:
            data = tx_data.replace(' ', '')
            # 如果16进制不是偶数个字符, 去掉最后一个, [ ]左闭右开
            if len(data) % 2 == 1:
                data = data[0:len(data) - 1]
            # 如果遇到非16进制字符
            # if data.isalnum() is False:
            #     QMessageBox.critical(self, '错误', '包含非十六进制数')
            # try:
            hex_data = binascii.a2b_hex(data)
            # except:
            #     QMessageBox.critical(self, '错误', '转换编码错误')

            # 发送16进制数据, 发送格式如 ‘31 32 33 41 42 43’, 代表'123ABC'
            # try:
            self.com.write(hex_data)
            # except:
            #     QMessageBox.critical(self, '异常', '十六进制发送错误')
            return

    # 串口接收模式处理函数
    def com_receive_normal(self, is_hex: bool, code_type: str) -> str:
        rx_data = bytes(self.com.readAll())
        if not is_hex:
            # code_type = self.comboBox_codetype.currentText()
            # self.textEdit_Recive.insertPlainText(rx_data.decode(code_type, errors='replace'))
            return rx_data.decode(code_type, errors='replace')
        else:
            data = binascii.b2a_hex(rx_data).decode('ascii')
            # re 正则表达式 (.{2}) 匹配两个字母
            hex_str = ' 0x'.join(re.findall('(.{2})', data))
            # 补齐第一个 0x
            hex_str = '0x' + hex_str + ' '

            return hex_str

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
        pass
        # if self.ready_to_get_paras:
        #     try:
        #         self.pararxData += self.com.readAll()
        #         if len(self.pararxData) >= len(self.paraWidgets) * 4:
        #             # print(len(self.pararxData))
        #             for i, item in enumerate(self.paraWidgets):
        #                 rxData = bytes(self.pararxData[0 + i * 4:3 + i * 4])
        #                 value = int.from_bytes(
        #                     rxData, 'little', signed=item.paras.signed)
        #                 item.paras.value = value
        #                 # self.listWidget_para.setIndexWidget(i, item)
        #                 item.para_value.setText(str(value))
        #                 print(i, value)
        #             self.pararxData.clear()
        #             self.ready_to_get_paras = False
        #     except:
        #         QMessageBox.critical(self, '严重错误', '串口接收数据错误')
        #         self.ready_to_get_paras = False
        #         self.pararxData.clear()

        # 串口刷新

    # 串口综合模式（改参数、波形、弹琴等）
    def com_receive_other(self):
        pass
