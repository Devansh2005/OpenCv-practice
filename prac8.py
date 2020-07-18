import cv2

# Img pyramid (Image size to half and double)


img=cv2.imread("download.jpg")
#Image choti- 
smaller= cv2.pyrDown(img)
# Image badi
larger= cv2.pyrUp(img) 

cv2.imshow("orignal", img)
cv2.imshow("smaller", smaller)
cv2.imshow("Larger", larger)

cv2.waitKey(0)
cv2.destroyAllWindows()

