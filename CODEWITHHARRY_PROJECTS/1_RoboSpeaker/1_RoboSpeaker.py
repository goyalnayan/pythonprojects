# a backslash (\) and a forward slash (/). The backslash is used only for computer coding.
# The forward slash, often simply referred to as a slash, is a punctuation mark used in English

import os
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Nayan")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == 'exit':
            y = "bye bye friend"
            os.system(f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{y}')")
            break
        command = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')"
        os.system(command)


# Use this when you have file inside folder (and use backslash)
# import os
# cwd = "1_RoboSpeaker\song.mp3"
# os.system(cwd)


import os
cwd = "song.mp3"
os.system(cwd)


from playsound import playsound
song_play = "Nayan.mp3"
playsound(song_play)
from playsound import playsound
playsound("C:/Users/Hp/PycharmProjects/Python_Projects/1_RoboSpeaker/Nayan.mp3")


import gtts
import playsound
print("Welcome to RoboSpeaker 1.1. Created by Nayan")
x = input("Enter what you want me to speak: ")
sound = gtts.gTTS(x, lang="en")
sound.save("Nayan.mp3")
playsound.playsound("Nayan.mp3")


from gtts import gTTS
import playsound
import os
x = ['sunny', 'sagar', 'ayan']
tts = 'tts'
for i in range(0, 3):
    tts = gTTS(text=x[i], lang='en')
    file1 = str("hello" + str(i) + "song.mp3")
    tts.save(file1)
    playsound.playsound(file1, True)
    os.remove(file1)


from pygame import mixer
import time
mixer.init()
mixer.music.load('song.mp3')
mixer.music.play()
time.sleep(5)
mixer.music.stop()
print('Song has been stopped after 5 secs')
