#!/usr/bin/env python

import os

dirname = raw_input("Enter dirname: ")

for file_number, filename in enumerate(os.listdir(dirname)):
    try:
        for line_number, line in enumerate(open(filename)):
            print "[{}] [{}] {}".format(file_number,
                                        line_number,
                                        line.rstrip())
    except IOError:
        print "Cannot open {}; ignoring".format(filename)
