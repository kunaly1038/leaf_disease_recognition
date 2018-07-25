#morphologigical

import numpy as np
import cv2


cap=cv2.VideoCapture(0)

while True:
    res,frame=cap.read()

    lower_red= np.array([150,150,50])
    upper_red= np.array([255,255,255])
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask=  cv2.inRange(hsv,lower_red,upper_red)
    kernel = np.ones((15, 15), np.float32) / 225
    res=cv2.bitwise_and(frame,frame,mask=mask)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    close = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('dilation', dilation)
    cv2.imshow('erosion', erosion)
    cv2.imshow('open', open)
    cv2.imshow('close', close)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
