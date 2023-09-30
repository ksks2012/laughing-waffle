import cv2

def binarization_file(file_name: str):
    if type(file_name) == str:
        img = cv2.imread(file_name)
    else:
        img = file_name
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   
    return img_gray

def thres_file(file_name: str):
    left_thred = 230
    img = cv2.imread(file_name)
    # ret, img_thresh = cv2.threshold(img, left_thred, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    ret, img_thresh = cv2.threshold(img, left_thred, 255, cv2.THRESH_BINARY_INV)  
    return img_thresh

def blur_file(file_name: str):
    img = cv2.imread(file_name)
    img_blur = cv2.blur(img, (3,3))
    return img_blur

def erode_file(file_name: str):
    img = cv2.imread(file_name)
    img_erode = cv2.erode(img, None, iterations=2)
    return img_erode

def dilate_file(file_name: str):
    img = cv2.imread(file_name)
    img_dilate = cv2.dilate(img, None, iterations=2)
    return img_dilate

def binarization_img(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   
    return img_gray

def thres_img(img, left_thred = 230):
    # ret, img_thresh = cv2.threshold(img, left_thred, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    ret, img_thresh = cv2.threshold(img, left_thred, 255, cv2.THRESH_BINARY_INV)  
    return img_thresh

def thres_img2(img, left_thred = 255, offset = 2):
    return cv2.adaptiveThreshold(img, left_thred, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, offset)

def thres_img3(img):
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

def thres_img4(img):
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, -10)

def  blur_img(img):
    img_blur = cv2.blur(img, (3,3))
    return img_blur

def erode_img(img, itr=2):
    img_erode = cv2.erode(img, None, iterations=itr)
    return img_erode

def dilate_img(img, itr=2):
    img_dilate = cv2.dilate(img, None, iterations=itr)
    return img_dilate