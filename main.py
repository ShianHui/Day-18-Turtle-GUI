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

def randomize_color():
    """Function to randomize Color"""
    r_value = random.randint(1, 255)
    g_value = random.randint(1, 255)
    b_value = random.randint(1, 255)
    tup_value = (r_value, g_value, b_value)
    return tup_value

for x in range(3, 10):
    tim.pencolor(randomize_color())
    draw_shape(x)






my_screen.exitonclick()
