from mpi4py import MPI
import numpy
from sys import stdout

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Send and receive buffers
n = 100000
data = numpy.full(n, rank, int)
buff = numpy.zeros(n, int)

if rank == 0:
    print("Send and Recv:")

# Message chain using Send and Recv
tgt = rank + 1
src = rank - 1
if rank == 0:
    comm.Send(data, dest=tgt)
    print("  Rank %d: sent %d elements to rank %d." % (rank, len(data), tgt))
else:
    comm.Recv(buff, source=src)
    print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))
    if rank < size - 1:
        comm.Send(data, dest=tgt)
        print("  Rank %d: sent %d elements." % (rank, len(data)))

# ... wait for every rank to finish ...
stdout.flush()
comm.barrier()
if rank == 0:
    print("")
    print("Sendrecv (in the middle of the chain):")

# Message chain using Sendrecv when sending *and* receiving
tgt = rank + 1
src = rank - 1
if rank == 0:          # start of chain; only send
    comm.Send(data, dest=tgt)
    print("  Rank %d: sent %d elements to rank %d." % (rank, len(data), tgt))
elif rank == size - 1: # end of chain; only receive
    comm.Recv(buff, source=src)
    print("  Rank %d: received a message from rank %d." % (rank, src))
    print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))
else:                  # middle of chain; send and receive
    comm.Sendrecv(data, dest=tgt, recvbuf=buff, source=src)
    print("  Rank %d: sent %d elements to rank %d." % (rank, len(data), tgt))
    print("  Rank %d: received a message from rank %d." % (rank, src))
    print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))

# ... wait for every rank to finish ...
stdout.flush()
comm.barrier()
if rank == 0:
    print("")
    print("Sendrecv (everywhere using PROC_NULL):")

# Simplified version using PROC_NULL
tgt = rank + 1
src = rank - 1
if tgt >= size:
    tgt = MPI.PROC_NULL
if src < 0:
    src = MPI.PROC_NULL

# use the same MPI call to do all communication
comm.Sendrecv(data, dest=tgt, recvbuf=buff, source=src)
print("  Rank %d: sent %d elements to rank %d." % (rank, len(data), tgt))
print("  Rank %d: received a message from rank %d." % (rank, src))
print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))

