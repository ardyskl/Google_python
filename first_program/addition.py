#!/usr/bin/env python3

import math

def add(a, b):
    return a + b

print("Welcome to two number adder app!")

cont = "y"
while(cont.lower() == "y"):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result: {0}".format(add(a, b)))
    print()
    cont = input("Do you want another calculation? [y to continue] & [n to exit]: ")

    if cont == "n":
        print("Thanks for using our adder app!")
        quit()
