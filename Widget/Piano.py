from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from src.keyMap import keyMap


class PianoView(QWidget):
    send_msg = pyqtSignal(bytes)
    def __init__(self, parent=None):
        super(PianoView, self).__init__(parent)
        self.transpose = 0
        self.pressedKeySet = set()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return
        # if self.tabWidget_other.currentIndex() != 3 or not self.uart.com.isOpen():
        k = event.key()
        # print(k)
        # print("keyPress")
        self.pressedKeySet.add(k)
        self.transpose = self.comboBox_transpose.currentIndex() - 3

        try:
            frenq = int(261.62557 * (2 ** ((keyMap[k] + self.transpose) / 12)))
            print(frenq)
        except KeyError:
            pass
        else:
            # self.com.write(frenq.to_bytes(1, "little", signed=False))
            self.send_msg.emit(b'\xb9' + str(frenq).encode(errors='ignore') + b'\n\x00')

    def keyReleaseEvent(self, event):
        # print("keyRelease")
        if event.isAutoRepeat():
            return
        # not self.tabWidget_other.hasFocus() or
        # if self.tabWidget_other.currentIndex() != 3 or not self.uart.com.isOpen():

        k = event.key()
        # print("keyRelease")
        self.pressedKeySet.discard(k)
        if len(self.pressedKeySet) == 0:
            self.send_msg.emit(b'\xb9' + b'0' + b'\n\x00')
