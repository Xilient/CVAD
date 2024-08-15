#Video Capture
import cv2
import datetime

cam = cv2.VideoCapture('Video.mp4')

while (cam.isOpened()):
    status , frame = cam.read()
    if status == True:
        date = str(datetime.datetime.now())
        #ภาพ , ข้อความ , ตำแหน่ง , font,ขนาดข้อความ, สีข้อความ ,ประเภทของ
        cv2.putText(frame, date,(10,40),cv2.FONT_HERSHEY_SIMPLEX,1,(100,150,100),cv2.LINE_4)
        cv2.imshow("Camera",frame) #gray
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cam.release()
cv2.destroyAllWindows()