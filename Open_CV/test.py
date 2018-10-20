import cv2
import numpy as np

img = cv2.imread('logo.png', cv2.IMREAD_COLOR)
rows, cols, channels = img.shape

img1 = cv2.imread('hello.jpg')
roi = img1[0:rows, 0:cols]

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY)

res = cv2.bitwise_and(img, img, mask = mask)

mask_inv = cv2.bitwise_not(mask)
roi = cv2.bitwise_and(roi, roi, mask = mask_inv)


final = cv2.add(roi, res)

img1[0:rows, 0:cols] = final
cv2.imshow('roi', roi)
cv2.imshow('image', res)
cv2.imshow('final', final)
cv2.imshow('hello', img1)
cv2.imwrite('hello2.jpg', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()