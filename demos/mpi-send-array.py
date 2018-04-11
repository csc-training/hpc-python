from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = numpy.arange(100, dtype=float)
    comm.Send(data, dest=1)
elif rank == 1:
    data = numpy.empty(100, dtype=float)
    comm.Recv(data, source=0)

if rank == 1:
    print("Received:\n" + str(data))

