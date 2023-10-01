import cv2

from script.find_contours import count_heads


def test_count_heads():
    for i in range(1, 7):
        image = cv2.imread(f"tmp_{i}_support.png")
        count = count_heads(image)
        print(count)


if __name__ == "__main__":
    test_count_heads()
