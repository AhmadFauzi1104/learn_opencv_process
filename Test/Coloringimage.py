import cv2
import numpy as np

#matriks
kernel = np.ones((5,5),np.uint8)

#file directory
file = "gambar/lena.png"

img = cv2.imread(file)
img_1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_2 = cv2.GaussianBlur(img_1,(5,5),0)
img_3 = cv2.Canny(img_2,100,200)
img_4 = cv2.dilate(img_3,kernel,iterations=1)
img_5 = cv2.erode(img_4,kernel,iterations=1)

#showing the image
cv2.imshow("lena",img)
cv2.imshow("Grey_lena", img_1 )
cv2.imshow("Blur_lena", img_2)
cv2.imshow("Canny_lena", img_3)
cv2.imshow("Dilation_lena",img_4)
cv2.imshow("Erotion_lena",img_5)

#delay
cv2.waitKey(0)