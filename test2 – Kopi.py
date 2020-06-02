import cv2
#import RPi.GPIO as GPIO
import datetime
from time import sleep




def les():
    # make capture object
    cap = cv2.VideoCapture(0)
    
    # make detector object
    detector = cv2.QRCodeDetector()
    _, img = cap.read() # Read image from capture
    data, bbox, _ = detector.detectAndDecode(img)
    
    
    cv2.imshow("code detector", img)
    cv2.waitKey(1)
    
    if data == "JONAS TEST":
        ok = True
    else:
        ok = False
        
    return data, ok

# Runn MAIN loop
while True:

    if les()[1] == True:
        print("åpne opp port!!!")
        sleep(0.5)
        
      
   
    
 
    print(".............")