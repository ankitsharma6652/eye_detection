import cv2
#Load the cascade
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml') 
#To capture the video
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#use video file as input--> cap=cv2.VideoCapture('filename.mp4)
#Function for detecting eyes
def detect(frame):
    #Detecting EYES
    eye = eye_cascade.detectMultiScale(frame, 1.2, 18) 
    #Draw the rectangle around each face
    for (x_eye, y_eye, w_eye, h_eye) in eye:
        cv2.rectangle(frame,(x_eye, y_eye),(x_eye+w_eye, y_eye+h_eye), (0, 180, 60), 2) 
    #return frame
    return frame
while True:
    _,frame=cap.read()
    canvas=detect(frame)
    #Display
    cv2.imshow('Detecting Eyes',frame)
    #Stop if escape key is pressed
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()