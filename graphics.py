import tkinter
import random

r_num = random.randint(1,100)
i = 0
pen = tkinter.Tk()

pen.title("Randome Game")

while True:
    pen.geometry = ("500x500")
    i = i+1
    if i == 10:
        break

    userinput = tkinter.Label(pen,text = "Enter Your Number: ").place(x = 100,y = 150)




pen.mainloop()






