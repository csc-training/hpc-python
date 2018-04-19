import numpy as np
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Set the colormap
plt.rcParams['image.cmap'] = 'BrBG'

# Basic variables
a = 0.5          # Diffusion constant.
timesteps = 500  # Number of time-steps to evolve system.
image_interval = 50 # write frequency for png files

# Grid spacings
dx = 0.01
dy = 0.01
dx2 = dx**2
dy2 = dy**2

# For stability, this is the largest interval possible
# for the size of the time-step:
dt = dx2*dy2 / ( 2*a*(dx2+dy2) )

# TODO: Read the initial temperature field from file


def evolve(u, u_previous, a, dt):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    # TODO: determine the new temperature field based on previous values
    # and the numerical Laplacian according the explicit time evolution method


# Write figure of initial field to a file
plt.imshow(field)
plt.axis('off')
plt.savefig('heat_{0:03d}.png'.format(0))

# TODO: Implement the main iteration loop and write the figure 
# (to a new) file after each 'image_interval' iteration
