#Convolution filter and mean
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("noise.png")

filter = cv2.filter2D(img,-1,np.ones((5,5),np.float32)/9)
mean = cv2.blur(img,(5,5))

titles = ["Original","Filter 5x5","Mean"]
images = [img,filter,mean]

for i in range(len(images)):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()