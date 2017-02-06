#!/usr/bin/env python

import random
number = random.randint(1,100)
print number

guess = int(raw_input("Enter a number: "))

if guess > number:
    print "Too high!"
elif guess < number:
    print "Too low!"
elif guess == number:
    print "Yes!  You got it!"
else:
    print "You should never see this."
