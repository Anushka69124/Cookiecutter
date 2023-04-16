import random
import time
import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np
folderpath='frames'
folderpath1='img'
mylist = os.listdir(folderpath1)
mylist  = os.listdir(folderpath)
graphic =[cv2.imread(f'{folderpath}/{imPath}')for imPath in mylist]
graphic =[cv2.imread(f'{folderpath1}/{imPath1}')for imPath1 in mylist]
intro =graphic[0]
kill =graphic[1]
winner = graphic[2]
cam =  cv2.VideoCapture(0)
detector = HandTrackingModule.HandDetector(maxHands=1,detectionCon=0.77)
#sets the minimum confidence threshold for the detection
no = random.randint(1, 5)
    if cur - prev >= no:
        prev = cur
        TIMER = TIMER - no
        if cv2.waitKey(10) & 0xFF == ord('w'):
            win = True
            break

        if isgreen:
            showFrame = cv2.resize(red, (0, 0), fx=0.69, fy=0.69)
            isgreen = False
            ref = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # ref = cv2.GaussianBlur(ref, (21, 21), 0)

        else:
            showFrame = cv2.resize(green, (0, 0), fx=0.69, fy=0.69)
            isgreen = True
    if not isgreen:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # gray = cv2.GaussianBlur(gray, (21, 21), 0)
        frameDelta = cv2.absdiff(ref, gray)
        thresh = cv2.threshold(frameDelta, 20, 255, cv2.THRESH_BINARY)[1]
        change = np.sum(thresh)
        # print(change)
        if change > maxMove:
            break
        camShow = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)

    camH, camW = camShow.shape[0], camShow.shape[1]
    showFrame[0:camH, -camW:] = camShow

#INITILIZING GAME COMPONENTS
#----------------------------------------------------------------
cv2.imshow('Squidgame',cv2.resize(intro,(0,0), fx=0.69, fy=0.69))
cv2.waitKey(1)

while True:
    cv2.imshow('Squid Game', cv2.resize(intro, (0,0), fx=0.69, fy=0.69))
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

    TIMER_MAX = 30
    TIMER =TIMER_MAX
    maxMove = 6500000
    font=cv2.FONT_HERSHEY_SIMPLEX
    cap = cv2.VideoCapture(0)
    frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

win = False

prev = time.time()
prevDoll = prev
showFrame = cv2.resize(green, (0, 0), fx=0.69, fy=0.69)
isgreen = True
sqr_img = graphic[1]
mlsa =  graphic[0]
#INTRO SCREEN WILL STAY UNTIL Q IS PRESSED
gameOver = False
NotWon =True
#GAME LOGIC UPTO THE TEAMS
#-----------------------------------------------------------------------------------------
while not gameOver:
        continue
#LOSS SCREEN
if NotWon:
    for i in range(10):
       #show the loss screen from the kill image read before
        cv2.imshow('Squid Game', cv2.resize(kill, (0, 0), fx=0.69, fy=0.69))

    while True:
        #show the loss screen from the kill image read before and end it after we press q
          cv2.imshow('Squid Game', cv2.resize(kill, (0, 0), fx=0.69, fy=0.69))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break


else:
#WIN SCREEN
#show the win screen from the winner image read before
 cv2.imshow('Squid Game', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
    cv2.waitKey(125)


    while True:
       #show the win screen from the winner image read before and end it after we press q
         cv2.imshow('Squid Game', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
        # cv2.imshow('shit',cv2.resize(graphic[3], (0, 0), fx = 0.5, fy = 0.5))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break


cv2.destroyAllWindows()

