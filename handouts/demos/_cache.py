"""
A generic class representing a cache.

Author:
    Ilias Bilionis

Date:
    6/6/2014

"""


__all__ = ['Cache']


class Cache(object):

    """
    A generic class representing a cache.
    """

    # The maximum size of the cache
    _max_size = None

    # A name for the object
    __name__ = None

    @property
    def max_size(self):
        """
        :getter:    The max size.
        """
        return self._max_size

    def __init__(self, max_size=256, name='Cache'):
        """
        Initialize the object.
        """
        assert isinstance(max_size, int)
        assert max_size > 0
        self._max_size = max_size
        self.__name__ = name

    @property
    def is_empty(self):
        """
        Is the cache empty?
        """
        return self.size == None

    @property
    def size(self):
        """
        :getter:    The current size of the cache.
        """
        raise NotImplementedError('Implement me!')

    def drop_one(self):
        """
        Drops one value from the cache assuming that there is at least one
        element.
        """
        raise NotImplementedError('Implement me!')

    def _do_append(self, value):
        """
        Adds ``value`` to the cache assuming the maximum size has not been
        reached.
        """
        raise NotImplementedError('Implement me!')

    def append(self, value):
        """
        Adds ``value`` to the cache.
        """
        if self.size == self.max_size:
            self.drop_one()
        self._do_append(value)

    def get_index_of(self, value):
        """
        Return the index of ``value``.

        It should return -1 if ``value`` is not stored in the cashe.
        """
        raise NotImplementedError('Implement me!')

    def _get_value_at(self, i):
        """
        Return the value of the cache corresponding to index ``i``.
        """
        raise NotImplementedError('Implement me!')

    def __getitem__(self, i):
        """
        Return the value of the cashe stored at index ``i``.
        """
        assert i >= 0 and i < self.size
        return self._get_value_at(i)

    def __str__(self):
        """
        Return a string representation of the object.
        """
        s = 'Name: ' + self.__name__
        return s
