#Threshold with Trackbar
import cv2

def display(value):
    pass

cv2.namedWindow("Image")
cv2.createTrackbar("value","Image",128,255,display)

while True:
    gray = cv2.imread("../day2/cat.jpg",0)
    thresh_val = cv2.getTrackbarPos("value","Image",)
    thresh , result = cv2.threshold(gray,thresh_val,255,cv2.THRESH_BINARY )
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

    cv2.imshow("Image",result)

cv2.destroyAllWindows()