#!/usr/bin/env python3

import random

print("A random list: ")
# A random list function
def random_lst():
    random_lst = []
    # range from
    for i in range(0, 50):
        # list will use any random number between 1 to 30)
        n = random.randint(1, 50)
        # adding numbers to our list
        random_lst.append(n)
    return random_lst
# print list
print(random_lst())
