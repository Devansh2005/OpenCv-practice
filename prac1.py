import cv2
img=cv2.imread("download.jpg")

cv2.imshow("output image", img)
cv2.imwrite("opt.jpg", img)
cv2.imwrite("opt.png", img)
print(img.shape) #height , width, layers(RGB)

print("Height Pixel values:",img.shape[0])
print("width pixel values:", img.shape[1])
print("Layer pixel values:", img.shape[2])



cv2.waitKey(0)
cv2.destroyAllWindows()

