import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('4.2.01.tiff')
img2 = cv2.imread('4.2.07.tiff')
img3 = cv2.imread('house.tiff')

img1 =cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 =cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img3 =cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

plt.subplot(2, 3, 1)
plt.imshow(img1)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 2)
plt.imshow(img2)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 3)
plt.imshow(img3)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 4)
plt.imshow(img3)
plt.xticks([])
plt.yticks([])
plt.show()

# cv2.imshow('image1', img1)
# cv2.imshow('image2', img2)
# cv2.imshow('image3', img3)

# cv2.waitKey(0)
# cv2.destroyAllWindows()