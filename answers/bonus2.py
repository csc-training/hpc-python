from __future__ import print_function
import numpy as np
import time

import matplotlib
import matplotlib.pyplot as plt

# Set the colormap
plt.rcParams['image.cmap'] = 'BrBG'

# Basic variables
a = 0.5          # Diffusion constant.
timesteps = 500  # Number of time-steps to evolve system.
image_interval = 4000 # write frequency for png files

# Grid spacings
dx = 0.01
dy = 0.01
dx2 = dx**2
dy2 = dy**2

# For stability, this is the largest interval possible
# for the size of the time-step:
dt = dx2*dy2 / ( 2*a*(dx2+dy2) )

# Read the initial temperature field from file
field = np.loadtxt('bottle.dat')
field0 = field.copy() # Array for field of previous time step


def evolve(u, u_previous, a, dt):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    u[1:-1, 1:-1] = u_previous[1:-1, 1:-1] + a * dt * ( \
            (u_previous[2:, 1:-1] - 2*u_previous[1:-1, 1:-1] + \
             u_previous[:-2, 1:-1]) / dx2 + \
            (u_previous[1:-1, 2:] - 2*u_previous[1:-1, 1:-1] + \
                 u_previous[1:-1, :-2]) / dy2 )
    u_previous[:] = u[:]

# Write initial field to a file
plt.imshow(field)
plt.axis('off')
plt.savefig('heat_{0:03d}.png'.format(0))
plt.hold(False)

# Iterate
t0 = time.time()
tc = 0.0
tio = 0.0
for m in range(1, timesteps+1):
    tc0 = time.time()
    evolve(field, field0, a, dt)
    tc += time.time() - tc0
    if m % image_interval == 0:
        tio0 = time.time()
        plt.imshow(field)
        plt.axis('off')
        plt.savefig('heat_{0:03d}.png'.format(m))
        tio += time.time() - tio0
        
t1 = time.time()

print("Running time: {0}".format(t1-t0))
print("Compute time: {0}".format(tc))
print("I/O time: {0}".format(tio))
