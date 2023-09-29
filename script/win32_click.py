import win32con
import win32api
import win32gui

import random
import time

from typing import Tuple

class WIN32_API():
    def __init__(self):
        # List all the windows' HWNDs and call enumHandler to handle them.
        self.window_name = 'BlueStacks App'
        self.target_hwnd = None

        win32gui.EnumWindows(self.enumHandler, None)

    def enumHandler(self, hwnd, _):
        # Use HWND to get the name of the current window.
        windowText = win32gui.GetWindowText(hwnd)
        # Determine if it is our target window
        if self.window_name in windowText:
        # Get Sub-Window
            hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
            global target_hwnd
            self.target_hwnd = hwndChild

    def tap(self, pos: Tuple[int, int]):
        # Mouse clicking coordinates
        lParam = win32api.MAKELONG(*pos)
        # Press the left button
        win32api.PostMessage(self.target_hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        # Release the left button.
        win32api.PostMessage(self.target_hwnd, win32con.WM_LBUTTONUP, None, lParam)

    def random_tap(self, upper_left: Tuple[int, int], lower_right: Tuple[int, int]):
        # Randomly tap a position within the upper left to lower right range
        rand_x = random.randint(upper_left[0], lower_right[0])
        rand_y = random.randint(upper_left[1], lower_right[1])
        print(f"random_tap: {upper_left=} {lower_right=} {rand_x=} {rand_y=}")


x = 200
y = 975

if __name__ == "__main__":
    win32 = WIN32_API()
    while True:
        time.sleep(1)
        win32.tap((x, y))
    