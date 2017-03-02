from mpi4py import MPI
import numpy as np
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4

if rank == 0:
    data = np.arange(8) / 10.
else:
    data = None

recv_buf = np.zeros(2)

if rank == 0:
    print("Original data")
    sys.stdout.flush()
comm.Barrier()

print("rank ", rank, data)
sys.stdout.flush()

comm.Scatter(data, recv_buf, root=0)

comm.Barrier()
if rank == 0:
    print()
    print("Final data")
    sys.stdout.flush()
comm.Barrier()

print("rank ", rank, recv_buf)


