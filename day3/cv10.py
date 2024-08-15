#Edge Detection
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("currency.jpg",0)

sobelX = cv2.Sobel(img,-1,1,0)
sobelY = cv2.Sobel(img,-1,0,1)
sobelXY = cv2.bitwise_or(sobelX,sobelY)
lapacian = cv2.Laplacian(img, -1)
canny = cv2.Canny(img,50,200)

titles = ["Original","SobelX","SobelY","SobelXY","Lapacian","Canny"]
images = [img,sobelX,sobelY,sobelXY,lapacian,canny]

for  i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()