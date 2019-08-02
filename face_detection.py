import cv2



face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("C:\\Users\\Neeraj Bhadani\\PycharmProjects\\face_recognition\\pic1.jpg")

# reading the image as grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# search the coordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(faces)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0) , 1)

cv2.imshow("RECOGNITION", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
