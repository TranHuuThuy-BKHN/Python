import cv2
import numpy as np

img = np.zeros([400, 800, 3], np.uint8)

row, col, channel = img.shape

img[0:row, 0:col] = [0, 255, 255]

cv2.circle(img, (col//2, row//2), 40, (0, 0, 255), -1)
cv2.circle(img, (300, 200), 40, (0, 0, 255), 2)	
cv2.rectangle(img, (200, 200), (300, 300), (255, 0, 0), -1)	

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.imwrite('xla.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()