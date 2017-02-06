# generate a random number from 1 - 100
# tell the user:

# good uess -- you're right!
# too high
# too low

import random

rand = int(random.random() * 100)

# rand = random.randint(1, 100)

print rand


guess = int(raw_input("Your guess:"))

if guess == rand:
    print "You're right!"
elif guess > rand:
    print "Too high"
else:
    print "Too low"
