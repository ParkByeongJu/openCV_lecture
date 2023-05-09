import numpy as py
import cv2 as cv

img = cv.imread("iu.jpg")

height = img.shape[0]
width = img.shape[1]

for y in range(0,height):
    img.itemset(y, int(width / 2), 0, 0)
    img.itemset(y, int(width / 2), 1, 0)
    img.itemset(y, int(width / 2), 2, 255)
for x in range(0, width):
    img.itemset(int(height / 2), x, 0, 255)
    img.itemset(int(height / 2), x, 1, 0)
    img.itemset(int(height / 2), x, 2, 0)
    
cv.imshow('win', img)

cv.waitKey(0)