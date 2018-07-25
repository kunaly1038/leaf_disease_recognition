#to save the picture which we read from commputer

import numpy as np
import matplotlib as plt
import cv2

img=cv2.imread('D:\QQ.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('q2.png',img)
    cv2.destroyAllWindows()

print(k)
cv2.destroyAllWindows()
