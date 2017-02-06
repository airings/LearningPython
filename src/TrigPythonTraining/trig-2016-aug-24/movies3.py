#!/usr/bin/env python

movies = [{'name':'Spotlight', 'length':129,
           'director':'Tom McCarthy'},
          {'name':'The Big Short', 'length':130,
           'director':'Adam McKay'},
          {'name':'The Martian', 'length':141,
           'director':'Ridley Scott', 'rental_time':'week'}]

look_for = raw_input("Enter movie name: ")

for one_movie in movies:
    if look_for == one_movie['name']:
        print "Found {}, {} min, dir {}".format(one_movie['name'],
                                                one_movie['length'],
                                                one_movie['director'])
        break
else:
    print "Did not find {}".format(look_for)
