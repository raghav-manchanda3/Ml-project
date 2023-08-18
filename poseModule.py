import cv2 as cv
#from cv2 import VideoCapture
#from cv2 import FONT_HERSHEY_COMPLEX
#from cv2 import COLOR_BGR2RGB
import mediapipe as mp
import time
import math

#mpDraw=mp.solutions.drawing_utils
#mppose=mp.solutions.pose
#pose=mppose.Pose()


class poseDetector():
    
    def __init__(self,mode=False,model_complaxity=1,smooth_landmark=True,upBody=False,smooth=True, detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.model_complaxity=model_complaxity
        self.smooth_landmark=smooth_landmark
        self.upBody=upBody
        self.smooth=smooth
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.mpDraw=mp.solutions.drawing_utils
        self.mppose=mp.solutions.pose
        self.pose=self.mppose.Pose(self.mode,self.model_complaxity,self.smooth_landmark,self.upBody,self.smooth,self.detectionCon,self.trackCon)

    

    def findPose(self,frame,draw=True):
        frameRGB=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        self.results=self.pose.process(frameRGB)

        if self.results.pose_landmarks:
            if draw:
            
                self.mpDraw.draw_landmarks(frame,self.results.pose_landmarks,self.mppose.POSE_CONNECTIONS)

        return frame



    def findPositions(self,frame,draw=True):
        self.lmList=[]
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c=frame.shape
                cx,cy=int(w*lm.x),int(h*lm.y)
                self.lmList.append([id,cx,cy])
                if draw:
                        cv.circle(frame ,(cx,cy),5,(255,0,0),cv.FILLED)
        return self.lmList   





    def findAngle(self,frame,p1,p2,p3,draw=True):
        x1,y1=self.lmList[p1][1:]
        x2,y2=self.lmList[p2][1:]
        x3,y3=self.lmList[p3][1:]

        # angle
        angle=math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2))
        if angle<0:
            angle=360+angle
       # print(angle)

        if draw:
            cv.line(frame,(x1,y1),(x2,y2),(0,255,255))
            cv.line(frame,(x2,y2),(x3,y3),(0,255,255))
            cv.circle(frame,(x1,y1),10,(0,0,255),cv.FILLED)
            cv.circle(frame,(x1,y1),15,(0,0,255),2)
            cv.circle(frame,(x2,y2),10,(0,0,255),cv.FILLED)
            cv.circle(frame,(x2,y2),15,(0,0,255),2)
            cv.circle(frame,(x3,y3),10,(0,0,255),cv.FILLED)
            cv.circle(frame,(x3,y3),15,(0,0,255),2)
            cv.putText(frame,str(int(angle)),(x2-50,y2 +50),cv.FONT_HERSHEY_PLAIN,2,(0,0,255),2)         

        return angle            
                     
#####################################################################

def main():
    pTime=0   

      
    cTime=0
    Time=0
    capture=cv.VideoCapture(r'C:\Users\Aniket\Desktop\project1\abc\pushup.mp4')
    detector=poseDetector()

    while True:
        isTrue,frame=capture.read()
        frame=detector.findPose(frame)
        lmList=detector.findPositions(frame)
        if len(lmList)!=0:
            detector.findAngle(frame,12,14,16)
            print(lmList[14])
            cv.circle(frame,(lmList[14][1],lmList[14][2]),15,(0,0,255),cv.FILLED)
        print(lmList)
        cTime=time.time()
        fps=1/(cTime-pTime)
    
        pTime=cTime

        cv.putText(frame,str('FPS: ')+str(int(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,1,(255,0,255),3)

        cv.imshow('Video',frame)


        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    capture.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()