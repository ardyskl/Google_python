#!/usr/bin/env python3

import math

print("Welcome to binary search!")

# binary_search function
def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise
    list usually sorted"""
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

# Get a list from user
def get_userlst():
    new_list = []
    n = int(input("Enter number of element for this list [list should be sorted]: "))
    for i in range(0, n):
        element = int(input())
        new_list.append(element)
    print(new_list)
    return new_list

# Loop if user wants another search
cont = "y"
while(cont.lower() == "y"):

# Main --------------------------------
    list = get_userlst()
    key = int(input("Enter key [choose an element]: "))

    halt = binary_search(list, key)

    if halt == -1:
        print("Key not found")
    else:
        print("The key " + str(key) + " was found at index position " + str(halt) + ".")
# Main -------------------------------- # End
        cont = input("Do you want another search? [y to continue] & [n to exit]: ")

        if cont == "n":
            print("Thanks for using Binary search [build by ardy!]")
            quit()
