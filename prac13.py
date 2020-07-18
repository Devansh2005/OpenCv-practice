import cv2

## Image Smoothning
import numpy as np
img=cv2.imread("download.jpg")
cv2.imshow("Orignal", img)
cv2.waitKey(0) 

#BOX FILTER
blur= cv2.blur(img, (7,7))   #kernal matrix like filter 2d matrix
cv2.imshow("Blur Image", blur)
cv2.waitKey(0)

#GAUSSIAN BLUR-Better performance

Gaussian=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Gauss", Gaussian)
cv2.waitKey(0)

#Median Blur
median=cv2.medianBlur(img, 5)
cv2.imshow("Med", median)
cv2.waitKey(0)

#BiLateral Filter - Best noice removal 

bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow("Bilateral", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()