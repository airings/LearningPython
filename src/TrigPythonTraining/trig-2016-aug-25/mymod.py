#!/usr/bin/env python
"This is the dumbest module ever written"

if __name__ == '__main__':
    print "Hello from {}!".format(__name__)

x = 100

def hello(name):
    "This is the friendliest function in the world!"
    return "Hello {}, from mymod!".format(name)

if __name__ == '__main__':
    print "Goodbye from {}!".format(__name__)
