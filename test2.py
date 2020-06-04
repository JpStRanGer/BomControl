import cv2
import RPi.GPIO as GPIO
import datetime
from time import sleep

# make capture object
cap = cv2.VideoCapture(0)

# make detector object
detector = cv2.QRCodeDetector()

# initialize GPIO
GPIO.setmode(GPIO.BCM)


# Set relay pins as output
GPIO.setup(21, GPIO.OUT)



# Runn MAIN loop
while True:
    retval, img = cap.read() # Read image from capture # retval = True If no frames has been grabbed (camera has been disconnected, or there are no more frames in video file),
    data, bbox, qr = detector.detectAndDecode(img) # Detect And Decode image from variable
    
    # check if file exist
    if(bbox is not None):
        for i in range(len(bbox)):
            cv2.line(img,
                     start_point = tuple(bbox[i][0]), 
                     end_point = tuple(bbox[(i+1) % len(bbox)][0]), 
                     color = (255, 0, 255), 
                     thickness = 2
                     )
        cv2.putText(img, 
                    text = data, 
                    org = (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), 
                    font = cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale = 0.5, 
                    color = (0, 255, 0), 
                    thickness = 2,
                    lineType = None,
                    bottomLeftOrigin = None)
    if data:
        print("data found: ", data)
        sleep (0.500)
    if data=="TEST JONAS":
        GPIO.output(21, 1)
        sleep (2)
        GPIO.output(21, 0)
        
       
   
    cv2.imshow("code detector", img)
    if(cv2.waitKey(1) == ord("q")):
        break
