import cv2

img = cv2.imread('gambar/lena.png')

cv2.imshow("Lena", img)

cv2.waitKey(0)
