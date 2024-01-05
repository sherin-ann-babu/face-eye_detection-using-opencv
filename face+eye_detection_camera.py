import cv2

video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/user/Documents/dl_march/open_cv/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/user/Documents/dl_march/open_cv/data/haarcascade_eye.xml')



while True:

    success,frame = video_capture.read()
    
    #convert to gray scale
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #gray scale image

    #Detect faces
    faces = face_cascade.detectMultiScale(gray_img)

    
    #print(faces)

    for (x,y,w,h) in faces:

   # To draw a rectangle around the detected face  
     cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=(255,0,0),thickness=2)
   
   #Detect eyes
    eyes = eye_cascade.detectMultiScale(gray_img)
    
   # To draw rectangle around detected eye
    for (ex,ey,ew,eh) in eyes:

   # To draw a rectangle around the detected face  
     cv2.rectangle(frame,pt1=(ex,ey),pt2=(ex+ew,ey+eh),color=(0,255,0),thickness=2)
   

    cv2.imshow('Web videocapture',frame)

    if cv2.waitKey(1) & 0xFF==27:    #0xFF=25 is the value of esc key
        break

video_capture.release()  #close window
cv2.destroyAllWindows()   #De-allocated any associated memory usage