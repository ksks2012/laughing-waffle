import cv2

from script.minst import MINSTModel


def test_load_model():
    minst_model = MINSTModel()
    minst_model.load_model()
    minst_model.test_model()


def test_real_img():
    minst_model = MINSTModel()
    minst_model.load_model()
    gray_image = cv2.imread("./equalized_thres_img4.png", 0)
    # gray_image = cv2.resize(gray_image, (28, 28))
    gray_image = gray_image[1:29, 1:29]
    minst_model.recognize_number(gray_image)


if __name__ == "__main__":
    # test_load_model()
    test_real_img()
