#!/usr/bin/env python3

import datetime
import os
import math
import sys
import traceback
from datetime import date

print("Welcome to our tasks app!")
print("[log only significant work per day]")

cont = "y"
while(cont.lower() == "y"):

    choice = int(input("\nHow many tasks did you finish today? [upto 10 only]: "))

    if choice == 1:
        task = str(input("What was the task? "))
        today = date.today()

        print(today.strftime("\n%d, %b %Y"))
        print("=================================")
        print(task)
        print("=================================")

        choice_input = str(input("Did you finish them? [Y/n]: "))

        if choice_input == 'y':
            print("""
  |
  |
  |
  |  Done.
            """)

        if choice_input == 'n':
            print("Don't give up.")

    if choice == 2:

        task1 = str(input("\nEnter first task: "))
        task2 = str(input("Enter second task: "))

        tasks = [task1, task2]
        today = date.today()

        print(today.strftime("\n%d, %b %Y"))
        print("=================================")

        for element in tasks:
            print(element)

        print("=================================")

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("""
  |
  |
  |
  |  Done.
            """)

        if choice_input == 'n':
            print("Don't give up.")

    if choice == 3:
        task1 = str(input("Enter first task: "))
        task2 = str(input("Enter second task: "))
        task3 = str(input("Enter third task: "))

        tasks = [task1, task2, task3]
        today = date.today()

        print(today.strftime("\n%d, %b %Y"))
        print("=================================")

        for element in tasks:
            print(element)

        print("=================================")

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("""
  |
  |
  |
  |  Done.
            """)

        if choice_input == 'n':
            print("Don't give up.")

    if choice == 4:
        task1 = str(input("Enter first task: "))
        task2 = str(input("Enter second task: "))
        task3 = str(input("Enter third task: "))
        task4 = str(input("Enter fourth task: "))

        tasks = [task1, task2, task3, task4]
        today = date.today()

        print(today.strftime("\n%d, %b %Y"))
        print("=================================")

        for element in tasks:
            print(element)

        print("=================================")

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("""
  |
  |
  |
  |  Done.
            """)

        if choice_input == 'n':
            print("Don't give up.")

    if choice == 5:
        task1 = str(input("Enter first task: "))
        task2 = str(input("Enter second task: "))
        task3 = str(input("Enter third task: "))
        task4 = str(input("Enter fourth task: "))
        task5 = str(input("Enter fifth task: "))

        tasks = [task1, task2, task3, task4, task5]
        today = date.today()

        print(today.strftime("\n%d, %b %Y"))
        print("=================================")

        for element in tasks:
            print(element)

        print("=================================")

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("""
  |
  |
  |
  |  Done.
            """)

        if choice_input == 'n':
            print("Don't give up.")

    if choice == 6:
        task1 = str(input("Enter first task: "))
        task2 = str(input("Enter second task: "))
        task3 = str(input("Enter third task: "))
        task4 = str(input("Enter fourth task: "))
        task5 = str(input("Enter fifth task: "))
        task6 = str(input("Enter sixth task: "))

        tasks = [task1, task2, task3, task4, task5, task6]
        today = date.today()

        print(today.strftime("\n%d, %b %Y"))
        print("=================================")

        for element in tasks:
            print(element)

        print("=================================")

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("""
  |
  |
  |
  |  Done.
            """)

        if choice_input == 'n':
            print("Don't give up.")

    if choice == 7:
        task1 = str(input("Enter first task: "))
        task2 = str(input("Enter second task: "))
        task3 = str(input("Enter third task: "))
        task4 = str(input("Enter fourth task: "))
        task5 = str(input("Enter fifth task: "))
        task6 = str(input("Enter sixth task: "))
        task7 = str(input("Enter seventh task: "))

        tasks = [task1, task2, task3, task4, task5, task6, task7]
        today = date.today()

        print(today.strftime("\n%d, %b %Y"))
        print("=================================")

        for element in tasks:
            print(element)

        print("=================================")

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("""
  |
  |
  |
  |  Done.
            """)

        if choice_input == 'n':
            print("Don't give up.")

    if choice == 8:
        task1 = str(input("Enter first task: "))
        task2 = str(input("Enter second task: "))
        task3 = str(input("Enter third task: "))
        task4 = str(input("Enter fourth task: "))
        task5 = str(input("Enter fifth task: "))
        task6 = str(input("Enter sixth task: "))
        task7 = str(input("Enter seventh task: "))
        task8 = str(input("Enter eights task: "))

        tasks = [task1, task2, task3, task4, task5, task6, task7, task8]
        today = date.today()

        print(today.strftime("\n%d, %b %Y"))
        print("=================================")

        for element in tasks:
            print(element)

        print("=================================")

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("""
  |
  |
  |
  |  Done.
            """)

        if choice_input == 'n':
            print("Don't give up.")


    if choice == 9:
        task1 = str(input("Enter first task: "))
        task2 = str(input("Enter second task: "))
        task3 = str(input("Enter third task: "))
        task4 = str(input("Enter fourth task: "))
        task5 = str(input("Enter fifth task: "))
        task6 = str(input("Enter sixth task: "))
        task7 = str(input("Enter seventh task: "))
        task8 = str(input("Enter eights task: "))
        task9 = str(input("Enter ninth task: "))

        tasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9]
        today = date.today()

        print(today.strftime("\n%d, %b %Y"))
        print("=================================")

        for element in tasks:
            print(element)

        print("=================================")

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("""
  |
  |
  |
  |  Done.
            """)

        if choice_input == 'n':
            print("Don't give up.")

    if choice == 10:
        task1 = str(input("Enter first task: "))
        task2 = str(input("Enter second task: "))
        task3 = str(input("Enter third task: "))
        task4 = str(input("Enter fourth task: "))
        task5 = str(input("Enter fifth task: "))
        task6 = str(input("Enter sixth task: "))
        task7 = str(input("Enter seventh task: "))
        task8 = str(input("Enter eights task: "))
        task9 = str(input("Enter ninth task: "))
        task10 = str(input("Enter tenth task: "))

        tasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10]
        today = date.today()

        print(today.strftime("\n%d, %b %Y"))
        print("=================================")

        for element in tasks:
            print(element)

        print("=================================")

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("""
  |
  |
  |
  |  Done.
            """)

        if choice_input == 'n':
            print("Don't give up.")

    cont = input("Do you want to enter more tasks? [y/n]: ")

    if cont == "n":
        print("Thanks for using Tasks!")
        quit()
