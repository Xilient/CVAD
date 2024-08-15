#Trackba]
import cv2
import numpy as np

img = np.zeros((200,250,3),np.uint8)
cv2.namedWindow("Color Trackbar")

def display(value):
    img[:] = [blue,green,red]

cv2.createTrackbar("B","Color Trackbar",0,255,display)
cv2.createTrackbar("G","Color Trackbar",0,255,display)
cv2.createTrackbar("R","Color Trackbar",0,255,display)

while True:
    cv2.imshow("Color Trackbar",img)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

    blue = cv2.getTrackbarPos("B","Color Trackbar")
    green = cv2.getTrackbarPos("G", "Color Trackbar")
    red = cv2.getTrackbarPos("R", "Color Trackbar")



cv2.destroyAllWindows()
