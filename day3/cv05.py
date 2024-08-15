#Adaptive Threshold
import cv2

img = cv2.imread("map.jpg",0)

thresh , thr1 = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
thr2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)
thr3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)

cv2.imshow("Image",thr1)
cv2.imshow("Mean",thr2)
cv2.imshow("Gaussian",thr3)

cv2.waitKey(0)
cv2.destroyAllWindows()