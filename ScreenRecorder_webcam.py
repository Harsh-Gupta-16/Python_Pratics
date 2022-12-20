from PIL import ImageGrab
from PIL.Image import fromarray
import numpy as np
import cv2
import datetime
from win32api import GetSystemMetrics


width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp =  datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_name = f'ScreenRecorderWebcam_{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
captured_video = cv2.VideoWriter(file_name,fourcc,20.0,(width,height))

# starting the first camera
webcam = cv2.VideoCapture(0)

while True:
    img = ImageGrab.grab(bbox=(0,0,width,height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _,frame = webcam.read()
    fr_height, fr_width, _ = frame.shape
    # print(fr_height, fr_width)
    img_final[0:fr_height,0:fr_width,:]=frame[0:fr_height,0:fr_width,:]
    cv2.imshow('Screen Recording', img_final)
    # cv2.imshow('webcam', frame)
    
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break
