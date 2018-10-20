import cv2
import numpy as np

img = cv2.imread('logo.png')
img1 = cv2.imread('messi.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

row, col, channel = img.shape

img2 = img1[0:row, 0:col]
img3 = cv2.add(img, img2)
img1[0:row, 0:col] = img3

minColor = np.array([254])
maxColor = np.array([255])

mask = cv2.inRange(hsv, minColor, maxColor)


cv2.imshow('image', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()