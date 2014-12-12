NdArrayIndexer.py
=================

Python class which adds lower axes indices to the last axe into a numpy ndarray.

Quick demonstration:

1. We enter the ndarray:[
    [[[7, 2, 76], [132, 32, 1], [201, 23, 224], [201, 23, 224]],
    [[101, 102, 103], [111, 112, 113], [121, 122, 123], [201, 23, 224]]],

    [[[7, 2, 76], [132, 32, 1], [201, 23, 224], [201, 23, 224]],
    [[101, 102, 103], [111, 112, 113], [121, 122, 123], [201, 23, 224]]]
]

Description
-----------

Retrieves the indexes for all axes but last in a multi axes ndarray.
Given a ndarray this class returns a new ndarray with each index key as a new
item into the last axes (dimension). For this reason if a ndarray of 3 axes is
passed by NdArrayIndexer, it will return the same ndarray with new 2 items in
the axe 2.

Requirements
------------

Python 2.7.3
numpy 1.9

Usage
-----

`ndarray = array([[[x1, y1, z1], [xn, yn, zn]], [...]])`

`indexer = NdArrayIndexer(ndarray)`

`indexer.run()`

`indexer.get()`

The usage example above returns:

`array([[[a1_1, a0_1, x1, y1, z1], [a1_n, a0_n, xn, yn, zn]], [...]])`

Examples
--------

Check the test files:

* tests/test_NdArrayIndexer_3axes.py
* tests/test_NdArrayIndexer_2axes.py
* tests/test_NdArrayIndexer_1axe.py (it has no effect with only one axe)
* tests/test_SimpleCV.py

License
-------

NdArrayIndexer is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

NdArrayIndexer is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with NdArrayIndexer.  If not, see <http://www.gnu.org/licenses/>.
