import numpy as np
import cv2

cap = cv2.VideoCapture(0)

low_red = np.array([136,200,111],np.uint8)
high_red = np.array([180,255,255],np.uint8)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maskRed = cv2.inRange(hsv, low_red, high_red)
    #maskRed = cv2.erode(maskRed, None, iterations=5)
    maskRed = cv2.dilate(maskRed, None, iterations=5)

    contours, _ = cv2.findContours(maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "Vermelho", (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("maskRed", maskRed)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
