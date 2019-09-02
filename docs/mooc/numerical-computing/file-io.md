<!-- Title: File I/O -->

<!-- Short description:

In this article we show how to read and write numeric data to simple files.

-->

# File I/O

NumPy provides functions for reading and writing numeric data to simple files
in a regular column layout. These I/O functions offer a very convenient way to
load and store data in a human-readable format.

Comments and column delimiters are handled automatically, so usually one can
read any data file in a column layout into a NumPy array.

Assume we have the following measurement data in a file called
`xy-coordinates.dat`. As you can see it also contains an invalid data
point that is commented out as well as one data point with an
undefined value (`nan`). 

~~~
# x          y
 -5.000000  25.131953
 -3.888889  15.056032
 -2.777778   7.261712
# -1.666667  -99999    << invalid data!
 -0.555556  -0.141217
  0.555556   0.176612
  1.666667   2.833694
  2.777778  nan
  3.888889  14.979309
  5.000000  25.299547
~~~

One can read the data into a NumPy array with a single **loadtxt()** function
call:

~~~python
xy = numpy.loadtxt('xy-coordinates.dat')

print(xy)
# output:
#   [[ -5.        25.131953]
#    [ -3.888889  15.056032]
#    [ -2.777778   7.261712]
#    [ -0.555556  -0.141217]
#    [  0.555556   0.176612]
#    [  1.666667   2.833694]
#    [  2.777778        nan]
#    [  3.888889  14.979309]
#    [  5.        25.299547]]
~~~

Comment lines are stripped away (both the header as well as the invalid data
row) and the undefined value (`nan`) is automatically recognised. The datatype
of the NumPy array is also automatically chosen based on the values.

If we want to write the data back to another file, this can be done with the
**writetxt()** function. One can also format the output e.g. by providing a
header comment (`header`) or by defining the number format (`fmt`) or column
delimiter (`delimiter`).

~~~python
args = {
  'header': 'XY coordinates',
  'fmt': '%7.3f',
  'delimiter': ','
}
numpy.savetxt('output.dat', xy, **args)
~~~

If we look into the output file, we can see that data has been written in a
nicely formatted column layout with the header we provided:

~~~
# XY coordinates
 -5.000, 25.132
 -3.889, 15.056
 -2.778,  7.262
 -0.556, -0.141
  0.556,  0.177
  1.667,  2.834
  2.778,    nan
  3.889, 14.979
  5.000, 25.300
~~~
