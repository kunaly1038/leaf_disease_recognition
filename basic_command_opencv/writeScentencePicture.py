#write any thing on the picture 

import numpy as np
import cv2

img=cv2.imread('D:\QQ.png',cv2.IMREAD_COLOR)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'hello world',(10,500),font,2,(255,255,6),2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
