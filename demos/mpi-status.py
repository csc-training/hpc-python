from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [1,3,5,7]
    comm.send(data, dest=1)

if rank == 1:
    info = MPI.Status()
    data = comm.recv(source=0, status=info)

    print("Received %d bytes of data." % info.Get_count())
    print("Received %d integers." % info.Get_elements(MPI.INT))

