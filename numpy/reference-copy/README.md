Investigate the behavior of the statements below by looking at the values of
the arrays a and b after assignments:

```
a = np.arange(5)
b = a
b[2] = -1
b = a[:]
b[1] = -1
b = a.copy()
b[0] = -1
```
