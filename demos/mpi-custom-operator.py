# SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>
#
# SPDX-License-Identifier: MIT

from mpi4py import MPI

def add(x,y):
    return x+y

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

mpi_add = MPI.Op.Create(add)

data = arange(10 * size, dtype=float) * (rank + 1)
buffer = zeros(size * 10, float)

n = comm.reduce(rank, op=mpi_add, root=0) # returns the value
comm.Reduce(data, buffer, op=mpi_add, root=0) # in-place modification

