#Rotate Image

import cv2
import numpy as np
img= cv2.imread("download.jpg")
height ,width= img.shape[:2]

rotation_matrix= cv2.getRotationMatrix2D((width/2, height/2), 75, .6)
rotated_image= cv2.warpAffine(img, rotation_matrix, (width,height))

cv2.imshow("rotated image", rotated_image)
cv2.imshow("orignal image", img)

cv2.waitKey(0)



#Transpose (Roatate 2 90 degress without information loss)

rotate_img= cv2.transpose(img)
cv2.imshow("Transpose image", rotate_img)
cv2.waitKey(0)

cv2.destroyAllWindows()



