#resize an image using python 

import os
import numpy as np
import cv2

def resize_image():
    pic_num=1
    while pic_num < 6:
        img = cv2.imread('peepal/'+str(pic_num)+'.jpg')
        resized = cv2.resize(img, (150, 150))
        cv2.imwrite('peepal/'+str(pic_num)+'.jpg',resized)
        pic_num+=1
        print(pic_num)

resize_image()
