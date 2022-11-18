from tensorflow.keras.models import load_model

model=load_model(r'weights.h5')

import cv2
import mediapipe as mp
import math
from keras.preprocessing import image
import numpy as np
import sv_ttk
import tkinter 
from PIL import ImageTk, Image 

import tensorflow as tf
from tensorflow import keras
import imutils
from tensorflow.keras.models import load_model
import numpy as np
from imutils import face_utils
import cv2
import time
import webbrowser

import vlc 
import random
import pafy
import pickle
from googleapiclient.discovery import build
import keyboard
emptyt=()
import pyttsx3
engine = pyttsx3.init()
class HandDetector:
    """
    Finds Hands using the mediapipe library. Exports the landmarks
    in pixel format. Adds extra functionalities like finding how
    many fingers are up or the distance between two fingers. Also
    provides bounding box info of the hand found.
    """
    
    def __init__(self, mode=False,maxHands=2, detectionCon=0.5, minTrackCon=0.5):
        """
        :param mode: In static mode, detection is done on each image: slower
        :param maxHands: Maximum number of hands to detect
        :param detectionCon: Minimum Detection Confidence Threshold
        :param minTrackCon: Minimum Tracking Confidence Threshold
        """
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.minTrackCon = minTrackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon, min_tracking_confidence = self.minTrackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingers = []
        self.lmList = []

    def findHands(self, img,flag, draw=True, flipType=True):
        """
        Finds hands in a BGR image.
        :param img: Image to find the hands in.
        :param draw: Flag to draw the output on the image.
        :return: Image with or without drawings
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
        self.results = self.hands.process(imgRGB)
        allHands = []
        h, w, c = img.shape
        if  self.results.multi_hand_landmarks:
            for handType,handLms in zip(self.results.multi_handedness,self.results.multi_hand_landmarks):
                myHand={}
                ## lmList
                mylmList = []
                xList = []
                yList = []
                for id, lm in enumerate(handLms.landmark):
                    px, py = int(lm.x * w), int(lm.y * h)
                    mylmList.append([px, py])
                    xList.append(px)
                    yList.append(py)

                ## bbox
             
                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                boxW, boxH = xmax - xmin, ymax - ymin
                bbox = xmin, ymin, boxW, boxH
                cx, cy = bbox[0] + (bbox[2] // 2), \
                         bbox[1] + (bbox[3] // 2)

                myHand["lmList"] = mylmList
                myHand["bbox"] = bbox
                myHand["center"] =  (cx, cy)

                if flipType:
                    if handType.classification[0].label =="Right":
                        myHand["type"] = "Left"
                    else:
                        myHand["type"] = "Right"
                else:myHand["type"] = handType.classification[0].label
                allHands.append(myHand)
            
                ## draw
                if draw:
                    
                    cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
                                  (bbox[0] + bbox[2] + 20, bbox[1] + bbox[3] + 20),
                                  (255, 0, 255), 2)
                    cv2.putText(img,myHand["type"],(bbox[0] - 30, bbox[1] - 30),cv2.FONT_HERSHEY_PLAIN,
                                2,(255, 0, 255),2)
        if not allHands:
              
             if flag==1:
              engine.say('Hand not detected')
              engine.runAndWait()
             
             return allHands,img,emptyt
        else:
             return allHands,img,bbox
       

  

def main(media):
    
    cap = cv2.VideoCapture(0)
    
   

  
    class1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    detector = HandDetector(detectionCon=0.8, maxHands=2)
    flag=0
    c=0
    d=0
    while True:
        # Get image frame
        success, img = cap.read()
        # Find the hand and its landmarks
     
        if(img is not None):
     
            hands,img,coor= detector.findHands(img,flag)  # with draw
            
            # hands = detector.findHands(img, draw=False)  # without draw
            
            cv2.imshow("Image", img)
            if not hands:          
              continue
           
            test_image=img[coor[1] - 20 : coor[1] + coor[3] + 20 , coor[0] - 20 : coor[0] + coor[2] + 20]
            test_image=cv2.resize(test_image,(50,50))
            test_image=np.asarray(test_image)
            test_image=np.expand_dims(test_image, axis=0)
            result=class1[np.argmax(model.predict(test_image))]
            print(result)
            if result == 15:
                c+=1
            else:
                c=0
                
            if result == 0 and flag!=1:
                 media.pause()
                 flag=1
            elif c==7:
                media.play()
                flag=0
            if  result==18:
                d+=1
            else:
                d=0
            if d==8:
                break
         
    
            if cv2.waitKey(10) & 0xFF == ord('q'):
               break
           
    cap.release()
    cv2.destroyAllWindows()



def play(q): 
    global media
    
    if(q!="stop_media"):
        api_key='' #enter your API key
        youtube=build('youtube','v3' , developerKey=api_key) #building the service object
        
        request = youtube.search().list(part='snippet',type='video',q=q,maxResults='40')#using the search instance method to search for songs(gives video IDs)
        response=request.execute()
        
        videoIDs=[]
        
        for i in response['items']:
            videoIDs.append(i['id']['videoId'])#this list stores the video id's of our search results which can be used to obtain the url
        
        
        videoID=random.choice(videoIDs)#selecting a random video from the results based on the search
        #print(videoID)
        url ='https://www.youtube.com/watch?v='+videoID #creating the URL for youtube video
        #print(url)
        
        video = pafy.new(url) #creating a pafy object
        best = video.getbest() #selects the stream with highest resolution
        
        media = vlc.MediaPlayer(best.url) #creating media player object
        media.play()
        main(media)
    else:
       
        media.stop()
def stop(media):
    media.stop()
        


