#adding two images of or we can say doing arithmetic operation on the picture


import numpy as np
import cv2

img1=cv2.imread('q2.jpg')
img2=cv2.imread('q2.png')
result=img1+img2
cv2.imshow('result',result)


result2=cv2.addWeighted(img1,0.6,img2,0.4,0 )
cv2.imshow('result2',result2)
cv2.waitKey(0)
cv2.destroyAllWindows()
