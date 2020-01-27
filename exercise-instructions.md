## Course setup

Download (clone) the exercise material with

```bash
$ git clone https://github.com/csc-training/hpc-python.git
```
The external Python packages can be installed with **pip** by using the provided 
[requirements.txt](requirements.txt) file. In CSC classroom this can be done 
(aftter cloning the material) as

```bash
$ cd hpc-python
$ pip3.4 install -r requirements.txt --user
```

You can test that all packages are available by
```bash
$ cd test
$ python3.4 test.py
```

## General exercise instructions

Simple exercises can be carried out directly in the interactive interpreter.
For more complex ones it is recommended to write the program into a .py file.
Still, it is useful to keep an interactive interpreter open for testing!
Some exercises contain references to functions/modules which are not addressed
in actual lectures. In these cases Python's interactive help (and google) are
useful, e.g.

```
In [4]: help(numpy)
```

It is not necessary to complete all the exercises, instead you may leave some
for further study at home. Also, some Bonus exercises are provided in the end.

### Visualisation

In some exercises it might be convenient to do visualisations with matplotlib
Python package. Interactive plotting is most convenient with the IPython
enhanced interpreter. For enabling interactive plotting, start IPython with
--matplotlib argument:
```
% ipython --matplotlib
```
Simple x-y plots can then be done as:

```
In [1]: import matplotlib.pyplot as plt
…
In [6]: plt.plot(x,y)  # line
In [7]: plt.plot(x,y, ’ro’)  # individual points in red
```
Look matplotlib documentation for additional information for visualisation.

### Parallel calculations

In class room workstations MPI parallel Python programs can be launched with mpiexec, e.g. to
run with 4 MPI tasks one issues

```
% mpiexec –n 4 python3.4 example.py
```

