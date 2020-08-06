import turtle

pen = turtle.Turtle()
sr = turtle.Screen()

pen_speed = 10



while(True):
    sr.onkeypress(pen.right(10),"Right")
    sr.onkeypress(pen.left(10),"Left")
    sr.onkeypress(pen.forword(10),"Up")
    sr.onkeypress(pen.backword(10),"Down")
    sr.listen()















