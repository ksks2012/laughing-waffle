import cv2
import numpy as np

from util.preprocess import thres_img2


def count_heads(image):
    """Count the number of heads in an image.

    Args:
        image: The image containing the heads.

    Returns:
        The number of heads in the image.
    """

    # Convert the image to grayscale.
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = thres_img2(gray_image)

    # Apply Canny edge detection to extract the edges in the image.
    edges = cv2.Canny(gray_image, 100, 200)
    # cv2.imwrite("tmp_1_support_canny.png", edges)

    # Apply morphological operations to remove noise from the image.
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
    # cv2.imwrite("tmp_1_support_edges.png", edges)

    # Find the contours in the image using the findContours() function.
    contours, hierarchy = cv2.findContours(
        edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    # Count the number of heads in the image.
    count = 0

    for contour in contours:
        # Calculate the area of the contour.
        area = cv2.contourArea(contour)
        # If the area of the contour is greater than a certain value, then it is a head.
        if area > 4000:
            # (x, y, w, h) = cv2.boundingRect(contour)
            # digit = edges[y : y + h, x : x + w]
            # cv2.imwrite(f"./{area}.png", digit)
            count += 1

    return count


if __name__ == "__main__":
    image = cv2.imread("tmp_1_support.png")

    # Count the number of heads in the image.
    count = count_heads(image)

    # Print the number of heads in the image.
    print(count)
