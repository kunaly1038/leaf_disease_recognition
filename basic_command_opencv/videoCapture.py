#in this we read the web camera and then read the and conver that file and open another file and display in some other color
import numpy  as np
import cv2

cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == 27 & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
