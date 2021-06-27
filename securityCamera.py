import cv2
import winsound

cap = cv2.VideoCapture(0)
wCam , hCam = 640 , 480
cap.set(3 , wCam)
cap.set(4 , hCam)

while cap.isOpened():
    success , img1 = cap.read()
    success , img2 = cap.read()

    diff = cv2.absdiff(img1 , img2)
    gray = cv2.cvtColor(diff , cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray , (5,5) ,0)
    _ , thresh = cv2.threshold(blur , 20, 255 , cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh , None , iterations=3)
    
    contours  , _ = cv2.findContours(dilated , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # cv2.drawContours(img1 , contours ,-1 , (0,255,0) , 2 )
    
    # detecting bigger contours
    for c in contours:
        if cv2.contourArea(c)<5000:
            continue
        x , y , w, h = cv2.boundingRect(c)
        cv2.rectangle(img1 , (x,y) , (x+w , y+h) , (0,255,0) , 2)
        # winsound.Beep( 500 , 200)
        winsound.PlaySound('alert.wav' , winsound.SND_ASYNC)

    cv2.imshow("Security Cam" , img1)

    if cv2.waitKey(1)== ord('q'):
        break