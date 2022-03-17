# import pyttsx3
# import speech_recognition as sr
#
# engine=pyttsx3.init('sapi5')
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)
#
# def speak(audio):
#     # engine.say(audio)
#     engine.say(audio)
#     engine.runAndWait()
#
#
#
# def takeCommand():
#     r = sr.Recognizer()
# # this class recognizer helps to recognize the audio
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"user said {query}")
#
#     except Exception as e:
#         # print(e)
#         print("Say that again Please..")
#         return "none"
#
#     speak(query)
#
# while True:
#     takeCommand()

a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")
print(a)

























