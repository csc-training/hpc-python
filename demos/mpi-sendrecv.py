from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = numpy.arange(10, dtype=float) * (rank + 1) # send buffer
buffer = numpy.empty(10, float)                   # receive buffer
if rank == 0:
    comm.Sendrecv(data, dest=1, recvbuf=buffer, source=1)
elif rank == 1:
    comm.Sendrecv(data, dest=0, recvbuf=buffer, source=0)

print("Rank %d: %s" % (rank, str(buffer)))

