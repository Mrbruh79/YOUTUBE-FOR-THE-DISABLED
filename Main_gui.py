# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:49:34 2022

@author: Restandsleep
"""
import sv_ttk
import tkinter
from PIL import ImageTk, Image 
import os
import gesture.handtracking as handtracking
import gesture.gesture_init as gesturein
import Emotion


root = tkinter.Tk()
sv_ttk.use_dark_theme()
root.title("software engineering project")
canvas = tkinter.Canvas(root,width=800 ,height=500)
canvas.grid(columnspan=5)
canvas.grid(rowspan=5)
img = Image.open(r"youtube_logo_dark.jpg")
img = img.resize((200,125))

abb = 0
img = ImageTk.PhotoImage(img)
def emotion2():

    Emotion.emotion_gui()

   
def voice():
    os.system(r"python STT.py")

    
def gesture():
    gesturein.gesture()
    
def analytics():
    os.system(r"python Analytics.py")


    
# Create a Label Widget to display the text or Image
label = tkinter.Label(root, image = img , width = 200 , height = 125)
label.grid(column=3,row=2)
header=tkinter.Label(root,text="YOUTUBE PLAYER FOR THE DISABLED",font=("Franklin Gothic Demi",30),fg="WHITE")
header.grid(column=3,row=3)
button1=tkinter.Button(root,text="EMOTION",font=("Franklin Gothic Demi",20),fg="yellow",command=lambda:emotion2())
button1.grid(column=0,row=5)
button2=tkinter.Button(root,text="Voice Mode",font=("Franklin Gothic Demi",20),fg="orange",command=lambda:voice())
button2.grid(column=1,row=5)
button3=tkinter.Button(root,text="Gesture Mode",font=("Franklin Gothic Demi",20),fg="white",command=lambda:gesture())
button3.grid(column=3,row=5)
button4=tkinter.Button(root,text="Analytics",font=("Franklin Gothic Demi",20),fg="white",command=lambda:analytics())
button4.grid(column=4,row=5)

root.mainloop()





