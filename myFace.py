import math
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import cv2

files_path = [x for x in os.listdir('images')]
print(files_path)

# quit()

for f in files_path:
    source_path = 'images/' + f
    target_directory = 'C:/Users/asus/PycharmProjects/pythonProject/save_img/'

    img = cv2.imread(source_path)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    haar_cascade = cv2.CascadeClassifier('service/haarcascade_frontalface_default.xml')

    faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

    folder_path = "save_img"

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        count = len(files)
        print("Number of files in the folder:", count)
    else:
        print("Folder does not exist or is not a directory.")

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        face = img[y:y + h, x:x + w]
        faces_resize = cv2.resize(face, (150, 150), interpolation=cv2.INTER_LINEAR)
        target_path = os.path.join(target_directory,f"myimg{count+1}.jpg")
        count = count+1

        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        cv2.imwrite(target_path,faces_resize)
        #cv2.imshow('Detected_face', faces_resize)


imgs = [x for x in os.listdir('save_img')]
nc = 4
nr = math.ceil(len(imgs)/4)
_, axs = plt.subplots(nr, nc, figsize=(12, 12))
axs = axs.flatten()
for img, ax in zip(imgs, axs):
    image = mpimg.imread('save_img/'+img)
    ax.imshow(image)
plt.show()

# cv2.imshow('Detected faces', img)
#
# cv2.waitKey(0)
