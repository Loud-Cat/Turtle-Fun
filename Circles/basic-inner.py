import turtle
turtle.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.pensize(4)

def home():
    t.clear()
    t.penup()
    t.goto(0, -250)
    t.setheading(0)
    t.pendown()

def loop():
    for i in range(360 + 1):
        home()
        t.circle(250)
        t.circle(250, i)
        t.pendown()
        t.circle(50)
        turtle.update()
loop()
