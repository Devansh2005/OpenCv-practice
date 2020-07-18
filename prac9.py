# Image cropping

import cv2
img= cv2.imread("download.jpg")

height, width= img.shape[:2]

# Extract the top corner

start_row, start_col = int(height*.25), int(width*.25)

#Extracting the end pixel coorinates
end_row, end_col=  int(height*.75) , int(width*.75)

cropped= img[start_row:end_row, start_col:end_col]

cv2.imshow("orignal", img)
cv2.waitKey(0)

cv2.imshow("cropped", cropped)
cv2.waitKey(0)

