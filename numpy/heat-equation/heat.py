import numpy as np
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Set the colormap
plt.rcParams['image.cmap'] = 'BrBG'


def evolve(u, u_previous, a, dt):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    # TODO: determine the new temperature field based on previous values
    # and the numerical Laplacian according the explicit time evolution method



def iterate(field, field0, a, dx, dy, timesteps, image_interval):
    """Run fixed number of time steps of heat equation"""
# TODO: Implement the main iteration loop and write the figure 
# (to a new) file after each 'image_interval' iteration

def init_fields(filename):
# TODO: Read the initial temperature field from file
# Create also a copy of the field for the previous time step

    return field, field0

def write_field(field, step):
    plt.gca().clear()
    plt.imshow(field)
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step))
