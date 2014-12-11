#!/usr/bin/env python
#
# Testing ndarray with 10 axes!!
#

import numpy as np

from NdArrayIndexer import NdArrayIndexer

# Structure of unsorted list to be converted in the same shape as testing_array
np.set_printoptions(threshold='nan')

testing_array = np.arange(150, 4665750).reshape((3, 5, 2, 6, 4, 3, 6, 5, 9, 8))

print testing_array

print "------------------"

arr = NdArrayIndexer(testing_array)
arr.run()
print arr.get()