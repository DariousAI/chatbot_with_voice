import speech_recognition as sr
from gtts import gTTS
import os

def listen():
    """Function to capture user's speech and convert to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return ""
        except sr.RequestError:
            print("Network error.")
            return ""

def speak(text):
    """Function to convert text to speech"""
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")  # For Windows. Use 'afplay' for Mac or 'xdg-open' for Linux.
