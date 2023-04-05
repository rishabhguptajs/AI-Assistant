import speech_recognition as sr
import pyttsx3
from bs4 import BeautifulSoup
from googlesearch import search
from datetime import datetime
import time

r = sr.Recognizer()
engine = pyttsx3.init()
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10)

    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
        return None


def speak(text):
    engine.say(text)
    engine.runAndWait()

def respond(text):
    global memorized_text
    if "hello" in text.lower():
        speak("Hello! How can I help you today?")
    elif "wait" in text.lower():
        # implment a wait function
        speak("Okay, I will wait for 5 seconds")
        time.sleep(5)
    elif "how are you" in text.lower():
        speak("I'm doing well, thank you!")
    elif "what time is it" in text.lower():
        now = datetime.now()
        speak("The time is " + now.strftime("%H:%M:%S"))
    elif "what is your name" in text.lower():
        speak("My name is Jarvis, how can I help you?")
    elif "who are you" in text.lower():
        speak("I am a virtual assistant, how can I help you?")
    elif "what is your favorite color" in text.lower():
        speak("My favorite color is blue, how can I help you?")
    elif "what is your best food" in text.lower():
        speak("My favorite food is pizza, how can I help you?")
    elif "what is your favourite movie" in text.lower():
        speak("My favorite movie is The Matrix")
    elif "what is your favourite song" in text.lower():
        speak("My favorite song is 'The Sound of Silence' by Disturbed")
    elif "what is your favourite book" in text.lower():
        speak("My favorite book is 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams")
    elif "what is your favourite game" in text.lower():
        speak("My favorite game is 'The Legend of Zelda: Breath of the Wild'")
    else:
        speak("I'm sorry, I don't know how to respond to that yet.")

while (True):
    text = recognize_speech()

    if text is None:
        response = "I'm sorry, I don't know how to respond to that yet."

        speak(response)
    else : 
        respond(text)
    
