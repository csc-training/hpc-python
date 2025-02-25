# SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>
#
# SPDX-License-Identifier: MIT

from mpi4py import MPI
from numpy import arange, empty

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 10
data = empty(n, float)
if rank == 0:
    data = arange(n, dtype=float)

comm.Bcast(data, 0)

if rank == 1:
    print("Received: " + str(data))

