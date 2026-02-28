import random
from turtle import Screen, Turtle
import turtle as t

screen = Screen()
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()

color_list = [(208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]

x_inicial = -255
y_inicial = -255

tim.penup()
tim.goto(x_inicial,y_inicial)

for linha in range(10):
    for coluna in range(10):
        random_color = random.choice(color_list)
        tim.dot(25,random_color)
        tim.forward(50)

    y_proxima_linha = y_inicial+(50*(linha+1))
    tim.goto(x_inicial, y_proxima_linha)

t.exitonclick()