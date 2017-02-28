from time import time
import numpy as np
cimport numpy as cnp

import cython

cdef int kernel(double zr, double zi, double cr, double ci, double lim, int cutoff):
    ''' Computes the number of iterations `n` such that 
        |z_n| > `lim`, where `z_n = z_{n-1}**2 + c`.
    '''
    cdef int count = 0
    while ((zr*zr + zi*zi) < (lim*lim)) and count < cutoff:
        zr, zi = zr * zr - zi * zi + cr, 2 * zr * zi + ci
        count += 1
    return count

@cython.boundscheck(False)
@cython.wraparound(False)
def compute_mandel(cr, ci, N, bound=1.5, lim=1000., cutoff=1e6):
    cdef cnp.ndarray[cnp.int_t, ndim=2] mandel
    mandel = np.empty((N, N), dtype=int)
    cdef cnp.ndarray[cnp.double_t, ndim=1] grid_x
    grid_x = np.linspace(-bound, bound, N)

    cdef int i,j
    cdef double x, y

    t0 = time()
    for i in range(N):
        for j in range(N):
            x = grid_x[i]
            y = grid_x[j]
            mandel[i,j] = kernel(x, y, cr, ci, lim, cutoff)
    return mandel, time() - t0

