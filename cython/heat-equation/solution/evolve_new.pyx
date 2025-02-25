# SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>
#
# SPDX-License-Identifier: MIT

# cython: profile=True

import numpy as np
cimport numpy as cnp

import cython

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cdef laplacian(cnp.ndarray[cnp.double_t, ndim=2]u, cnp.ndarray[cnp.double_t, ndim=2]du, double dx2, double dy2):

    cdef int n = u.shape[0]
    cdef int m = u.shape[1]

    cdef int i,j

    # Multiplication is more efficient than division
    cdef double dx2inv = 1. / dx2
    cdef double dy2inv = 1. / dy2

    for i in range(1, n-1):
        for j in range(1, m-1):
            du[i, j] = (u[i+1, j] - 2*u[i, j] + u[i-1, j]) * dx2inv + \
                       (u[i, j+1] - 2*u[i, j] + u[i, j-1]) * dy2inv

    

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def evolve(cnp.ndarray[cnp.double_t, ndim=2]u, 
           cnp.ndarray[cnp.double_t, ndim=2]u_previous, 
           double a, double dt, double dx2, double dy2):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    laplacian(u_previous, u, dx2, dy2)
    # u *= a * dt
    u = u_previous + a*dt * u

    u_previous[:] = u[:]

