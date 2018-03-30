import cv2 
import numpy as np

global img

def erode(erosion_size):
    erosion_size = 2*erosion_size+1
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(erosion_size,erosion_size))
    eroded = cv2.erode(img,kernel)
    cv2.imshow('erosion demo',eroded)

def dilate(dilation_size):
    dilation_size = 2*dilation_size+1
    kernel =  cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(dilation_size,dilation_size))
    dilated = cv2.dilate(img,kernel)
    cv2.imshow('dilation demo',dilated)


erosion_size = 0   # initial kernel size  = 1
dilation_size = 0

max_kernel_size = 21  # maximum kernel size = 43

img = cv2.imread('lpq.pgm')

cv2.namedWindow('erosion demo',2)
cv2.namedWindow('dilation demo',2)

# Creating trackbar for kernel size
cv2.createTrackbar('Size: 2n+1','erosion demo',erosion_size,max_kernel_size,erode)
cv2.createTrackbar('Size: 2n+1','dilation demo',dilation_size,max_kernel_size,dilate)

erode(0)
dilate(0)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
