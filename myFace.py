import os

import cv2
from PIL import Image

source_path = 'images/myphoto.jpg'
target_directory = 'C:/Users/asus/PycharmProjects/pythonProject/save_img/'

img = cv2.imread(source_path)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar_cascade = cv2.CascadeClassifier('service/haarcascade_frontalface_default.xml')

faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)



for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    face = img[y:y + h, x:x + w]
    faces_resize = cv2.resize(face, (150, 150), interpolation=cv2.INTER_LINEAR)
    target_path = os.path.join(target_directory,"myimg1.jpg")

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    cv2.imwrite(target_path,faces_resize)
    cv2.imshow('Detected_face', faces_resize)


cv2.imshow('Detected faces', img)

cv2.waitKey(0)
