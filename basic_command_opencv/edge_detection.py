
#edge detection

import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()

    laplas=cv2.Laplacian(frame,cv2.CV_64F)
    soblex=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobley=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    edges=cv2.Canny(frame,200,200)

    cv2.imshow('frame', frame)
    cv2.imshow('laplas', laplas)
    cv2.imshow('soblex', soblex)
    cv2.imshow('sobley', sobley)
    cv2.imshow('edges', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
