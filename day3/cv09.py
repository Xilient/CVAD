#Convolution
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("noise.png")

filter = cv2.filter2D(img,-1,np.ones((3,3),np.float32)/9)
mean = cv2.blur(img,(5,5))
median = cv2.medianBlur(img,5)
gaussian = cv2.GaussianBlur(img,(5,5),10)

titles = ["Original","Filter 5x5","Mean","Median","Gaussian"]
images = [img,filter,mean,median,gaussian]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
