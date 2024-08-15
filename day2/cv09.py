#Face detection
import cv2
img = cv2.imread("faces.jpg",1)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

scaleFactor = 1.1
minNeighbor = 3
face_detect = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbor)

for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=5)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# cap = cv2.VideoCapture("Video.mp4")
#
# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#
# while (cap.isOpened()):
#     status, frame = cap.read()
#     if status == True:
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#         scaleFactor = 1.3
#         minNeighbor = 5
#         face_detect = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbor)
#
#         for (x,y,w,h) in face_detect:
#             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),thickness=5)
#         cv2.imshow("Video",frame)
#
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#             break
#     else:
#         break
#
# cap.release()
# cv2.destroyAllWindows()