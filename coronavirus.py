from plyer import notification
import requests
from bs4 import BeautifulSoup

icon = "icon.ico"

def notifyme(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = icon,
        timeout = 10

    )


def getData(url):
    r = requests.get(url)
    return r.text


notifyme("Rishi", "dont Click here")
# getData("view-source:https://www.mohfw.gov.in/")

myhtmldata = getData("https://www.mohfw.gov.in/")
soup = BeautifulSoup(myhtmldata,"html.parser")

mydatastr = ""
for tr in soup.find_all("tbody")[1].find_all("tr"):
    mydatastr += tr.get_text()

mydatastr = mydatastr[1:]
print(mydatastr)



