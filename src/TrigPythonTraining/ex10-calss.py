
class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('green tea')
s4 = Scoop('coffee')
s5 = Scoop('flavor5')
s6 = Scoop('flavor6')

for one_scoop in [s1,s2,s3]:
    print one_scoop.flavor

class Bowl():
    maxScoops = 3
    def __init__(self):
        self.scoops = []

    def add_scoops(self,*args):
        # self.scoops += args
        # for scoop in args:
        #     self.scoops.append(scoop)
        self.scoops += args[:self.maxScoops - len(self.scoops)]

    def flavors(self):
        return [scoop.flavor for scoop in self.scoops]

class BigBowl(Bowl):
    maxScoops = 5

b = Bowl()
b.add_scoops()
b.add_scoops(s1,s2)
b.add_scoops(s3)
b.add_scoops(s4)
b.add_scoops(s5,s6)
print ",".join(b.flavors())

c = BigBowl()
c.add_scoops()
c.add_scoops(s1,s2)
c.add_scoops(s3)
c.add_scoops(s4)
c.add_scoops(s5,s6)
print ",".join(c.flavors())

