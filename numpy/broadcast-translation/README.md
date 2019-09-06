## Translation with broadcasting

NumPy broadcasting is powerful tool for dealing with different, but compatible
shape arrays.

File [points_circle.dat](points_circle.dat) contains x, y coordinates along a
circle. Translate all the coordinates with some vector e.g. (2.1, 1.1). Plot
both the original and translated points in order to see the effect of
translation.

In case you are not familiar with `matplotlib`, below is a simple example for
plotting coordinates:

~~~python
import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(10)
y = np.random.random(10)
plt.plot(x, y, 'o')
plt.show()
~~~

