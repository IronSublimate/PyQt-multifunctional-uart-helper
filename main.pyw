#!/usr/bin/env python3
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QPixmap
from GUI.Ui_Loading import Ui_Form_loading
# import res_rc
import sys


# sys.path.append("GUI")

class Widget_loading(QSplashScreen, Ui_Form_loading):
    def __init__(self, pic: QPixmap):
        super(Widget_loading, self).__init__(pic)
        self.setupUi(self)


def main():
    # import PyQt5.QtWebEngineWidgets
    app = QApplication(sys.argv)
    img = QPixmap(":/img/loading.jpg")
    # QPixmap()
    uiSplash = Widget_loading(img)
    uiSplash.show()
    from src import Smartcar_SerialPort
    myWin = Smartcar_SerialPort.MyMainWindow()
    # myWin.setWindowTitle("PyQt智能车串口调试助手")
    # myWin.test()
    myWin.show()
    uiSplash.progressBar.setValue(100)
    uiSplash.finish(myWin)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
