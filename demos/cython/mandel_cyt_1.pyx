from time import time
import numpy as np

def kernel(double zr, double zi, double cr, double ci, double lim, int cutoff):
    ''' Computes the number of iterations `n` such that 
        |z_n| > `lim`, where `z_n = z_{n-1}**2 + c`.
    '''
    cdef int count = 0
    while ((zr*zr + zi*zi) < (lim*lim)) and count < cutoff:
        zr, zi = zr * zr - zi * zi + cr, 2 * zr * zi + ci
        count += 1
    return count

def compute_mandel(cr, ci, N, bound=1.5, lim=1000., cutoff=1e6):
    mandel = np.empty((N, N), dtype=int)
    grid_x = np.linspace(-bound, bound, N)
    t0 = time()
    for i, x in enumerate(grid_x):
        for j, y in enumerate(grid_x):
            mandel[i,j] = kernel(x, y, cr, ci, lim, cutoff=cutoff)
    return mandel, time() - t0

