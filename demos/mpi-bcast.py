from mpi4py import MPI
import numpy as np
from sys import stdout

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4

if rank == 0:
    data = np.arange(8) / 10. # NumPy array
    py_data = {'key1' : 0.0, 'key2' : 11} # Python object
else:
    data = np.zeros(8)
    py_data = None

if rank == 0:
    print("Original data")
stdout.flush()
comm.Barrier()

print("rank ", rank, data)
print("rank ", rank, py_data)
stdout.flush()

comm.Bcast(data, root=0)
new_data = comm.bcast(py_data, root=0)

comm.Barrier()
if rank == 0:
    print()
    print("Final data")
stdout.flush()
comm.Barrier()

print("rank ", rank, data)
print("rank ", rank, new_data)


