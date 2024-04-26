import os
import cv2


cap = cv2.VideoCapture(0)
haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count=0

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
        c = 0
        for (x, y, w, h) in faces_rect:
            target_directory = 'C:/Users/asus/PycharmProjects/pythonProject/save_img/'

            face = frame[y:y+h, x:x+w]
            faces_resize = cv2.resize(face, (150, 150), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('face'+str(c), faces_resize)
            c = c + 1

            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            folder_path = "save_img"

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            if count % 5 == 0 or count % 5 == 1:
                save_path = os.path.join(target_directory,f"face_{count}.jpg")
                cv2.imwrite(save_path, faces_resize)
            count += 1


        cv2.imshow('Frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q') or count == 60:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()