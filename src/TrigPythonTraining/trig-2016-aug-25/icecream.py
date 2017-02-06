#!/usr/bin/env python

# scoop (ball)

# create a Scoop class

class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('green tea')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')
s6 = Scoop('flavor 6')

for one_scoop in [s1,s2, s3]:
    print one_scoop.flavor
    
# is-a relationship (inheritance)   A is-a B
#   scoop is-a bowl?     bowl is-a scoop?  no.

# has-a relationship (composition) A has-a B
#   bowl has-a scoop?  yes.


# You can only put 3 scoops in a bowl
# Any more than that are dropped/lost/melted/eaten
# So: The first 3 scoops get in, the rest are ignored

class Bowl(object):
    max_scoops = 3

    def __init__(self):
        self.scoops = [ ]

    def add_scoops(self, *new_scoops):
        # for one_scoop in new_scoops:
        #     if len(self.scoops) >= 3:
        #         break
        #     self.scoops.append(one_scoop)

        self.scoops += new_scoops[:self.max_scoops -
                                  len(self.scoops)]
    def flavors(self):
        return [scoop.flavor
                for scoop in self.scoops]
        # output = []
        # for scoop in self.scoops:
        #     output.append(scoop)
        # return output

class BigBowl(Bowl):
    max_scoops = 5

# create a Bowl class
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3, s4, s5, s6)
print ','.join(b.flavors())

bb = BigBowl()
bb.add_scoops(s1, s2)
bb.add_scoops(s3, s4, s5, s6)
print ','.join(bb.flavors())

