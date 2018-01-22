import numpy as np
from math import sin, cos, pi
import numpy.ma as ma
import matplotlib.pyplot as plt

data = np.loadtxt('points_circle.dat')
plt.plot(data[:,0], data[:,1], 'o')

theta = 90.0 * pi / 180.0 
R = np.array(((cos(theta), -sin(theta)), (sin(theta), cos(theta))))
data_rot = np.dot(data, R)
plt.plot(data_rot[:,0], data_rot[:,1], 'd')
plt.axis('equal')
plt.show()
