import numpy as np
import os

def maxmem():
    # Check maximum memory from /proc/
    # Based on Python Cookbook
    # http://code.activestate.com/recipes/286222/
    # Works on most Linux systems but not in Mac OSX or Windows

    _scale = {'kB': 1024.0, 'mB': 1024.0 * 1024.0,
              'KB': 1024.0, 'MB': 1024.0 * 1024.0}

    _proc_status = '/proc/{0}/status'.format(os.getpid())
    with open(_proc_status) as f:
        v = f.read()

    # Find VmHWM value
    i = v.index('VmHWM:')
    v = v[i:].split(None, 3)
    return float(v[1]) * _scale[v[2]]

# Python and Numpy library memory usage
overhead = maxmem()

a = np.random.random((1024, 1024, 10))
b = np.random.random((1024, 1024, 10))
c = a - b
#c = 2.0 * a - 4.5 * b
#c = 2.0 * a - 4.5 * b + np.sin(a) - np.cos(b)
#c = 2.0 * a - 4.5 * b + (np.sin(a) - np.cos(b))
#c = (np.sin(a) - np.cos(b)) + 2.0 * a - 4.5 * b

#c = 2.0 * a
#c -= 4.5 * b
#c += np.sin(a)
#c -= np.cos(b)

mem = maxmem() - overhead

print("Size of single array: {0} MB".format(a.nbytes / 1024.0**2))
print("Maximum memory: {0:.3f} arrays".format(mem / a.nbytes))
