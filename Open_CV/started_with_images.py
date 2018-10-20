import cv2
img = cv2.imread('hello.jpg', -1)
cv2.imshow('My friends', img)
cv2.waitKey(0)
cv2.imwrite('huuthuy.jpg', img)
cv2.destroyAllWindows()