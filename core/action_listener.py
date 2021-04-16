from .sound_manager import speak, listen
from .base_functions import match

#from threading import Thread

import random

# Import actions
from actions import (
    create_note,
    read_note,
    download_video,
    play_song,
    tell_joke,
    who_is
    )

def begin():
    record = ""

    while not record:
        record = listen()

    # TELL JOKE CALL
    if match(tell_joke.keyword.lower(), record):
        return tell_joke.start(speak, listen)

    # NOTE MANAGEMENT CALL
    elif match(create_note.keyword, record) or match(read_note.keyword, record):
        if "read" in record:
            read_note.start(speak, listen)
        else:
            create_note.start(speak, listen)
    
    # DOWNLOAD VIDEO CALL
    elif match(download_video.keyword, record):
        download_video.start(speak, listen)

    # PLAY SONG CALL
    elif match(play_song.keyword, record):
        play_song.start(speak, listen)
    
    # WIKIPEDIA CALL
    elif match(who_is.keyword, record):
        who_is.start(speak, listen)

    else:
        return speak(random.choice([
            "Hmm... I can't understand you. Sorry.",
            "I did not quite get that. Can you repeat?",
            "Repeat please!",
            "I didn't understand! Sorry!"
        ]))