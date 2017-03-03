from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Send and receive buffers
n = 100000
data = numpy.full(n, rank, int)
buff = numpy.full(n, -1, int)

# Destination and source for messages (using PROC_NULL for out-of-bounds)
tgt = rank + 1
src = rank - 1
if tgt >= size:
    tgt = MPI.PROC_NULL
if src < 0:
    src = MPI.PROC_NULL

# Use a single MPI call to do communication
comm.Sendrecv(data, dest=tgt, recvbuf=buff, source=src)
print("  Rank %d: receive buffer is filled with %ds." % (rank, buff[0]))

