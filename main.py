"""Main Module"""
import turtle
import random

tim = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.colormode(255)

for x in range(3, 10):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.pencolor(r, g, b)
    for i in range(1, x+1):
        tim.forward(100)
        tim.right(360/x)
        print(f"x is {x} and i is {i}")
        print(360/x)





my_screen.exitonclick()
