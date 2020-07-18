import cv2
img=cv2.imread("download.jpg",0)
cv2.imshow("out-gray scale image", img)
cv2.waitKey(0)

ret, bw=cv2.threshold(img,58,220,cv2.THRESH_BINARY)
cv2.imshow("binary image",bw)
cv2.waitKey(0)



# gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray Scale Image", gray_img)
# cv2.waitKey(0)


cv2.destroyAllWindows()