import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

data = np.loadtxt('faulty_data.dat')
plt.plot(data[:,0], data[:,1], 'o')

x = data[:,0]
y = data[:,1]
mask = y > 35
y_m = ma.masked_array(y, mask)
x_m = ma.masked_array(x, mask)

fit_orig = np.polyfit(x, y, 2)
fit_masked = ma.polyfit(x_m, y_m, 2)

x_i = np.linspace(-6, 6, 35)
plt.plot(x_i, np.polyval(fit_orig, x_i), label='original')
plt.plot(x_i, np.polyval(fit_masked, x_i), label='masked')
plt.legend()
plt.show()
