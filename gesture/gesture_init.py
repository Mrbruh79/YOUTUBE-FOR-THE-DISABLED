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
import gesture.handtracking as handtracking










def gesture():    

    root = tkinter.Tk()
    sv_ttk.use_dark_theme()
    root.title("GESTURE RECOGNITION")
    canvas = tkinter.Canvas(root,width=800 ,height=500)
    
    inputtxt = tkinter.Text(root,height = 5,width = 20)
    inputtxt.pack()
    
    media = ""
    
    
    
    # Button Creation
    video = tkinter.Button(root,text = "Play media", command = lambda:handtracking.play(inputtxt.get(1.0, "end-1c") ))
    video.pack()
    close = tkinter.Button(root,text = "Stop media", command = lambda:handtracking.play("stop_media"))
    close.pack()
    # Label Creation
    root.mainloop()
    
    
    
def play_from_speech(media):
    root = tkinter.Tk()
    sv_ttk.use_dark_theme()
    root.title("GESTURE RECOGNITION")
    canvas = tkinter.Canvas(root,width=800 ,height=500)
    handtracking.main(media)
    

    
    
    
    # Button Creation
    close = tkinter.Button(root,text = "Stop media", command = lambda:media.stop())
    close.pack()
    ex = tkinter.Button(root,text = "EXIT", command = lambda:root.quit())
    ex.pack()
    root.mainloop()
