import cv2
import numpy as np 
import matplotlib.pyplot as plt 

cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')
cap.set(3, 300)
cap.set(4, 400)

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	cv2.imshow('gray', gray)
	cv2.imshow('hsv', hsv)
	cv2.imshow('frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()		