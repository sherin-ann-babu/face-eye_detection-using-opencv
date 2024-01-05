import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/user/Documents/dl_march/open_cv/data/haarcascade_frontalface_default.xml')

while True:

    success,frame = cap.read()

    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #gray scale image


    faces = face_cascade.detectMultiScale(gray_img)

    print(faces)
    
    for (x,y,w,h) in faces:

   # To draw a rectangle around the detected face  
     cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(255,0,0),thickness=2)
     
    cv2.imshow('Web_capture',frame)

    if cv2.waitKey(1) & 0xFF==27:    #0xFF=25 is the value of esc key
        break

cap.release()
cv2.destroyAllWindows()