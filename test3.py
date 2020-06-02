import cv2
#import RPi.GPIO as GPIO
import datetime
from time import sleep


# make capture object
cap = cv2.VideoCapture(0)

# make detector object
detector = cv2.QRCodeDetector()

# Runn MAIN loop
while True:
    _, img = cap.read() # Read image from capture
    data, bbox, _ = detector.detectAndDecode(img)
    
    
    cv2.imshow("code detector", img)
    if(cv2.waitKey(1) == ord("q")):
        break
    

    # print(data)
    # print(type(data))
    if data != "":
        print(data)
        if data == "test jonas":
            print("Åpneport")
        elif data == "JONAS TES":
            print("STENG port")
        sleep(2)
    else:
        print(".............")
   
    
 
