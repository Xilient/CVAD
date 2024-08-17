#point and connections
import cv2
import numpy

img = cv2.imread("cat.jpg")
img = cv2.resize(img,(600,600))
img  = numpy.zeros([400,400,3])

points = []

def click_position(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,255,0),5)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-2],points[-1],(255,0,0),2)

        cv2.imshow("Image",img)

cv2.imshow("Image",img)
cv2.setMouseCallback("Image",click_position)
cv2.waitKey(0)
cv2.destroyAllWindows()
