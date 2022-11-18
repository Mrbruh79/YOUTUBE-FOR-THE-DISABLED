import random
import time
import speech_recognition as sr
from app import handy1
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import pyttsx3
import time
import vlc 
import random
import pafy
import pickle
from googleapiclient.discovery import build
import keyboard
import Emotion
import Playlist
import sv_ttk
from tkinter import *
import tkinter
from PIL import ImageTk, Image 
import os
import gesture.handtracking
import logging
import threading
import time
from word2number import w2n
import mysql.connector
import gesture.gesture_init as gesture_init

mydb2 = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database = "Analytics"
)
print(mydb2)
cursor2 = mydb2.cursor()







root2 = tkinter.Tk()
sv_ttk.use_dark_theme()
root2.title("software engineering project")
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
label = Label(root2, text="")
label2 = Label(root2, text="")
label3 = Label(root2, text="")
label4 = Label(root2, text="")
label5 = Label(root2, text="")
label6 = Label(root2, text="")
label7 = Label(root2, text="")
label8 = Label(root2, text="")
    #this creates a new label to the GUI
label.pack(expand = True) 
label2.pack(expand = True)
label3.pack(expand = True)
label3.pack(expand = True)
label4.pack(expand = True)
label5.pack(expand = True)
label6.pack(expand = True)
label7.pack(expand = True)
label8.pack(expand = True)
def printSomething(textaa):
    label["text"]= label2["text"]
    label2["text"]= label3["text"]
    
    label3["text"]= label4["text"]
    label4["text"]= label5["text"]
    label5["text"]= label6["text"]
    label6["text"]= label7["text"]
    label7["text"]= label8["text"]
    label8["text"]= textaa
    root2.update()

def printresult(string):
    resultstr = "Found results \n"
    for i in range(0,len(string)):
        resultstr = resultstr + str(i + 1) + ".  " + string[i] + "\n"
    printSomething(resultstr)





def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitiviFalsety to ambient noise and record audio
    # from the microphone
    recognizer.dynamic_energy_threshold =True 
    with microphone as source:
        recognizer.energy_threshold=1500
        recognizer.pause_threshold=0.6
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response




def automateYoutube(song):
    api_key='' #enter your API key
    youtube= build('youtube','v3' , developerKey=api_key) #building the service objec
    request = youtube.search().list(part='snippet',type='video',q=song,maxResults='10')#using the search instance method to search for songs(gives video IDs)
    response=request.execute()
    videoIDs=[]
    titles = []

    for i in response['items']:
        videoIDs.append(i['id']['videoId'])#this list stores the video id's of our search results which can be used to obtain the url
    for i in response["items"]:
        titles.append(i["snippet"]["title"])
    
    #print(videoID)
    url ='https://www.youtube.com/wach?v='+videoIDs[0] #creating the URL for youtube video
    #print(url)t
    
    return  url  , videoIDs , titles

def create_media(url):
    video = pafy.new(url) #creating a pafy object
    best = video.getbest() #selects the stream with highest resolution
    media = vlc.MediaPlayer(best.url) #creating media player object
    return media

def create_url(videoID):
    url ='https://www.youtube.com/wach?v='+videoID
    return url


def urlplay(url):
    video = pafy.new(url) #creating a pafy object
    best = video.getbest() #selects the stream with highest resolution
    media = vlc.MediaPlayer(best.url) #creating media player object
    media.play() 
    return media 
    
def speech_main():
    # if __name__ == "__main__":
    # set the list of words, maxnumber of guesses, and prompt limit
    # WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
    NUM_GUESSES = 100
    PROMPT_LIMIT = 100

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=1)

    # # get a random word from the list
    # word = random.choice(WORDS)

    # # format the instructions string
    # instructions = (
    #     "I'm thinking of one of these words:\n"
    #     "{words}\n"
    #     "You have {n} tries to guess which one.\n"
    # ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    # show instructions and wait 3 seconds before starting the game
    # print(instructions)
    # time.sleep(2)
    playlist = "" 
    url = ""
    my_w = ""
    media = ""
    videoids = ""
    titles = ""
    songnum = 0
    emote = 0
    searchwrd = ''
    srwr = ""
    anal = 0
    
    for i in range(NUM_GUESSES):

        # get the guess from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their guess again. Do this up
        #     to PROMPT_LIMIT times
        for j in range(PROMPT_LIMIT):
            
            
            
            print('{}. Speak!'.format(i+1))
            printSomething('{}. Speak!'.format(i+1))
            
            
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            
            
            print("I didn't catch that. What did you say?\n")
            printSomething("I didn't catch that. What did you say?\n")
            
            

        print("You said: {}".format(guess["transcription"]))
        printSomething("You said: {}".format(guess["transcription"]))
        
        
        if guess["transcription"]==None:
            continue
        
        vid_name=guess["transcription"]
        
