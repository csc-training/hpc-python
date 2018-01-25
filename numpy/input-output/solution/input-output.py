import numpy as np
import sys

filename = sys.argv[1]
xy = np.loadtxt(filename)
xy[:,1] += 2.5
np.savetxt('new-' + filename, xy, fmt='%.6f', header='modified data')
