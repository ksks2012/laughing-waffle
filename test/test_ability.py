import cv2
import pytesseract

from PIL import Image

import util.define as DEFINE

from screen_read.ability import Ability

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

NUMBER_CONFIG_TEMPLATE = """--psm {PSM_CONFIG} --oem {OEM_CONFIG} -c tessedit_char_whitelist=0123456789"""
MAX_OEM_CONFIG = 3
MAX_PSM_CONFIG = 13

PREFIX_FOLDER = "data/test/ability/"

TEST_IMAGE = "./test_training_ability.png"
# TEST_IMAGE = "./fullscreen_1696012088_gray.png"

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
                config = NUMBER_CONFIG_TEMPLATE.format(PSM_CONFIG=str(psm), OEM_CONFIG=str(oem))
                print(f"Current {config=}")
                num = int(pytesseract.image_to_string(num_img, lang='eng', config=config))
                print(f"Current {DEFINE.ABILITY_POS_LIST[pos_idx]}: {num}")
            except:
                print("error")

def test_get_training_abilities():
    ability = Ability(DEFINE.TRAINING_ABILITY_POS_LIST, DEFINE.TRAINING_ABILITY_NAME_LIST, TEST_IMAGE)
    print(ability.get_training_abilities())

def test_abilities_with_diff_preprocess():
    cur = []
    for i in range(200, 255):
        for j in range(-50, 50):
            img = cv2.imread(f"./thres2_test/{i}_{j}.png", 0)
            NUMBER_CONFIG = "--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789"
            try:          
                num = int(pytesseract.image_to_string(img, lang='eng', config=NUMBER_CONFIG))
            except:
                pass
            else:
                if num == 2:
                    cur.append([i, j])
            # print(num)
    print(cur)

RESULTS = [[200, -27], [200, -25], [200, -24], [200, -1], [200, 1], [200, 16], [200, 20], [201, -25], [201, -24], [201, 1], [201, 15], [201, 16], [202, -25], [202, -24], [202, -1], [202, 0], [202, 1], [202, 15], [203, -24], [203, 1], [203, 15], [203, 20], [204, -25], [204, 1], [204, 20], [205, -29], [205, -25], [205, -24], [205, 20], [206, -25], [206, -24], [206, -1], [206, 1], [206, 20], [207, -24], [207, 0], [207, 1], [207, 20], [208, -25], [208, -24], [208, 1], [209, -25], [209, -24], [209, -1], [209, 1], [209, 16], [210, -25], [210, -24], [210, -1], [210, 1], [210, 16], [211, -25], [211, -24], [211, 1], [212, -25], [212, -24], [212, -1], [212, 1], [213, -25], [213, -24], [213, 1], [213, 15], [213, 20], [214, -29], [214, -25], [214, -24], [214, -1], [214, 15], [215, -25], [215, -24], [216, -29], [216, -25], [216, -24], [216, -1], [216, 0], [216, 20], [217, -27], [217, -25], [217, -24], [217, -1], [217, 1], [218, -25], [218, -24], [218, -1], [218, 20], [219, -25], [219, -1], [219, 1], [219, 15], [220, -24], [220, -1], [220, 1], [221, -1], [221, 0], [221, 20], [222, -24], [222, -1], [222, 1], [223, -25], [223, -1], [223, 20], [224, -25], [224, -24], [225, -25], [225, -24], [225, -1], [225, 1], [226, -25], [226, -24], [226, -1], [226, 1], [227, -24], [227, 1], [228, -24], [228, -1], [228, 0], [228, 1], [228, 20], [229, -25], [229, -24], [229, -1], [229, 1], [230, -25], [230, -24], [230, -1], [230, 1], [231, -25], [231, -24], [231, -1], [231, 1], [232, -24], [233, -29], [233, -25], [233, -24], [233, -1], [233, 1], [233, 20], [234, -25], [234, -1], [234, 1], [235, -24], [235, 1], [235, 20], [236, -24], [236, 20], [237, -24], [237, -1], [237, 1], [238, -25], [238, -24], [238, -1], [238, 16], [239, -24], [239, -1], [239, 1], [239, 16], [240, -24], [240, 1], [240, 16], [241, -25], [241, -24], [241, 1], [242, -24], [242, -1], [242, 1], [242, 20], [243, -24], [243, -1], [243, 1], [243, 16], [243, 20], [244, -25], [244, 20], [245, -24], [245, -1], [245, 1], [245, 16], [245, 20], [246, -29], [246, -24], [246, -1], [246, 20], [247, -25], [247, -24], [247, -1], [248, -24], [248, -1], [248, 20], [249, -24], [249, -1], [249, 20], [250, -24], [250, 17], [250, 18], [250, 20], [251, -24], [251, -1], [251, 18], [251, 20], [252, -24], [252, -1], [252, 18], [252, 20], [253, -25], [253, -24], [253, -1], [253, 7], [253, 18], [253, 20], [254, -24], [254, -1], [254, 16], [254, 20]]

def test_preprocess():
    from util.preprocess import blur_img, thres_img, thres_img2, thres_img3, thres_img4
    img = cv2.imread("./equalized.png", 0)
    # img_blur = blur_img(img)
    # cv2.imwrite(f"./equalized_blur.png", img_blur)
    num_img = thres_img4(img)
    cv2.imwrite(f"./equalized_thres_img4.png", num_img)
    NUMBER_CONFIG = "--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789"          
    num = int(pytesseract.image_to_string(num_img, lang='eng', config=NUMBER_CONFIG))
    print(num)

if __name__ == "__main__":
    # test_abilities()
    # test_total_abilities()
    # test_get_training_abilities()

    # img = cv2.imread("./MORPH_TOPHAT.png")
    test_abilities_with_diff_preprocess()