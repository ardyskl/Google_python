#!/usr/bin/env python3

import traceback
import sys

sys.setrecursionlimit(2 ** 20)

def test(n):

    if n == 0:
        return 1

    return n * test(n - 1)

if __name__ == '__main__':

    # take input from user
    input = int(input("Enter a number: \n"))
    print(test(input))
