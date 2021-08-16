"""
Requires: numpy, opencv-python
"""
from datetime import datetime

import cv2 as cv
import transparentwindow as tw


def callback(key: int) -> None:
    title = datetime.now().strftime("%H:%M:%S.%f")
    img = tw.capture_as_opencv_img(*tw.get_tpwin_xywh())
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()


tw.show_tpwin(callback=callback)
