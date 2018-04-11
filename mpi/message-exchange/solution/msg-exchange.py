from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Simple message exchange
meta = {'rank': rank}

if rank == 0:
    comm.send(meta, dest=1)
    msg = comm.recv(source=1)
elif rank == 1:
    msg = comm.recv(source=0)
    comm.send(meta, dest=0)
print("Rank %d received a message from rank %d." % (rank, msg['rank']))

# Simple message exchange using numpy arrays
n = 100000
data = numpy.full(n, rank, int)
buff = numpy.empty(n, int)

if rank == 0:
    comm.Send(data, dest=1)
    comm.Recv(buff, source=1)
elif rank == 1:
    comm.Recv(buff, source=0)
    comm.Send(data, dest=0)
print("Rank %d received an array filled with %ds." % (rank, buff[0]))

