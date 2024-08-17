#matplotlib
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../day2/cat.jpg")
cv2.imshow("Image",img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.imshow(img,cmap="gray")
plt.show()