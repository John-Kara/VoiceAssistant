import youtube_dl
from notifypy import Notify

keyword = "download a video"

settings = {
    "outtmpl": "videos/%(title)s-%(channel)s.%(ext)s",
    "format": "best",
    "noplaylist": True,
    "no_warnings": True,
    "ignoreerrors": True,
    "quiet": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",
    "logtostder": False,
    "nocheckcertificate": True
}

source = youtube_dl.YoutubeDL(settings)

class YTDownloader:
    def __init__(self, url):
        self.url = url
    
    def download(self):
        source.extract_info(self.url)
        notification = Notify()
        notification.title = "Video Downloaded"
        notification.message = "Your video was successfully downloaded"
        notification.application_name = "YTDownloader"
        notification.icon = "assets/youtube_logo.png"
        notification.audio = "assets/notification_sound.wav"
        notification.send()
        return True

def start(speak, receiver):
    speak("Alright, what's the name of the video you want to download?")
    video_name = ""

    while not video_name:
        video_name = receiver()

    speak("Received input. Is this the name of your video? " + video_name)

    answer = ""

    while not "no" in answer.lower() and not "yes" in answer.lower():
        answer = receiver()
    
    if "no" in answer.lower():
        return speak("Alright. Looks like I got the wrong video!")
    speak("Ok. Downloading video!")
    YTDownloader(video_name).download()
    speak("Your video was downloaded.")
