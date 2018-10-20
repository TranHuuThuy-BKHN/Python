import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('ada_threshold.png')

ret, mask = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('image', img)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()