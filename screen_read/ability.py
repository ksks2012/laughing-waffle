import cv2
import pytesseract

from PIL import Image
from typing import List

from script.screen_shot import get_full_screen_gray
from util import define as DEFINE

# TODO: Set this
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

SCREEN = "./fullscreen.png"
SCREEN_GRAY = "./fullscreen_gray.png"
SCREEN_GRAY_SPEED = "./speed_gray.png"
NUMBER_CONFIG = "--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789"

class Ability():
    def __init__(self, pos_list: List, name_list: List, input_file=DEFINE.TEMP_FILE):
        self.pos_list = pos_list
        self.name_list = name_list
        self.input_file = input_file

    def get_ability(self, pos_idx: int) -> int:
        # Check speed
        img = Image.open(self.input_file)
        cropped = img.crop(self.pos_list[pos_idx])
        cropped.save(f"./{self.name_list[pos_idx]}_gray.png")

        num_img = Image.open(f"./{self.name_list[pos_idx]}_gray.png")
        num = int(pytesseract.image_to_string(num_img, lang='eng', config=NUMBER_CONFIG))
        print(f"Current {self.name_list[pos_idx]}: {num}")
        return num

    def total_abilities(self) -> int:
        # Sum total abilities
        sum = 0
        get_full_screen_gray()
        for i in range(len(self.pos_list)):
            sum += self.get_ability(i)

        return sum

    def get_training_abilities(self) -> List:
        # get increased in sub training page
        ability = []
        training_img = Image.open(self.input_file)
        # num = int(pytesseract.image_to_string(training_img, lang='eng', config=ability.NUMBER_CONFIG))



if __name__ == "__main__":
    ability = Ability(DEFINE.ABILITY_POS_LIST, DEFINE.ABILITY_NAME_LIST)
    # for i in range(len(DEFINE.ABILITY_POS_LIST)):
    #     ability.get_ability(i)
    print(ability.total_abilities())