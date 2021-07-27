#!/usr/bin/env python3

import math
import sys
import traceback
import os

#@profile
def encrypt(text, s):

    result = ""

    for i in range(len(text)):
        char = text[i]
        # For uppercase characters
        if(char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        # For lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

print("Welcome to Caesar cipher!")

cont = "y"
while(cont.lower() == "y"):

    choice = str(input("Please choose an option: [decrypt/encrypt]: "))

    if choice == 'encrypt':
        text = str(input("Enter your message: "))
        s = int(input("Shift places: "))
        print("Cipher is: ", encrypt(" " + text, s))

    else:
        print("choose an option above")

    if choice == 'decrypt':
        text = str(input("Enter encrypted message: "))
        s = int(input("Key: "))
        print("Decrypted(n = space): ", encrypt(text, 26 - s))

    cont = input("Do you want to decode/encode another message? [y to continue] & [n to exit]: ")

    if cont == "n":
        print("Thanks for using Caesar cipher!")
        quit()

#if __name__ == '__main__':
    #encrypt(text, s)
