#!/usr/bin/env python3

import sys
import time

def start_game():

    ready = str(input("Ready to start?: (y/n): "))

    return "---------------------------------------------------------")
    return "Welcome to Zork - The Unofficial Python Version.")

def first_part():

            # First loop
            return "---------------------------------------------------------"
			return "You are standing in an open field west of a white house, with a boarded front door.")
			return "(A secret path leads southwest into the forest.)")
		    return "There is a Small Mailbox.")

			choice = input("What do you do? [enter in lowercase]\n")

            if choice == 'take mainbox':
                return "---------------------------------------------------------"
                return "It is securely anchored."

            if choice == 'open mailbox':
                return "---------------------------------------------------------"
                return "Opening the small mailbox reveals a leaflet."

            if choice == 'go east':
                return "---------------------------------------------------------"
                return "The door is boarded and you cannot remove the boards.")

            if choice == 'open door':
                return "---------------------------------------------------------"
                return "The door cannot be opened.")

            if choice == 'take boards':
                return "---------------------------------------------------------"
                return "The boards are securely fastened.")

            if choice == 'look at house':
                return "---------------------------------------------------------"
                return "The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")

            if choice == 'read leaflet':
                return "---------------------------------------------------------"
                return "Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")

            if choice == 'go southwest':
                return pass # jump to different function

            else:

                player_choices = ['take mainbox', 'open mailbox', 'go east', 'open door', 'take boards', 'look at house', 'go southwest']

                choice = str(input("Want to try agian or [see choices]? [lowercase]"))

                if choice == 'see choices':
                    for element in player_choices:
                        print(element)

def second_part():
    #something
    return pass
