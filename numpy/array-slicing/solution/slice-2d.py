import numpy as np

my_list = [[1.1, 1.2, 1.3, 1.4], 
           [2.1, 2.2, 2.3, 2.4],
           [3.1, 3.2, 3.3, 3.4],
           [4.1, 4.2, 4.3, 4.4],
           ]

arr = np.array(my_list)
print(arr)
print()
print(arr[1,:])
print()
print(arr[:,2])
print()
arr[:2, :2] = 0.21
print(arr)
print()

checker = np.zeros((8,8))
checker[::2, ::2] = 1
checker[1::2, 1::2] = 1
print(checker)
