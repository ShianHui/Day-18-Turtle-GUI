"""Main Module"""
import turtle
import random

direction = [0, 90, 180, 270,]
tim = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.colormode(255)
x = 3

def draw_shape(num_of_sides):
    """Function to Draw Shape"""
    for _ in range(1, num_of_sides + 1):
        tim.forward(100)
        tim.right(360 / num_of_sides)


def randomize_color():
    """Function to randomize Color"""
    r_value = random.randint(1, 255)
    g_value = random.randint(1, 255)
    b_value = random.randint(1, 255)
    tup_value = (r_value, g_value, b_value)
    return tup_value

def random_move(paces):
    """Function to turn and move"""
    tim.setheading(random.choice(direction))
    tim.forward(paces)

tim.pensize(10)
tim.speed("fastest")
for x in range(1, 100):
    tim.pencolor(randomize_color())
    random_move(30)

print("It's over")


my_screen.exitonclick()
