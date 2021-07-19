"""
Space-Key: capture and show a screen image
ESC-Key: exit

to use this, please install 'numpy' and 'opencv-python'
"""
import time
import multiprocessing

import cv2
from transparentwindow import (
    capture_transparentwindow,
    SetProcessDpiAwarenessContext,
    show,
)


def sub_process(pressed_key: multiprocessing.Value) -> None:
    def set_pressed_key(key: int) -> None:
        pressed_key.value = key

    SetProcessDpiAwarenessContext()
    show(callback=set_pressed_key)
    pressed_key.value = 27  # ESC-Key


def monitor_pressed_key(pressed_key: multiprocessing.Value) -> None:
    SetProcessDpiAwarenessContext()
    while True:
        if pressed_key.value == 32:  # Space-Key
            img = capture_transparentwindow()
            cv2.imshow("img", img)
            cv2.waitKey(0)
        if pressed_key.value == 27:  # ESC-Key
            break
        pressed_key.value = 0
        time.sleep(0.1)


if __name__ == "__main__":
    print(__doc__)
    pressed_key = multiprocessing.Value("i", 0)
    sub = multiprocessing.Process(target=sub_process, args=(pressed_key,), daemon=True)
    sub.start()
    monitor_pressed_key(pressed_key)
