#!/usr/bin/env python3

import turtle

window = turtle.Screen()
turtle.speed(5)
turtle.pensize(5)

# Draw the outline of a sqaure
turtle.penup()
turtle.goto(-350, 100)
turtle.pendown()
turtle.color("black")

turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.penup()

# Draw outline in the square
turtle.goto(-175, 100)
turtle.color("magenta")
turtle.pendown()

for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.penup()

# Multi-coloured stroke square
turtle.goto(0, 100)
turtle.pendown()
for colours in ["yellow", "red", "purple", "blue"]:
    turtle.color(colours)
    turtle.forward(150)
    turtle.left(90)
turtle.penup()

# Fill square with colour
turtle.goto(175, 100)
turtle.color("orange", "yellow")
turtle.pendown()
turtle.begin_fill()

for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.end_fill()

window.exitonclick()
