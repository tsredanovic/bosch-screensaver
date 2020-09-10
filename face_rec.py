import cv2

OPENCV_FILE_PATH = '/home/toni/Projects/bosch-screensaver/opencv/haarcascade_frontalface_default.xml'

# Load the cascade
face_cascade = cv2.CascadeClassifier(OPENCV_FILE_PATH)

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    print(True if len(faces) else False)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()