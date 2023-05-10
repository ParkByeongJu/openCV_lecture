import cv2
import numpy as np

def nothing():
    pass

cv2.namedWindow('RGB Track Bar')
cv2.createTrackbar('Red color', 'RGB Track Bar', 0, 255, nothing)
cv2.createTrackbar('Green color', 'RGB Track Bar', 0, 255, nothing)
cv2.createTrackbar('Blue color', 'RGB Track Bar', 0, 255, nothing)

cv2.setTrackbarPos('Red color', 'RGB Track Bar', 125)
cv2.setTrackbarPos('Green color', 'RGB Track Bar', 125)
cv2.setTrackbarPos('Blue color', 'RGB Track Bar', 125)

img = np.zeros((512, 512, 3), np.uint8)

while(1):
    redval = cv2.getTrackbarPos('Red color', 'RGB Track Bar')
    greenval = cv2.getTrackbarPos('Green color', 'RGB Track Bar')
    blueval = cv2.getTrackbarPos('Blue color', 'RGB Track Bar')
    
    cv2.rectangle(img, (0, 0), (512, 512), (blueval, greenval, redval), -1)
    cv2.imshow('RGB Track Bar', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()