from mpi4py import MPI
from numpy import arange, empty

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = arange(size, dtype=float) * (rank + 1)
buffer = empty(size, float)

obj = comm.alltoall(data)    # returns the value
comm.Alltoall(data, buffer)  # in-place modification

print("Rank %d: obj=%s" % (rank, str(obj)))
print("Rank %d: buffer=%s" % (rank, str(buffer)))

