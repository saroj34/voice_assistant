from logging import exception
import os
import time
import playsound
import speech_recognition as sr
# from gtts import gTTs


def get_audio():


 r1 = sr.Recognizer()
with sr.Microphone() as source:
   audio = r1.listen(source)
   said = ""
   try:
        said = "r1.recognizer_google(audio)"
        print(said)
   except Exception as e:
    print("exception:" + str(e))


speak("hello")
get_audio()
