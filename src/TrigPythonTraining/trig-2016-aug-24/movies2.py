#!/usr/bin/env python

movies = [('Spotlight', 129, 'Tom McCarthy'),
          ('The Big Short', 130, 'Adam McKay'),
          ('The Martian', 141, 'Ridley Scott')]

look_for = raw_input("Enter movie name: ")

for one_movie in movies:
    if look_for == one_movie[0]:
        print "Found {}, {} minutes, director {}".format(one_movie[0],
                                                         one_movie[1],
                                                         one_movie[2])
        break
else:
    print "Did not find {}".format(look_for)
