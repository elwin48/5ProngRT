import cvzone
import cv2
from serial import Serial
from cvzone import HandDetector


frameWidth = 640
frameHeight = 480
brightnessImage = 130


cap = cv2.VideoCapture(0)
cap.set(10, brightnessImage)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

mySerial = cvzone.SerialObject("COM7", 9600, 1)

detector = HandDetector(maxHands=1, detectionCon=0.5)
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if lmList:
        fingers = detector.fingersUp()
        print(fingers)
        mySerial.sendData(fingers)
        #val = '$' + ''.join(str(e) for e in fingers)
       # mySerial.write(val.encode())
    cv2.imshow("Image", img)
    cv2.waitKey(1)