#!/usr/bin/env python3

#======================
# Ardy, stanford week 1
# ======================

import math, random
from math import log
import sys

# Main function
def karatsuba(x ,y):
    if x <= 100 or y <= 100:
        return x * y
    else:
        n = 10 ** int(math.log10(x) / 2.0 + 0.5)
        a, b = x // n, x % n
        c, d = y // n, y % n
        # step 1
        step1 = karatsuba(a, c)
        # step 2
        step2 = karatsuba(b, d)
        # step 3
        step3 = karatsuba(a+b, c+d) - step1 - step2
        return n * n * step1 + n * step3 + step2

# Driver code
print("Welcome to Karatsuba multiplication algo!")

cont = "y"
while(cont.lower() == "y"):

    # x = 3141592653589793238462643383279502884197169399375105820974944592
    x = int(input("Enter an integer >= 64 digits: "))
    # y = 2718281828459045235360287471352662497757247093699959574966967627
    y = int(input("Enter another integer >= 64 digits: "))

    multiply = karatsuba(x, y)
    print(multiply)

    cont = input("Do you want another calculation? [y/n]: ")

    if cont == "n":
        print("Thanks for using my Karatsuba algo!")
        quit()
