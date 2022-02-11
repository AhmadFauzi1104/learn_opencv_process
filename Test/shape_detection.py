import cv2
import numpy as np

frameWidht = 640
frameHight = 480
cap = cv2.VideoCapture(1)

cap.set(3,frameWidht)
cap.set(4,frameHight)


def empty(a):
    pass
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",300,200)
cv2.createTrackbar("Treshold1","Parameters",48,179,empty)
cv2.createTrackbar("Treshold2","Parameters",76,179,empty)
cv2.createTrackbar("Area","Parameters",5000,30000,empty)

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])

    rowAvailable = isinstance(imgArray[0],list)
    widht = imgArray[0][0].shape[1]

    height = imgArray[0][0].shape[0]

    if rowAvailable:
        for x in range (0,rows):
            for y in range(0,cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y],(0,0),None,scale,scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y],(imgArray[0][0].shape[1],imgArray[0][0].shape[0]),None,scale,scale)
                if len(imgArray[x][y].shape) == 2 : imgArray[x][y] = cv2.cvtColor(imgArray[x][y],cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height,widht,3),np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0,rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:

        for x in range(0,rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x],(0,0),None,scale,scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x],(imgArray[0].shape[1],imgArray[0].shape[0]),None,scale,scale)
            if len(imgArray[x].shape) == 2 : imgArray[x] = cv2.cvtColor(imgArray[x],cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

def getContour(img,imgContour):

    contours, hierarky = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for cnt  in contours:
        area = cv2.contourArea(cnt)
        MinArea = cv2.getTrackbarPos("Area","Parameters")
        if area > 1000:
            cv2.drawContours(imgContour,cnt,-1,(255,0,255),7)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),5)
            cv2.putText(imgContour, "Points: " + str(len(approx)) , (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0, 255, 0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)
while True:
    succes, image = cap.read()
    imgContour = image.copy()
    img_blur = cv2.GaussianBlur(image,(7,7),1)
    img_grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    treshold1 = cv2.getTrackbarPos("Treshold1","Parameters")
    treshold2 = cv2.getTrackbarPos("Treshold2","Parameters")

    imgCanny = cv2.Canny(img_grey,treshold1,treshold2)

    kernel = np.ones((5,5))
    img_dil = cv2.dilate(imgCanny,kernel,iterations=1)

    getContour(img_dil,imgContour)

    imgStack = stackImages(0.5,([image,img_grey,imgCanny],[img_dil,imgContour,imgContour]))
    cv2.imshow("My camera",imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break