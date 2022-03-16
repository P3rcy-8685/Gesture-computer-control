import cv2
import mediapipe as mp
import math
import pyautogui
import time 
cap=cv2.VideoCapture(1)
mpHands=mp.solutions.hands
hands=mpHands.Hands(False)
mpDraw=mp.solutions.drawing_utils
def dis(x1,y1,x2,y2):
    return math.hypot(x1-x2,y1-y2)
while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    if results.multi_hand_landmarks:
            allHands=[]
            for handtype,handlms in zip(results.multi_handedness,results.multi_hand_landmarks):
                myHand={}
                lmList=[]
                xList=[]
                yList=[]
                for id,lm in enumerate(handlms.landmark):
                    h, w,c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([cx,cy])
                    xList.append(cx)
                    yList.append(cy)
                myHand["lmList"]=lmList
                if handtype.classification[0].label=="Right":
                    myHand["type"]="Left"
                else:
                    myHand["type"]="Right"
                allHands.append(myHand)
            else:
                if handtype.classification[0].label=="Left":
                    ind=dis(xList[4],yList[4],xList[8],yList[8])
                    mid=dis(xList[4],yList[4],xList[12],yList[12])
                    ring=dis(xList[4],yList[4],xList[16],yList[16])
                    pink=dis(xList[4],yList[4],xList[20],yList[20])
                    if ind<70 and mid<70 and ring<70 and pink<70:       
                        pyautogui.hotkey('winleft', 'd')
                        time.sleep(1)
    cv2.imshow("Image",img)
    cv2.waitKey(1)