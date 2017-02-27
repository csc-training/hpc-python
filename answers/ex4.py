import numpy as np

my_list = [[1.1, 1.2, 1.3, 1.4], 
           [2.1, 2.2, 2.3, 2.4],
           [3.1, 3.2, 3.3, 3.4],
           [4.1, 4.2, 4.3, 4.4],
           ]

arr = np.array(my_list)
print(arr)
print()

sub1, sub2 = np.split(arr, 2)
print(sub1)
print()
print(sub2)
print()

orig = np.concatenate((sub1, sub2))
print(orig)
print()

sub1, sub2 = np.split(arr, 2, axis=1)
print(sub1)
print()
print(sub2)
print()

orig = np.concatenate((sub1, sub2), axis=1)
print(orig)
print()
