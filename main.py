"""Main Module"""
import turtle
import random

tim = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.colormode(255)


def draw_shape(num_of_sides):
    """Function to Draw Shape"""
    for _ in range(1, num_of_sides+1):
        tim.forward(100)
        tim.right(360/num_of_sides)

for x in range(3, 10):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.pencolor(r, g, b)
    draw_shape(x)






my_screen.exitonclick()
