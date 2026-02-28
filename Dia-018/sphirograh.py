import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_sphirograph(size_gap):
    for _ in range(int(360/size_gap)):
        tim.color(random_color())
        tim.circle(120)
        new_heading = tim.heading() + size_gap
        tim.setheading(new_heading)


draw_sphirograph(5)
screen = t.Screen()
screen.exitonclick()
