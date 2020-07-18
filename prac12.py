# Image Blurring
import cv2
import numpy as np
img=cv2.imread("download.jpg")
cv2.imshow("Orignal", img)
cv2.waitKey(0) 

#kerenal matrix 3 X 3 , taken only odd
# if we take 5x5 thn divide by 25, 7x7 / by 49, 3x3 / by 9
 
kernal_3x3= np.ones((3,3),np.float32)/9

# to blur we use filter 2d function
blurred = cv2.filter2D(img, -1, kernal_3x3)
cv2.imshow("3x3 kernal Blurring", blurred)
# 7x7 kernal more blur image
kernal_7x7= np.ones((7,7),np.float32)/49
blurred2=cv2.filter2D(img, -1,kernal_7x7)
cv2.imshow("7x7 kernal Blurring", blurred2)
cv2.waitKey(0)

cv2.destroyAllWindows()

