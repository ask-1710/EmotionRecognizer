import cv2
from deepface import DeepFace

faceCascade = cv2.CascadeClassifier("D:\Projects\Opencv\PycharmProjects\OpencvPython\haarcascade_frontalface_default.xml")

img = cv2.imread("D:\Projects\Opencv\PycharmProjects\OpencvPython\Resources\happy_girl.jpg")

result = DeepFace.analyze(img, actions=['emotion'])
# detecting faces
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, 1.1, 4)

# draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# putText() to write on image
font = cv2.FONT_ITALIC
data = result['dominant_emotion']
cv2.putText(img, data, (0 , 20), font, 1, (0, 255, 255), cv2.LINE_4)
# print(result['dominant_emotion'])

cv2.imshow("IMAGE", img)
cv2.waitKey(0)
