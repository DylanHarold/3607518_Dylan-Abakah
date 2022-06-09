Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2 as cv
import numpy as np

def rescale(frame, scale=0.1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)
    
    return cv.resize(frame, dimension, cv.INTER_AREA)

img = cv.imread('Images/People.jpg')
img = rescale(img)
cv.imshow('Test', img)

new_image = np.zeros(img.shape, img.dtype)

beta = 50

new_image = cv.convertScaleAbs(img, beta=beta)

cv.imshow('New Image', new_image)

cv.waitKey(0)

