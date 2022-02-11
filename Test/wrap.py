import cv2
import numpy as np

path = "gambar/king.png"

img = cv2.imread(path)
print(img.shape)

widht , height = 250 , 350
pts1 = np.float32([[486,86],[594,469],[757,11],[865,392]])
pts2 = np.float32([[0,0],[0,height],[widht,0],[widht,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
img_output = cv2.warpPerspective(img,matrix,(widht,height))

print(pts1)
for i in range(0,4):
    cv2.circle(img,(int(pts1[i][0]),int(pts1[i][1])),5,(0,0,150), cv2.FILLED)
cv2.imshow("King card", img)
cv2.imshow("image output", img_output)

cv2.waitKey(0)