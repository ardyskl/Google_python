#!/usr/bin/env python3

import turtle
window = turtle.Screen()

turtle.speed(0)
#turtle.bgcolor("black")
turtle.Screen().bgcolor("#191919")

for i in range(10):
    for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white", "pink", "grey"]:
        turtle.color(colours)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)

window.exitonclick()
