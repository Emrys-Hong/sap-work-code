import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/i351707/Desktop/printed_images_with_no_boarder/59.png', cv2.IMREAD_GRAYSCALE)

def compute_skew(image):
    # image = cv2.bitwise_not(image)
    height, width = image.shape

    edges = cv2.Canny(image, 150, 200, 3, 5)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=width / 2.0, maxLineGap=20)
    angle = 0.0
    number_of_line = lines.size
    for x1, y1, x2, y2 in lines[0]:
        if x1 != x2:
            angle += np.arctan(y2 - y1 / x2 - x1)
    return angle / number_of_line, angle, number_of_line


def deskew(image, angle):
    # image = cv2.bitwise_not(image)
    non_zero_pixels = cv2.findNonZero(image)
    center, wh, theta = cv2.minAreaRect(non_zero_pixels)

    root_mat = cv2.getRotationMatrix2D(center, angle, 1)
    rows, cols = image.shape
    rotated = cv2.warpAffine(image, root_mat, (cols, rows), flags=cv2.INTER_CUBIC)

    return cv2.getRectSubPix(rotated, (cols, rows), center)

deskewed_image = deskew(img.copy(), -6)

cv2.imshow('original', img)
cv2.imshow('deskew', deskewed_image)
cv2.waitKey(0)