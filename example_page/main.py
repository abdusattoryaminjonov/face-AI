import cv2

#cap = cv2.VideoCapture(r'D:\Projects\resourses\videos\SMARTBASE3.mp4')
cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
