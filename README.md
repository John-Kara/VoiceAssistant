# **Python Voice Assistant**
> You can now have your own voice assistant to execute tasks for you. All you need, is a microphone.

## Features
- Multiple commands
- Easy to use
- Auto microphone detection
- Cache & log usage for improved performance

## Setting Up
**! PYTHON IS REQUIRED !**
Make sure you have the **Latest** python version installed. You can download it [here](https://python.org/).

In order to setup the Voice Assistant, you must first install all the dependencies for the project.
Use `pip install -r requirements.txt` on the command prompt. Make sure you have changed the directory to the project folder.

> **PyAudio Errors**
Sometimes there might be an issue with installing the PyAudio dependency. To fix it, download the latest version of PyAudio at found at [this website](https://www.lfd.uci.edu/~gohlke/pythonlibs/).
![](https://i.gyazo.com/22f754fb1f06173f81bdbd681a05cdff.gif)

## How To Use
Once you've got everything setup, it's time to use the assistant!
1. Run `__main__.py`
2. Wait for a few seconds, and then proceed with saying the activation keyword. `hey computer`
3. There are plenty of actions you can command the computer to do now. Here are they;

- **Note Management**
**Keyword**: `create a note`
**Description**: Create a note in the `notes` folder! You simply have to tell the computer what to write. Say `stop writing` to stop. Afterwards the computer will ask you how to name the file. Say the name and a text file will be created in the folder.

- **Read Note**
**Keyword**: `read note`
**Description**: Once activated the computer will ask you for the exact name of the note. The note must be inside the `notes` folder. If found, the computer will read it. Simple as that!

- **Tell Joke**
**Keyword**: `tell joke`
**Description**: Well.. the computer will simply say an *awful* joke.

- **Who/What is**
**Keyword**: `who is` or `what is`
**Description**: The computer will search for your query in wikipedia and return a summary! This feature is still in development, and it might take some time for the computer to return the results as it needs to download the voice file.

- **Play Song**
**Keyword**: `play a song`
**Description**: Once activated the computer will ask you for the name of the song. Then, it will search youtube for it. Once it finds and downloads the song, it will start playing it, and delete it afterwards.

- **Download Video**
**Keyword**: `download a video`
**Description**: Just like the previous action, the computer will ask you for the name of the video you wish to download. Once it has received input, it will download and then save the video in the `videos` folder.

# Modifying Keywords
You can change the keywords by simply modifying the files inside the `actions` folder. You will see a variable named `keyword` in it, which you can change to whatever you want.

# Adding your own actions
To add an action, it requires some Python knowledge.
This is an example of the file you must create inside the `actions` folder;
```py
# Import any packages you wish, if you need any

keyword = "keyword to activate action"

"""
The `speak` argument is the voice engine of the machine.
Calling it with some string will cause the computer to convert it to speech

Example:
speak("Hello world!")

The receiver is to receive audio from the user. Example usage:
user_voice_input = receiver()
"""
def start(speak, receiver):
    # Code
```
You're not done, yet. Head over to the `core` folder and open the `action_listener.py` file. From there, do these modifications;
```py
from actions import(
    . . .
    your_action_file_name # Without the .py extension
)

# -- Inside the begin function
# Before ELSE;
elif match(your_action_file_name.keyword, record):
    your_action_file_name.start(speak, listen)
```
It is complicated, but you can always create an issue and let me know if you face any difficulty!