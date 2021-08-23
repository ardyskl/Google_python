#!/usr/bin/env python3

# import trinket
import turtle
import sys
import traceback

turtle.hideturtle()

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

p = turtle.Pen()
for i in range(360):
    p.pencolor(colors[i % 6])
    p.width(i/100 + 1)
    p.forward(i)
    p.left(59)

turtle.exitonclick()
