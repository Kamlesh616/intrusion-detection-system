import cv2
from cvzone.PoseModule import PoseDetector
import send
import time

detector = PoseDetector()
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
l = []
flag = True

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    imlist, bbox = detector.findPosition(img)
    
    if len(imlist) > 0:
        print("Human Detected")
        l.append(1)
        
        # Save the frame with detection
        if len(l) > 50 and flag:
            flag = False
            timestamp = int(time.time())
            filename = f'detection_{timestamp}.jpg'
            cv2.imwrite(filename, img)
            send.sendSms(filename)
    
    cv2.imshow("Output", img)
    q = cv2.waitKey(1)
    if q == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
