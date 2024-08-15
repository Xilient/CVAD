#color view
import cv2
import numpy

img = cv2.imread("cat.jpg")
img = cv2.resize(img,(600,600))

def click_position(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue,green,red = img[y,x,0] , img[y,x,1] , img[y,x,2]
        colors = str(blue) + "," + str(green) + "," +str(red)
        coordinate = str(x)+","+str(y)
        cv2.putText(img, colors,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(150,100,150),cv2.LINE_4)
        pick_color = numpy.zeros([300,300,3],numpy.uint8)
        pick_color[:] =[blue,green,red]
        cv2.imshow("Image",img)
        cv2.imshow("Color",pick_color)

cv2.imshow("Image",img)
cv2.setMouseCallback("Image",click_position)
cv2.waitKey(0)
cv2.destroyAllWindows()
