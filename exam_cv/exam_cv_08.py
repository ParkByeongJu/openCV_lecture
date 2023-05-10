import cv2
from math import *
import numpy as np

cv2.namedWindow('Free Fall')

width = 512
heigth = 960
img = np.zeros((heigth, width, 3), np.uint8)

time = ypos = 0
while(True):
    if(ypos + 30) < heigth:
        cv2.circle(img, (256, 30 + ypos), 10, (255, 0, 0), -1)
        time += 1
        ypos = int((9.8 * time ** 2) / 2)
        print(time, ':', ypos)
    cv2.imshow('Clock', img)
    if cv2.waitKey(100) >= 0:
        break
    
cv2.destroyWindow('Free Fall')