#*************************TRANSCRIPTION CHECKING*********************************        
        
        
        if guess["transcription"].split()[0]=="play" and (guess["transcription"].split()[1] != "number" or len(guess["transcription"].split()) != 3):
            
            if(media == ""):
                songnum = 0
                url , videoids , titles =automateYoutube(vid_name[5:])
                media = create_media(url)
                media.play()
                printresult(titles)
                printSomething("Currently playing {title}\n".format(title = titles[songnum]))
                cursor2.execute("update tmstp set x = current_timestamp();")
                mydb2.commit()
                searchwrd = vid_name[5:]
                srwr = searchwrd
                
            else:
                printSomething("Media is already is playing\n")
                
                
        if(guess["transcription"].split()[0]=="search"):
                url , videoids , titles =automateYoutube(vid_name[6:])
                printresult(titles)   
                srwr = "vid_name[6:]"
                
        if (guess["transcription"].split()[0]=="show") and len(guess["transcription"].split()) >1 :
                printresult(titles)   
                
                
        if guess["transcription"].split()[0]=="play" and guess["transcription"].split()[1] == "number" and len(guess["transcription"].split()) == 3:
            
            if(media == ""):
                
                songnum = w2n.word_to_num(guess["transcription"].split()[2]) - 1
                if(songnum >len(videoids) - 1):
                    printSomething("Invalid songnum")
                    continue
                media = create_media(create_url(videoids[songnum]))
                media.play()
                printresult(titles)
                printSomething("Currently playing {title}\n".format(title = titles[songnum]))      
                cursor2.execute("update tmstp set x = current_timestamp();")
                mydb2.commit()
                searchwrd = srwr
                
            else:
                printSomething("Media is already is playing\n")
                
        if guess["transcription"].split()[0]=="next":
            
            if(media != ""):
                media.stop()
                songnum += 1
                if(songnum >len(videoids)):
                    printSomething("No next video")
                    continue
                media = create_media(create_url(videoids[songnum]))
                media.play()
                printresult(titles)
                printSomething("Currently playing {title}\n".format(title = titles[songnum]))
            else:
                printSomething("No Media is playing\n")

                
        
            
        if(guess["transcription"]=="exit"):
          
                
            
            
            
            if(media != ""):

                cursor2.execute("""insert into analytics(Searchword , EMOTION , starttime , endtime , duration)VALUES("{song}" , {emote} , (SELECT * FROM tmstp) , CURRENT_TIMESTAMP() , CURRENT_TIMESTAMP() - (SELECT * FROM tmstp) );""".format(song = searchwrd , emote = emote))
                mydb2.commit()
                media.stop()# vdeo stopped
                media = ""
                emote = 0
                songnum = 0
            else:
                printSomething("No media playing\n")
                
                
        if guess["transcription"]=='pause':
            if(media != ""):
                media.pause()#video paused
            else:
                printSomething("No media playing\n")
                
        if guess["transcription"]=='resume':
            if(media != ""):
                media.play()#video play
            else:
                printSomething("No media playing\n")
              
              
              
        if guess["transcription"]=='emotion':
            if(media == ""):
                media,url,searchwrd ,emote,videoids,titles = Emotion.emotion()#video play
                print(media)
                print(url)
                media.play()
            else:
                printSomething("Media is already is playing\n")
          
              
        if guess["transcription"].split()[0] =='create' and guess["transcription"].split()[1] =='playlist':
            print(guess["transcription"][16:])
            Playlist.create(guess["transcription"][16:].replace(" ", "_"))#video play
            
        if guess["transcription"].split()[0] =='save' and guess["transcription"].split()[1] =='as':
            print(guess["transcription"][8:])
            print(playlist,guess["transcription"][8:].replace(" ", "_") , url)
            a = Playlist.save(playlist , (guess["transcription"][8:].replace(" ", "-")).lower() , url)#video play
            if not(a == ""):
                printSomething(a)
            
        if guess["transcription"].split()[0] =='use':
            print(guess["transcription"][4:])
            playlist = guess["transcription"][4:].replace(" ", "_")
            
        if guess["transcription"].split()[0] =='save' and guess["transcription"].split()[1] =='play':
            if(Playlist == ""):
                printSomething("No playlist selected")
              
            else:
                url = Playlist.geturl(playlist , (guess["transcription"][10:].replace(" ", "-")).lower())
                print(url)
                if url == "Song dosent exist" :
                    printSomething(a)
                else:
                    if(media == ""):
                        videoids = []
                        media  = urlplay(url)
                        cursor2.execute("update tmstp set x = current_timestamp();")
                        mydb2.commit()
                        searchwrd = "None"
                    else:
                        printSomething("Media is already is playing\n")
                    
            
        if guess["transcription"].split()[0] =='show' and len(guess["transcription"].split())== 1:
            if(Playlist == ""):
                printSomething("No playlist selected")
                
            else:
                my_w = Playlist.show(playlist)
          
        if guess["transcription"].split()[0] =='close':
            if(Playlist == ""):
                printSomething("No playlist selected")
                
            else:
                Playlist.close(my_w)
          
        if guess["transcription"].split()[0] =='remove':
            print(guess["transcription"][8:])
            print(playlist,guess["transcription"][7:].replace(" ", "_") , url)
            guess["transcription"] = guess["transcription"][7:].replace(" ", "-")
            guess["transcription"] = guess["transcription"].lower()
            a = Playlist.remove(playlist , guess["transcription"] )#video play
            if not(a == ""):
                printSomething(a)
                
                
        if guess["transcription"].split()[0].lower() =='analytics':
            os.system(r"python C:\Users\Restandsleep\Desktop\VIT\Software_Engineering\Analytics.py")
            anal = 1
        
        
            
            
            
        if guess["transcription"] =='bye':
            if(media != ""):
                media.stop()
            root2.destroy()
            break
        root2.update()
        if guess["transcription"] =='gesture':
            gesture_init.play_from_speech(media)
            break

speech_main()


          
          
        
            
             
      
        


