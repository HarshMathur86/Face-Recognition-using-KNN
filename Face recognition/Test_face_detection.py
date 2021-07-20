# read video stream from  webcam
import cv2

cap = cv2.VideoCapture(0)#0 will the oder of webcam if there are multiple webcam
face_casade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

while True:    
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == False:
        continue

    faces = face_casade.detectMultiScale(gray_frame, 1.3, 5)
    #1.3 will be scaled size of image and 5 
    #data will we returnes as x,y,w,h
    print(faces)
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h),(0,255,0),2)

    cv2.imshow("Video", frame)

    #Wait for user to input 'q'
    key_pressed = cv2.waitKey(1) & 0xFF #getting 8 bit of waitKey from 32 bit
    if ord('q') == key_pressed:
        break

cap.release()
cv2.destroyAllWindows()