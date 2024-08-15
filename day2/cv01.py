#Read Image
import cv2

imge = cv2.imread("cat.jpg",1)

print(type(imge))
print(imge.ndim)
print(imge)

# img = cv2.imread("cat.jpg",0)
# print(type(img))
# print(img.ndim)
# print(img)