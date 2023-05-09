import cv2

cap = cv2.VideoCapture("./exam_cv/vtest.mp4")
# cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('image', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if(key == 27):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows() 