#Object Detection
import cv2
import numpy

while True:
    img = cv2.imread("ball_colors.jpg")
    img = cv2.resize(img,(600,600))

    #https://redketchup.io/color-picker BGR
    lower = numpy.array([175, 56, 61]) #เข้มที่สุด
    upper = numpy.array([230, 67, 75]) #จางที่สุด

    mask = cv2.inRange(img,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)

    if cv2.waitKey(0) & 0xFF == ord("e"):
        break

    cv2.imshow("Orginal",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",result)

cv2.destroyAllWindows()