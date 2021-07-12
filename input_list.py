#!/usr/bin/env python3

import random

# New function
def get_userlst():
    new_list = []
    n = int(input("Enter number of element for this list: "))
    for i in range(0, n):
        element = int(input())
        new_list.append(element)
    return new_list
print(get_userlst())
