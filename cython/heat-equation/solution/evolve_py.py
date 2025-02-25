# SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>
#
# SPDX-License-Identifier: MIT

import numpy as np
from numba import jit, void, double

# @jit(void(double[:,:], double[:,:], double, double, double, double), nopython=True, cache=True, fastmath=True, error_model='numpy')
# @jit(nopython=True, cache=True, fastmath=True)
@jit(nopython=True)
def evolve(u, u_previous, a, dt, dx2, dy2):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    n, m = u.shape

    # dx2inv = 1.0 / dx2
    # dy2inv = 1.0 / dy2
    for i in range(1, n-1):
        for j in range(1, m-1):
            u[i, j] = u_previous[i, j] + a * dt * ( \
             (u_previous[i+1, j] - 2*u_previous[i, j] + \
              u_previous[i-1, j]) / dx2 + \
              # u_previous[i-1, j]) * dx2inv + \
             (u_previous[i, j+1] - 2*u_previous[i, j] + \
              u_previous[i, j-1]) / dy2 )
              # u_previous[i, j-1]) * dy2inv )
    u_previous[:] = u[:]

