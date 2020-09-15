import cv2 
#Load the cascade
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml') 
#Load the image
img=cv2.imread(r'E:\PythonPrograms\face_detection\vk.jpg')
# Detecting EYE
eye = eye_cascade.detectMultiScale(img, 1.2, 18) 
#creating Rectangle
for (x_eye, y_eye, w_eye, h_eye) in eye:
    cv2.rectangle(img,(x_eye, y_eye),(x_eye+w_eye, y_eye+h_eye), (0, 180, 60), 2)
#Display
cv2.imshow('Detected eyes',img)
#Press any key to escape
cv2.waitKey()