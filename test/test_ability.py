import pytesseract

from PIL import Image

import util.define as DEFINE

from screen_read.ability import Ability

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

NUMBER_CONFIG = """--psm {PSM_CONFIG} --oem {OEM_CONFIG} -c tessedit_char_whitelist=0123456789"""
MAX_OEM_CONFIG = 3
MAX_PSM_CONFIG = 13

PREFIX_FOLDER = "data/test/ability/"

TEST_IMAGE = "./fullscreen_1696012088_gray.png"

def test_abilities():
    ability = Ability(DEFINE.ABILITY_POS_LIST, DEFINE.ABILITY_NAME_LIST)
    for i in range(len(DEFINE.ABILITY_POS_LIST)):
        ability.get_ability(i)

def test_total_abilities():
    ability = Ability(DEFINE.ABILITY_POS_LIST, DEFINE.ABILITY_NAME_LIST)
    print(f"{ability.total_abilities()}")

# FIXME:
def test_abilities_config(pos_idx: int):
    num_img = Image.open(f"./{PREFIX_FOLDER}/{DEFINE.ABILITY_POS_LIST[pos_idx]}_gray.png")
    for oem in range(0, MAX_OEM_CONFIG):
        for psm in range(0, MAX_PSM_CONFIG):
            try:
                config = NUMBER_CONFIG.format(PSM_CONFIG=str(psm), OEM_CONFIG=str(oem))
                print(f"Current {config=}")
                num = int(pytesseract.image_to_string(num_img, lang='eng', config=config))
                print(f"Current {DEFINE.ABILITY_POS_LIST[pos_idx]}: {num}")
            except:
                print("error")

def test_get_training_abilities():
    return 

if __name__ == "__main__":
    # for i in range(len(DEFINE.ABILITY_POS_LIST)):
    #     test_abilities_config(i)
    test_abilities()
    test_total_abilities()