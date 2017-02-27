from mpi4py import MPI
from numpy import zeros, ones

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = ones((4,4), float) * -1
data[1:-1,1:-1] = rank
recvbuf_hor = zeros(4, float)
recvbuf_ver = zeros(4, float)

dimensions = (4, 4)
periodicity = (True, True)

grid = comm.Create_cart(dimensions, 
                         periodicity, reorder=True)

# Shift(direction, displacement)
nbr_up, nbr_down = grid.Shift(0, 1)
nbr_left, nbr_right = grid.Shift(1, 1)

sendbuf_hor = data[:,1].copy()
sendbuf_ver = data[1,:].copy()

grid.Sendrecv(sendbuf_hor, recvbuf=recvbuf_hor, 
                      dest=nbr_left, source=nbr_right)
grid.Sendrecv(sendbuf_ver, recvbuf=recvbuf_ver, 
                      dest=nbr_up, source=nbr_down)

data[:,-1] = recvbuf_hor
data[-1,:] = recvbuf_ver

sendbuf_hor = data[:,-2].copy()
sendbuf_ver = data[-2,:].copy()

grid.Sendrecv(sendbuf_hor, recvbuf=recvbuf_hor, 
                      dest=nbr_right, source=nbr_left)
grid.Sendrecv(sendbuf_ver, recvbuf=recvbuf_ver, 
                      dest=nbr_down, source=nbr_up)

data[:,0] = recvbuf_hor
data[0,:] = recvbuf_ver

if rank == 1:
    print("Rank 1:\n" + str(data))

