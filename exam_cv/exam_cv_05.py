import cv2
import time

cam = cv2.VideoCapture("./exam_cv/vtest.mp4")
if cam.isOpened() == False:
    print
    'Can not open the Camera(vtest)'
    exit()
    
cv2.namedWindow('vtest')

while(True):
    ret, frame = cam.read()
    
    now = time.localtime()
    str = "%d. %d. %d. %d:%d:%d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    
    cv2.putText(frame, str, (0, 100), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 255, 0))
    
    cv2.imshow("vtest", frame)
    
    if cv2.waitKey(10) >= 0:
        break

cam.release()
cv2.destroyAllWindows