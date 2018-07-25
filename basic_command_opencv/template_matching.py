#template matching
import numpy as np
import cv2


img1=cv2.imread('cpu1.jpg')
img_bgr=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2=cv2.imread('cpu2.jpg',0)

w,h=img2.shape[::-1]
res=cv2.matchTemplate(img_bgr,img2,cv2.TM_CCOEFF_NORMED)
threshold=0.8

loc=np.where(res>=threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img1, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img1)


cv2.waitKey(0)
cv2.destroyAllWindows()
