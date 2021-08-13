#!/usr/bin/env python3

import os
import sys
import math
import traceback

def main():

    try:
        # Function to add to string
        def toString(list):
            return ''.join(list)

        # Main permutation Function
        def permute(x, y, z):
            if y == z:
                print(toString(x))
            else:
                for i in range(y, z+1):
                    x[y], x[i] = x[i], x[y]
                    permute(x, y+1, z)
                    x[y], x[i] = x[i], x[y] # backtrack

        print("Welcome to Permutations!")

        cont = "y"
        while(cont.lower() == "y"):

            string = str(input("Please enter your text: "))
            n = len(string)
            a = list(string)
            permute(a, 0, n-1)

            cont = input("Do you want to permute another text? [y/n]: ")

            if cont == "n":
                print("Thanks for using my Backtracking algorithm!")
                quit()

    except KeyboardInterrupt:
        print("\n--- Backtracking takes a while ---")
        quit()

    except Exception:
        traceback.print_exc(file=sys.stdout)
        sys.exit(0)

if __name__ == "__main__":
    main()
