import win32com.client
import requests
import json
import time

def stop(sec):
    time.sleep(sec)

speak = win32com.client.Dispatch("SAPI.SpVoice")


url = ("http://newsapi.org/v2/top-headlines?country=in&apiKey=5fa28dd1df07427aa3835f910a73cb89")
get = requests.get(url).text
data = json.loads(get)

art = data['articles']
i = 0
for articles in art:
    i = i + 1

    speak.Speak(f"News Number{i}..............THIS NEWS IF FROM   {articles['author']}.......AND  THE NEWS IS ..{articles['title']}")
