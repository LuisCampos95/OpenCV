import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_red = np.array([0, 200, 111])
    high_red = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low_red, high_red)
    #mask = cv2.erode(mask, None, iterations=2)
    #mask = cv2.dilate(mask, None, iterations=2)

    cv2.imshow("Camera", frame)
    cv2.imshow("Red Mask", mask)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()