#!/usr/bin/env python

def line_to_dict(line):
    brand, color, size = line.strip().split("\t")
    return {'brand':brand,
            'color':color,
            'size':size}

shoes = [line_to_dict(line)
         for line in open('Files/shoe-data.txt')]

# Sort in order of size
def by_size(shoe_dict):
    return shoe_dict['size']

shoes.sort(key=by_size)

print shoes

# Read from shoe-data.txt using a list comprehension
# The result should be a list of dictionaries

# [ {'brand':'Adidas', 'color':'orange', 'size':'43'},
#    {'brand':'Nike', 'color':'black', 'size':'41'} ...]


# Start with a list of strings, with each string
# being one line in the file

# Then make a list of lists

# Then (finally) turn that list into a dict,
# using a function you've written
