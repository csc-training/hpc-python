from time import time
import numpy as np

def kernel(zr, zi, cr, ci, lim, cutoff):
    ''' Computes the number of iterations `n` such that 
        |z_n| > `lim`, where `z_n = z_{n-1}**2 + c`.
    '''
    count = 0
    while ((zr*zr + zi*zi) < (lim*lim)) and count < cutoff:
        zr, zi = zr * zr - zi * zi + cr, 2 * zr * zi + ci
        count += 1
    return count

def compute_mandel(cr, ci, N, bound=1.5, lim=1000., cutoff=1e6):
    """
    Compute a 2delelelel of - > _.

    Args:
        cr: (todo): write your description
        ci: (todo): write your description
        N: (todo): write your description
        bound: (todo): write your description
        lim: (todo): write your description
        cutoff: (float): write your description
    """
    mandel = np.empty((N, N), dtype=int)
    grid_x = np.linspace(-bound, bound, N)
    t0 = time()
    for i, x in enumerate(grid_x):
        for j, y in enumerate(grid_x):
            mandel[i,j] = kernel(x, y, cr, ci, lim, cutoff)
    return mandel, time() - t0

