#Camera Capture
import cv2

cam = cv2.VideoCapture(0)

while (cam.isOpened()):
    status , frame = cam.read()
    cv2.imshow("Camera",frame)
    if cv2.waitKey(10) & 0xFF == ord("e"):
        break

cam.release()
cv2.destroyAllWindows()