import cv2

class qrReader:
    """
    Dette er en klasse for å ta bilder med webcamera og identifisere QR-koder
    takePIC
    readQr
    drawBox
    showImg
    getImg
    getData
    """
    def __init__(self):
        
        # make capture object
        self._cap = cv2.VideoCapture(0)
        
        # make detector object
        self._detector = cv2.QRCodeDetector()
    
    def takePic(self):
         self._retval, self._img = self.cap.read() # Read image from capture # retval = True If no frames has been grabbed (camera has been disconnected, or there are no more frames in video file),
    
    def readQr(self):
        self._data, self._bbox, self._qr = self.detector.detectAndDecode(self.img) # Detect And Decode image from variable
    
    def drawBox(self):
        # check if file exist
        if(self._bbox is not None):
            for i in range(len(self._bbox)):
                cv2.line(self._img,
                         start_point = tuple(self._bbox[i][0]), 
                         end_point = tuple(self._bbox[(i+1) % len(self._bbox)][0]), 
                         color = (255, 0, 255), 
                         thickness = 2
                         )
            cv2.putText(self._img, 
                        text = self._data, 
                        org = (int(self._bbox[0][0][0]), int(self._bbox[0][0][1]) - 10), 
                        font = cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale = 0.5, 
                        color = (0, 255, 0), 
                        thickness = 2,
                        lineType = None,
                        bottomLeftOrigin = None)
    def showImg(self):
        cv2.imshow("Code Detectror",self._img)
        cv2.waitKey(1)
        
    def getImg(self):
        try:
            return self._img
        except NameError:
            print("Det er ikke tatt noe bilde enda...")
    
    def getData(self):
        try:
            return self._data
        except NameError:
            print("Det er ingen variabel som heter DATA...")
            
if __name__ == "__main__":
    import time
    
    
    QR_reader = qrReader() # setter opp kamera-scanner-object (Gjør ting klart)
    
    while(True):
        
        print("Ta bilde")
        QR_reader.takePic() # Ta bilde
        
        print("Scan bilde og let etter QR-kode")
        QR_reader.readQr() # Scan bilde og let etter QR-kode
        
        print("Tegn inn en boks rundt QR-koden og skrive dataen i tekst under bildet.")
        QR_reader.drawBox() # Tegn inn en boks rundt QR-koden og skrive dataen i tekst under bildet.
        
        print("")
        QR_reader.showImg()