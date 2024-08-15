#Show and Write Image
import cv2

img = cv2.imread("cat.jpg",0)
img = cv2.resize(img,(400,400))

cv2.imshow("img",img)
cv2.imwrite("cat_gray.jpg", img)
cv2.waitKey(0)