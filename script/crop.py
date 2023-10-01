import cv2
import time

from PIL import Image
from typing import Tuple, List

import util.define as DEFINE

from util.preprocess import thres_img2

SCREEN = "./fullscreen_gray.png"
SCREEN2 = "fullscreen_half_stamina_gray.png"

# POS = (840, 140, 1060, 170) # stamina
# POS = (950, 140, 1060, 170) # half stamina
# POS = (1070, 760, 1200, 850) # skill
# POS = (1075, 870, 1200, 950)
# POS = (1080, 870, 1110, 900)

POS = (
    DEFINE.TRAINING_UPPER_LEFT_RANGE[0],
    DEFINE.TRAINING_UPPER_LEFT_RANGE[1],
    DEFINE.TRAINING_LOWER_RIGHT_RANGE[0],
    DEFINE.TRAINING_LOWER_RIGHT_RANGE[1],
)


def crop(output: str):
    # Check speed
    img = Image.open(SCREEN2)
    cropped = img.crop(POS)
    cropped.save(output)


def crop_cv(input, pos: Tuple):
    return input[pos[1] : pos[3], pos[0] : pos[2]]


def crop_digits(img, left_thred=220, offset=-25, save=False, idx=0) -> List[int]:
    binary = thres_img2(img, left_thred, offset)

    contours, hierachy = cv2.findContours(
        binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    digits = []
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        # print(x, y, w, h)
        if w < 15 or h < 15:
            continue
        digit = binary[y : y + h, x : x + w]
        digits.append(digit)

    if save is True:
        for i, digit in enumerate(digits):
            cv2.imwrite(f"./test_data/training/{idx}_{i}_digit.png", digit)

    return digits


if __name__ == "__main__":
    # crop("./RACE_gray.png")
    crop_digits("./2_image.png")
