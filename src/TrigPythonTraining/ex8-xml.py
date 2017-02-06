def xml(tag, value='', **kwargs):
    props = ''
    for key, value in kwargs.items():
        props += ' {}="{}"'.format(key,value)

    return '<{0}{2}>{1}</{0}>'.format(tag, value, props)

print xml('foo')
print xml('foo',xml('i','123'))
print xml('foo','bar', a=1)
print xml('foo','bar', a=1,b=2)
print xml('p',xml('i',xml('b', 'Hello')))