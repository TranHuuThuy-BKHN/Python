import cv2
import numpy as np

img = np.zeros((400, 300, 3), np.uint8)

for i in range(30):
	img = cv2.circle(img, (80, 200), i + 30, (0, 255 , 0))
	img = cv2.circle(img, (220, 200), i + 30, (255, 0, 0))
	img = cv2.circle(img, (150, 80), i + 30, (0, 0, 255))

img = cv2.putText(img, 'OpenCV', (30, 350), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)

cv2.imwrite('opencv.jpg', img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()