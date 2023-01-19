"""Main Module"""
import turtle
import heroes as h


tim = turtle.Turtle()
my_screen = turtle.Screen()

for i in range(1, 5):
    tim.forward(100)
    tim.right(90)

tim.pu()
tim.left(90)
tim.forward(20)
tim.right(90)

for i in range(1, 51):
    if i % 2 == 0:
        tim.pu()
    else:
        tim.pd()
    tim.forward(10)

my_screen.exitonclick()

print(h.gen())
