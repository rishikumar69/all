from pygame import mixer
import pygame
import time
import datetime
import tkinter

datetime.datetime.now()
today = str(datetime.datetime.now())
# def popup(t,file):
#     pen = tkinter.Tk()
#     pen.title("You Are Healty!!!")
#     pen.geometry("250x150")
#
#     while True:
#         i = 0
#         mixer.init()
#         pen = tkinter.Tk()
#         pen.title("You Are Healty!!!")
#         pen.geometry("250x150")
#         tkinter.Label(pen, text=f"Enter {t} if you have Done your Work").place(x=25, y=50)
#         user_input = tkinter.Entry(pen).place(x=50, y=75)
#         mixer.music.load(file)
#         mixer.music.play(-1)
#         while pygame.mixer.music.get_busy():
#             pygame.time.Clock().tick(10)
#         i = i + 1
#         if t == user_input:
#             mixer.music.stop()
#         elif i == 10:
#             break
#         else:
#             continue
#
#
#     pen.mainloop()
#
# popup("d","water.mp3")

def playwater():

    file = 'water.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    mixer.music.play(-1)
    mixer.music.set_volume(0.3)


    while True:
        user_input = input("Enter 'W' if You Have Done Drinking water:  ")
        if user_input == "W":
            mixer.music.stop()
            break
        else:
            continue

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def playforeyes():
    file = 'exercise.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    mixer.music.play(-1)
    mixer.music.set_volume(0.3)
    while True:
        user_input = input("Enter 'DE' if You Have Done Your Eye's Exercise:  ")
        if user_input == "DE":
            mixer.music.stop()
            break
        else:
            continue


    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(2)

def playforexercice():
    file = 'forwater.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        user_input = input("Enter 'D' if You Have Done Your Exercise:  ")
        if user_input == "D":
            mixer.music.stop()
            break
        else:
            continue

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

i = 0
while True:
    i = i + 1
    time.sleep(0)
    playforeyes()
    time.sleep(0)
    playwater()
    time.sleep(3)
    playforexercice()
    if i == 9:
        break