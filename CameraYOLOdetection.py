import cv2
import numpy
from ultralytics import YOLO
from picamera2 import Picamera2
import math
import pigpio

model=YOLO("yolov8n_ncnn_model") #ncnn is fater 2x
labels = model.names 
objectName=("person")

pi = pigpio.pi()
servoXpin=12
servoYpin=13

minAngle=0
maxAngle=180
maxPulse=180*2193

AngleX=90
AngleY=120

run=1

pi.set_servo_pulsewidth(servoXpin, (771+ (90/180)* (2193-771) ))
pi.set_servo_pulsewidth(servoYpin, (771+ (90/180)* (2193-771) ))

piCamera = Picamera2()                       
config = piCamera.create_video_configuration(main={"format": "RGB888", "size": (640, 480)})
piCamera.configure(config)                          
piCamera.start()     


def moveServos(objectCenterX, objectCenterY):

    global AngleX, AngleY
    
    distanceX = objectCenterX-320
    AngleX = AngleX  - (distanceX*0.03)
    if AngleX < minAngle:
     AngleX=minAngle
    elif AngleX > maxAngle:
     AngleX = maxAngle
    pi.set_servo_pulsewidth(servoXpin,  (771+ (AngleX/180)* (2193-771) ))
        
    
    distanceY = objectCenterY-240
    AngleY = AngleY  - (distanceY*0.03)
    if AngleY < minAngle:
     AngleY=minAngle
    elif AngleY > maxAngle:
     AngleY = maxAngle
    pi.set_servo_pulsewidth(servoYpin,  (771+ (AngleY/180)* (2193-771) ))
    
    





while True:
    
       image = piCamera.capture_array()
       
       imageCenterX=320
       imageCenterY=240
       cv2.circle(image, (imageCenterX, imageCenterY), 10, (0,255,0), -1)
       
       results = model(image ,verbose=False) 
       detections=results[0].boxes
       found =[]
       if run == 1:
            for box in detections:
                classID=int(box.cls.item())
                classname = labels[classID]
                if classname not in found:
                    found.append(classname)
                if len(found) == 3:
                    run=2
                    print("Detected objects: ")
                    for item in found:
                        print(item)
                    choice= input ("enter the name of the object you want to follow:  ")
                    objectName=choice.strip().lower()
                    break
            
        
        
         
       
           
       for i in detections:
           classID = int(i.cls.item())
           classname = labels[classID]
           
           if classname == objectName and i.conf.item() > 0.5:
                print("found the object!")
           
                xyxy = i.xyxy.cpu().numpy().squeeze().astype(int)   
                xMin, yMin, Xmax, Ymax = xyxy  
                objectCenterX = ((Xmax + xMin ) //2 )
                objectCenterY = ((Ymax + yMin ) //2 )
                moveServos(objectCenterX, objectCenterY)
           
           
                cv2.rectangle(image, (xMin, yMin), (Xmax, Ymax), (0, 255, 0), 5)
                cv2.line(image, (320, 240), (objectCenterX, objectCenterY), (255, 0, 0), 2)
               
                print(f"Distance X: {objectCenterX - 320}, Distance Y: {objectCenterY - 240}")  # print pixel distances
                print(f"Total Distance: {math.sqrt( ((objectCenterX - 320)**2) + ((objectCenterY - 240)**2) )}") 
       


       cv2.imshow("Tracking", image)
       key = cv2.waitKey(1) & 0xFF                   
        
       if key == ord('q'):                             
         break
       
    
    
