import pyttsx3
import webbrowser
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import datetime
import time


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    print('Al : ' + audio)
    engine.say(audio)
    engine.runAndWait()

def wish():
        now = datetime.datetime.now()
        hour = now.hour
        if hour < 12:
                speak("Good morning  vaan")
                sp = ['what can i help you with ','what can i help you with','is there any thing i can help you with','what shall we do today']
                speak(random.choice(sp))

        elif hour < 16:
                speak("Good afternoon vaan")
                sp = ['how may i help you','what can i help you with','is there any thing i can help you with','what shall we do today']
                speak(random.choice(sp))

        else:
                speak("Good evening vaan")
                sp = ['how may i help you','what can i help you with','is there any thing i can help you with','what shall we do today']
                speak(random.choice(sp))
wish()
def spch():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        r.pause_threshold =  0.5
    try:
        cmd = r.recognize_google(audio).lower()
        print('vaan: ' + cmd + '\n')

    except sr.UnknownValueError:
        speak('would you mind typing your command sir')
        cmd = str(input('vaan: '))

    return cmd
        
if __name__ == '__main__':

    while True:
        cmd = spch()
        cmd = cmd.lower()
        
        if 'open youtube' in cmd or 'youtube' in cmd or 'Al open youtube' in cmd:
            speak('okay,opening youtube')
            webbrowser.open('www.youtube.com')
        if  'google' in cmd or 'open google' in cmd:
            speak('sure, opening a new google tab')
            webbrowser.open('https://www.google.com/')
        elif 'how are you' in cmd or 'how are you' in cmd or 'how are you' in cmd:
            speak('i am great, how are you')
        elif'i am good ' in cmd or 'i am great' in cmd or 'im doing well' in cmd:
            speak("thats great")
        elif 'wikipedia' in cmd: 
            speak('Searching Wikipedia...') 
            cmd = cmd.replace("wikipedia", "") 
            results = wikipedia.summary(cmd, sentences = 1) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results)
        elif 'instagram' in cmd or 'open instagram' in cmd:
            speak('sure opening instagram')
            webbrowser.open('https://www.instagram.com/')
        elif 'play my anthem' in cmd:
            speak('okay')
            webbrowser.open('https://www.youtube.com/watch?v=YKLX3QbKBg0')
        elif 'spotify' in cmd:
                speak('sure')
                os.system('spotify.exe')
        elif 'hello' in cmd or 'hey there'in cmd or 'yo' in cmd :
                helo = ['hello there','hey there','well hello','hello master vaan']
                speak(random.choice(helo))
        elif 'open netflix' in cmd or 'netflix' in cmd or 'do mind opening netflix for me'in cmd:
                speak('sure, opening netflix')
                webbrowser.open('https://www.netflix.com/browse')
        elif 'hey Al i wanna watch haiku do u mind opening it for me' in cmd or 'haiku' in cmd or 'its time for some haiku' in cmd:
                webbrowser.open('https://www.netflix.com')
        elif 'go away' in cmd or 'shut up' in cmd or 'bye' in cmd :
                speak('sure bye, feel free to ask if you need some help')
                sys.exit()
        elif 'wait for 5 mins' in cmd:
            time.sleep(300)
        elif 'wait for 10 mins' in cmd:
            time.sleep(600)
        
        
        
            
            
  
            
            

        

