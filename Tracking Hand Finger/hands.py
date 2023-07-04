import cv2
import mediapipe as mp
import numpy as np
mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles

cam=cv2.VideoCapture(0)
with mp_hands.Hands(model_complexity=0,min_detection_confidence=0.5,min_tracking_confidence=0.5)as hands:
    while cam.isOpened():
        success,image=cam.read()
        imageWidth,imageHeight=image.shape[:2]
        if not success:
            continue
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        results=hands.process(image)
        image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks,
                                      mp_hands.HAND_CONNECTIONS,
                                      mp_drawing_styles.get_default_hand_landmarks_style(),
                                      mp_drawing_styles.get_default_hand_connections_style())
            cv2.imshow('Hand Tracking',image)
            if cv2.waitKey(5) & 0xFF == 27:
                break
cam.release()