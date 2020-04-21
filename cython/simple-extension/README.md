## Simple Cython extension

### Creating a Cython extension
Create a simple Cython module (you can name it e.g. `cyt_module.pyx`)
containing the following function:
```
def subtract(x, y):
    result = x - y
    return result
```

Create then a **setup.py** for building the extension module.
Try to utilize the module e.g. as
```
from cyt_module import subtract

subtract(4.5, 2)
```
in interactive interpreter or in a simple script. Try different argument
types.

