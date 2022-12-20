from pickletools import pyset
import cv2
import mediapipe as mp
import pyautogui
# cature videos
cap = cv2.VideoCapture(0)
# detecting the hand
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y=0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # calculate frame high and frame width
    frame_height, frame_width, _ = frame.shape
    # convert the RBG
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # procssing the hand detector
    output = hand_detector.process(rgb_frame)
    # print the hand landmark
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            # conver landmark into enum
            landmarks = hand.landmark
            for id, landmarks in enumerate(landmarks):
                x = int(landmarks.x*frame_width)
                y = int(landmarks.y*frame_height)
                # pick the index fingure
                if id == 8:
                    cv2.circle(img=frame, center=(x, y),
                               radius=15, color=(0, 255, 255))
                    # calcate the actually location of x and y
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)

                if id == 4:
                    cv2.circle(img=frame, center=(x, y),
                               radius=15, color=(0, 255, 255))
                    # calcate the actually thumb location of x and y
                    thumb_x= screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    # click when index fingure and thumb
                    if abs(index_y-thumb_y)<17:
                        pyautogui.click()
                        pyautogui.sleep(1)

    #print(hands)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
