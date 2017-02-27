from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    n = 100
    data = numpy.arange(n, dtype=float)
    comm.bcast(n, root=0)
    comm.Bcast(data, root=0)
else:
    n = comm.bcast(None, root=0)
    data = numpy.zeros(n, float)
    comm.Bcast(data, root=0)

if rank == 1:
    print(n)
    print(data)

