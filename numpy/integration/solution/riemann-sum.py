import numpy as np

# Construct xi
dx = 0.01
xi = np.arange(0, np.pi/2, dx)

xip = (xi[1:] + xi[:-1]) / 2.
s = np.sum(np.sin(xip) * dx)
print("Riemann sum: {0:f}".format(s))


