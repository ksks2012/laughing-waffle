import cv2

from script.crop import crop_digits


def test_crop_digits():
    # tmp = 0
    for i in range(2, 11):
        input = f"./test_data/training/{i}_image.png"
        input = cv2.imread(input, 0)
        crop_digits(input, save=True, idx=i)

    # print(tmp)


def test_crop_digits_params():
    result = []
    img_list = list(range(1, 12))

    for i in range(2, 11):
        img_list[i] = cv2.imread(f"./test_data/training/{i}_image.png", 0)

    max_tmp = 0
    for i in range(200, 255):
        for j in range(-50, 50):
            tmp = 0
            for k in range(2, 11):
                tmp += len(crop_digits(img_list[k], i, j))

            print(tmp)
            max_tmp = max(max_tmp, tmp)
            if tmp == 15:
                result.append([i, j])


    print(result, max_tmp)

if __name__ == "__main__":
    test_crop_digits()
    # test_crop_digits_params()
