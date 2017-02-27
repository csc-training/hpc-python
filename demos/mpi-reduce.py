from mpi4py import MPI
from numpy import arange, empty

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = arange(size * 10, dtype=float) * (rank + 1)
buffer = empty(size * 10, float)
if rank == 0:
    n = comm.reduce(rank, op=MPI.SUM, root=0)  # returns the value
else:
    comm.reduce(rank, op=MPI.SUM, root=0)

comm.Reduce(data, buffer, op=MPI.SUM, root=0)  # in-place modification

if rank == 0:
    print("Sum of ranks: " + str(n))
    print("Received data:\n" + str(buffer))

