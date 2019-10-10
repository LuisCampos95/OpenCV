import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    red_low = np.array([0, 235, 125], dtype=np.uint8)
    red_high = np.array([179, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, red_low, red_high)
    mask = cv2.dilate(mask, None, iterations=2)

    moments = cv2.moments(mask)
    area = moments['m00']

    print(area)
    if(area > 2000):

        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])

        cv2.rectangle(frame, (x-5, y-5), (x+5, y+5),(0,0,255), 2)
        cv2.putText(frame, "pos: "+ str(x)+","+str(y), (x+10,y+10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 3)

    cv2.imshow('mask', mask)
    cv2.imshow('Camera', frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()