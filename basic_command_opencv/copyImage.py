#copy and region of image to some other area of the picture

import numpy as np
import cv2

img=cv2.imread('D:\QQ.png',cv2.IMREAD_COLOR)
img[55,100]=[255,255,0]
px=img[55,55]
#print(px)


#region of the image(roi)
img[55:100,100:200]=[255,255,0]
#roi=img
#print(roi)

image_copy=img[37:111,107:194]
img[0:74,0:87]=image_copy

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
