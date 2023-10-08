import cv2
import time

from typing import Tuple
from PIL import Image

from screen_read import match
from script import screen_shot
from util import define as DEFINE

SKILL_POS = (1070, 760, 1200, 850)

SCREEN_GRAY = "./fullscreen_gray.png"


def check_traning_main_page(test_mode=False, save_mode=False) -> bool:
    if test_mode:
        return match.check_file_match(DEFINE.SKILL_GRAY_FILE)
    else:
        img = screen_shot.get_full_screen_gray(save_mode)
        return match.check_file_match(DEFINE.SKILL_GRAY_FILE, DEFINE.TEMP_FILE)

# TODO:
def check_training_sub_page():
    pass

def check_state_pre_race(test_mode=False, save_mode=False) -> bool:
    # TODO: check open race
    if test_mode:
        return match.check_file_match(DEFINE.LOCK_GRAY_FILE, f"./{DEFINE.DATA_FOLDER}/page/RACE_gray.png")
    else:
        img = screen_shot.get_race_gray(save_mode)
        return match.check_file_match(DEFINE.LOCK_GRAY_FILE, DEFINE.TEMP_FILE)


if __name__ == "__main__":
    # img = Image.open(SCREEN_GRAY)   
    # cropped = img.crop(SKILL_POS)
    # cropped.save(f"./SKILL_gray.png")

    # check_file_match(f"./{DEFINE.DATA_FOLDER}/test_not_match.png")
    # check_state_pre_race()

    current_state = DEFINE.STATE_UNKNOWN
    time.sleep(5)

    if check_traning_main_page(save_mode=True) is True:
        if check_state_pre_race(save_mode=True) is True:
            current_state = DEFINE.STATE_PRE_RACE

    print("state: ", current_state)