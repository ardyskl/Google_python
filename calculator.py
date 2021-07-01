#!/usr/bin/env python3

import math

# A simple calculator
def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Welcome to our simple calculator")

cont = "y"
while(cont.lower() == "y"):

    choice = input("Please choose an operation: (+, -, *, /): ")

    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(num1, "+", num2, "= {0}".format(add(num1, num2)))

        elif choice == '-':
            print(num1, "+", num2, "= {0}".format(subtract(num1, num2)))

        elif choice == '*':
            print(num1, "*", num2, "= {0}".format(multiply(num1, num2)))

        elif choice == '/':
            print(num1, "+", num2, "= {0}".format(divide(num1, num2)))
        break

    else:
        print("Please enter a valid operation: Try again")
