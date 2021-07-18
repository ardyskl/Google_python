#!/usr/bin/env python3

import math
import os
import sys
import traceback

def main():

    try:

        MORSE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-' }

        def encrypt(message):

            cipher = ''

            for letter in message:

                if letter != ' ':
                    cipher += MORSE_DICT[letter] + ' '
                else:
                    cipher += ' '

            return cipher

        def decrypt(message):

            message += ' '
            decipher = ''
            citext = ''

            for letter in message:
                if letter != ' ':
                    i = 0
                    citext += letter
                else:
                    i += 1
                    if i == 2:
                        decipher += ' '
                    else:
                        decipher += list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(citext)]
                        citext = ''
            return decipher

        def encrypt_result():

            message_string = str(input("Your message: "))
            result = encrypt(message_string.upper())
            return result

        def decrypt_result():

            dots_dashes = str(input("Enter dots & dashes: "))
            result = decrypt(dots_dashes)
            return result

        print("Welcome to Morse code cipher!")

        cont = "y"
        while(cont.lower() == "y"):

            choice = str(input("Please choose an option: [decrypt/encrypt]: "))

            if choice == 'encrypt':
                print(encrypt_result())

            if choice == 'decrypt':
                print(decrypt_result())

            cont = input("Do you want to decode/encode another message? [y to continue] & [n to exit]: ")

            if cont == "n":
                print("Thanks for using Morse code cipher!")
            else:
                print("--- Enter [y/n] exiting ---")
            quit()

    except ValueError:
        print("--- Enter correct Morse code ---")

    except Exception:
        traceback.print_exc(file=sys.stdout)
        sys.exit(0)

    except KeyboardInterrupt:
        input_key = input("\n--- Press [ENTER] to exit ---")
        if input_key == '':
            quit()

    except Exception:
        traceback.print_exc(file=sys.stdout)
        sys.exit(0)

if __name__ == "__main__":
    main()
