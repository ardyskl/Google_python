#!/usr/bin/env python3

import random
import csv

# New function
def get_userlst():
    new_list = []
    n = int(input("Enter number of element for this list: "))
    for i in range(0, n):
        element = int(input())
        new_list.append(element)
    print(new_list)
    return new_list

with open('input_list.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # writing the input list to csv
    writer.writerow(get_userlst())
