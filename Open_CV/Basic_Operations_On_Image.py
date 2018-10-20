import cv2
import numpy as np

img = np.zeros((300, 300, 3), np.uint8)
# cv2.namedWindow('image')
		
img_2 = cv2.imread('hello.jpg')

img_3 = cv2.imread('messi.jpg')



print(img_3.shape)

print(img_3.size)

print(img_3.dtype)

img_2 = img_3[100:200, 100:150]
img_3 = img_3[200:400, 200:300]
b, g, r = cv2.split(img_3)

b1, g1, r1 = cv2.split(img_2)

# img_3 = cv2.merge((g, b, r1))
cv2.imshow('image', img_2)
# cv2.imshow('image', img_2)
cv2.waitKey(0)
cv2.destroyAllWindows()