import numpy as np
from scipy import linalg

A = np.array([[1,0],[1,1],[1,2]])
b = np.array([6,0,0])

print A.T.dot(b.T)

print linalg.qr(A)