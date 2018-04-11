from mpi4py import MPI

comm = MPI.COMM_WORLD  # communicator object containing all processes
rank = comm.Get_rank()

if rank == 0:
   data = {'a': 7, 'b': 3.14}
   comm.send(data, dest=1)
elif rank == 1:
   data = comm.recv(source=0)

if rank == 1:
   print("Received: " + str(data))

