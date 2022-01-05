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

def loop():
    for i in range(360 + 1):
        home()
        t.circle(250)
        t.circle(250, i)
        t.pendown()
        t.circle(50)

        t.penup()
        t.left(90)
        t.forward(100)
        t.right(90)
        t.pendown()
        t.circle(150)

        turtle.update()
loop()
