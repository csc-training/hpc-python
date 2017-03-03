from mpi4py import MPI
import numpy as np
from sys import stdout

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4

if rank == 0:
    data = np.arange(8) / 10.  # NumPy array
    # Python sequence, lenght has to be equal number to MPI tasks
    py_data = ['foo', 'bar', 11.2, {'key' : 22}]
else:
    data = None
    py_data = None

recv_buf = np.zeros(2)

if rank == 0:
    print("Original data")

stdout.flush()
comm.Barrier()

print("rank ", rank, data)
print("rank ", rank, py_data)
stdout.flush()

comm.Scatter(data, recv_buf, root=0)
new_data = comm.scatter(py_data, root=0)

comm.Barrier()
if rank == 0:
    print()
    print("Final data")

stdout.flush()
comm.Barrier()

print("rank ", rank, recv_buf)
print("rank ", rank, new_data)


