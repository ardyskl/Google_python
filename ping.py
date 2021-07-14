#!/usr/bin/env python3

import csv
from os import system

def ping():

        choice = ['google', 'amazon', 'ibm', 'mysejahtera', 'my_url']
        for element in choice:
            print("Ping " + element)

        choice_input = input("Please select a site: [use lowercase]: ")

        if choice_input == 'google':
            system("ping google.com")

        elif choice_input == 'amazon':
            system("ping amazon.com")

        elif choice_input == 'ibm':
            system("ping ibm.com")

        elif choice_input == 'mysejahtera':
            system("ping mysejahtera.malaysia.gov.my")

        elif choice_input == 'my_url':
            url = input("Enter URL: ")
            system("ping " + url)

        else:
            print("Invalid input")
cont = "y"
while(cont.lower() == "y"):

    ping()

    cont = input("Do you want to ping another page? [y to continue] & [n to exit]: ")

    if cont == "n":
        print("Thanks for using my Ping program!")
        quit()
