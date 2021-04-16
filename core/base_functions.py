from difflib import SequenceMatcher
from .sound_manager import listen, speak, playsound

import random

# Similarity Check Function
def match(s_1, s_2):
    return SequenceMatcher(None, s_1, s_2[:len(s_1)-1]).ratio() >= 0.5

# Should Activate(?) Function
def activate():
    record = listen()

    keyword = "hey computer"

    if match(record[:len(keyword)-1], keyword):

        playsound("core/activation.mp3")

        speak(random.choice([
            "Hey! Thanks for calling me, what's up?",
            "Listening...",
            "My name was sounded."
        ]))
        return True
    else:
        return False