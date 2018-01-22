from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4, 'Number of MPI tasks has to be 4.'

if rank == 0:
    print('First collective:')

# TODO: create data vector at task 0 and send it to everyone else
#       using collective communication
if rank == 0:
    data = ...
else:
    data = ...
...
print('  Task {0}: {1}'.format(rank, data))


# Prepare data vectors ..
data = ...  # TODO: create the data vectors
# .. and receive buffers
buff = numpy.full(8, -1, int)

# ... wait for every rank to finish ...
comm.barrier()
if rank == 0:
    print('')
    print('-' * 32)
    print('')
    print('Data vectors:')
print('  Task {0}: {1}'.format(rank, data))
comm.barrier()
if rank == 0:
    print('')
    print('c)')

# TODO: how to get the desired receive buffer using a single collective
#       communication routine?
...
print('  Task {0}: {1}'.format(rank, buff))

# ... wait for every rank to finish ...
buff[:] = -1
comm.barrier()
if rank == 0:
    print('')
    print('d)')

# TODO: how to get the desired receive buffer using a single collective
#       communication routine?
#       Hint: the receive buffer for Gatherv() is of the form:
#             [buffer, count, offset, MPI.INT64_T], where count and offset
#             are tuples of integers for each MPI task giving the number of
#             elements to receive and the displacement from the beginning of
#             the receive buffer, respectively
...
print('  Task {0}: {1}'.format(rank, buff))

# ... wait for every rank to finish ...
buff[:] = -1
comm.barrier()
if rank == 0:
    print('')
    print('e)')

# TODO: how to get the desired receive buffer using a single collective
#       communication routine?
...
print('  Task {0}: {1}'.format(rank, buff))

