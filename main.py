import cv2 as cv


cap = cv.VideoCapture(0)


while(True):
    rec , frame_back = cap.read()
    frame = cv.flip(frame_back, 1)
    # qrcode reader
    detector = cv.QRCodeDetector()
    value , box , _ = detector.detectAndDecode(frame)
    try: 
        pts = box[0].astype(int)
        pt1 = (pts[0][0], pts[0][1])  
        pt2 = (pts[2][0], pts[2][1])  
        cv.rectangle(frame, pt1, pt2, (255, 0, 255), 3)
        cv.putText(frame, value, (10,50), cv.FONT_ITALIC, 1, (25,50,20), 2)
    except:
        print("Not identified")
    



    cv.imshow('hello', frame)

    key_exit = cv.waitKey(5) & 0xFF
    if key_exit == 27:
        break




cv.destroyAllWindows()
cap.release()

