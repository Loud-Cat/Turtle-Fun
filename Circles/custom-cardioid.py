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

def Cardioid(rad):
    """Draws a cardioid with a given size rad"""
    points = []
    for deg in range(360 + 1):
        home(rad)
        t.circle(rad, deg)

        t.circle(rad / 3, deg)
        points.append( t.pos() )

        t.color("red")
        t.goto(*points[0])
        t.pendown()
        for x,y in points:
            t.goto(x, y)

        turtle.update()
    return points

if __name__ == "__main__":
    Cardioid(200)
