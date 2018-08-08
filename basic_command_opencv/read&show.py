#to read and show the picture any where in the computer

import cv2
import numpy as np
import  matplotlib.pyplot  as plt

img=cv2.imread('D:\QQ.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
k=cv2.waitKey(0)
x=cv2.destroyAllWindows()
print(k)
print(x)

plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([50],[100],'c',Linewidth=5)
plt.show()

cv2.imwrite('q2.jpg',img)
