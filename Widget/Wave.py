import random

from PyQt5.QtChart import QChartView, QChart, QLineSeries, QSplineSeries, QValueAxis
from PyQt5.QtCore import QTime, Qt
from PyQt5.QtGui import QPainter, QColor


class DynamicWaveView(QChartView):
    def __init__(self, parent=None):
        super(DynamicWaveView, self).__init__(parent)
        self.time = QTime()
        self.x = 0  # 横坐标值
        self.ymax = 100  # 纵坐标最大值
        self.ymin = 0  # 纵坐标最小值
        self.lines = dict()
        self.chart().legend().show()

        # self.chart().addSeries(self.line)
        # self.setChart(QChart())
        self.chart().setTitle("波形")
        # self.chart().createDefaultAxes()
        self.ax = QValueAxis()
        self.ax.setTitleText("t")
        self.ax.setRange(0, 10)

        # self.ay = self.chart.axisY()
        self.ay = QValueAxis()
        self.ay.setRange(-1, 1)
        self.ay.setTitleText("value")

        self.chart().addAxis(self.ax, Qt.AlignBottom)
        self.chart().addAxis(self.ay, Qt.AlignLeft)
        self.chart().setAnimationOptions(QChart.SeriesAnimations) #动画
        self.setRenderHint(QPainter.Antialiasing)  # 消除混叠现象，消除走样，图形保真;

    def add_new_data(self, data: dict):
        self.x += self.time.msec()
        self.time.start()
        for key in data:
            if key in self.lines:
                self.lines[key].append(self.x, data[key])
            else:
                ls = QSplineSeries(self)
                ls.append(self.x, data[key])
                ls.setColor(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                ls.setName(key)
                self.chart().addSeries(ls)
                self.chart().setAxisX(self.ax, ls)
                self.chart().setAxisX(self.ay, ls)
                self.lines[key] = ls
