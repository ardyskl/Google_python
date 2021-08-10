#!/usr/bin/env python3

#===========================
# Codeacademy code for understadning QuickSort
#===========================

import csv
from random import randrange, shuffle

def quicksort(list, start, end):
  # this portion of list has been sorted
  if start >= end:
    return
  print("Running quicksort on {0}".format(list[start: end + 1]))
  # select random element to be pivot
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  print("Selected pivot {0}".format(pivot_element))
  # swap random element with last element in sub-lists
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  less_than_pointer = start

  for i in range(start, end):
    # we found an element out of place
    if list[i] < pivot_element:
      # swap element to the right-most portion of lesser elements
      print("Swapping {0} with {1}".format(list[i], pivot_element))
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      # tally that we have one more lesser element
      less_than_pointer += 1
  # move pivot element to the right-most portion of lesser elements
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  print("{0} successfully partitioned".format(list[start: end + 1]))
  # recursively sort left and right sub-lists
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)

def get_userlst():
    new_list = []
    n = int(input("Enter number of element for this list: "))
    for i in range(0, n):
        element = int(input())
        new_list.append(element)
    print(new_list)
    return new_list

list = get_userlst()
shuffle(list)
print("PRE SORT: ", list)
quicksort(list, 0, len(list) -1)
print("POST SORT: ", list)

with open('sorted.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # writing the input list to csv
    writer.writerow(list)
