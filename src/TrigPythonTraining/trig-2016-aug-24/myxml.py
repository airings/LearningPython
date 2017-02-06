#!/usr/bin/env python

def xml(tagname, text='', **kwargs):
    attributes = ''
    for key, value in kwargs.items():
        attributes += ' {}="{}"'.format(key, value)

    return "<{0}{2}>{1}</{0}>".format(tagname, text, attributes)

print xml('foo')         #     => <foo></foo>
print xml('foo', 'bar')  #     => <foo>bar</foo>

print xml('p', xml('i', xml('b', 'Hello')))
# # # # # # # # # # =>    <p><i><b>Hello</b></i></p>

print xml('foo', 'bar', a=1)       #  => <foo a="1">bar</foo>
print xml('foo', 'bar', a=1, b=2)   #  => <foo a="1" b="2">bar</foo>
print xml('foo', 'bar', a=1, b=2, c=3 )
# # # # # # # # #     #  <foo a="1" b="2" c="3">bar</foo>

# # attributes in the opening tag do NOT need to be in any order
# # yes, that is a hint!
