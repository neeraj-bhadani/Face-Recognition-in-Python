import cv2, time

# creating an object
video = cv2.VideoCapture(0)

a = 1  # frame count

# a while loop that runs through all the frames until check returns true
# check returns true if the camera captures a frame

while True:
    a = a + 1
    check, frame = video.read()
    print(frame)

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

    cv2.imshow("Video", gray)
    for x,y,w,h in faces:
        img = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 3)

    key = cv2.waitKey(1)
    if key == ord('q'): # when q is pressed video stops
        break

print(a) # prints no. of frames
video.release()
cv2.destroyAllWindows()

