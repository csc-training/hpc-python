from mpi4py import MPI
from numpy import arange, empty

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 10
data = empty(n, float)
if rank == 0:
    data = arange(n, dtype=float)

if rank == 0:
    for i in range(1, size):
        comm.Send(data, i)
else:
    comm.Recv(data, 0)

if rank == 1:
    print("Received: " + str(data))

