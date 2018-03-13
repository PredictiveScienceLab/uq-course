"""
A trivial test model.

Author:
    Ilias Bilionis

Date:
    6/16/2014

"""


__all__ = ['TestModel1']


import numpy as np
from vuq import Model


class TestModel1(Model):

    """
    This is a very simple model quadratic in x with one dimension.
    """

    def __init__(self, name='Test model 1'):
        """
        Initialize the object.
        """
        super(TestModel1, self).__init__(1, 1, name=name)

    def _eval(self, x):
        state = {}
        state['f'] = x ** 2
        state['f_grad'] = x.reshape((1, 1))
        state['f_grad_2'] = np.eye(1).reshape((1, 1, 1))
        return state

