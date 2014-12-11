#!/usr/bin/env python
#
# Testing ndarray with 2 axes
#

import numpy as np

import NdArrayIndexer


# Structure of unsorted list to be converted in the same shape as testing_array
testing_list = [
    [7, 2, 76], [132, 32, 1], [201, 23, 224],
    [101, 102, 103], [111, 112, 113], [121, 122, 123],
    [1, 20, 203], [51, 212, 13], [21, 102, 1],
    [4, 5, 6], [11, 12, 13], [21, 22, 23],
    [101, 102, 103], [111, 112, 113], [121, 122, 123],
    [201, 202, 203], [211, 212, 213], [221, 222, 223]
]

testing_array = np.array(testing_list)

shape = testing_array.shape

print testing_array

print "------------------"

arr = NdArrayIndexer(testing_array)
arr.run()
print arr.get()