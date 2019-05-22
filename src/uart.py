import binascii
import re
from PyQt5.QtSerialPort import QSerialPort
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize, QByteArray, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap, QBitmap


class Uart(QSerialPort):
    signal_update_standard_gui = pyqtSignal(int)

    def __init__(self, parent=None):
        super(Uart, self).__init__(parent)
        # Qt 串口类
        # self.com = QSerialPort()
        self.comParity = (QSerialPort.NoParity, QSerialPort.EvenParity, QSerialPort.OddParity, QSerialPort.SpaceParity,
                          QSerialPort.MarkParity)
        self.list_of_msg = list()
        # 图像类
        self.img = QPixmap()
        self.imgHeight = 80
        self.imgWidth = 60
        self.img_rx_data = QByteArray()
        self.totalImgSize = self.imgHeight * self.imgWidth
        # 上位机改参数类
        self.ready_to_get_paras = False

        # self.imgrxData = bytearray()
        # self.pararxData = bytearray()
        # 标准模式类
        self.standard_rx_data = QByteArray()
        self.change_paras = dict()  # 上位机改参数字典
        self.watch_paras = dict()  # 上位机看参数
        self.wave_paras = dict()  # 波形字典

        # 串口普通模式发送数据

    def com_send_data(self, tx_data: str, is_hex: bool, codetype: str):
        if len(tx_data) == 0:
            return
        if not is_hex:
            self.write(tx_data.encode(codetype))
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
            self.write(hex_data)
            # except:
            #     QMessageBox.critical(self, '异常', '十六进制发送错误')
            return

    # 串口改参数模式发送函数
    def com_send_change(self, name: str, tx_data_index: str, tx_data_value: str):
        if self.isOpen():
            # self.paras.value = self.para_value.text()
            # print(self.index)
            tx_data0 = b'\xb1'
            # self.para_value.setText(tx_data_value)
            if tx_data_index.isalnum() and tx_data_value.isalnum():
                self.write(tx_data0 + tx_data_index.encode() + b' ' + tx_data_value.encode() + b'\n\x00')
                self.change_paras[name] = tx_data_value
            # print("sendParasToMCU")

    # 串口接收模式处理函数
    def com_receive_normal(self, is_hex: bool, code_type: str) -> str:
        rx_data = bytes(self.readAll())
        if not is_hex:
            # code_type = selfboBox_codetype.currentText()
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
    def com_receive_image(self, cb_index, extra_bytes_len) -> (QBitmap, tuple):
        if len(self.img_rx_data) == 0:
            self.img_rx_data = self.readAll()
            # print(type(self.imgrxData))
            if self.img_rx_data[:2] != b'\x01\xfe':  # 不是图像的起始位
                self.img_rx_data.clear()
                return None
            else:
                # self.imgrxData=self.imgrxData[2:]
                return None
        else:
            self.img_rx_data += self.readAll()
        # if self.imgrxData[:2]==b'\x01\xfe' and self.imgrxData[-2:]==b'\xfe\x01':
        if len(self.img_rx_data) >= self.totalImgSize + 2 + extra_bytes_len:  # 校验位两位，其余14位为传的数据
            self.clear()
            # cb_index = selfboBox_imgType.currentIndex()
            extra_data = tuple(
                bytes(self.img_rx_data[2:2 + extra_bytes_len]))  # 14位额外数据
            # print(type( self.label_img.extra_data[0]))
            # print(self.label_img.extra_data)
            if cb_index == 0:  # 二值化图像
                self.img = QBitmap.fromData(QSize(self.imgWidth, self.imgHeight),
                                            bytes(self.img_rx_data[2 + extra_bytes_len:]),
                                            QImage.Format_Mono)
            elif cb_index == 1:  # 灰度图像
                # imgbytes = bytes(self.imgrxData[2:])
                # self.img = QImage(imgbytes, self.imgWidth,self.imgHeight, QImage.Format_Mono)
                imgbytes = bytes([255 if int.from_bytes(b, 'little') > 0 else 0 for b in
                                  self.img_rx_data[2 + extra_bytes_len:]])
                self.img = QBitmap.fromImage(
                    QImage(imgbytes, self.imgWidth, self.imgHeight, QImage.Format_Grayscale8))
                # import numpy as np
                # a=np.frombuffer(bytes(self.imgrxData[2:]),dtype=np.uint8)*128
                # imgbytes=bytes(a)
            # OpenCVUse.process(imgbytes, self.imgHeight, self.imgWidth)
            # self.label_img.setPixmap(self.img)
            self.img_rx_data.clear()
            return self.img, extra_data

    # 串口其他模式处理函数
    def com_receive_standard(self):
        rx_data = self.readAll()
        self.standard_rx_data += rx_data
        while True:
            index = self.standard_rx_data.indexOf(b'\x00')
            if index < 0:  # 直到self.standard_rx_data没有'\x00'跳出循环
                break
            # rx_data.resize(index)
            standard_rx_data_temp = QByteArray(self.standard_rx_data[:index])
            self.standard_rx_data = self.standard_rx_data[index + 1:]

            if len(standard_rx_data_temp) <= 0:
                continue
                # self.standard_rx_data.resize(self.standard_rx_data.indexOf(b'\x00'))
            self.list_of_msg = standard_rx_data_temp[1:].split('\n')  # 字符串列表
            msg = standard_rx_data_temp[0]
            # self.standard_rx_data.clear()
            if msg == b'\xa0':  # 看参数模式
                self.add_to_dict(self.watch_paras, self.list_of_msg)
                self.signal_update_standard_gui.emit(0)
            elif msg == b'\xa8':  # 波形模式
                self.add_to_dict(self.wave_paras, self.list_of_msg)
                self.signal_update_standard_gui.emit(2)
            elif msg == b'\xb2':  # 改参数模式，读取参数
                self.add_to_dict(self.change_paras, self.list_of_msg)
                self.signal_update_standard_gui.emit(1)
            elif msg == b'\xb0':  # 改参数模式，成功修改参数
                self.signal_update_standard_gui.emit(-1)

    # 将字符串添加到对应的字典中
    @staticmethod
    def add_to_dict(dic: dict, list_of_msg: list):
        for entry in list_of_msg:
            if entry != b'':
                try:
                    key, value = bytes(entry).split(b':', 1)
                    dic[key.decode(errors='ignore')] = value.decode(errors='ignore')
                except ValueError:
                    pass
                # dic[key.decode(errors='ignore').replace('\x00', '')] = value.decode(errors='ignore')

    # 串口调参模式处理函数 且 已发送 hyxr
    # def com_receive_para(self):
    #     pass
    # if self.ready_to_get_paras:
    #     try:
    #         self.pararxData += self.readAll()
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

    # def process_standard_rx_data(self):
