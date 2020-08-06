import win32com.client

# Calling the Disptach method of the module which
# interact with Microsoft Speech SDK to speak
# the given input from the keyboard

speaker = win32com.client.Dispatch("SAPI.SpVoice")
i =0
while True:
    i = i + 1
    print("Enter the word you want to speak it out by computer:")
    s = input()
    speaker.Speak(s)
    if i == 10:
        break