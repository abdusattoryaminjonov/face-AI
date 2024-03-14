import cv2

#cap = cv2.VideoCapture(r'D:\Projects\resourses\vf.avi')
#cap = cv2.VideoCapture(r'D:\Projects\resourses\videos\cars_1.mp4')
cap = cv2.VideoCapture(0)

if (cap.isOpened() == False):
    print("Error opening video file")

haar_cascade = cv2.CascadeClassifier('Haarcascade_frontalface_default.xml')
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

        for (x, y, w, h) in faces_rect:
            face = frame[y:y+h ,x:x+w]
            faces_resize = cv2.resize(face, (150,150),interpolation = cv2.INTER_LINEAR)
            cv2.imshow('myFace', faces_resize)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)


        cv2.imshow('Frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()

cv2.destroyAllWindows()
