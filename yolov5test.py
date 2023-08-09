import torch
import cv2
import pandas as pd
import time
import numpy as np



model = torch.hub.load('ultralytics/yolov5', 'best')

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap=cv2.VideoCapture(0)


count=0
while True:    
   ret,frame = cap.read()   
   count += 1
   if count % 3 != 0:
      continue


   frame=cv2.resize(frame,(1020,760))
   results=model(frame)
   cv2.imshow("test window", frame)
   print(results.pandas().xyxy[0])
   time.sleep(1)

cap.release()
cv2.destroyAllWindows()
