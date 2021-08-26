#!/usr/bin/env python3

import datetime
import os
import os.path
import sys
import traceback
from datetime import date
from time import gmtime, strftime

def tasks():

    choice = int(input("\nHow many tasks did you finish today? [upto 10 only]: "))

    if choice == 1:

        task = str(input("What was the task?\n"))
        today = datetime.datetime.now()
        path = 'tasks/'

        filename = os.path.join(path, strftime("%Y%m%d-%H%M%S"))
        f = open(filename + '.txt', "a")
        print(today.strftime("\n%d %b %Y"), file=f)
        print(today.strftime("\n%d %b %Y"))
        print("=================================", file=f)
        print(task)
        print(task, file=f)
        print("=================================", file=f)

        choice_input = str(input("\nDid you finish them? [y/n]: "))

        if choice_input == 'y':
            print("Done.")
            print("Log exported.")
            print("""
  |
  |
  |
  |  Done.
            """, file=f)

        if choice_input == 'n':
            print("Don't give up.")
            print("Don't give up.", file=f)

        f.close()

    if choice == 2:

        task1 = str(input("\nEnter first task: "))
        task2 = str(input("Enter second task: "))

        tasks = [task1, task2]
        today = datetime.datetime.now()
        path = 'tasks/'

        filename = os.path.join(path, today.strftime("%Y%m%d-%H%M%S"))
        f = open(filename + '.txt', "a")
        print(today.strftime("\n%d %b %Y"), file=f)
        print(today.strftime("\n%d, %b %Y"))
        print("=================================", file=f)

        for element in tasks:
            print(element, file=f)
            print(element)

        print("=================================", file=f)

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("Done.")
            print("Log exported.")
            print("""
  |
  |
  |
  |  Done.
            """, file=f)

        if choice_input == 'n':
            print("Don't give up.")
            print("Don't give up.", file=f)

        f.close()

    if choice == 3:

        task1 = str(input("Enter first task: "))
        task2 = str(input("Enter second task: "))
        task3 = str(input("Enter third task: "))

        tasks = [task1, task2, task3]
        today = datetime.datetime.now()
        path = 'tasks/'

        filename = os.path.join(path, today.strftime("%Y%m%d-%H%M%S"))
        f = open(filename + '.txt', "a")
        print(today.strftime("\n%d %b %Y"), file=f)
        print(today.strftime("\n%d, %b %Y"))
        print("=================================", file=f)

        for element in tasks:
            print(element, file=f)
            print(element)

        print("=================================", file=f)

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("Done.")
            print("Log exported.")
            print("""
  |
  |
  |
  |  Done.
            """, file=f)

        if choice_input == 'n':
            print("Don't give up.")
            print("Don't give up.", file=f)

        f.close()

    if choice == 4:
        task1 = str(input("Enter first task: "))
        task2 = str(input("Enter second task: "))
        task3 = str(input("Enter third task: "))
        task4 = str(input("Enter fourth task: "))

        tasks = [task1, task2, task3, task4]
        today = datetime.datetime.now()
        path = 'tasks/'

        filename = os.path.join(path, today.strftime("%Y%m%d-%H%M%S"))
        f = open(filename + '.txt', "a")
        print(today.strftime("\n%d %b %Y"), file=f)
        print(today.strftime("\n%d, %b %Y"))
        print("=================================", file=f)

        for element in tasks:
            print(element, file=f)
            print(element)

        print("=================================", file=f)

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("Done.")
            print("Log exported.")
            print("""
  |
  |
  |
  |  Done.
            """, file=f)

        if choice_input == 'n':
            print("Don't give up.")
            print("Don't give up.", file=f)

        f.close()

    if choice == 5:
        task1 = str(input("Enter first task: "))
        task2 = str(input("Enter second task: "))
        task3 = str(input("Enter third task: "))
        task4 = str(input("Enter fourth task: "))
        task5 = str(input("Enter fifth task: "))

        tasks = [task1, task2, task3, task4, task5]
        today = datetime.datetime.now()
        path = 'tasks/'

        filename = os.path.join(path, today.strftime("%Y%m%d-%H%M%S"))
        f = open(filename + '.txt', "a")
        print(today.strftime("\n%d %b %Y"), file=f)
        print(today.strftime("\n%d, %b %Y"))
        print("=================================", file=f)

        for element in tasks:
            print(element, file=f)
            print(element)

        print("=================================", file=f)

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("Done.")
            print("Log exported.")
            print("""
  |
  |
  |
  |  Done.
            """, file=f)

        if choice_input == 'n':
            print("Don't give up.")
            print("Don't give up.", file=f)

        f.close()

    if choice == 6:
        task1 = str(input("Enter first task: "))
        task2 = str(input("Enter second task: "))
        task3 = str(input("Enter third task: "))
        task4 = str(input("Enter fourth task: "))
        task5 = str(input("Enter fifth task: "))
        task6 = str(input("Enter sixth task: "))

        tasks = [task1, task2, task3, task4, task5, task6]
        today = datetime.datetime.now()
        path = 'tasks/'

        filename = os.path.join(path, today.strftime("%Y%m%d-%H%M%S"))
        f = open(filename + '.txt', "a")
        print(today.strftime("\n%d %b %Y"), file=f)
        print(today.strftime("\n%d, %b %Y"))
        print("=================================", file=f)

        for element in tasks:
            print(element, file=f)
            print(element)

        print("=================================", file=f)

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("Done.")
            print("Log exported.")
            print("""
  |
  |
  |
  |  Done.
            """, file=f)

        if choice_input == 'n':
            print("Don't give up.")
            print("Don't give up.", file=f)

        f.close()

    if choice == 7:
        task1 = str(input("Enter first task: "))
        task2 = str(input("Enter second task: "))
        task3 = str(input("Enter third task: "))
        task4 = str(input("Enter fourth task: "))
        task5 = str(input("Enter fifth task: "))
        task6 = str(input("Enter sixth task: "))
        task7 = str(input("Enter seventh task: "))

        tasks = [task1, task2, task3, task4, task5, task6, task7]
        today = datetime.datetime.now()
        path = 'tasks/'

        filename = os.path.join(path, today.strftime("%Y%m%d-%H%M%S"))
        f = open(filename + '.txt', "a")
        print(today.strftime("\n%d %b %Y"), file=f)
        print(today.strftime("\n%d, %b %Y"))
        print("=================================", file=f)

        for element in tasks:
            print(element, file=f)
            print(element)

        print("=================================", file=f)

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("Done.")
            print("Log exported.")
            print("""
  |
  |
  |
  |  Done.
            """, file=f)

        if choice_input == 'n':
            print("Don't give up.")
            print("Don't give up.", file=f)

        f.close()

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
        today = datetime.datetime.now()
        path = 'tasks/'

        filename = os.path.join(path, today.strftime("%Y%m%d-%H%M%S"))
        f = open(filename + '.txt', "a")
        print(today.strftime("\n%d %b %Y"), file=f)
        print(today.strftime("\n%d, %b %Y"))
        print("=================================", file=f)

        for element in tasks:
            print(element, file=f)
            print(element)

        print("=================================", file=f)

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("Done.")
            print("Log exported.")
            print("""
  |
  |
  |
  |  Done.
            """, file=f)

        if choice_input == 'n':
            print("Don't give up.")
            print("Don't give up.", file=f)

        f.close()


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
        today = datetime.datetime.now()
        path = 'tasks/'

        filename = os.path.join(path, today.strftime("%Y%m%d-%H%M%S"))
        f = open(filename + '.txt', "a")
        print(today.strftime("\n%d %b %Y"), file=f)
        print(today.strftime("\n%d, %b %Y"))
        print("=================================", file=f)

        for element in tasks:
            print(element, file=f)
            print(element)

        print("=================================", file=f)

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("Done.")
            print("Log exported.")
            print("""
  |
  |
  |
  |  Done.
            """, file=f)

        if choice_input == 'n':
            print("Don't give up.")
            print("Don't give up.", file=f)

        f.close()

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
        today = datetime.datetime.now()
        path = 'tasks/'

        filename = os.path.join(path, today.strftime("%Y%m%d-%H%M%S"))
        f = open(filename + '.txt', "a")
        print(today.strftime("\n%d %b %Y"), file=f)
        print(today.strftime("\n%d, %b %Y"))
        print("=================================", file=f)

        for element in tasks:
            print(element, file=f)
            print(element)

        print("=================================", file=f)

        choice_input = str(input("Did you finish them? [y/n]: "))

        if choice_input == 'y':
            print("Done.")
            print("Log exported.")
            print("""
  |
  |
  |
  |  Done.
            """, file=f)

        if choice_input == 'n':
            print("Don't give up.")
            print("Don't give up.", file=f)

        f.close()


    # f = open(filename + '.txt', 'a')
    # f.write(str(tasks() + '\n'))
    # f.close()

print("Welcome to our tasks app!")
print("[log only significant work per day]")

#ont = "y"
#while(cont.lower() == "y"):

tasks()
    #cont = input("Press [Q] to exit: ")

    #if cont == "q" or "Q":
        #print("==== Exiting ====")
sys.exit(0)
