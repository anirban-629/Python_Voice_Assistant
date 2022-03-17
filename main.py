import random
import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def greet():
    hour=int(datetime.datetime.now().hour)
    if(hour>=5 and hour<12):
        speak(f"good morning,   Hello sir, I'm Jarvis how Can I help you")
    elif(hour>=12 and hour<17):
        speak(f"good Afternoon,    Hello sir, I'm Jarvis how Can I help you")
    else:
        speak(f"good Evening,   Hello sir, I'm Jarvis how Can I help you")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r=sr.Recognizer()
    # this class recognizer helps to recognize the audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said {query}")

    except Exception as e:
        # print(e)
        print("Say that again Please..")
        return "none"

    return query

if __name__ == '__main__':
    greet()
    while True:
        q=takeCommand().lower()

        if 'wikipedia' in q:
            speak("searching in wikipedia")
            q.replace("wikipedia","")
            result=wikipedia.summary(q,sentences=2)
            speak(f"according to wikipedia {result}")

        elif 'open youtube' in q:
            webbrowser.open("youtube.com")
        elif 'open google' in q:
            webbrowser.open("google.com")
        elif 'open facebook' in q:
            webbrowser.open("facebook.com")
        elif 'open stackoverflow' in q:
            webbrowser.open("stackoverflow.com")
        elif 'open instagram' in q:
            webbrowser.open("instagram.com")

        elif 'the time' in q:
            t=datetime.datetime.now().hour
            t1=datetime.datetime.now().minute
            speak(f'Sir, The time is {t} {t1}')

        elif 'what is your name' in q:
            speak("Sir I'm your personal assistant,  I'm  Jarvis ")

        elif 'play music'in q:
            music="D:\\CODE EDITORs\\Python_Language\\Project- Assistant\\music"
            songs=os.listdir(music)
            r=random.randint(0,len(songs)-1)
            print(r)
            os.startfile(os.path.join(music,songs[r]))

        elif 'open intelligence' in q:
            path="C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.3.1\\bin\\idea64.exe"
            os.startfile(path)

        elif 'send email' in q:
            speak("redirecting to gmail.com")
            webbrowser.open("gmail.com")
            pass

        elif 'break' in q:
            break
        elif 'exit' in q:
            speak("Thank you sir,    have a nice day..!!")
            exit(0)
    
    # speak(question)