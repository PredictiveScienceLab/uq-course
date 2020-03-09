"""
A cache specifically designed for numpy arrays.

Author:
    Ilias Bilionis

Date:
    6/6/2014

"""


__all__ = ['NumpyArrayCache']


import numpy as np
from . import Cache
from . import euclidean_distance


class NumpyArrayCache(Cache):

    """
    A cache specifically designed for numpy arrays.

    See :class:`vuq.Cache` for the documentation of the overloaded functions.

    :param dist:    The distance metric.
    :param tol:     The tolerance below which two entries are considered to be
                    identical.
    """

    # The underlying cache (list of numpy arrays)
    _cache = None

    # The distance metric
    _dist = None

    def __init__(self, dist=euclidean_distance, tol=1e-16,
                 max_size=256, name='Numpy Array Cache'):
        """
        Initialize the object.
        """
        super(NumpyArrayCache, self).__init__(max_size=max_size, name=name)
        self._dist = dist
        self._tol = tol
        self._cache = []

    @property
    def size(self):
        return len(self._cache)

    def _do_append(self, value):
        self._cache.append(value)

    def drop_one(self):
        self._cache = self._cache[1:]

    def get_index_of(self, value):
        i = -1
        # We start iterating from the end of the sequence because it is more
        # probably that we will be asked to query a value from the top of the
        # cache
        for j in range(self.size - 1, -1, -1):
            d = self._dist(value, self._cache[i])
            if d <= self._tol:
                i = j
                break
        return i

    def _get_value_at(self, i):
        return self._cache[i]
