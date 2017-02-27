from mpi4py import MPI
from numpy import arange, zeros

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = arange(10, dtype=float) * (rank + 1)
buffer = zeros(size * 10, float)
if rank == 0:
    n = comm.gather(rank, root=0)
else:
    comm.gather(rank, root=0)

comm.Gather(data, buffer, root=0)

if rank == 0:
    print(n)
    print(buffer)

