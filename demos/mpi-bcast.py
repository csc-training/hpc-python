from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4

if rank == 0:
    data = np.arange(8) / 10.
else:
    data = np.zeros(8)

if rank == 0:
    print("Original data")
comm.Barrier()

print("rank ", rank, data)

comm.Bcast(data, root=0)

comm.Barrier()
if rank == 0:
    print()
    print("Final data")
comm.Barrier()

print("rank ", rank, data)


