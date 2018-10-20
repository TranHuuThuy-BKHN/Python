import numpy as np
import cv2

img_1 = cv2.imread('hello.jpg')
img_2 = cv2.imread('hello1.jpg')

img_2 = img_2[0:720, 0:960]

# img_3 = cv2.addWeighted(img_1, 0.6,img_2, 0.4, 10)

img_3 = cv2.cvtColor(img_1, cv2.COLOR_BGR2HSV)

cv2.imshow('image', img_3)
cv2.waitKey(0)
cv2.destroyAllWindows()		