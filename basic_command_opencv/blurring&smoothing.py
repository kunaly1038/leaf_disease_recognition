import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
    ret ,frame=cap.read()
    lower_red= np.array([150,150,50])
    upper_red= np.array([255,255,255])
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)


    kernel=np.ones((15,15),np.float32)/225
    smooth=cv2.filter2D(res,-1,kernel)

    blur=cv2.GaussianBlur(res,(15,15),0)
    median=cv2.medianBlur(res,15)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)
    cv2.imshow('bilateral Blur', bilateral)

    cv2.imshow('res', res)
    cv2.imshow('smooth', smooth)
    cv2.imshow('frame', frame)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
