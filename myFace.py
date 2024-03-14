import cv2

img = cv2.imread('myphoto.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    face = img[y:y + h, x:x + w]
    faces_resize = cv2.resize(face, (150, 150), interpolation=cv2.INTER_LINEAR)
    cv2.imshow('Detected_face', faces_resize)


cv2.imshow('Detected faces', img)

cv2.waitKey(0)
