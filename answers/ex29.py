from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Send and receive buffers
n = 100000
data = numpy.full(n, rank, int)
buff = numpy.zeros(n, int)

# Destination and source for messages
tgt = rank + 1
src = rank - 1

if rank == 0:
    print("Send and Recv:")

# Message chain using Send and Recv
if rank == 0:
    comm.Send(data, dest=tgt, tag=tgt)
    print("  Rank %d: sent %d elements using tag '%d'." % \
            (rank, len(data), tgt))
else:
    comm.Recv(buff, source=src, tag=rank)
    print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))
    if rank < size - 1:
        comm.Send(data, dest=tgt, tag=tgt)
        print("  Rank %d: sent %d elements using tag '%d'." % \
                (rank, len(data), tgt))

# ... wait for every rank to finish ...
comm.barrier()
if rank == 0:
    print("")
    print("Status with ANY_SOURCE:")

# Alternative version that finds out the sender after communication
if rank == 0:
    comm.Send(data, dest=tgt, tag=tgt)
    print("  Rank %d: sent %d elements using tag '%d'." % \
            (rank, len(data), tgt))
else:
    info = MPI.Status()  # prepare an instance of Status
    comm.Recv(buff, source=MPI.ANY_SOURCE, tag=rank, status=info)
    print("  Rank %d: received a message from rank %d." % \
            (rank, info.Get_source()))
    print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))
    if rank < size - 1:
        comm.Send(data, dest=tgt, tag=tgt)
        print("  Rank %d: sent %d elements using tag '%d'." % \
                (rank, len(data), tgt))

# ... wait for every rank to finish ...
comm.barrier()
if rank == 0:
    print("")
    print("Simplified with PROC_NULL:")

# Simplified version where all ranks can send
send_tag = tgt
if tgt >= size:
    tgt = MPI.PROC_NULL  # set destination to "nowhere" in last rank
    send_tag = 0         # send tag can't be equal to MPI.PROC_NULL
if rank == 0:
    comm.Send(data, dest=tgt, tag=tgt)
    print("  Rank %d: sent %d elements using tag '%d'." % \
            (rank, len(data), tgt))
else:
    info = MPI.Status()
    comm.Recv(buff, source=MPI.ANY_SOURCE, tag=rank, status=info)
    print("  Rank %d: received a message from rank %d." % \
            (rank, info.Get_source()))
    print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))
    comm.Send(data, dest=tgt, tag=send_tag)
    print("  Rank %d: sent %d elements using tag '%d'." % \
            (rank, len(data), tgt))

# ... wait for every rank to finish ...
comm.barrier()
if rank == 0:
    print("")
    print("Sendrecv:")

### Full example using Sendrecv

# Destination and source for messages (using PROC_NULL for out-of-bounds)
tgt = rank + 1
src = rank - 1
send_tag = tgt
if tgt >= size:
    tgt = MPI.PROC_NULL
    send_tag = 0
if src < 0:
    src = MPI.PROC_NULL

# Use a single MPI call to do communication
info = MPI.Status()
comm.Sendrecv(data, dest=tgt, sendtag=send_tag,
        recvbuf=buff, source=src, recvtag=rank,
        status=info)
print("  Rank %d: sent %d elements using tag '%d'." % \
        (rank, len(data), send_tag))
print("  Rank %d: received a message from rank %d." % \
        (rank, info.Get_source()))
print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))

