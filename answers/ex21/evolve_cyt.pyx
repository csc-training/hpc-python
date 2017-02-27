import numpy as np
cimport numpy as cnp

cdef extern from "evolve.h":

    void evolve(double *u, double *u_previous, int nx, int ny,
                double a, double dt, double dx2, double dy2)

def evolve_py(cnp.ndarray[cnp.double_t,ndim=2] field,
              cnp.ndarray[cnp.double_t,ndim=2] field0,
              double a, double dt, double dx2, double dy2):

    cdef int nx = field.shape[0]
    cdef int ny = field.shape[1]

    evolve(&field[0,0], &field0[0,0], nx, ny, a, dt, dx2, dy2)


             
