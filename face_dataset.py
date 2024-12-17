import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

# face_detector = cv2.CascadeClassifier('Face_Recognition/haarcascade_frontalface_default.xml')
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# For each person, enter one numeric face id
face_id = input('\n enter user id')

print("\n [INFO] Initializing face capture....")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    if not ret:
        print("Camera not capturing images")
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.cvtColor(img, img)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)
    
    k = cv2.waitKey(100) & 0xff 
    if k == 27:
        break
    elif count >= 50: 
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program")
cam.release()
cv2.destroyAllWindows()