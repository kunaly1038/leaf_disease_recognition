#drawing an circle & ellipse and rectangle on the picture

import numpy as np
import cv2

img=cv2.imread('D:\qq.png',cv2.IMREAD_COLOR)
cv2.circle(img,(100,100),55,(255,255,255),-1)               #use -1 for dark circle
cv2.circle(img,(200,200),55,(255,0,0),0)                    #use 0 for the light circle
cv2.rectangle(img,(400,500),(300,150),(0,0,255),15)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
