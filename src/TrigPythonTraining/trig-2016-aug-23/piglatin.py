#!/usr/bin/env python

word = raw_input("Enter a word: ").strip()

if word[0] in 'aeiou':
    print word + 'way'
else:
    print word[1:] + word[0] + 'ay'

# Pig Latin

# If the word starts with a vowel (a, e, i, o, or u)
# then we add "way" to the word

# eat -> eatway
# inside -> insideway
# up -> upway

# If the word doesn't start with a vowel,
# we move the first letter to the end
# and then add "ay"

# class -> lasscay
# table -> abletay
# computer -> omputercay

# Ask the user for a word, and print the translation into Pig Latin
