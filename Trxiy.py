import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voice')
engine.setProperty('voice', voices[1])
def talk(text): engine.say(text)
engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'devil' in command:
                command = command.replace('devil', '')
                print(command)
    except:
        pass
    return command
def run_devil():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        tm = datetime.datetime.now().strftime('%I:%M:S %p')
        talk('Current Time is' + tm)
    elif 'can you tell me about' in command:
        person = command.replace('can you tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry you are not my type')
    elif 'are you single' in command:
        talk('Aapne kaaam se kaaam rakh na')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(talk(' '))
    else:
        talk('Please say the command again.')
while True:   run_devil()
print("hello")