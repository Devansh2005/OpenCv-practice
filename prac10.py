import cv2
import numpy as np
# Image Airthmetics

img= cv2.imread("download.jpg")
cv2.imshow("Orgnal", img)

cv2.waitKey(0)
M=np.ones(img.shape, dtype="uint8") *150

# Alternate method for matrix
# M1=np.zeros(img.shape, dtype="uint8") + 150

added=cv2.add(img, M)
cv2.imshow("Added", added)

substracted=cv2.subtract(img, M)
cv2.imshow("Substracted", substracted)

mul=cv2.multiply(img, M)
cv2.imshow("Mul", mul)

cv2.waitKey(0)
cv2.destroyAllWindows()

