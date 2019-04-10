from PyQt5.QtWidgets import QWidget, QMessageBox
from GUI.Ui_PataList import Ui_PataList
from parameter import parameterList, Parameter
from PyQt5.QtSerialPort import QSerialPort


class Widget_ParaItem(QWidget, Ui_PataList):
    def __init__(self, paras: Parameter, _index: str, _com: QSerialPort, parent=None):
        super(Widget_ParaItem, self).__init__(parent)
        super(QWidget, self).__init__()
        # super(Ui_PataList).__init__()
        self.setupUi(self)
        self.paras = paras
        self.index = _index
        self.para_name.setText(paras.name)
        self.para_value.setText(str(paras.value))
        self.com = _com

        self.CreateSignalSlot()

    def CreateSignalSlot(self):
        self.send_to_MCU.clicked.connect(self.sendParasToMCU)

    def sendParasToMCU(self):
        if self.com.isOpen():
            self.paras.value = self.para_value.text()
            # print(self.index)
            tx_data0 = b'\xb3'
            tx_data_index = self.index
            tx_data_value = self.paras.value
            try:
                self.com.write(tx_data0 + tx_data_index + b' ' + tx_data_value + b'\n')
                # print("sendParasToMCU")
            except:
                QMessageBox.critical(self, '异常', '参数发送错误')
        # else :
        #     self.para_value.setText(str(1))
