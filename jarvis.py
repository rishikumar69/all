import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import win32com.client
import os
# from plyer import *


user_name = "Rishi"


if __name__ == '__main__':

    appicon = "iron-man-removebg-preview.ico"
    speak = win32com.client.Dispatch("SAPI.SpVoice")



    def product(lst):
        # print(lst)
        # num = 1
        ans = 1
        for item in lst:
            ans = int(item) * ans

        return ans


    def notifyme(title, message):
        pass


    def wishme():
        hour = datetime.datetime.now().hour
        print(hour)

        if hour < 12:
            speak.Speak(f"GOOD MORNING {user_name} SIR.")

        elif hour >= 12 and hour < 17:
            speak.Speak(f"GOOD Afternoon {user_name} SIR.")

        elif hour >= 17:
            speak.Speak(f"GOOD evening {user_name}     SIR.")
        speak.Speak("Hello I AM JARVIS. HOW MAY I HELP YOU ..Sir ")


    def takecommend():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            notifyme("Jarvis", "Listening...")
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            notifyme("Jarvis", "Recognizing...")
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            notifyme("Jarvis", "Say that again please...")
            print("Say that again please...")
            return "None"

        return query


    def give_time():
        time = datetime.datetime.now()
        return time


    wishme()

    while True:
        quarry = takecommend().lower()

        if 'wikipedia' in quarry:
            speak.Speak("Searching result in wikipedia...")
            notifyme("Jarvis", "Searching Result In Wikipedia...")
            quarry = quarry.replace("wekipedia", " ")
            results = wikipedia.summary(quarry, sentences=2)
            speak.Speak(results)

        elif'open youtube' in quarry:
            notifyme("Jarvis", "Opening Youtube...")
            webbrowser.open("www.youtube.com")
            break

        elif 'open google' in quarry:
            notifyme("Jarvis", "Opening Google...")
            webbrowser.open("https://www.google.com/")
            break

        elif 'stackoverflow' in quarry:
            notifyme("Jarvis", "Opening StackOverFlow...")
            webbrowser.open("www.stackoverflow.com")
            break

        elif 'date' in quarry:
            notifyme("Jarvis", f"{give_time().date()}")
            speak.Speak(give_time().date())

        elif 'who are you ' in quarry:
            # notifyme("Jarvis", "Created By Rishi Kumar on 23rd June 2020.")
            speak.Speak("I am jarvis. created by Rishi kumar on 23rd june 2020. i can be your assistent...")

        elif 'what is my name' in quarry:
            # notifyme("Jarvis", f"You Are Probably {user_name}")
            speak.Speak(f"your name is {user_name} and i am your assistant")

        elif 'what is your name' in quarry:
            # notifyme("Jarvis", "I AM JARVIS!!!")
            speak.Speak(f"I AM JARVIS. I AM a ASSISTENT AND mr.rishi created me")

        elif 'close' in quarry:
            # notifyme("Jarvis", "Closing...")
            print("Exiting thanks for your time...")
            exit()

        # if 'good morning' or 'good afternoon' or 'good evening' or 'good night' in quarry:
        #     wishme()

        elif 'open game' in quarry:
            os.startfile("C:\\Users\\Rishi\\Desktop\\Tekken_3.exe")
        # elif 'multiply' or 'multiplication' in quarry:
        #     all_numbers = "1234567890"
        #     number = []
        #     for item in quarry.split():
        #         if item.isdigit():
        #             number.append(item)
        #
        #     # print(number)
        #     speak.Speak(product(number))

        elif "say" in quarry:
            quarry.replace("say", " ")
            speak.Speak(quarry)

        else:
            speak.Speak("sorry we do not have that function for now ")
