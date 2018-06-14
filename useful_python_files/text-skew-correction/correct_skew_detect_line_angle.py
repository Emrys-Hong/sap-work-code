import cv2
import numpy as np
import math
from pytesseract import image_to_string

def skew_angle(img):
    edges = cv2.Canny(img,50,150,apertureSize = 3)

    lines = cv2.HoughLines(edges,1,np.pi/180,200)

    angle_sum=0;count=0
    for coordinates in lines:
        for rho,theta in coordinates:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            
            angle = math.atan2((y2-y1),(x2-x1))/math.pi*180
            if  60 < angle < 90:
                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
                angle_sum += angle
                count += 1
    angle_ave = angle_sum / count
    return angle_ave 

def deskew(image, angle):
    # image = cv2.bitwise_not(image)
    non_zero_pixels = cv2.findNonZero(image)
    center, wh, theta = cv2.minAreaRect(non_zero_pixels)

    root_mat = cv2.getRotationMatrix2D(center, angle, 1)
    rows, cols = image.shape
    rotated = cv2.warpAffine(image, root_mat, (cols, rows), flags=cv2.INTER_CUBIC)

    return cv2.getRectSubPix(rotated, (cols, rows), center)

def img2txt(address):
    img = cv2.imread(address, cv2.IMREAD_GRAYSCALE)
    angle = skew_angle(img)
    deskewed_image = deskew(img.copy(),angle)
    cv2.imwrite('/Users/i351707/Desktop/image.png',deskewed_image)
    txt = image_to_string(deskewed_image,lang='tha+eng')
    return txt

print(img2txt('/Users/i351707/Desktop/test5.png'))