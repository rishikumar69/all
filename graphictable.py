import tkinter

pen = tkinter.Tk()
pen.title("FUN :-) ;-)")
pen.geometry("350x350")

pos_y = 100

for i in range(6):
    pos_x = 100
    pos_y = pos_y+15
    if i == 0:
        tkinter.Label(pen,text = "Maths:").place(x = 100,y = pos_y)

    elif i == 1:
        tkinter.Label(pen,text = "Science:").place(x = 100,y = pos_y)

    elif i == 2:
        tkinter.Label(pen,text = "S.S:").place(x = 100,y = pos_y)

    elif i == 3:
        tkinter.Label(pen,text = "English:").place(x = 100,y = pos_y)

    elif i == 4:
        tkinter.Label(pen,text = "Hindi:").place(x = 100,y = pos_y)

    elif i == 5:
        tkinter.Label(pen,text = "Marathi:").place(x = 100,y = pos_y)

pos_y = 100
for i in range(6):
    pos_y = pos_y + 15
    first = tkinter.Entry(pen).place(x = 186, y = pos_y )
    f = open("marks.txt")
    f.write(first)
    f.close()

pen.mainloop()
