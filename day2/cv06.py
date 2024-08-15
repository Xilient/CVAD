#Drawing
import cv2

img = cv2.imread("cat.jpg",1)
img = cv2.resize(img,(800,600))

cv2.line(img,(100,100),(400,100),(255,0,0),10)
cv2.arrowedLine(img,(100,150),(400,150),(0,255,0),10)
cv2.arrowedLine(img,(400,200),(100,200),(0,0,255),10)
cv2.rectangle(img,(100,250),(400,300),(255,255,255),10)
cv2.rectangle(img,(100,350),(400,400),(255,255,255),-1)
#circle(ภาพ,จุดศูนย์กลาง,รัศมี,ความหนา)
cv2.circle(img,(150,500),50,(125,125,125),5)
cv2.circle(img,(300,500),50,(125,125,125),-1)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()