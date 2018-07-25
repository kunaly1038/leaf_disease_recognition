#in this we will do thresholding of the images this means that the image will be either in format of 0's or 1's

import numpy as np
import cv2

img = cv2.imread('123.jpg')
retval,threshold= cv2.threshold(img,12,255,cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
# cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
retval3,otsu = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('img',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('grayscaled',grayscaled)
cv2.imshow('gaus',gaus)
cv2.imshow('otsu',otsu)


cv2.waitKey(0)
cv2.destroyAllWindows()
