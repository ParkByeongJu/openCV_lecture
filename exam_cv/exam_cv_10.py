import cv2
from math import *
import numpy as np

cv2.namedWindow('Pibonacci graphic')

width = 960
heigth = 960
img = np.zeros((heigth, width, 3), np.uint8)

init_posx = 480
init_posy = 480

drawing_unit = 5
idx, a, b = 0, 0, 1

while a < 70:
    cv2.imshow('Pibonacci graphic', img)
    a,b = b, a + b
    Begin_Ang = int(90 * (idx % 4))
    End_Ang = int(90 * (idx % 4 + 1))
    if Begin_Ang == 0:
        init_posx -= (b - a) * drawing_unit
    elif Begin_Ang == 90:
        init_posy -= (b - a) * drawing_unit
    elif Begin_Ang == 180:
        init_posx += (b - a) * drawing_unit
    elif Begin_Ang == 270:
        init_posy += (b - a) * drawing_unit
        
    print(idx, 'turn : ', 'Pibonacci number -', b)
    cv2.ellipse(img, (init_posx, init_posy), (b * drawing_unit, b * drawing_unit), 0, Begin_Ang, End_Ang, (0,255, 0), 2)
    idx += 1
    
while (True):
    if cv2.waitKey(10) >= 0:
        break

cv2.destroyAllWindows('Pibonacci graphic')