#!/usr/bin/env python

filename = 'Files/wcfile.txt'

counts = { 'lines' : 0,
           'characters': 0,
           'words': 0,
           'unique words': 0}

unique_words = set()

for line in open(filename):
    counts['lines'] += 1
    counts['characters'] += len(line)
    counts['words'] += len(line.split())
    unique_words.update(line.split())

# Report
counts['unique words'] = len(unique_words)

for key, value in counts.items():
    print "{}: {}".format(key, value)

# ask the user for a filename (or hard-code it)

# Print out:
# - Number of lines
# - Number of characters (yes, including whitespace)
# - Number of words (separated by whitespace)
# - Number of different words in the file
