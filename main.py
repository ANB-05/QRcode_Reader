import cv2 as cv


cap = cv.VideoCapture(0)


while(True):
    rec , frame_back = cap.read()
    frame = cv.flip(frame_back, 1)
    cv.imshow('hello', frame)
    
    

    key_exit = cv.waitKey(5) & 0xFF
    if key_exit == 27:
        break




cv.destroyAllWindows()
cap.release()

