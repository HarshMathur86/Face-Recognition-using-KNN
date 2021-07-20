# Write a Python Script that captures images from your webcam video stream
# Extracts all Faces from the image frame (using haarcascades)
# Stores the Face information into numpy arrays

# 1. Read and show video stream, capture images
# 2. Detect Faces and show bounding box (haarcascade)
# 3. Flatten the largest face image(gray scale) and save in a numpy array
# 4. Repeat the above for multiple people to generate training data


import cv2
import numpy as np 

#Inititalising camera
cap = cv2.VideoCapture(0)

#Face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

skip = 0
face_data = []

file_name = input("Enter the name of the person: ")
Dataset  = "/home/harsh_linux/Data science master/projects/Face recognition/"
while True:
    ret, frame = cap.read()

    if ret == False:
        continue
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    faces = sorted(faces, key=lambda f:f[2]*f[3])#f[2]*f[3] is the are of the face

    #Pick the largest face
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame, (x, y), (x+w, y+h),(0,255,0),2)
        
        #Extract (Croup out the required face): Region of interest
        offset = 10
        face_section = frame[y-offset:y+h+offset ,x-offset:x+w+offset]
        face_section = cv2.resize(face_section ,(200, 200))

        #storing every 10th image
        if(skip%10 == 0):
            face_data.append(face_section)
            print(len(face_data))
        skip += 1
    cv2.imshow("Video", frame)
    cv2.imshow("Face Section", face_section)

    key_pressed = cv2.waitKey(1) & 0xFF #getting 8 bit of waitKey from 32 bit
    if ord('q') == key_pressed:
        break


#Convert the face list array into a numpy array
face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0], -1))
print(face_data.shape)

#save the data into file system
np.save(Dataset +file_name + '.npy', face_data)
print("Data Successfully Saved in " + file_name + '.npy')

cap.release()
cv2.destroyAllWindows()