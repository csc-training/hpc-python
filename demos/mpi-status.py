from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [1,3,5,7]
    comm.send(data, dest=1, tag=11)

if rank == 1:
    info = MPI.Status()  # prepare an instance of Status
    data = comm.recv(source=0, tag=MPI.ANY_TAG, status=info)

    print("Message tag was: %d" % info.Get_tag())
    print("Received %d bytes of data." % info.Get_count())

    print("Received %d integers." % info.Get_elements(MPI.INT))

