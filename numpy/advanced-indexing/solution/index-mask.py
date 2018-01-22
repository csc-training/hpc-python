import numpy as np

arr = np.random.random(size=(10,10))
mask = arr > 0.5
print(arr[mask])

ind = np.nonzero(mask)
print("Indices")
print(ind)
print("Values")
print(arr[ind])
