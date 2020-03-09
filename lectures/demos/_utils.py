"""
Various utilities used throughout the code.

Author:
    Ilias Bilionis

Date:
    5/19/2014

"""


__all__ = ['regularize_array', 'make_vector', 'call_many', 'view_as_column',
           'euclidean_distance']


import numpy as np
from scipy.spatial.distance import cdist


def regularize_array(x):
    """
    Regularize a numpy array.

    If x is 2D then nothing happens to it. If it is 1D then it is converted to
    2D with 1 row and as many columns as the number of elements in x.

    :param x:   The array to regularize.
    :type x:    :class:`numpy.ndarray`
    :returns:   Regularized version of x.
    :rtype:     :class:`numpy.ndarray`

    .. note::
        It does nothing if ``x`` is not a numpy array.
    """
    if not isinstance(x, np.ndarray):
        return x
    if x.ndim == 1:
        x = x[None, :]
    return x


def make_vector(x):
    """
    Make a vector out of x. We will attempt to make an array out of x and then
    flatten it.
    """
    return np.array(x).flatten()


def call_many(x, func, return_numpy=True):
    """
    Assuming the ``x`` is a 2D array, evaluate ``func(x[i, :])`` for each ``i``
    and return the result as a numpy array.

    :param x:               The evaluation points.
    :type x:                :class:`numpy.ndarray`
    :param func:            The function.
    :param return_numpy:    If ``True``, then it puts all the outputs in a numpy array.
                            Otherwise, it returns a list.
    """
    x = regularize_array(x)
    out = [func(x[i, :]) for i in range(x.shape[0])]
    if return_numpy:
        return np.array(out)
    return out


def view_as_column(x):
    """
    View x as a column vector.
    """
    if x.ndim == 1:
        x = x[:, None]
    elif x.ndim == 2 and x.shape[0] == 1:
        x = x.T
    return x


def euclidean_distance(x, y):
    """
    Returns the Euclidean distance between two numpy arrays.
    """
    return cdist(regularize_array(x), regularize_array(y))
