import cv2
import numpy as np
img=cv2.imread("download.jpg")

height, width = img.shape[:2]
print(height)
print(width)

quater_heigth, quater_width= height/4, width/4
print(quater_heigth)
print(quater_width)

T= np.array([[1,0,quater_width],[0,1,quater_heigth]])
print(T)

#warpAffine Transformation - Width and height aere linear
#warpNon Affine Transformation- Width and hight are not linear

#Image Translation

img_translation= cv2.warpAffine(img, T, (width, height))
cv2.imshow("Orignal",img)
cv2.waitKey(0)

cv2.imshow("Again",img_translation)
cv2.waitKey(0)


cv2.destroyAllWindows()