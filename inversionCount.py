#!/usr/bin/env python3

import sys
import math

def InvCount(arr, n):

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                count += 1
    return count

def get_userlst():
    array = []
    n = int(input("Enter number of element for this array: "))
    for i in range(0, n):
        element = int(input())
        array.append(element)
    print(array)
    return array

# Driver code
print("Welcome my inversion counting algo!")

cont = "y"
while(cont.lower() == "y"):

    arr = get_userlst()
    x = len(arr)

    print("Number of inversions for your array:", InvCount(arr, x))

    cont = input("Do you want more inversions? [y/n]: ")

    if cont == "n":
        print("Thanks for using Inversion count!")
        sys.exit(0)
