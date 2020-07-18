import cv2

#RESIZING  

img=cv2.imread("download.jpg")

cv2.imshow("Orignal Image", img)
cv2.waitKey(0)

#Linear Interplotation - reduce size
#Cubic Interploatation-size increase

img_scaled_choti=cv2.resize(img,None, fx=0.75, fy=0.75)  #75% of image 
cv2.imshow("Scaling linear Interplotation", img_scaled_choti)
cv2.waitKey(0)

#Technique 2

img_scaled_badi=cv2.resize(img,None, fx=2, fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("Scaling-Cubic interploatation", img_scaled_badi)
cv2.waitKey(0)

# Technique 3 (Area)- expand the area of the image.

img_scaled_area= cv2.resize(img, (900, 400), interpolation=cv2.INTER_AREA)
cv2.imshow("Scaling image -Skewed size", img_scaled_area)
cv2.waitKey(0)

cv2.destroyAllWindows()




