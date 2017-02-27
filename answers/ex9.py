import numpy as np

A = np.random.random((2,2))
Asym = A + A.T
B = np.random.random((2,2))
Bsym = B + B.T
C =np.dot(Asym, Bsym)
eigs = np.linalg.eigvals(C)

print "Eigenvalues are: ", eigs

