import turtle

pen = turtle.Turtle()
sr = turtle.Screen()

def right():
    pen.right(30)

def left():
    pen.left(30)

def forw():
    pen.forward(100)

def backw():
    pen.backward(100)

if sr.onkeypress() == "Right":

sr.listen()
input()