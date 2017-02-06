#!/usr/bin/env python

x = 100

def foo():
    global x
    x = 200
    print "In foo, the value of x is {}".format(x)

print "Before, the value of x is {}".format(x)
foo()
print "After, the value of x is {}".format(x)

# Scoping rules:

# L - local
# (E - enclosing function)

# G - global
# B - builtins
