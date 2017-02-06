#!/usr/bin/env python

def mysum(numbers):
    total = 0
    for one_number in numbers:
        total += one_number
    return total

# define a new function, mysum, which works
# like the builtin "sum" function

# (No, don't use sum in your definition)

print mysum([10, 20, 30])             # returns 60
print mysum((10, 20, 30, 40))         # returns 100
print mysum({10, 20, 30, 40, 50})     # returns 150

# param can be a list, tuple, or set of numbers

# return the sum
