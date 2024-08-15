#Camera Record
import cv2

cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
result = cv2.VideoWriter("Result.mp4",fourcc,30,(640,480))

while (cam.isOpened()):
    status , frame = cam.read()
    if status == True:
        cv2.imshow("Camera",frame)
        result.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break

result.release()
cam.release()
cv2.destroyAllWindows()