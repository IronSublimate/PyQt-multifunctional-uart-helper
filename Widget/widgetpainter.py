from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox
from PyQt5.QtCore import Qt, QPointF, QPoint, QLineF
from PyQt5.QtGui import QPainter, QPaintEvent, QPixmap, QMouseEvent, QPen, QBrush
from PyQt5 import QtGui


# from Call_Ui_SerialPort import MyMainWindow


class WidgetPainter(QWidget):
    def __init__(self, parent=None):
        super(WidgetPainter, self).__init__(parent)
        # self.painter3 = QPainter(self)
        self.qpix = QPixmap()
        # self.parentUi = None
        self.imgWidth = 80
        self.imgHeight = 60
        self.label_position = None  #: QLabel
        self.label_pause = None  #: QLabel
        self.grid_points = []
        self.enable_grid = False
        self.pause = False
        self.enable_extra_14_bytes = False
        self.extra_bytes_len = 0
        self.extra_data = None  # tuple
        # [0]中心点的行数
        # [1]中心点的列数
        # [2]列左极限
        # [3]列右极限
        # [4]控制中心的列数

    def set_img_height_width(self, height: int, width: int):
        self.imgWidth = width
        self.imgHeight = height
        self.calculate_grid_points()

    def setPixmap(self, pix: QPixmap):
        if not self.pause:
            self.qpix = pix
            # self.draw_pixmap()
            self.repaint()

    def calculate_grid_points(self):
        x = 0.0
        y = 0.0
        pix_width = self.width() / self.imgWidth
        pix_height = self.height() / self.imgHeight
        self.grid_points.clear()
        while (x <= self.width()):
            self.grid_points.append(QLineF(x, 0, x, self.height()))
            x += pix_width
        while (y <= self.height()):
            self.grid_points.append(QLineF(0, y, self.width(), y))
            y += pix_height

    def paintEvent(self, a0: QPaintEvent):
        # print("paint")
        painter = QPainter(self)

        # painter.begin(self)
        painter.drawPixmap(0, 0, self.width(), self.height(), self.qpix)
        if self.enable_extra_14_bytes and self.extra_data:
            pix_width = self.width() / self.imgWidth
            pix_height = self.height() / self.imgHeight
            # painter.setPen(QPen(Qt.red, -14))
            painter.setBrush(QBrush(Qt.red))
            painter.drawEllipse(self.extra_data[1] * pix_width, self.extra_data[0] * pix_height, pix_width, pix_height)
            painter.drawEllipse(self.extra_data[2] * pix_width, self.extra_data[0] * pix_height, pix_width, pix_height)
            painter.drawEllipse(self.extra_data[3] * pix_width, self.extra_data[0] * pix_height, pix_width, pix_height)
            painter.drawEllipse(self.extra_data[4] * pix_width, self.extra_data[0] * pix_height, pix_width, pix_height)

        if self.enable_grid:
            painter.setPen(Qt.darkBlue)
            painter.drawLines(self.grid_points)
        # painter.end()

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        # print("resize")
        if self.enable_grid:
            self.calculate_grid_points()

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        # print("mousemove")
        # self.setStatusTip("123")
        x = int(a0.x() / self.width() * self.imgWidth)
        y = int(a0.y() / self.height() * self.imgHeight)
        s = "鼠标位置 x:{:4d},y:{:4d}".format(x, y)
        self.label_position.setText(s)

    def keyPressEvent(self, a0: QtGui.QKeyEvent):
        if a0.key() == Qt.Key_P:
            # print("Key press")
            self.pause = not self.pause
            if self.pause:
                self.label_pause.setText("已暂停")
            else:
                self.label_pause.clear()
