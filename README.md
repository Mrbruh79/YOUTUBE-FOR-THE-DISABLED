# YOUTUBE-FOR-THE-DISABLED
Youtube for the disabled. This project aims to provide a voice based youtube control mechanism for disabled people also consisting of gesture based control and Emotion based video search.

## This project has 4 modules: 
1. Voice 
2. Emotion 
3. Gesture 
4. Analytics

## To run the application download it as it is and run main_gui.py in a python 3 enviornment . 
##### Libraraies that are required to run it are:
```
tensorflow 
tensorflow-gpu
keras
cv2
speechrecogniton
numpy
pandas
matplotlib
deepface
vlc
random 
pafy
pickle
googleapiclient
keyboard
mysqlconnector
tkinter
webbrowser
imutils
selenium
pyttsx3
word2number
logging 
pillow
sv_ttk
mediapipe
```
##### **Make sure these libraries are installed and configured in the python enviornment**
##### **tensorflow gpu can be ignored if installing the latest version of tensorflow**
##### Please Configure all files as follows:
1. Add your API Key to STT.py , Emotion.py , handtracking.py for interacting with the Youtube API
2. Configure your mySQL Databse and change the connecion username,password as necessary in the codefile or you could configure it to our settings 
3. We have 3 databases Playlists , Analytics and emot . You can use the provided MySQL file
4. You can also change your mic by changing the device index in the STT.py file 

##### Video presentation link:
https://vitacin-my.sharepoint.com/:f:/g/personal/arnav_bansal2020_vitstudent_ac_in/EqrUMcdBx2lEkKbwOw__j0cBoUiRxsiTbasrEGofv6JBwQ?e=SkD9G8
