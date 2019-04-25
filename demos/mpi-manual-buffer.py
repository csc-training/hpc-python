from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = numpy.empty(100, dtype=float)
if rank == 0:
    data[:] = numpy.arange(100, dtype=float)
    comm.Send([data, 100, MPI.DOUBLE], dest=1)
elif rank == 1:
    comm.Recv([data, 100, MPI.DOUBLE], source=0)

if rank == 1:
    print("Received:\n" + str(data))
