#!/usr/bin/env python
################################################################################
# NdArrayIndexer v-0.5 - Adds lower axes indices to the last axe into ndarray. #
################################################################################
#
# Description
# -----------
# Retrieves the indexes for all axes but last in a multi axes ndarray.
# Given a ndarray this class returns a new ndarray with each index key as a new
# item into the last axes (dimension). For this reason if a ndarray of 3 axes is
# passed by NdArrayIndexer, it will return the same ndarray with new 2 items in
# the axe 2.
#
# Usage
# -----
# ndarray = array([[[x1, y1, z1], [xn, yn, zn]], [...]])
# indexer = NdArrayIndexer(ndarray)
# indexer.run()
# indexer.get()
#
# The usage example above returns:
# array([[[a1_1, a0_1, x1, y1, z1], [a1_n, a0_n, xn, yn, zn]], [...]])
#
# Usage with SimpleCV
# -------------------
# It is useful for example to make accessible the (x, y) coordinates for an
# image converted to numpy. See: http://simplecv.org
#
# # Converts image to ndarray
# img = Image("lenna")
# raw_img = img.getNumpy()
#
# # rawImg is array([[[r1, g1, b1], [rn, gn, bn]], [...]])
# # Where r is Red, g is Green and b is Blue dimensions by pixel.
# # The axe 0 is the coordinate y and the axe 1 is the coordinate x.
# # Now we are going to get the coordinates per pixel.
# indexer = NdArrayIndexer(raw_img)
# indexer.run()
# img_with_coords = indexer.get()
#
# # img_with_coords is the ndarray:
# # array([[[x1, y1, r1, g1, b1], [xn, yn, rn, gn, bn]], [...]])
#
# Examples
# --------
# Check the test files:
# test/test_NdArrayIndexer_3axes.py
# test/test_NdArrayIndexer_2axes.py
# test/test_NdArrayIndexer_1axe.py (it has no effect with only one axe)
#
# License
# -------
# NdArrayIndexer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# NdArrayIndexer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with NdArrayIndexer.  If not, see <http://www.gnu.org/licenses/>.
#
#
__author__ = "Jaume Mila"
__email__ = "jaume@westial.com"
__license__ = "GPL-v.3 <http://www.gnu.org/licenses/gpl-3.0.txt>"
__version__ = "0.5.0"
__file__ = "NdArrayIndexer.py"

################################################################################

import numpy as np


class NdArrayIndexer:

    def __init__(self, ndarray_src):
        """
        Constructor.

        Sets ndarray_src to properties.
        Flats destination ndarray_src shape.
        Initializes axes ndarray_src and counters.

        :param ndarray_src ndarray
        :return void
        """
        if not type(ndarray_src) is np.ndarray:
            raise ValueError('Input data is not a valid ndarray.')

        self._ndarray_src = ndarray_src
        self._ndarray_dst = np.ravel(ndarray_src)

        self._axes = self.convert_shape(ndarray_src.shape)

        self._axes_count = len(self._axes)
        self._axes_indexes = [0] * self._axes_count

        self._highest_axe = None

        self.__update_highest_axe()

        pass

    # Public

    def run(self):
        """
        Main. Iterates on all axes but lowest and calculates the parent index
        according to its position in flatten array.

        :return void
        """
        iterations = len(self._ndarray_dst) / self._highest_axe
        axes_count = len(self._axes)
        indices_count = axes_count - 1

        positions = []
        values = []

        for iteration in range(0, iterations):

            position = self._highest_axe * iteration
            positions += [position] * indices_count

            deeply_axe = 1

            values += self.__axes_indices(iteration, axes_count, deeply_axe)

        self.__resize(positions, values)

        self._axes[0] += indices_count
        self.__update_highest_axe()

        pass

    def __axes_indices(self, iteration, axes_count, deeply_axe):
        """
        Goes over all axes but first and calculates the index by position in
        a flatten array.

        Returns the list of indices for all axes but first

        :param iteration int: loop count for each item on penultimate axe
        :param axes_count int
        :param deeply_axe int: walking to the deeper axe this value is the
            product of multiply the reached axes. We use to know the position
            of the first item in the last axe relative to the flatten array.
        :return list<int>
        """
        values = []

        for axe_index in range(1, axes_count):

            lower_axe = self._axes[axe_index]
            axe = self._axes[axe_index - 1]

            deeply_axe *= axe

            value = ((self._highest_axe * iteration) // deeply_axe) % lower_axe

            values.append(value)

        return values

    def get(self):
        """
        Returns ndarray destination. Prior run execution is required.

        :return ndarray
        """
        shape = self.revert_shape(self._axes)

        return self._ndarray_dst.reshape(shape)

    # Helpers

    def __resize(self, positions, values):
        """
        Resizes destination ndarray to allow containing new item on the highest
        axe. Resizing into one axe only.

        :param positions: list<int> indices where to insert the values
        :param values: list<int> values to insert

        :return void
        """

        self._ndarray_dst = np.insert(arr=self._ndarray_dst, obj=positions,
                                      values=values)

        pass

    def __update_highest_axe(self):
        """
        Updates highest axe counter

        :return void
        """
        self._highest_axe = self._axes[0]

        pass

    # Static

    @classmethod
    def convert_shape(cls, original_axes):
        """
        Returns a reverted list of shape values.

        :param original_axes tuple<int>
        :return list<int>
        """
        axes = list(original_axes[::-1])

        return axes

    @classmethod
    def revert_shape(cls, current_axes):
        """
        Returns tuple with the current shape reverting the convert_shapes
        transformation.

        :param current_axes list<int>
        :return tuple<int>
        """
        shape = tuple(current_axes[::-1])

        return shape