import cv2
import numpy as np

circles = np.zeros((4,2),int)
iteration = 0



def mouseClicks(event,x,y,flags,params):
    global iteration
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        circles[iteration] = x,y
        iteration = iteration + 1

path = "gambar/R.jpg"

img = cv2.imread(path)
img = cv2.resize(img,(1000,800))
while True:

    if iteration == 4:
        widht, height = 250, 350
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [0, height], [widht, 0], [widht, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        img_output = cv2.warpPerspective(img, matrix, (widht, height))
        cv2.imshow("image output", img_output)


    for i in range(0, 4):
        cv2.circle(img, (int(circles[i][0]), int(circles[i][1])), 3, (0, 0, 150), cv2.FILLED)

    cv2.imshow("original image", img)
    cv2.setMouseCallback("original image", mouseClicks)

    cv2.waitKey(1)