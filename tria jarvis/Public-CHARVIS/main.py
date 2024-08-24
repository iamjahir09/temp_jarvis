import os
import eel

from engine.features import *
from engine.command import *

def start():
    
    eel.init("www")

    playAssistantSound()


    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost',block=True)

def activate_charvis():
    #logic to activate Charvis goes here
    print("Charvis Activated!")

user_input = "hi"
print(charvis_response(user_input))  

    
    