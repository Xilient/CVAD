#Video Capture
import cv2

cam = cv2.VideoCapture('Video.mp4')

while (cam.isOpened()):
    status , frame = cam.read()
    if status == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Camera",gray) #gray
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cam.release()
cv2.destroyAllWindows()