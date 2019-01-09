import numpy as np
import cv2

_win_name = "cvWin"
_has_init = False


def init():
    global _has_init
    if not _has_init:
        cv2.namedWindow(_win_name, cv2.WINDOW_FREERATIO)
        _has_init = True


def close():
    cv2.destroyAllWindows()


def process(_img_bytes: bytes, height: int, width: int):
    img: np.array = np.frombuffer(_img_bytes, dtype=np.uint8).reshape(height, width)
    cv2.namedWindow(_win_name, cv2.WINDOW_FREERATIO)
    cv2.imshow(_win_name, img)
    cv2.waitKey(1)
