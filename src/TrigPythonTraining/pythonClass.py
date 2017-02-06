class people(object):
    def __new__(cls, *args, **kwargs):
        print "__new__"
    def __init__(self, name):
        print "__init__"
        self.name = name
    def hello(self):
        return "Hello {}".format(self.name)

