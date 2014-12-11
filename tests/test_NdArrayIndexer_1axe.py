#!/usr/bin/env python
#
# Testing ndarray with 1 axe. It has no effect. Read the comments in file for
# more information.
#

import numpy as np

from NdArrayIndexer import NdArrayIndexer


# Structure of unsorted list to be converted in the same shape as testing_array
testing_list = [7, 2, 76, 132, 32, 1, 221, 222, 223]

testing_array = np.array(testing_list)

print testing_array

print "------------------"

arr = NdArrayIndexer(testing_array)
arr.run()
print arr.get()