import youtube_dl
import playsound
import os

keyword = "play a song"

settings = {
    "outtmpl": "songs/%(title)s.%(ext)s",
    "format": "bestaudio",
    "noplaylist": True,
    "no_warnings": True,
    "ignoreerrors": True,
    "quiet": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",
    "logtostder": False,
    "nocheckcertificate": True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

source = youtube_dl.YoutubeDL(settings)

class YTDownloader:
    def __init__(self, url):
        self.url = url
    
    def download(self):
        return source.extract_info(self.url)

def start(speak, receiver):
    speak("Alright, what's the name of the song you want to play?")
    video_name = ""

    while not video_name:
        video_name = receiver()

    speak("Received input. Is this the name of your song? " + video_name)

    answer = ""

    while not "no" in answer.lower() and not "yes" in answer.lower():
        answer = receiver()
    
    if "no" in answer.lower():
        return speak("Alright. Looks like I got the wrong song!")
    speak("Ok. Downloading song!")
    song = YTDownloader(video_name).download()
    speak("Your song was downloaded. Playing.")
    song = song['entries'][0]
    songName = f"./songs/{song['title']}.mp3"
    playsound.playsound(songName)
    os.remove(songName)
    speak("Hope you enjoyed your song!")
