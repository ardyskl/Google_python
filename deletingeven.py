#!/usr/bin/env python3
import random

random_lst = []
for i in range(0, 50):
    n = random.randint(1, 30)
    random_lst.append(n)
return random_lst

#def delete_starting_even(random_lst):
#    while (len(random_lst) > 0 and random_lst[0] % 2 == 0):
#        random_lst = random_lst[1:]
#    return lst
# Testing with random list elements
#print(delete_starting_even(random_lst)
#print(delete_starting_even(random_lst)
