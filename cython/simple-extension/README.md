## Simple Cython extension

### Creating a Cython extension
Create a simple Cython module (you can name it e.g. `cyt_module.pyx`)
containing the following function:
```
def subtract(x, y):
    return x - y
```

Use the provided [setup.py](setup.py) for building the extension module.
Try to utilize the module e.g. as
```
from cyt_module import subtract

subtract(4.5, 2)
```
in interactive interpreter or in a simple script. Try different argument
types.

### Type declarations

Declare the function arguments as **int** and rebuild the extension (Note: if working with interactive interpreter you need to exit or reload the module).
What happens if you call now the subtract function with floating point
arguments?


