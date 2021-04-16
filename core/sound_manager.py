# Import voice/audio modules
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

import os # To remove the cache files

# Function to generate speech
def speak(text):
    filename = "cache/voiceover.mp3"

    tts = gTTS(text, lang='en-US')
    tts.save(filename)
    # ================= CREATING LOG ENTRIES
    print("\nGENERATED TEXT VOICE OVER")
    print("==============================")
    print(text)
    print("==============================\n")
    # ================= END OF LOG ENTRIES
    playsound(filename)
    os.remove(filename)

# Decorator to receive audio
def listen(): # func => function
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(f"Received Input: {said}")
        except:
            pass
    return said.lower()