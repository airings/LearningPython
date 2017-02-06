def mysum(seq):
    'seq only contains numbers'
    sum = 0
    for ele in seq:
        sum += ele
    return sum

print mysum([1,2,3])
print mysum((1,2,30))
print mysum({1,2,8})
print mysum({1,2,8,'r'})