#!/usr/bin/env python

class MyIter(object):
    def __init__(self, data):
        self.data = data
        self.index = 0

    # when iter() is invoked on our object,
    # the __iter__ method is called
    def __iter__(self):
        return self             # I'm my own iterator

    # when next() is called, our next() method is called
    # (in Python 3,  it's called __next__)
    def next(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

m = MyIter('abc')
for item in m:
    print item
    
