import cv2
import numpy as np

frame = cv2.imread('/Users/i351707/Desktop/images/137.jpeg')
 

blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)



_, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# for contour in contours:
#     area = cv2.contourArea(contour)

#     if area > 5000:
#         cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

cnts = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
	# if our approximated contour has four points, then we
	# can assume that we have found our screen
	if len(approx) <= 10 and cv2.contourArea(c) > 5000:
		screenCnt = approx
		break
cv2.drawContours(frame, [screenCnt], -1, (0, 255, 0), 2)
 

cv2.imwrite('/Users/i351707/Desktop/houghlines3.jpg',frame)