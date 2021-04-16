import wikipedia

keyword = "what is"

def start(speak, search):
    results = wikipedia.summary(search)
    speak(f"Results for {search}.")
    speak(results)