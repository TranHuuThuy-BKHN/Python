import cv2
import numpy as np

# lis = [i for i in dir(cv2) if 'FONT' in i]
# print(lis)
def mouseCallBack(event, x, y, flag, userdata):
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.rectangle(img, (x, y), (x + 30, y + 30), (255, 0, 0), 4)
	if event == cv2.EVENT_RBUTTONDOWN:
		cv2.putText(img, 'Hust',(x, y),  cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 4, cv2.LINE_AA)	

img = np.zeros((300, 300, 3), np.uint8)
cv2.namedWindow('image')

while True:
	cv2.imshow('image', img)
	cv2.setMouseCallback('image', mouseCallBack)
	if cv2.waitKey(1) == ord('q'):
		break

cv2.destroyAllWindows()