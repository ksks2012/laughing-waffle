import time

import util.define as DEFINE

from script.win32_click import WIN32_API

class Training():
    def __init__(self) -> None:
        self.win32 = WIN32_API()

    def click_training(self):
        self.win32.random_tap(DEFINE.TRAINING_UPPER_LEFT_RANGE, DEFINE.TRAINING_LOWER_RIGHT_RANGE)

    def click_training_back(self):
        self.win32.random_tap(DEFINE.TRAINING_BACK_LEFT_RANGE, DEFINE.TRAINING_BACK_RIGHT_RANGE)


if __name__ == "__main__":
    training = Training()
    time.sleep(5)
    training.click_training()
    time.sleep(5)
    training.click_training_back()
    