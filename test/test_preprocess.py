import cv2

from util.preprocess import binarization_file, erode_img, dilate_img, thres_img, thres_img2

TEST_FILE = "./fullscreen_1696012088_gray.png"
OUTPUT_FILE = "./test_training_ability.png"

def test_binarization(file_name: str):
    img = binarization_file(TEST_FILE)
    cv2.imwrite(OUTPUT_FILE, img)

def test_equalizeHist():
    gray_image = cv2.imread("./image.png", 0)
    equalized_image = cv2.equalizeHist(gray_image)
    cv2.imwrite(f"./equalized.png", equalized_image)
    # cv2.imshow('oxxostudio', equalized_image)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def test_thres_img_left():
    gray_image = cv2.imread("./image.png", 0)
    for i in range(255):
        thres = thres_img(gray_image, i)
        cv2.imwrite(f"./thres_test/{i}.png", thres)

def test_thres2_img_left():
    gray_image = cv2.imread("./image.png", 0)
    for i in range(200, 255):
        for j in range(-50, 50):
            thres = thres_img2(gray_image, i, j)
            cv2.imwrite(f"./thres2_test/{i}_{j}.png", thres)

def test_erode_img():
    gray_image = cv2.imread("./thres2.png", 0)
    erode = erode_img(gray_image, 1)
    cv2.imwrite(f"./erode.png", erode)

def test_dilate_img():
    gray_image = cv2.imread("./thres2.png", 0)
    dilate = dilate_img(gray_image, 1)
    cv2.imwrite(f"./dilate.png", dilate)

if __name__ == "__main__":
    # test_binarization(TEST_FILE)
    # test_equalizeHist()
    # test_erode_img()
    # test_dilate_img()
    # test_thres_img_left()
    test_thres2_img_left()