import win32com.client



speak = win32com.client.Dispatch("SAPI.SpVoice")

for i in range(10):
    inp = input("Write something here: ")
    speak.Speak(inp)
