import speech_recognition as sr 
import webbrowser
import time
from time import ctime
import playsound
import os 
import random
from gtts import gTTS
from PIL import Image
import pyautogui
import requests
import urllib.request




class person:
    name = ""
    def setName(self,name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True



r = sr.Recognizer()

def record_audio(ask=False):

    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        
        audio = r.listen(source)
        voice_data = ""
        try: 
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            alexis_speak("Sorry, I did not get that")

        except sr.RequestError:
            alexis_speak("Sorry, my speech service is down")

        return voice_data


def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)





def respond(voice_data):
    
    # 1. Karşılama, merhaba vs  
    if there_exists(["hey","hi","hello"]):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey,what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings)-1)]
        alexis_speak(greet)

    # 2. Name
    if there_exists(["what is your name", "what's your name","tell me your name"]):
        if person_obj.name:
            alexis_speak("my name is Alexis")
        else:
            alexis_speak("my name is Alexis. What's your name?")


    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        alexis_speak(f"okay, I will remember that {person_name}")
        person_obj.setName(person_name)


    # 3. Hal , hatır sorma evresi :D
    if there_exists(["how are you", "how are you doing"]):
        alexis_speak(f"I'm very well, thanks for asking {person_obj.name}")


    if "what time is it" in voice_data:
        alexis_speak(ctime())


    if "search" in voice_data:
        search = record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        alexis_speak("Here is what I found for " + search)


    if "find location" in voice_data:
        location = record_audio("What is the location=")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        alexis_speak("Here is the location of" + location)

    # Fotoğraf açma
    if there_exists(["show picture"]):

        im = Image.open(r"sample.jpeg")
        alexis_speak("Let me show you ...")
        im.show()

    # Ekran görüntüsü alma
    if there_exists(["capture","my screen","screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save("screen.png")
        alexis_speak("Okay")
        

    # Konumum
    if there_exists(["what is my exact location"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        alexis_speak("You must be somewhere near here, as per Google maps")



    if there_exists(["exit","see you later"]):
        alexis_speak(f"See you later {person_obj.name}.")
        exit()


time.sleep(1)
person_obj = person()
person_obj.name = ""

while 1:

    voice_data = record_audio()
    respond(voice_data)

