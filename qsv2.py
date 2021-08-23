#!/usr/bin/env python3
# coding: UTF-8

#==========================================
# week 3, Stanford algorithm specialization
#===========================================
# Thanks to Dustin Goodman (github.com/dustinsgoodman) for this short and efficient code
# compiled by ardy

# This has all 3 parts
# Please see and understand all the lectures before going through this solution

# Quicksort uses divide-and-conquer and it's a recursive algorithm.

'''
PART 1
Integers between 1 and 10,000 are in unsorted order. (QuickSort.txt)
The integer in the i^th th row of the file gives you the i^th th
entry of an input array. Your task is to compute the total number of comparisons
used to sort the given input file by QuickSort.  As you know, the number of
comparisons depends on which elements are chosen as pivots.
So we'll ask you to explore three different pivoting rules.
'''

'''
PART 2
Compute the number of comparisons (as in Problem 1),
always using the final element of the given array as the pivot
element.  Again, be sure to implement the Partition subroutine exactly as it
is described in the video lectures. Recall from the lectures that,
just before the main Partition subroutine, you should exchange the pivot element
(i.e., the last element) with the first element.
'''

'''
PART 3
Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule.
[The primary motivation behind this rule is to do a little bit of extra work to get much better
performance on input arrays that are nearly sorted or reverse sorted.] In more detail, you should choose the pivot as follows.  Consider the first, middle, and final elements
of the given array.  (If the array has odd length it should be clear what the "middle" element is;
for an array with even length 2k, use the kth element as the "middle" element. So for the array 4 5 6 7,  the "middle" element is the second one i.e 5 and not 6)
Identify which of these three elements is the median (i.e., the one whose value is in between the other two)
and use this as your pivot.  As discussed in the first and second parts of this programming assignment,
be sure to implement Partition exactly as described in the video lectures (including exchanging the pivot element with the first element just before the main Partition subroutine).
'''

import sys
import traceback
import math

count = 0
def main():
    global count

    try:

        # Partition subroutine
        def partition(array):
            pivot = array[0]
            i = 1

            for j in range(1, len(array)):
                if array[j] < pivot:
                    array[j], array[i] = array[i], array[j]
                    i += 1

            position = i - 1
            array[0], array[position] = array[position], array[0]
            return position

        # PART 1
        def qs1(array):
            global count
            if len(array) <= 1:
                return array
            count += len(array) - 1
            pivot = partition(array)
            return qs1(array[:pivot]) + [array[pivot]] + qs1(array[pivot + 1:])

        # PART 2
        def qs2(array):
            global count
            if len(array) <= 1:
                return array
            count += len(array) - 1

            array[0], array[-1] = array[-1], array[0]
            pivot = partition(array)
            return qs2(array[:pivot]) + [array[pivot]] + qs2(array[pivot + 1:])

        # PART 3
        def qs3(array):
            global count
            if len(array) < 1:
                return array
            count += len(array) - 1

            # choosing pivot
            if len(array) % 2 == 0:
                ordset = [array[0], array[len(array)//2 - 1], array[-1]]
            else:
                ordset = [array[0], array[len(array)//2], array[-1]]
            ordset.sort()
            position = array.index(ordset[1])
            array[0], array[position] = array[position], array[0]

            pivot = partition(array)
            return qs3(array[:pivot]) + [array[pivot]] + qs3(array[pivot + 1:])

        # Driver code
        print("Welcome to QuickSort")

        cont = "y"
        while(cont.lower() == "y"):

            # choice = str(input("See choices? [y/n]: "))
            # if choice == 'y':

            choice_lst = ['1. Number of possible comparisions', '2. Comparisons using last element as pivot', '3. Comparisons using median of three']
            for element in choice_lst:
                print(element)

            choice_input = int(input("Please choose [1, 2 or 3]: "))

            if choice_input == 1:
                count = 0
                with open('QuickSort.txt', 'r') as f:
                    qs1([int(l) for l in f])
                print("\n=========running on QuickSort.txt=========")
                print("Number of possible comparisions:", count)

            if choice_input == 2:
                count = 0
                with open('QuickSort.txt', 'r') as f:
                    qs2([int(l) for l in f])
                print("\n=========running on QuickSort.txt=========")
                print("Comparisons using last element as pivot:", count)

            if choice_input == 3:
                count = 0
                with open('QuickSort.txt', 'r') as f:
                    qs3([int(l) for l in f])
                print("\n=========running on QuickSort.txt=========")
                print("Comparisons using median of three:", count)

            # elif choice == 'n':
                # print("==== Exiting ====")
                # sys.exit(0)

            cont = input("Press [Q] to exit: ")

            if cont == "q" or "Q":
                print("==== Exiting ====")
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

# count = 0
if __name__ == "__main__":
    # global count
    main()
