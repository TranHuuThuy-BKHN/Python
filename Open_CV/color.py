import cv2
import numpy as np

def nothing(x):
    pass

#create a black image
img = np.zeros((200, 400, 3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('Red', 'image', 0, 255, nothing)
cv2.createTrackbar('Blue', 'image', 0, 255, nothing)
cv2.createTrackbar('Green', 'image', 0, 255, nothing)

cv2.createTrackbar('0.OFF\n1.ON', 'image', 0, 1, nothing)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    r = cv2.getTrackbarPos('Red', 'image') 
    b = cv2.getTrackbarPos('Blue', 'image')
    g = cv2.getTrackbarPos('Green', 'image')
    s = cv2.getTrackbarPos('0.OFF\n1.ON', 'image')

    if s == 0:
        img[:] = 0

    else :
        img[:] = [b, g, r]    
cv2.destroyAllWindows()
