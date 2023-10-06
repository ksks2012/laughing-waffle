import cv2
import numpy as np
import traceback

import util.define as DEFINE

from matplotlib import pyplot as plt

SCREEN_GRAY = "./fullscreen_gray.png"
SKILL_GRAY = f"./{DEFINE.DATA_FOLDER}/page/SKILL_gray.png"

# All the 6 methods for comparison in a list
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#  'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

METHODS = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF_NORMED']

THRESHOLD = [100000000.0,]

def target_match(img, template):
    '''
        Description: Use multiple method to match
        imge: base
        template: target
    '''
    # w, h = template.shape[::-1]
    
    matched = 0
    try:
        for idx, meth in enumerate(METHODS):
            # img = img2.copy()
            method = eval(meth)
            # Apply template Matching
            res = cv2.matchTemplate(img, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val > DEFINE.MATCHED_THRESHOLD:
                matched += 1
            print(f"{METHODS[idx]} ", min_val, max_val, min_loc, max_loc)
            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
                # bottom_right = (top_left[0] + w, top_left[1] + h)
            # cv2.rectangle(img,top_left, bottom_right, 255, 2)
            # plt.subplot(121),plt.imshow(res,cmap = 'gray')
            # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            # plt.subplot(122),plt.imshow(img,cmap = 'gray')
            # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            # plt.suptitle(meth)
            # plt.show()
    except Exception as e:
        traceback.print_exc()
        print(f"Error: {e}")

    return matched == 3

def check_file_match(filename: str, base=SCREEN_GRAY):
    img1 = cv2.imread(base)
    img2 = cv2.imread(filename)
    checked = target_match(img1, img2)
    print(f"{filename} is matched: {checked}")
    return checked

def check_match(filename: str, base):
    img = cv2.imread(filename)
    checked = target_match(img, base)
    print(f"is matched: {checked}")
    return checked

if __name__ == "__main__":
    img = cv2.imread(SCREEN_GRAY, cv2.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"

    img2 = img.copy()
    
    # template = cv2.imread(f"./{DEFINE.DATA_FOLDER}/test_not_match.png", cv2.IMREAD_GRAYSCALE)
    template = cv2.imread(SKILL_GRAY, cv2.IMREAD_GRAYSCALE)
    assert template is not None, "file could not be read, check with os.path.exists()"


    
    print(target_match(img, template))
