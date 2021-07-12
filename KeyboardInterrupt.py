#!/usr/bin/env python3

import math

# New function
def user_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("press control-c again to exit")
    return input(prompt)
print("Hello")
