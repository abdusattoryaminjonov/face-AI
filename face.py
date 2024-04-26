# import the necessary packages
import os

import numpy as np
import cv2

files_path = [x for x in os.listdir('images')]

net = cv2.dnn.readNetFromCaffe('service/deploy.prototxt.txt', 'service/res10_300x300_ssd_iter_140000.caffemodel')

for f in files_path :
    source_path = 'C:/Users/asus/PycharmProjects/pythonProject/images/' + f
    target_directory = 'C:/Users/asus/PycharmProjects/pythonProject/save_img/'

    image = cv2.imread(source_path)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (160, 160)), 1.0,(160, 160), (104.0, 177.0, 123.0))

    folder_path = "save_img"

    net.setInput(blob)
    detections = net.forward()
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        count = len(files)
        print("Number of files in the folder:", count)
    else:
        print("Folder does not exist or is not a directory.")

    for i in range(0, detections.shape[2]):

        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            # cv2.rectangle(image, (startX, startY), (endX, endY),
            #     (0, 0, 255), 2)
            # cv2.putText(image, text, (startX, y),
            #     cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

            face = image[startY:endY, startX:endX].copy()
            faces_resize = cv2.resize(face, (160, 160), interpolation=cv2.INTER_LINEAR)
            save_path = os.path.join(target_directory, f)
            cv2.imwrite(save_path, faces_resize)

# cv2.imshow("Output", image)
# cv2.waitKey(0)