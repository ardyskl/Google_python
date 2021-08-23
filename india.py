#!/usr/bin/env python3

import turtle
from turtle import *

TK_SILENCE_DEPRECATION=1

window = turtle.Screen()

turtle.speed(5)
turtle.pensize(2)

turtle.setup(800, 500)

turtle.penup()
turtle.goto(-400, 250)
turtle.pendown()

# Saffron indicates strenght and courage
turtle.color("orange")
turtle.begin_fill()
turtle.forward(800)
turtle.right(90)
turtle.forward(167)
turtle.right(90)
turtle.forward(800)
turtle.end_fill()

turtle.left(90)
turtle.forward(167)

# Green is for prosperity and growth
turtle.color("#006400")
turtle.begin_fill()
turtle.forward(167)
turtle.left(90)
turtle.forward(800)
turtle.left(90)
turtle.forward(167)
turtle.end_fill()

# The white middle band indicates peace and truth
# A big story behind the middle circle in our flag from gandhi to our freedom
# Drawing the Dharma Chakra

# =============================
turtle.penup()
turtle.goto(70, 0)
turtle.pendown()
turtle.color("navy")
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()

turtle.penup()
turtle.goto(60, 0)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

turtle.penup()
turtle.goto(-57, -8)
turtle.pendown()
turtle.color("navy")
for i in range(24):
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(15)
    turtle.right(15)
    turtle.pendown()

turtle.penup()
turtle.goto(20, 0)
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# Drawing the chakra blue spokes
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.pensize(2)
for i in range(24):
    turtle.forward(60)
    turtle.backward(60)
    turtle.left(15)

# ====================================
window.exitonclick()
