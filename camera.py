from itertools import count
from turtle import color
import cv2 as cv
from cv2 import VideoCapture
import numpy as np
import mediapipe as mp
import poseModule as pm
import time


detector=pm.poseDetector()
dir=0
countt=0
halfwaycount=0
class showVideo(object):

    def __init__(self):
        self.video=cv.VideoCapture(0)
    def __del__(self):
        self.video.release()

    def makecount_zero(self):
        global countt
        countt=0
    def get_frame(self,mode):

        
        global dir
        global countt
        global halfwaycount
        ret,frame=self.video.read()   
        #frame=cv.resize(frame,(1600,1200))
        frame=detector.findPose(frame,False)
        lmlist=detector.findPositions(frame,False)
        bar=650
        per=0
        color=(255,255,255)
        
        if len(lmlist)!=0:
       # detector.findAngle(img,12,14,16,)

            if mode=='tricep':

                angle= detector.findAngle(frame,11,13,15,)
                bar=np.interp(angle,(220,300),(350,100))
                per=np.interp(angle,(220,300),(0,100))

            if mode=='squats':
                angle= detector.findAngle(frame,24,26,28,)
                bar=np.interp(angle,(190,270),(350,100))
                per=np.interp(angle,(190,270 ),(0,100))

            if mode=='jumping_jack':
                angle = detector.findAngle(frame,11,12,14)
                detector.findAngle(frame,26,24,23)
                bar=np.interp(angle,(110,250),(350,100))
                per=np.interp(angle,(110,250 ),(0,100))

            if mode=='bicep_curls':
                angle= detector.findAngle(frame,11,13,15,)
                bar=np.interp(angle,(215,300),(350,100))
                per=np.interp(angle,(215,300 ),(0,100))    

            if mode=='pushup':
                angle= detector.findAngle(frame,11,13,15,)
                bar=np.interp(angle,(200,280),(350,100))
                per=np.interp(angle,(200,280 ),(0,100))   

            if mode=='pullup':
                angle= detector.findAngle(frame,12,14,16,)
                bar=np.interp(angle,(70,140),(350,100))
                per=np.interp(angle,(70,140 ),(0,100))         
       #print (angle,per)
       ## counting curls

            color=(255,255,255)
            if per==100 and countt%1==0:
                color=(0,255,0)
                if dir==0:
                    countt=countt+0.5

            if halfwaycount>5 and countt%1==0.5 and per==100:
                color=(0,255,0)
                dir=1
            if halfwaycount<=5 and countt%1==0.5:
                halfwaycount=halfwaycount+1
                print('halfwaycount: '+str(halfwaycount))
            if per==0 and countt%1==0.5 and halfwaycount>5:
                color=(0,255,0)
                if dir==1:
                    countt=countt+0.5
                    dir=0
                    halfwaycount=0
            print(countt)
            print (countt)       
            cv.rectangle(frame,(500,100),(575,350),color,3)
            cv.rectangle(frame,(500,int(bar)),(575,350),color,cv.FILLED)
        cv.putText(frame,f'{int(per)}%',(500,75),cv.FONT_HERSHEY_PLAIN,4,color,4)

        cv.putText(frame,str(int(countt)),(100,70),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),5)





        ret,jpg=cv.imencode('.jpg',frame)
        return jpg.tobytes()