## Image Processing Using Yolo Rasbeery Pi4
The system successfully detects the object specified by the user and keeps it centered in the camera frame.
Pan and tilt mechanisms of the MG966R servo motors responds to the movement of the tracked object.
Terminal  continuously tracks how far the detected location of the center of the object from the centre of the video frame. 

## Assumptions
There will be only one of the specified object in front of the camera to avoid confusion of which object to look at.
If possible testing board numbered 8 will used.

## Parameters
- 50% is set for the detection confidence for objects.
- Maximum Pulse length set as 180deg =2193 and minimum pulse length set as minPulse=771.
- Movement step gain set ar 0.03 for the servos (distanceX*0.03)


## Instructions on The Starting Procedure
0. Download the YoloTrackingWithServo.py file
1. Use the 8 numbered Raspberry Pi4 board. Sevo controls calibrated up for that board specificly. If calibrate servo angles again for the given board which should be easy to modify just change the AngleX and Angle Y variables.
2. Start the Raspberry Pi4
3. Open the Terminal Window
4. Install the yolov8n and yolov8n_ncnn models. Alos intall pigpiod library for servo movements. Lastly make sure models and the program file is in the same directory.
5. Enter the following commands : 
    "source yolo/yoloenv/bin/activate"
    "python3"
    "import ultralytics"
    "exit()"
    "sudo pigpiod"
    "python YoloTrackingWithServo.py"
6. When the  program starts on the terminal it will list 3 object it sees after that it will ask the user which object to track.
7. User needs to enter the name of the object to track
8. After the object name entered camera should be following the given object by the user and user can see the live video feed on the monitor.
9. On the live camera feed user can see the center point of the camera and the line between that center point of the camera to object center point.
10. On terminal user can see the the distance variables in terms of pixels in terms of x, y coordinate differences and the straigth lien distance.
11. Unless the Q keyboard key entered the program should be running indefinitly.  

## List of Components
1. Rasberry Pi4 - For controlling both camera logic and the servos
2. 2 MG966R Servo motors - Pitch and yaw controls
3. HD Rasberry Pi camera
4. Moving camera dock

## Pin Connection for Rasberry Pi4
- Pin 12 -> Servo X CONTROL PIN (bottom servo)
- Pin 13 -> Servo Y CONTROL PIN (top servo)
- Connect both servos to 5V power either on board of the rasberry Pi4 which is PIN2 and PIN4. Connect the ground pins of the servos the grounds on common ground pins on the Pi4 which are 9,6,25,34,39,30. 
- Or connect the power cable which is the red cable of the servos the external power supply and run a common ground between the power supply servos and the Pi4.


## Project status and Roadmap
Project is done based on the rubric requirements. But it can be imporved indefinitly.
 Good areas to imporve in the future:
        1. Camera Calibration
        2. Using a faster computer other than Pi4 for better performance
        4. Code optmizations for improving fps performance it currently runs around 2.1 fps
        5. Making a smoother and faster working ServoControl function to reduce jitters and improve reaction time.


## Used Sources

1. Pigpio library for smooth movement low jitter used on the last experiemnt -> https://abyz.me.uk/rpi/pigpio/examples.html#Python%20code

2. MG966R sevo pulse width is 771 2193 from -> https://www.projectgus.com/2009/07/servo-pulse-width-range-with-arduino/

3. Quick Start Guide: Raspberry Pi with Ultralytics YOLO11 - https://docs.ultralytics.com/guides/raspberry-pi/

4. Youtube video titled: How to Run YOLO Object Detection Models on the Raspberry Pi -> https://www.youtube.com/watch?v=z70ZrSZNi-8

5. MG966R Data Sheet -> https://www.digikey.co.uk/en/htmldatasheets/production/5014637/0/0/1/mg996r

6. Picamera2 Library -> https://pip-assets.raspberrypi.com/categories/652-raspberry-pi-camera-module-2/documents/RP-008156-DS-2-picamera2-manual.pdf?disposition=inline

7. Rasbeery Pi4 PinOUT -> https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/5/GPIO.png


## Authors and acknowledgment
Mehmet Samil Ayoz - Developer

## Support
Contact: ma4123@live.mdx.ac.uk


