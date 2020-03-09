"""
Implementation of a cached function of a numpy array input.

Author:
    Ilias Bilionis

Date:
    6/6/2014

"""


__all__ = ['CachedFunction']


from . import Cache
from . import NumpyArrayCache


class CachedFunction(object):

    """
    A class representing a cached function.
    """

    # The input cache
    _input_cashe = None

    # The output cache
    _output_cache = None

    # The underlying function
    _f = None

    # The object that implements the function (if any)
    _obj = None

    def __init__(self, f,
                 input_cache_type=NumpyArrayCache,
                 input_cache_args={'name': 'Input Cache'},
                 output_cache_type=NumpyArrayCache,
                 output_cache_args={'name': 'Output Cache'}):
        """
        Initialize the object.
        """
        self._count = 0
        self._count_eval = 0
        self._f = f
        self._input_cache = input_cache_type(**input_cache_args)
        self._output_cache = output_cache_type(**output_cache_args)

    def __get__(self, obj, type=None):
        return self.__class__(self._f.__get__(obj, type))

    def __call__(self, *args, **kw):
        """
        Call the function at x.
        """
        x = args[0]
        # Look for x in the cache
        i = self._input_cache.get_index_of(x)
        self._count += 1
        if i == -1:
            # Not found in cache, so evaluate
            y = self._f(*args, **kw)
            self._count_eval += 1
            self._input_cache.append(x)
            self._output_cache.append(y)
        else:
            # Found in cache, recover
            y = self._output_cache[i]
        return y
    
    def __str__(self):
        """
        Return a string representation of the object.
        """
        s = 'Cached function:\n'
        s = ('Evaluations = ' + str(self._count) +
             ' (' + str(self._count_eval) + ' actual)')
        return s
