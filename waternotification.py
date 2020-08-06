from plyer import notification
import time

def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 5

         )
while True:
    time.sleep(10)
    notifyme("Water Reminder","Hey Rishi Drink Water")


