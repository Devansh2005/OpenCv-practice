import cv2
img=cv2.imread("download.jpg")
cv2.imshow("opt", img)
img_HSV=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("Hue channel",img_HSV[:, :, 0])
cv2.imshow("saturation", img_HSV[:,:,1])
cv2.imshow("Value channel",img_HSV[:, :, 2])
cv2.waitKey(0)
cv2.destroyAllWindows()
