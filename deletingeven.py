#!/usr/bin/env python3

print("We'll test deleting even numbers from starting of a list")

def delete_starting_even(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
       lst = lst[1:]
    return lst

# Testing with random list elements
print("New list: ")
print(delete_starting_even([4, 8, 10, 11, 12, 15]))
print("New list: ")
print(delete_starting_even([4, 8, 10, 11, 17,]))
