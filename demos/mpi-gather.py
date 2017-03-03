from mpi4py import MPI
import numpy as np
from sys import stdout

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4

data = np.arange(2) / 10. + rank  # NumPy array

# Let's create different Python objects for different MPI tasks
if rank == 0:
    py_data = 'foo.bar'
elif rank == 1:
    py_data = 12.34
elif rank == 2:
    py_data = {'key1' : 99.0, 'key2' : [-1, 2.3]}
else:
    py_data = [6.5, 4.3]


if rank == 1:
    recv_buf = np.zeros(8)
else:
    recv_buf = None

if rank == 0:
    print("Original data")

stdout.flush()
comm.Barrier()

print("rank ", rank, data)
print("rank ", rank, py_data)
stdout.flush()

comm.Gather(data, recv_buf, root=1)
new_data = comm.gather(py_data, root=1)

comm.Barrier()
if rank == 0:
    print()
    print("Final data")

stdout.flush()
comm.Barrier()

print("rank ", rank, recv_buf)
print("rank ", rank, new_data)

