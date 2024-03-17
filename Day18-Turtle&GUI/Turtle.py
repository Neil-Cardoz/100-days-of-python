import turtle
from turtle import Turtle,Screen

tia = Turtle()
tia.shape("turtle")
tia.color("green")

for i in range(10):
    tia.forward(10)
    tia.penup()
    tia.forward(10)
    tia.pendown()

screen = Screen()
screen.exitonclick()

