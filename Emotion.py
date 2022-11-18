# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 13:44:54 2022

@author: Restandsleep
"""

import cv2

from deepface import DeepFace
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

import mysql.connector
import tkinter  as tk 
from tkinter import * 
mydb = mysql.connector.connect(
 host="localhost",  user="root",
      password="admin",
      database = "emot"
    )
print(mydb)
cursor = mydb.cursor()


mydb2 = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database = "Analytics"
)
cursor2 = mydb2.cursor()

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
    
    
    
    
def emotion():
    time_limit=30 #time window
    prevalent_emotion={'angry':0, 'disgust':0 , 'fear':0 ,'happy':0, 'sad':0, 'surprise':0, 'neutral':0}#this dictionary will be used to store the count of each emotion predicted in real time
    #labels={0:'angry', 1:'Disgust', 2:'Fear', 3:'Happy', 4:'Sad', 5:'Surprise', 6:'Neutral'}
    emotion=['angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']
    
    
    faceCascade= cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError('cannot open webcam')
        
    
    while True:
        ret,frame=cap.read()
        result=DeepFace.analyze(frame,actions=['emotion'],enforce_detection=False)
        prevalent_emotion[result['dominant_emotion']]+=1 
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        faces=faceCascade.detectMultiScale(gray,1.1,4)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
        font = cv2.FONT_HERSHEY_SIMPLEX
    
        cv2.putText(frame,result['dominant_emotion'],
                (0,50),
                font,1,
                (0,0,255),
                2,
                cv2.LINE_4);
        cv2.imshow('DEmo video',frame)
     
        if cv2.waitKey(2) & 0xFF == ord('q'):
           break
    
    cap.release()
    cv2.destroyAllWindows()
    emotion = max(prevalent_emotion, key=prevalent_emotion.get)#obtaining the most prevalent emotion(emotion with highest value  stored in the prevalent_emotion dictionary))
    
    for x in prevalent_emotion:
        cursor.execute(""" update emot set duration = duration + {val}  where EMOTION= "{a}" ;""".format(val=prevalent_emotion[x] , a = x))

    mydb.commit()
    
    
    
    if emotion == 'angry':
        song='Relaxing and soothing songs'
    elif emotion == 'sad' or emotion == 'disgust' or emotion == 'fear':
        song='Dance music'
    elif emotion == 'happy' or emotion == 'neutral' or emotion == 'surprise':
        song='Rock Music'
    
        
    api_key='' #enter your API key
    youtube=build('youtube','v3' , developerKey=api_key) #building the service object
    
    request = youtube.search().list(part='snippet',type='video',q=song,maxResults='40')#using the search instance method to search for songs(gives video IDs)
    response=request.execute()
    
    videoIDs=[]
    titles = []

    for i in response['items']:
        videoIDs.append(i['id']['videoId'])#this list stores the video id's of our search results which can be used to obtain the url
    for i in response["items"]:
        titles.append(i["snippet"]["title"])
    
    videoID=random.choice(videoIDs)#selecting a random video from the results based on the search
    #print(videoID)
    url ='https://www.youtube.com/watch?v='+videoID #creating the URL for youtube video
    #print(url)
    
    video = pafy.new(url) #creating a pafy object
    best = video.getbest() #selects the stream with highest resolution
    
    
    media = vlc.MediaPlayer(best.url) #creating media player object
    media.play() 
    
    
    
    cursor2.execute("update tmstp set x = current_timestamp();")
    mydb2.commit()
    
    
    def switch(lang):
        if lang == "angry":
            return 1
        elif lang == "disgust":
            return 2
        elif lang == "fear":
            return 3
        elif lang == "happy":
            return 4
        elif lang == "sad":
            return 5
        elif lang == "surprise":
            return 6
        elif lang == "neutral":
            return 7
    emotion = switch(emotion)
    
    
    
    
    return media , url , song , emotion , videoIDs , titles

def emotion_gui():
    time_limit=30 #time window
    prevalent_emotion={'angry':0, 'disgust':0 , 'fear':0 ,'happy':0, 'sad':0, 'surprise':0, 'neutral':0}#this dictionary will be used to store the count of each emotion predicted in real time
    #labels={0:'angry', 1:'Disgust', 2:'Fear', 3:'Happy', 4:'Sad', 5:'Surprise', 6:'Neutral'}
    emotion=['angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']
    
    
    faceCascade= cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError('cannot open webcam')
        
    
    while True:
        ret,frame=cap.read()
        result=DeepFace.analyze(frame,actions=['emotion'],enforce_detection=False)
        prevalent_emotion[result['dominant_emotion']]+=1 
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        faces=faceCascade.detectMultiScale(gray,1.1,4)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
        font = cv2.FONT_HERSHEY_SIMPLEX
    
        cv2.putText(frame,result['dominant_emotion'],
                (0,50),
                font,1,
                (0,0,255),
                2,
                cv2.LINE_4);
        cv2.imshow('DEmo video',frame)
     
        if cv2.waitKey(2) & 0xFF == ord('q'):
           break
    
    cap.release()
    cv2.destroyAllWindows()
    emotion = max(prevalent_emotion, key=prevalent_emotion.get)#obtaining the most prevalent emotion(emotion with highest value  stored in the prevalent_emotion dictionary))
    
    for x in prevalent_emotion:
        cursor.execute(""" update emot set duration = duration + {val}  where EMOTION= "{a}" ;""".format(val=prevalent_emotion[x] , a = x))
    mydb.commit()
    
 
    
    if emotion == 'angry':
        song='Relaxing and soothing songs'
    elif emotion == 'sad' or emotion == 'disgust' or emotion == 'fear':
        song='Dance music'
    elif emotion == 'happy' or emotion == 'neutral' or emotion == 'surprise':
        song='Rock Music'
    
   
        
    api_key='' #enter your API key
    youtube=build('youtube','v3' , developerKey=api_key) #building the service object
    
    request = youtube.search().list(part='snippet',type='video',q=song,maxResults='40')#using the search instance method to search for songs(gives video IDs)
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
    
    cursor2.execute("update tmstp set x = current_timestamp();")
    mydb2.commit()
    
    
    
    def switch(lang):
        if lang == "angry":
            return 1
        elif lang == "disgust":
            return 2
        elif lang == "fear":
            return 3
        elif lang == "happy":
            return 4
        elif lang == "sad":
            return 5
        elif lang == "surprise":
            return 6
        elif lang == "neutral":
            return 7
    emotion = switch(emotion)
    while True:
        if  keyboard.is_pressed('s'):
            cursor2.execute("""insert into analytics(Searchword , EMOTION , starttime , endtime , duration)VALUES("{song}" , {emote} , (SELECT * FROM tmstp) , CURRENT_TIMESTAMP() , CURRENT_TIMESTAMP() - (SELECT * FROM tmstp) );""".format(song = song , emote = emotion ))
            mydb2.commit()
            media.stop()
            break
        
    
    
