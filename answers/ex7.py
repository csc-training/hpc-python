import numpy as np
import matplotlib.pyplot as plt
import sys

filename = sys.argv[1]
xy = np.loadtxt(filename)

coef = np.polyfit(xy[:,0], xy[:,1], 2)
x = np.linspace(-6, 6, 35)
y_fit = np.polyval(coef, x)

plt.plot(xy[:,0], xy[:,1], 'o', markersize=14)
plt.plot(x, y_fit, linewidth=2)
plt.show()
