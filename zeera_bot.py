import speech_recognition as sr
import pyttsx3
import datetime 
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# print(voices)` `

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak ("Good Morning")
    elif hour>=12 and hour<17:
        speak ("Good Afternoon")
    else:
        speak ("Good Evening")
speak("Hello, I am Zeera. Please tell me how may I help you ?")

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    
    except Exception as e:
        # print(e)
        
        print("sapeak again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('1172dipu@gmail.com', 'your-password')
    server.sendmail('himorishu@gmail.com', to, content)
    server.close()



if __name__ =="__main__":
    wishMe()
    while True:
#   if 1:
        query = takeCommand().lower()
        # logic
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences =3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open learnvern' in query:
            webbrowser.open('learnvern.com')
        elif 'open github' in query:
            webbrowser.open('github.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open codewithharry' in query:
            webbrowser.open('codewithharry.com')
        elif 'open kunalkushwaha' in query:
            webbrowser.open('kunalkushwaha.com')
        elif 'open udemy' in query:
            webbrowser.open('udemy.com')
        elif 'open coursera' in query:
            webbrowser.open('coursera.com')
        elif 'play music' in query:
            music = 'C:\\Users\\Administrator\\OneDrive\\Desktop\\Butterscotch\\4.2 spotify clone\\music'
            songs =os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music,songs[4]))
        elif 'play video song' in query:
            vsong ='https://www.youtube.com/watch?v=BH-JuqbASFI&list=RDMMBH-JuqbASFI&start_radio=1'
            os.startfile(vsong)

        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:S%")
            speak(f"sir, the time is {strTime}")
        elif 'open vs code' in query:
            codepath="C:\\Users\\Administrator\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "himorishu@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend, I am not able to send this email at this moment.")    

