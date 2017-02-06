#!/usr/bin/env python

class Person(object):
    population = 0  # class attribute

    def __init__(self, name):
        # class attributes
        # retrieving -- use the class or the instance
        # setting -- ONLY USE THE CLASS

        self.population = self.population + 1
        self.name = name
    def hello(self):
        return "Hello, {}".format(self.name)


p1 = Person('A')
p2 = Person('B')
print Person.population
print p1.population
print p2.population

print p1.hello()
print p1.__str__()
