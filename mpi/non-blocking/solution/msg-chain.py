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

# Destination and source for messages
tgt = rank + 1
src = rank - 1

if rank == 0:
    print("Isend and Irecv:")

# Message chain using Send and Recv
if rank > 0:
    req_recv = comm.Irecv(buff, source=src)
if rank < size - 1:
    req_send = comm.Isend(data, dest=tgt)
    req_send.Wait()
    print("  Rank %d: sent %d elements." % (rank, len(data)))
if rank > 0:
    req_recv.Wait()
    print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))

# ... wait for every rank to finish ...
stdout.flush()
comm.barrier()
if rank == 0:
    print("")
    print("Status with ANY_SOURCE:")

# Alternative version that finds out the sender after communication
if rank > 0:
    req_recv = comm.Irecv(buff, source=MPI.ANY_SOURCE, tag=rank)
if rank < size - 1:
    req_send = comm.Isend(data, dest=tgt, tag=tgt)
    req_send.Wait()
    print("  Rank %d: sent %d elements using tag '%d'." % \
            (rank, len(data), tgt))
if rank > 0:
    info = MPI.Status()
    req_recv.Wait(info)
    print("  Rank %d: received a message from rank %d." %
            (rank, info.Get_source()))
    print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))

# ... wait for every rank to finish ...
stdout.flush()
comm.barrier()
if rank == 0:
    print("")
    print("Simplified with PROC_NULL:")

# Simplified version where all ranks can send
send_tag = tgt
if tgt >= size:
    tgt = MPI.PROC_NULL  # set destination to "nowhere" in last rank
    send_tag = 0         # send tag can't be equal to MPI.PROC_NULL
req_recv = comm.Irecv(buff, source=MPI.ANY_SOURCE, tag=rank)
req_send = comm.Isend(data, dest=tgt, tag=send_tag)
req_send.Wait()
print("  Rank %d: sent %d elements using tag '%d'." % \
        (rank, len(data), tgt))
if rank > 0:
    info = MPI.Status()
    req_recv.Wait(info)
    print("  Rank %d: received a message from rank %d." %
            (rank, info.Get_source()))
    print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))

