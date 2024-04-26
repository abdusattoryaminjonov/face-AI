# Importing Libraries
import cv2
import mediapipe as mp

# Used to convert protobuf message to a dictionary.
from google.protobuf.json_format import MessageToDict

# Initializing the Model
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=0,
    min_detection_confidence=0.70,
    min_tracking_confidence=0.60,
    max_num_hands=10)

# Start capturing video from webcam
cap = cv2.VideoCapture(0)



while True:
    # Read video frame by frame
    success, img = cap.read()

    # Flip the image(frame)
    img = cv2.flip(img, 1)

    # Convert BGR image to RGB image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the RGB image
    results = hands.process(imgRGB)
    lhand = 0
    rhand = 0

    # If hands are present in image(frame)
    if results.multi_hand_landmarks:

        # Both Hands are present in image(frame)
        # or hands == 3 or hands == 4 or hands == 5 or hands == 6 or hands < 6
        if len(results.multi_handedness) == 2 :

            # Display 'Both Hands' on the image
            cv2.putText(img, 'Both Hands', (250, 50),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1.5, (0, 255, 0), 2)

        # If any hand present
        else:
            for i in results.multi_handedness:

                # Return whether it is Right or Left Hand
                label = MessageToDict(i)['classification'][0]['label']

                if label == 'Left':
                    lhand += 1

                if label == 'Right':
                    rhand += 1

                    # Display the count of left and right hands
                cv2.putText(img, 'Left Hands: ' + str(lhand), (20, 50), cv2.FONT_HERSHEY_COMPLEX,
                            1, (0, 255, 0), 2)
                cv2.putText(img,str(rhand)+'Right Hands: ', (350, 50), cv2.FONT_HERSHEY_COMPLEX,
                            1, (0, 0, 255), 2)

                # Display Video and when 'q'
    # is entered, destroy the window
    cv2.imshow('Image', img)
    if cv2.waitKey(30) & 0xff == ord('q'):
        break
