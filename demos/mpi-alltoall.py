from mpi4py import MPI
import numpy as np
from sys import stdout

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4

data = np.arange(8) / 10. + rank
recv_buf = np.zeros(8)
# Python sequence, lenght has to be equal number to MPI tasks
py_data = []
for r in range(4):
    py_data.append({'key{0:02d}'.format(10*rank + r) : 10*rank + r})

if rank == 0:
    print("Original data")
comm.Barrier()

for r in range(size):
    if rank == r:
        print("rank ", rank, data)
        print("rank ", rank, py_data)
    comm.Barrier()

stdout.flush()

comm.Alltoall(data, recv_buf)
new_data = comm.alltoall(py_data)

comm.Barrier()
if rank == 0:
    print()
    print("Final data")

stdout.flush()
comm.Barrier()

for r in range(size):
    if rank == r:
        print("rank ", rank, recv_buf)
        print("rank ", rank, new_data)
    comm.Barrier()

stdout.flush()


