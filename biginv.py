#!/usr/bin/env python3
# coding: UTF-8

#=============================
# week 2, Stanford
#=============================
# written by ardy

'''
IntegerArray.txt
This file contains all of the 100,000 integers between 1 and
100,000 (inclusive) in some order, with no integer repeated.
Your task is to compute the number of inversions in the file
given, where the ith row of the file indicates the ith entry
of an array.
'''

# Time complexity in computing numbers in IntegerArray.txt is θ(n log n) or O(n log n) an ASSUMPTION; complixity analysis needed.

import math
import sys
import traceback

def main():
    try:

        def mergecount(b, c):
            res_arr, inv_count = [], 0
            # inv_count = [], 0
            while len(b) > 0 or len(c) > 0:
                if len(b) > 0 and len(c) > 0:
                    if b[0] < c[0]:
                        res_arr.append(b[0])
                        b = b[1:]
                    else:
                        res_arr.append(c[0])
                        c = c[1:]
                        inv_count += len(b)
                elif len(b) > 0:
                    res_arr.append(b[0])
                    b = b[1:]
                elif len(c) > 0:
                    res_arr.append(c[0])
                    c = c[1:]

            return res_arr, inv_count

        def sortcount(a):
            array_l = len(a)
            if array_l <= 1:
                return a, 0

            b, x = sortcount(a[:(array_l//2)])
            c, y = sortcount(a[(array_l//2):])
            d, z = mergecount(b, c)

            return d, x + y + z

        def get_userlst():
            array = []
            n = int(input("Enter number of element for test array: "))
            for i in range(0, n):
                element = int(input())
                array.append(element)
            #print(array)
            return array

        # Uncommented to loop back for more inversions
        # Driver code

        print("Welcome my inversion counting!")

        cont = "y"
        while(cont.lower() == "y"):
            #=============================
            # User test case

            choice = str(input("Want to test? [y/n]: "))

            if choice == 'n':
                print("==== Exiting ====")
                sys.exit(0)
            elif choice == 'y':
                Test = get_userlst()
                print("Testing using:", Test)
                # Should be based on user input array
                print("Returned:", sortcount(Test)[1])

            # Uncomment below for your own test cases
            # Test2 = [234, 45, 56, 76, 23, 56, 12, 24, 23, 21, 20, 3, 2, 1]
            # print("Testing using: ", Test3)
            # should be ?
            # print("Returned:", sortcount(Test2)[1])
            #===============================

            print("\n=====running on IntegerArray.txt======")
            with open('IntegerArray.txt', 'r') as f:
                print("Number of inversions possible:", sortcount([int(l) for l in f])[1])

                cont = input("Do you want more inversions? [y/n]: ")

                if cont == "n":
                    print("Thanks for using Inversion count!")
                    sys.exit(0)

    except (ValueError, KeyError):
        print("--- Enter integer value for array ---")

    except Exception:
        traceback.print_exc(file=sys.stdout)
        sys.exit(0)

    except KeyboardInterrupt:
        print("\n--- Shutdown requested exiting ---")
        quit()

    except Exception:
        traceback.print_exc(file=sys.stdout)
        sys.exit(0)

if __name__ == "__main__":
    main()
