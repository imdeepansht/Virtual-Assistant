import keyboard
import pyttsx3#pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("hello")

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'cheenu@501')
    server.sendmail('receiveremail@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("https://youtube.com")

            elif 'open google' in query:
                webbrowser.open("https://google.com")

            elif 'open stack overflow' in query:
                webbrowser.open("https://stackoverflow.com")
            
            elif 'open facebook' in query:
                webbrowser.open("https://facebook.com")
            
            elif 'open instagram' in query:
                webbrowser.open("https://instagram.com")
            
            elif 'open GitHub' in query:
                webbrowser.open("https://github.com")
            
            elif 'open w3schools' in query:
                webbrowser.open("https://w3schools.com")
            
            elif 'open codewithharry' in query:
                webbrowser.open("https://codewithharry.com")

            elif 'thank you' in query or 'thanks' in query:
                speak("Welcome Sir")   

            elif 'you need a break' in query:
                speak("Ok Sir, I am just a call away")
                speak("Just Say, Hey Jarvis")
                break

        
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "Your Path"
                os.startfile(codePath)

            elif 'email' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "deepanshtelang07@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Sir. I am not able to send this email")

            elif 'bye' in query:
                speak("Thanks you sir. Please come soon")   
                quit() 
