from mpi4py import MPI
from numpy import arange, empty

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

dimensions = (4, 4)
periodicity = (True, True)

grid = comm.Create_cart(dimensions, periodicity, reorder=True)
coords = grid.Get_coords(rank)

if rank == 0:
    print("Dim: " + str(grid.Get_dim()))
    print("Topology: " + str(grid.Get_topo()))

print("Rank %d: %s" % (rank, str(coords)))

