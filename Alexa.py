import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("speak")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'jarvis' in command:
                command=command.replace('jarvis','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk(time)
    elif 'who is' in command:
        person=command.replace('who is',"")
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    else:
        talk('say it again')

while True:
    run_alexa()
