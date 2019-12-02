"""
The Model class.

Author:
    Ilias Bilionis

Date:
    5/21/2014

"""


import numpy as np
from . import call_many
from . import CachedFunction


class Model(object):

    """
    Defines the concept of a model.

    Only the ``_eval()`` method of this class should be implemented by the children.
    See :meth:`vuq.Model._eval()` for further details on implementing this method.
    The bottom line is that it should evaluate the model and its first derivatives
    with respect to every parameter.

    """

    # A name for the model
    __name__ = None

    # The number of input dimensions
    _num_input = None

    # The number of output dimensions
    _num_output = None

    # Can this model compute gradients?
    _compute_grad = None

    # Can this model compute hessians?
    _compute_hessian = None

    @property
    def num_input(self):
        """
        :getter:    The number of input dimensions.
        """
        return self._num_input

    @property
    def num_output(self):
        """
        :getter:    The number of output dimensions.
        """
        return self._num_output

    @property
    def compute_grad(self):
        """
        :getter:    ``True`` if this model can compute gradients.
        """
        return self._compute_grad

    @property
    def compute_hessian(self):
        """
        :getter:    ``True`` if this model can compute hessian.
        """
        return self._compute_hessian

    def __init__(self, num_input, num_output, name='Model',
                 compute_grad=True, compute_hessian=True):
        """
        Initialize the object.
        """
        self._num_input = int(num_input)
        self._num_output = int(num_output)
        self.__name__ = str(name)
        self._compute_grad = compute_grad
        self._compute_hessian = compute_hessian
        if self.compute_hessian:
            assert self.compute_grad

    def _eval(self, x):
        """
        Evaluate the model at a single input ``x``.

        :param x:   The input at which we want to evaluate the model. It should have
                    the :attr:`vuq.Model.num_input` dimensions.
        :type x:    :class:`numpy.ndarray`
        :returns:   A dictionary containing the following keys:
                    + f:        The output of the model, 1D array of num_output
                                dimensions.
                    + f_grad:   The Jacobian of the model at x, a 2D array of size
                                num_output x num_input dimensions. Return None, if
                                you cannot compute the Jacobian.
                    + f_grad_2: a 3D array of num_ouptut x num_input x num_input
                                dimensions. Return None, if you cannot compute the
                                Hessian.
        """
        raise NotImplementedError('My children should implement this!')

    def __call__(self, x):
        """
        Evaluate the model at many inputs ``x``.

        :param x:  The input. It should always be a 2D matrix with the rows representing
                   different points and the columns different inputs. The dimensions
                   of x should be ``num_points x num_input``.
        :type x:   :class:`numpy.ndarray`
        :returns:  A dictionary containing the following keys:
                   + f:         The output at each row of x, 1D array of size x.shape[0].
                                Each element if of whatever type is the output of   
                                the model.
                   + f_grad:    A list of the Jacobians of each row of x.
                   + f_grad_2:  A list of the Hessians of each row of x.
        """
        out = call_many(x, self._eval, return_numpy=False)
        state = {}
        state['f'] = np.array([s['f'] for s in out])
        state['f_grad'] = [s['f_grad'] for s in out]
        state['f_grad_2'] = [s['f_grad_2'] for s in out]
        return state

    def __str__(self):
        """
        Return a string representation of the object.
        """
        s = 'Name: ' + self.__name__ + '\n'
        s += 'Number of input parameters: ' + str(self.num_input) + '\n'
        s += 'Number of output parameters: ' + str(self.num_output) + '\n'
        return s
