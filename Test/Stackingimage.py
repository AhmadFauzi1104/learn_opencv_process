import cv2
import numpy as np

path_1 = 'gambar/lena.png'
path_2 = 'gambar/OIP.jpg'

img_1 = cv2.imread(path_1)
img_2 = cv2.imread(path_2)
print(img_1.shape)
print(img_2.shape)

img_1 = cv2.resize(img_1, (180, 303), None, 0.5, 0.5)
img_2 = cv2.resize(img_2, (180, 303), None, 0.5, 0.5)

horizontal = np.hstack((img_1,img_2))
vertical = np.vstack((img_1,img_2))

cv2.imshow("Stack Horizontal", horizontal)
cv2.imshow("Stack Vertical", vertical)

cv2.waitKey(0)