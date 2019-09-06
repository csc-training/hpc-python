<!-- Title: Creating Cython modules -->

<!-- Short description:

In this article we show how to turn Python modules into Cythonized ones.

-->

# Creating Cython modules

Normally, when working with Cython one does not Cythonize the whole program
but only selected modules.

Let's have a look at a very simple Python module that we could store in
**my_module.py**:

~~~python
def add(x, y):
    result = x + y
    return result
~~~

The module would then be used from some other Python code for example as:

~~~python
from my_module import add

z = add(4, 5)
~~~

Cython can transform the Python code into an equivalent C-code utilizing the
Python API as:

~~~bash
$ cython3 my_module.py
~~~

The result is a file **my_module.c**, which can then be compiled into a
Python C-extension. One can investigate the C-file, but it is not really
meant for humans to read, and the length of the file is over 3000 lines!

Normally, Cython language extensions are used in the modules so that they are
no longer valid Python. Therefore one normally uses **.pyx** suffix in the
file names of Cython modules to indicate this, i.e. **my_module.py** would be
made into **my_module.pyx**.

In order to make building of C-extensions from Cython easier, one does not
normally use Cython directly from the command line but via Python distutils
**setup.py** build file:

~~~python
from distutils.core import setup
from Cython.Build import cythonize

setup(
     ext_modules=cythonize("my_module.pyx"),
)
~~~

In larger real-world applications, this setup file could contain several
modules.

One can then create the C-extension module with:

~~~bash
$ python3 setup.py build_ext --inplace
running build_ext
building 'my_module' extension
creating build
creating build/temp.linux-x86_64-3.6
gcc -pthread -Wno-unused-result -Wsign-compare -DDYNAMIC_ANNOTATIONS_ENABLED=1 -DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -fPIC -I/usr/include/python3.6m -c my_module.c -o build/temp.linux-x86_64-3.6/my_module.o
gcc -pthread -shared ...
~~~

where the `--inplace` option places the C-extension in the current directory.
The end result is a .so file containing the C-extension that can be imported
and used just the same as the pure Python module:

~~~python
from my_module import add

z = add(4, 5)
~~~

As the C-extension implements the fully dynamic Python code (just using the
Python C-API), transforming the pure Python module into C-extension gives
normally only very modest speed-ups. However, as we will discuss in the
following steps, by adding Cython language extensions into the code (so it is
no longer valid Python code) it is possible to achieve much more significant
performance improvements.
