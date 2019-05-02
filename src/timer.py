from PyQt5.QtCore import QTimer


class Timer(QTimer):
    def __init__(self, parent=None):
        super(Timer, self).__init__(parent)


__timer = None


def instance():
    global __timer
    if __timer is None:
        __timer = Timer()
    return __timer
