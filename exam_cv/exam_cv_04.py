import cv2
import numpy as np

def draw_rectangle(event, x, y, flags, aram):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(img, (x + 150 , y + 150), (x + 50, y + 50), (255, 0, 0), -1)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img, (x, y), (x + 50, y + 50), (0, 255, 0), -1)
        

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()