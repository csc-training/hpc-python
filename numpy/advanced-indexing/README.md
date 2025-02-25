<!--
SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>

SPDX-License-Identifier: CC-BY-NC-SA-4.0
-->

## Advanced indexing

Start with 10x10 array of uniformly distribute random numbers
(`np.random.random()`). Find all the elements larger than 0.5 by using Boolean
mask.

Find also the indices of elements larger than 0.5. You can use the above mask
and `numpy.nonzero()` for finding the indices. Check that the values obtained
by using the index array are the same as with the earlier direct Boolean
indexing.

