#Threshold
import cv2
import matplotlib.pyplot as plt

gray = cv2.imread("gradient.png")

thresh , thr1 = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)
thresh , thr2 = cv2.threshold(gray,128,255,cv2.THRESH_BINARY_INV)
thresh , thr3 = cv2.threshold(gray,128,255,cv2.THRESH_TRUNC)
thresh , thr4 = cv2.threshold(gray,128,255,cv2.THRESH_TOZERO)
thresh , thr5 = cv2.threshold(gray,128,255,cv2.THRESH_TOZERO_INV)

# cv2.imshow("thr3",thr3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print(thresh)

imgs = [gray,thr1,thr2,thr3,thr4,thr5]
titles = ["Image","BINARY","BINARY_INV","TRUNC","TO_ZERO","TO_ZERO_INV"]

for i in range(len(imgs)):
    #แถว,คอลลัม,
    plt.subplot(2,3,i+1)
    plt.imshow(imgs[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()