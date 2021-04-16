from PyJS.modules import fs

keyword = "read note"

def start(speak, receiver):
    speak("On it! Which note do you want me to read?")
    note_name = ""

    while not note_name:
        note_name = receiver()
    
    speak("Ok. Reading note " + note_name)
    
    content = fs.createReadStream(f"notes/{note_name}.txt").chunk()

    speak(content)

    speak("This was your note. Hope I did well!")