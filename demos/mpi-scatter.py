from mpi4py import MPI
from numpy import arange, empty

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

buffer = empty(size, float)    # prepare a receive buffer
if rank == 0:
    n = range(size)
    data = arange(size**2, dtype=float)
    comm.scatter(n, root=0)
    comm.Scatter(data, buffer, root=0)
else:
    n = comm.scatter(None, root=0)      # returns the value
    comm.Scatter(None, buffer, root=0)  # in-place modification

if rank == 1:
    print("Rank 1: n=" + str(n))
    print("Rank 1: buffer=" + str(buffer))

