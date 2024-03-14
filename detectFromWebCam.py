import cv2
cap = cv2.VideoCapture(r'D:\Projects\resourses\vf.avi')
haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
        i = 0
        for (x, y, w, h) in faces_rect:
            face = frame[y:y+h, x:x+w]
            cv2.imshow('face'+str(i), face)
            i = i + 1
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()