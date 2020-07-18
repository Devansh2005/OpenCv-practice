import cv2
#Edge detecting technique
import numpy as np
img=cv2.imread("download.jpg",0) #gray scale

height, width = img.shape[:2]

# Extract sobel edges--very bad method(noisy)
sobel_x = cv2.Sobel(img, cv2.CV_64F,1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F,0, 1, ksize=5)

cv2.imshow("Orignal", img)
cv2.waitKey(0)
cv2.imshow("sobelx ", sobel_x)
cv2.waitKey(0)
cv2.imshow("sobely", sobel_y)
cv2.waitKey(0)

#BITWISE OR
sobel_or=cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow("sobel or Image", sobel_or)

cv2.waitKey(0) 

# Lappacian Technique 2nd number

laplacian= cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow("lap",laplacian)
cv2.waitKey(0)

#canny edge detection- best technique
canny= cv2.Canny(img,20, 170)
cv2.imshow("canny edges", canny)
cv2.waitKey(0)
