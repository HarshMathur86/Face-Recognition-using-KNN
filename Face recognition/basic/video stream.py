# read video stream from  webcam
import cv2

cap = cv2.VideoCapture(0)#0 will the oder of webcam if there are multiple webcam

while True:    
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == False:
        continue

    cv2.imshow("Video Frame", frame)
    cv2.imshow("Video Frame - GRAY", gray_frame)

    #Wait for user to input 'q'
    key_pressed = cv2.waitKey(1) & 0xFF #getting 8 bit of waitKey from 32 bit
    if ord('q') == key_pressed:
        break

cap.release()
cv2.destroyAllWindows()