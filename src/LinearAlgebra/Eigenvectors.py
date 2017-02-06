import numpy as np
from scipy import linalg
from fractions import Fraction
A = np.array([[4,4], [-3,3]])
print A.T.dot(A)
la, v = linalg.eig(A.T.dot(A))
print la
print "v: ", v
print linalg.norm(v[:,1])
print Fraction(v[0,1])
print Fraction(10,8)

print A.dot(A.T)
la, u = linalg.eig(A.dot(A.T))
print la
print u

sigma = np.array([[np.sqrt(32), 0], [0, np.sqrt(18)]])
v = v.T
u = u

print v
print u
print u.dot(sigma).dot(v)

q = linalg.lu(A)
print q

