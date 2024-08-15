#Threshold levels with images 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../day2/cat.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh_val = [50,100,150,200,250]
#แถม คอลลัม ภาพ
plt.subplot(231,xticks=[],yticks=[])
plt.title("Image")
plt.imshow(gray,cmap="gray")

for i in range(len(thresh_val)):
    thresh , result = cv2.threshold(gray, thresh_val[i],255,cv2.THRESH_BINARY)
    plt.subplot(232+i)
    plt.title("%d"%thresh_val[i])
    plt.imshow(result,cmap="gray")
    plt.xticks([]),plt.yticks([])

plt.show()