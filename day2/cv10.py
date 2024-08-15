#Eyes detection
import cv2
cap = cv2.VideoCapture("Video.mp4")

eye_cascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

while (cap.isOpened()):
    status, frame = cap.read()
    if status == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        scaleFactor = 1.1
        minNeighbor = 3
        eye_detect = eye_cascade.detectMultiScale(gray, scaleFactor, minNeighbor)

        for (x,y,w,h) in eye_detect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),thickness=5)
        cv2.imshow("Video",frame)

        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()