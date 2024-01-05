# face-eye_detection-using-opencv
The code uses Python and OpenCV and OpenCV Frontal Face Haarcascade to detect faces in images as well as live video footage. However, during this era of Advance Deep Learning Age and Robust Model Building, Haarcascade techniques are'nt that efficient but works just fine. All thanks to OpenCV and Adrian from PyImageSearch for this code

The project contains four python files:

 1.  face_detection_image.py

 This file is used to only detect the face of a person from specified image. I had used a group pic image of people, make sure that the image should be at same location where the code is saved.

 2.  face_detection_camera.py

 This file is used to only detect the face of a person from webcam. This code is written for thos who are using inbuilt webcam for those how are using external webcam make some changes in code as  "cap = cv2.VideoCapture(0)" make it as cap = cv2.VideoCapture(1) i.e. in place of 0 write 1.

 3.  face_eye_detection_image.py

 This file is used to detect the face and eyes of a person from specified image. 
 
 4. face_eye_detection_camera.py

 This file is used to detect the face and eyes of a person from webcam. This code is written for thos who are using inbuilt webcam for those how are using external webcam make some changes in code as the line number 5 is "cap = cv2.VideoCapture(0)" make it as cap = cv2.VideoCapture(1) i.e. in place of 0 write 1.

