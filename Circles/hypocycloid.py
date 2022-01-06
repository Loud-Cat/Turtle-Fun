import turtle

# Setup screen for animation
turtle.tracer(0)

# Initiate and hide turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(4)

def home(rad):
    """Clear screen and set position at the bottom of a cardioid (leaves pen up)"""
    t.clear()
    t.penup()
    t.goto(0, -rad)
    t.setheading(0)
    t.pendown()

def loop(rad):
    points = []
    for deg in range(360 + 1):
        home(rad)
        t.circle(rad)

        t.penup()
        t.circle(rad, deg)
        t.pendown()

        t.circle(rad / 6)
        t.circle(rad / 6, -6*deg - 180)
        points.append( t.pos() )
        t.dot(10)

        t.penup()
        t.goto(*points[0])
        t.pendown()

        t.color("red")
        for x,y in points:
            t.goto(x,y)
        t.color("black")

        turtle.update()

loop(200)
