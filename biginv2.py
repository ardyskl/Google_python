#!/usr/bin/env python3
# coding: UTF-8

#=============================
# week 2, Stanford
#=============================
# written by ardy

# implementing biginv2 to be more efficient
# time complexity: o(log n) UNTESTED ASSUMPTION;

import sys
import traceback
import math

# Here Lets import IntegerArray.txt firsthand
File = "IntegerArray.txt"
inFile = open(File, 'r')
# inFile = inFile.read()

with inFile as f:
    intList = [int(integers.strip()) for integers in f.readlines()]

count = 0

def invCount2(x):
    global count
    midsection = len(x)//2
    leftArray = x[:midsection]
    rightArray = x[midsection:]
    if len(x) > 1:
        # recursive calls to divide and conqure from left to right
        invCount2(leftArray)
        invCount2(rightArray)

        # Merging sorted arrays here
        # count of split inversions
        i, j = 0, 0
        a = leftArray; b = rightArray
        for k in range(len(a) + len(b) + 1):
            if a[i] <= b[j]:
                x[k] = a [i]
                i += 1
                if i == len(a) and j != len(b):
                    while j != len(b):
                        k += 1
                        x[k] = b[j]
                        j += 1
                    break
            elif a[i] > b[j]:
                x[k] = b[j]
                count += (len(a) - i)
                j += 1
                if j == len(b) and i != len(a):
                   while i != len(a):
                      k += 1
                      x[k] = a[i]
                      i += 1
                   break
    return x

# Driver code
print("Welcome to Inversion counting v2!")

cont = "y"
while(cont.lower() == "y"):

    # print the integers in an array
    print(invCount2(intList))
    print("\n=====ran on IntegerArray.txt======")
    # Final inversion count
    print("Result:", count)

    cont = input("Press [n] to exit: ")
    # you can test with your open integer dumb txts change line 17
    # place the text or csv file in the same directory

    if cont == "n":
        print("Thanks for using Inversion count v2!")
        sys.exit(0)
