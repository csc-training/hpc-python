import numpy as np

A = np.random.random((2,2))
Asym = A + A.T
B = np.random.random((2,2))
Bsym = B + B.T

C = np.dot(Asym, Bsym)
print(C)

eigs = np.linalg.eigvals(C)
print("Eigenvalues are: " + str(eigs))

