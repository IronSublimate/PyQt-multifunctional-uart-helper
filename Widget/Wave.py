from PyQt5.QtChart import QChartView, QChart, QLineSeries


class DynamicWaveView(QChartView):
    def __init__(self, parent=None):
        super(DynamicWaveView, self).__init__(parent)
