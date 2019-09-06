import numpy as np

my_list = [[j +1 + (i + 1) / 10 for i in range(8)] for j in range(8)]

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
