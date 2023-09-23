import cv2

def binarization(file_name: str):
    if type(file_name) == str:
        img = cv2.imread(file_name)
    else:
        img = file_name
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   
    return img_gray

def thres(file_name: str):
    left_thred = 230
    img = cv2.imread(file_name)
    ret, img_thresh = cv2.threshold(img, left_thred, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU) 
    return img_thresh

def blur(file_name: str):
    img = cv2.imread(file_name)
    img_blur = cv2.blur(img, (3,3))
    return img_blur

def erode(file_name: str):
    img = cv2.imread(file_name)
    img_erode = cv2.erode(img, None, iterations=2)
    return img_erode

def dilate(file_name: str):
    img = cv2.imread(file_name)
    img_dilate = cv2.dilate(img, None, iterations=2)
    return img_dilate