#!/usr/bin/env python3

import sys
import os
import math

print("Prints every letter")

cont = "y"
while(cont.lower() == "y"):

    word = str(input("Enter your word: "))
    for element in word:
        print(element)

    cont = input("Do you want to try again? [y to continue] & [n to exit]: ")

    if cont == "n":
        print("Thanks for testing this script!")
        quit()
