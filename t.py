# Import packages 
import cv2
import numpy as np

#Create MSER object
mser = cv2.MSER_create()

#Your image path i-e receipt path
img = cv2.imread('1.jpeg')

#Convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

vis = img.copy()

#detect regions in gray scale image
regions, _ = mser.detectRegions(gray)

hulls = [cv2.convexHull(p) for p in regions]

cv2.polylines(vis, hulls, 1, (0, 255, 0))
cv2.imshow('img', vis)

cv2.waitKey(0)

#####################################################

mask = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8)

for contour in hulls:

    cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)
    print (contour)
#this is used to find only text regions, remaining are ignored
text_only = cv2.bitwise_and(img, img, mask=mask)
#cv2.imwrite("2.jpeg", text_only)
cv2.imshow("text only", mask)

cv2.waitKey(0)