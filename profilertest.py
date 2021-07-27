#!/usr/bin/env python3

@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

print(my_func())

if __name__ == '__main__':
    my_func()
