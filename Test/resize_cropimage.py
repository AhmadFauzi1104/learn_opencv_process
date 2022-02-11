#import library
import cv2
#file directory
road = "gambar/OIP.jpg"
#Read image
img = cv2.imread(road)
print(img.shape)

#resizing image
lebar, panjang = 500 , 500
img_resize = cv2.resize(img, (lebar, panjang))
#cropping
img_crop = img[70:180,0:303]

cv2.imshow("Road",img)
cv2.imshow("Road_resize", img_resize)
cv2.imshow("Road_cropped", img_crop)
cv2.waitKey(0)