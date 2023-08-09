import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from yolov5 import detect
import servo
import time
import timeit
import torch
from models.common import DetectMultiBackend


#model=YOLO('best (1).pt')


#def RGB(event, x, y, flags, param):
#    if event == cv2.EVENT_MOUSEMOVE :  
#        colorsBGR = [x, y]
#        print(colorsBGR)
        
#cv2.setMouseCallback('RGB', RGB)

cap=cv2.VideoCapture(0)

device=''


my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")
#print(class_list)
count=0

#model = detect.run(weights = 'best.pt', source = 'Trash.jpg', justGettingModel = True)

model = torch.hub.load("ultralytics/yolov5","custom","best.pt")
while True:    
    ret,frame = cap.read()   
    #count += 1
    #if count % 3 != 0:
    #    continue


    frame=cv2.resize(frame,(1020,760))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #frame=cv2.resize(frame,(64,48))
    
    #results=model.predict(frame)
 #   print(results)
    #a=results[0].boxes.boxes
    #px=pd.DataFrame(a).astype("float")
#    print(px)
#    for index,row in px.iterrows():
#        print(row)
# 
#        x1=int(row[0])
#        y1=int(row[1])
#        x2=int(row[2])
#        y2=int(row[3])
#        d=int(row[5])
#        #c=class_list[d]
#        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2) 
#        cv2.putText(frame,str(d),(x1,y1),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)
    #cv2.imshow("RGB", frame)
    #cv2.imwrite("Trash.jpg",frame)
    #detection = detect.run(weights = 'best.pt', source = 'Trash.jpg', model=model, modelGiven = True)#, nosave = True)
    #visualize = increment_path(save_dir / Path(path).stem, mkdir=False) if visualize else False
    pred = model(frame)
    
    pred.show()
    #pred.show()
    #print(timeit.Timer('detect.run(weights = "best.pt", source = "Trash.jpg", model=model, modelGiven = True)').timeit(number=1))
    pred = str(pred).split('\n')[0].split(' ')[-1]
    print('\n' + str(pred) + '\n')
    if not pred == 'predictions)':
        servo.dump(pred)
    #cv2.imshow("RGB",cv2.imread("yolov5/runs/detect/withDet.jpg"))
    time.sleep(1)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
#cv2.destroyAllWindows()
