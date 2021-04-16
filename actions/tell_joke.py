import requests, time

keyword = "tell joke"

def start(speak, receiver):
    response = requests.get("https://official-joke-api.appspot.com/random_joke").json()
    setup, punchline = response["setup"], response["punchline"]
    
    speak(setup)
    speak(punchline)
    #if random.randint(0,5) >= 4:
    speak("HaHaHaHaHaHaHa.")