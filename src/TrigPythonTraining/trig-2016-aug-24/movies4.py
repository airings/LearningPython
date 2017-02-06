#!/usr/bin/env python

movies = {'Spotlight' : { 'length':129, 'director':'Tom McCarthy'},
          'The Big Short': { 'length':130, 'director':'Adam McKay'},
          'The Martian': { 'length':141, 'director':'Ridley Scott',}
          }

look_for = raw_input("Enter movie name: ")

if look_for in movies:
    one_movie = movies[look_for]
    print "Found {}, {} min, dir {}".format(look_for,
                                            one_movie['length'],
                                            one_movie['director'])
else:
    print "Did not find {}".format(look_for)
