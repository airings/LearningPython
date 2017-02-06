#!/usr/bin/env python

# get a sentence from the user
# and translate each word
# and then print the resulting translation
# on a single line

# (all lowercase letters, no punctuation)

sentence = raw_input("Enter a sentence: ").strip()

output = [ ]
for word in sentence.split():
    if word[0] in 'aeiou':
        output.append(word + 'way')
    else:
        output.append(word[1:] + word[0] + 'ay')

print ' '.join(output)
