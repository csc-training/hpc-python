from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4

data = np.arange(2) / 10. + rank

if rank == 0:
    recv_buf = np.zeros(8)
else:
    recv_buf = None

if rank == 0:
    print("Original data")
comm.Barrier()

print("rank ", rank, data)

comm.Gather(data, recv_buf, root=0)

comm.Barrier()
if rank == 0:
    print()
    print("Final data")
comm.Barrier()

print("rank ", rank, recv_buf)


