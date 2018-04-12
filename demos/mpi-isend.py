from mpi4py import MPI
from numpy import arange, empty

def calculate_something(rank):
    print("Calculating something at rank %d ..." % rank)
    for i in range(1000):
        x = i*5.2 + i**2
    print("... and rank %d is done with calculus." % rank)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = arange(size, dtype=float) * (rank + 1)
    req = comm.Isend(data, dest=1)    # start a send
    calculate_something(rank)         # .. do something else ..
    req.wait()                        # wait for send to finish
    # safe to read/write data again

elif rank == 1:
    data = empty(size, float)
    req = comm.Irecv(data, source=0)  # post a receive
    calculate_something(rank)         # .. do something else ..
    req.wait()                        # wait for receive to finish
    # data is now ready for use

if rank == 1:
    print("Received:\n" + str(data))

