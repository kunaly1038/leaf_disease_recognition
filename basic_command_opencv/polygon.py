#drawing an polygon on the picture

import numpy as np
import cv2

img=cv2.imread('D:\qq.png',cv2.IMREAD_COLOR)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
