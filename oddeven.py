#!/usr/bin/env python3

print("Welcome to our odd even finder")

def oddeven():
    if num % 2 == 0:
        print("{0} is even". format(num))
    else:
        print("{0} is odd". format(num))

cont = "y"
while(cont.lower() == "y"):
    num = int(input("Enter your number: "))
    oddeven()
    cont = input("Do you want go agian? [y to continue] & [n to exit]: ")

    if cont == "n":
        print("Thanks for using our little app!")
quit()
