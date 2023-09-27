import cv2
import pytesseract

from PIL import Image

from script.screen_shot import get_full_screen_gray
from util import define as DEFINE

# TODO: Set this
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

SPEED_POS = (720, 700, 770, 720)
ENDURANCE_POS = (810, 700, 860, 720)
POWER_POS = (900, 700, 950, 720)
VOLITION_POS = (990, 700, 1040, 720)
INTELLIGENCE_POS = (1070, 700, 1120, 720)

ABILITY_POS_LIST = [SPEED_POS, ENDURANCE_POS, POWER_POS, VOLITION_POS, INTELLIGENCE_POS]
ABILITY_NAME_LIST = ["SPEED", "ENDURANCE", "POWER", "VOLITION", "INTELLIGENCE"]

SCREEN = "./fullscreen.png"
SCREEN_GRAY = "./fullscreen_gray.png"
SCREEN_GRAY_SPEED = "./speed_gray.png"
NUMBER_CONFIG = "--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789"

def get_ability(pos_idx: int) -> int:
    # Check speed
    img = Image.open(DEFINE.TEMP_FILE)
    cropped = img.crop(ABILITY_POS_LIST[pos_idx])
    cropped.save(f"./{ABILITY_NAME_LIST[pos_idx]}_gray.png")

    num_img = Image.open(f"./{ABILITY_NAME_LIST[pos_idx]}_gray.png")
    num = int(pytesseract.image_to_string(num_img, lang='eng', config=NUMBER_CONFIG))
    print(f"Current {ABILITY_NAME_LIST[pos_idx]}: {num}")
    return num

def main2():
    # Check speed
    img = Image.open(SCREEN)   
    cropped = img.crop(SPEED_POS)
    cropped.save(SCREEN_GRAY_SPEED)

def total_abilities():
    sum = 0
    get_full_screen_gray()
    for i in range(len(ABILITY_POS_LIST)):
        sum += get_ability(i)

    return sum


if __name__ == "__main__":
    # for i in range(len(ABILITY_POS_LIST)):
    #     get_ability(i)
    print(total_abilities())