import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from yolov5 import detect
import servo
import time

cap=cv2.VideoCapture(0)

while True:    
    ret,frame = cap.read()   
    


    frame=cv2.resize(frame,(1020,760))
    cv2.imwrite("Trash.jpg",frame)
    detection = detect.run(weights = 'best.pt', source = 'Trash.jpg')
    print(detection)
    servo.dump(detection)
    #time.sleep(1)
    if cv2.waitKey(1)&0xFF==27:
        break
        
cap.release()
