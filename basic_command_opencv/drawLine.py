#drawing an line on an picture
import numpy as np
import cv2

img=cv2.imread('D:\QQ.png',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(100,100),(255,0,0),1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
