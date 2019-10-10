import numpy as np
import cv2

cap = cv2.VideoCapture(0)

low_red = (136, 87, 111)
high_red = (179, 255, 255)

while True:
	_, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	maskRed = cv2.inRange(hsv, low_red, high_red)
	maskRed = cv2.dilate(maskRed, None, iterations=5)

	cntRed, _ = cv2.findContours(maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

	if len(cntRed) > 0:

		cRed = max(cntRed, key=cv2.contourArea)
		rectRed = cv2.minAreaRect(cRed)
		boxRed = cv2.boxPoints(rectRed)
		boxRed = np.int0(boxRed)
		cv2.drawContours(frame, [boxRed], -1, (0, 255, 0), 3)

	cv2.imshow("Frame", frame)
	cv2.imshow("Frame2", maskRed)

	key = cv2.waitKey(1)

	if key == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()
