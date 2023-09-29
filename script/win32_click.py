import win32con
import win32api
import win32gui

import random
import time

from typing import Tuple


import util.define as DEFINE

from util.utils import randon_point

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

    def mouse_move(self, pos: Tuple[int, int], mov: Tuple[int, int]):
        offset_pos = (pos[0] - DEFINE.OFFEST[0], pos[1] - DEFINE.OFFEST[1])
        lParam = win32api.MAKELONG(*offset_pos)
        # Press the left button
        win32api.PostMessage(self.target_hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        time.sleep(1)
        # win32api.mouse_event(win32con.MOUSEEVENTF_MOVE , mov[0], mov[1]) 
        win32api.SetCursorPos((pos[0] + mov[0], pos[1] + mov[1]))
        time.sleep(1)
        # Release the left button.
        win32api.PostMessage(self.target_hwnd, win32con.WM_LBUTTONUP, None, lParam)

    def tap(self, pos: Tuple[int, int]):
        # Mouse clicking coordinates
        pos = (pos[0] - DEFINE.OFFEST[0], pos[1] - DEFINE.OFFEST[1])
        lParam = win32api.MAKELONG(*pos)
        # Press the left button
        win32api.PostMessage(self.target_hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        # Release the left button.
        win32api.PostMessage(self.target_hwnd, win32con.WM_LBUTTONUP, None, lParam)

    def random_tap(self, upper_left: Tuple[int, int], lower_right: Tuple[int, int]):
        # Randomly tap a position within the upper left to lower right range
        rand_x, rand_y = randon_point(upper_left, lower_right)
        print(f"random_tap: {upper_left=} {lower_right=} {rand_x=} {rand_y=}")
        self.tap((rand_x, rand_y))

# x = 200
# y = 975

# x = 980
# x = 200
x = 340
y = 795

if __name__ == "__main__":
    win32 = WIN32_API()
    # while True:
    #     time.sleep(1)
    #     win32.tap((x, y))
    for i in range(len(DEFINE.TRAINING_ABILITY_UPPER_LEFT_RANGE)):
        time.sleep(3)
        win32.mouse_move(randon_point(DEFINE.TRAINING_ABILITY_UPPER_LEFT_RANGE[i], DEFINE.TRAINING_ABILITY_LOWER_RIGHT_RANGE[i]), (0, -500))