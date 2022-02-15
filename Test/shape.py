import cv2
import numpy as np
 
img = np.zeros((512,512,3),np.uint8)
print(img.shape)
#draw line and rectangle
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),2)
cv2.rectangle(img,(0,412),(100,512),(0,100,255),cv2.FILLED)
cv2.circle(img,(462,50), 50, (223,225,224),1)
cv2.putText(img,"Draw Shape", (150,50),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,200,0),2)

#show the image
cv2.imshow("img blank", img)
cv2.waitKey(0)