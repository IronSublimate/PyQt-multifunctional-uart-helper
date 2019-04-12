from PyQt5.QtWidgets import QWidget, QMessageBox
from GUI.Ui_PataList import Ui_PataList
# from parameter import Parameter
from PyQt5.QtSerialPort import QSerialPort
from src.uart import Uart


class Widget_ParaItem(QWidget, Ui_PataList):
    def __init__(self, para_name: str, pos: str, para_value: str, _com: Uart, parent=None):
        super(Widget_ParaItem, self).__init__(parent)
        super(QWidget, self).__init__()
        # super(Ui_PataList).__init__()
        self.setupUi(self)
        # self.paras = paras
        # self.index = _index
        self.pos = pos
        self.para_name.setText(para_name)
        self.para_value.setText(para_value)
        self.uart = _com

        self.create_signal_slot()

    def create_signal_slot(self):
        self.send_to_MCU.clicked.connect(self.send_paras_to_mcu)

    def send_paras_to_mcu(self):
        self.uart.com_send_change(self.para_name.text(), self.pos, self.para_value.text())
        # if self.uart.com.isOpen():
        #     # self.paras.value = self.para_value.text()
        #     # print(self.index)
        #     tx_data0 = b'\xb1'
        #     tx_data_index = self.pos
        #     tx_data_value = self.para_value.text()
        #     # self.para_value.setText(tx_data_value)
        #     try:
        #         if tx_data_index.isalnum() and tx_data_value.isalnum():
        #             self.uart.com.write(tx_data0 + tx_data_index.encode() + b' ' + tx_data_value.encode() + b'\n\x00')
        #             self.uart.change_paras[self.para_name.text()] = tx_data_value
        #         # print("sendParasToMCU")
        #     except:
        #         QMessageBox.critical(self, '异常', '参数发送错误')
        # else :
        #     self.para_value.setText(str(1))
