keyword = "create a note"

def start(speak, receiver):
    speak("Ok. Creating note. What would you like me to write?")
    content = []
    
    while True:
        append_content = receiver()
        if append_content.endswith("stop writing"):
            break
        content.append(append_content)
    
    speak("Noted! What would you like to name the file as?")

    name = ""

    while not name:
        name = receiver()
    
    with open(f"notes/{name}.txt", "w+") as f:
        f.write('. '.join(content))
    
    speak("Your file was created.")