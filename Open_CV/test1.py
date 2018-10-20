import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('4.2.01.tiff')
rows, cols, channels = img.shape

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, imgThreshold = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('image', imgThreshold)
cv2.waitKey(0)
cv2.destroyAllWindows()