import turtle
turtle.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.pensize(3)

def home():
    t.clear()
    t.penup()
    t.goto(0, -150)
    t.setheading(0)

spots = []
def loop():
    for i in range(360 + 1):
        home()
        t.circle(150)
        t.circle(150, i)
        t.pendown()
        t.circle(50)

        t.penup()
        t.circle(50, i)
        t.dot(10)
        spots.append( t.pos() )
        t.circle(50, -i)

        t.left(90)
        t.forward(100)
        t.right(90)
        t.pendown()
        t.circle(50)

        t.color("red")
        t.penup()
        t.goto(*spots[0])
        t.pendown()

        for x,y in spots:
          t.goto(x,y)
        t.color("black")

        turtle.update()

loop()
