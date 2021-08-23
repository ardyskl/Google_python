#!/usr/bin/env python3

# ========================
# Ardy
# Fun code for DNA squescing
# ** None of these sequences are in anyway inteded to be tested in a lab
# or represent life as we know**
# ===========================

import sys
import traceback
import random

# Function to create a random DNA sequence
def sequence(length):
    return ''.join(random.choice('ACTG') for _ in range(length))

# Probability of DNA each base appearing is 0.25
# DNA string should be equal with base probability
def bases(DNA):
    DnaDict = {}
    for base in 'ATCG':
        DnaDict[base] = DNA.count(base)/float(len(DNA))
    return DnaDict

cont = "y"
while(cont.lower() == "y"):

    print("Welcome to DNA sequencer!")
    
    length = int(input("Enter lenght of the sequence: "))
    DNA = sequence(length)
    print(DNA)
    print(bases(DNA))

    cont = input("Do you want to find more sequences? [y/n]: ")

    if cont == "n":
        print("Thanks for using DNA sequencer!")
        quit()
