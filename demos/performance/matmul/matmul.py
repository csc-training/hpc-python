import numpy as np

def multiply(a, b):
    n, m = a.shape
    c = np.zeros_like(a)
    for i in range(n):
        for j in range(m):
            for k in range(m):
                c[i,j] += a[i, k] * b[k, j]

    return c
    
