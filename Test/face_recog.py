import cv2
import numpy as np
import face_recognition

img_elon = face_recognition.load_image_file("gambar/elon_mask_true.jpg")
img_elon = cv2.cvtColor(img_elon,cv2.COLOR_BGR2RGB)
img_elon = cv2.resize(img_elon,(500,500))
img_test = face_recognition.load_image_file("gambar/elon_mask.jpg")
img_test = cv2.cvtColor(img_test,cv2.COLOR_BGR2RGB)


faceLocation = face_recognition.face_locations(img_elon)[0]
print(faceLocation)
encode_elon = face_recognition.face_encodings(img_elon)[0]
cv2.rectangle(img_elon,(faceLocation[3],faceLocation[0]),(faceLocation[1],faceLocation[2]),(255,0,0),5)

faceLocationTest = face_recognition.face_locations(img_test)[0]
encode_elon_test = face_recognition.face_encodings(img_test)[0]
cv2.rectangle(img_test,(faceLocationTest[3],faceLocationTest[0]),(faceLocationTest[1],faceLocationTest[2]),(255,0,0),5)

result = face_recognition.compare_faces([encode_elon],encode_elon_test)
faceDistance = face_recognition.face_distance([encode_elon],encode_elon_test)
cv2.putText(img_test,f"{result} {round(faceDistance[0],2)}",(300,230),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,250),2)
print(result)
print(faceDistance)

cv2.imshow("Image Elon", img_elon)
cv2.imshow("Image test", img_test)
cv2.waitKey(0)
