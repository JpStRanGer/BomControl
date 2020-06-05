import cv2
import datetime
from time import sleep

# make capture object
cap = cv2.VideoCapture(0)

# make detector object
detector = cv2.QRCodeDetector()



# Runn MAIN loop
while True:
    # retval, img = cap.read() # Read image from capture # retval = True If no frames has been grabbed (camera has been disconnected, or there are no more frames in video file),
    img = cv2.imread("TEST JONAS 2.png")
    
    data, bbox, qr = detector.detectAndDecode(img) # Detect And Decode image from variable
# =============================================================================
#     bbox inneholder informasjon (kordinater,x,y) om kantene til boksen der 0=oppVenstre, 1=oppHøyre, 2=nedVestre, 3=nedHøyre 
# =============================================================================
    
    # check if file exist
    if(bbox is not None):
        for i in range(len(bbox)):
            cv2.line(img,
                     pt1 = tuple(bbox[i][0]), 
                     pt2 = tuple(bbox[(i+1) % len(bbox)][0]), 
                     color = (255, 0, 255), 
                     thickness = 2
                     )
        cv2.putText(img, 
                    text = data, 
                    org = (int(bbox[3,0,0]), int(bbox[3,0,1]) + 16), 
                    fontFace = cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale = 0.5, 
                    color = (0, 255, 0), 
                    thickness = 1,
                    lineType = False,
                    bottomLeftOrigin = False)
        
    if data == None:
        print("DATA IS NONE!! : ", data)
    elif len(data) != 0:
        print("data found: ", data)
    elif data == "":
        print("data found: lenght = ", len(data))
    elif data=="TEST JONAS":
        print("################## data found: ", data)
        sleep (5)
        
       
   
    cv2.imshow("code detector", img)
    if(cv2.waitKey(1) == ord("q")):
        break
