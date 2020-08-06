import win32com.client
import requests
import json

url = ('http://newsapi.org/v2/top-headlines?country=in&apiKey=5fa28dd1df07427aa3835f910a73cb89')

speak = win32com.client.Dispatch("SAPI.SpVoice")


getnews = requests.get(url).text
conv = json.loads(getnews)
arts = conv['articles']
i = 0
for articles in arts:
    i = i +1
    speak.Speak(f"news numper {i}. this news is from {articles['author']} and the news is {articles['title']}")
